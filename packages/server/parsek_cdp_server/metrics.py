"""Prometheus metrics for the server: browsers, targets, CDP events, CPU/RAM.

Exposed at ``GET /metrics``.  The exposition is split in two so a scrape never
blocks the event loop:

* **live counters** -- :meth:`ServerMetrics.record_event` is called from the page
  bridges on every CDP event, bumping an in-memory ``(browser, target, domain)``
  counter synchronously;
* **a periodic snapshot** -- a background task polls each browser's
  ``/json/list`` (targets + their types + nesting via ``parentId``) and samples
  the browser process tree with :mod:`psutil` (CPU%, RSS), off the loop in a
  thread.  :meth:`collect` (called at scrape time) only reads these cached
  values.

Metrics:

Only *active* browsers (supervisor state ``READY``) are reported; browsers that
are still starting, crashed, restarting or closed contribute no series, and any
event counters they left behind are pruned -- so stale data never lingers.

==================================  =====  ===========================================
``parsek_browsers``                 gauge  active (READY) browsers
``parsek_targets``                  gauge  targets, labelled ``browser``, ``type``
``parsek_nested_targets``           gauge  targets with a ``parentId``, per ``browser``
``parsek_browser_cpu_percent``      gauge  CPU% of the browser tree, per ``browser``
``parsek_browser_memory_bytes``     gauge  RSS of the browser tree, per ``browser``
``parsek_cdp_events_total``         count  CDP events, labelled ``browser``, ``target``, ``domain``
==================================  =====  ===========================================

Cardinality note: ``parsek_cdp_events_total`` is labelled by target id, which is
unbounded over time.  Series for targets that disappear from ``/json/list`` are
pruned on every snapshot, so the live set tracks the browser, not history.
"""

from __future__ import annotations

import asyncio
import json
import urllib.error
import urllib.request
from collections import defaultdict
from typing import TYPE_CHECKING, Dict, Optional, Set, Tuple

import psutil
from aiohttp import web
from prometheus_client import CONTENT_TYPE_LATEST, CollectorRegistry, generate_latest
from prometheus_client.core import CounterMetricFamily, GaugeMetricFamily

from parsek_cdp._logging import get_logger

if TYPE_CHECKING:
    from .proxy import ParsekServer

logger = get_logger(__name__)

#: (browser_uuid, target_id, domain) -> event count.
EventKey = Tuple[str, str, str]


class _BrowserSnapshot:
    """Cached per-browser facts sampled by the refresh task."""

    __slots__ = ("targets_by_type", "nested", "cpu_percent", "memory_bytes", "target_ids")

    def __init__(self) -> None:
        self.targets_by_type: Dict[str, int] = {}
        self.nested: int = 0
        self.cpu_percent: float = 0.0
        self.memory_bytes: int = 0
        self.target_ids: Set[str] = set()


class ServerMetrics:
    """Collects and exposes Prometheus metrics for a :class:`ParsekServer`."""

    def __init__(self, server: "ParsekServer", *, refresh_interval: float = 5.0) -> None:
        self._server = server
        self._refresh_interval = refresh_interval
        self._events: Dict[EventKey, int] = defaultdict(int)
        self._snapshot: Dict[str, _BrowserSnapshot] = {}
        #: psutil.Process cache so cpu_percent() deltas are meaningful across sweeps.
        self._proc_cache: Dict[int, psutil.Process] = {}
        self._refresh_task: Optional[asyncio.Task] = None
        self._registry = CollectorRegistry()
        self._registry.register(_Collector(self))

    # -- live event counting ---------------------------------------------- #

    def record_event(self, browser_uuid: str, target_id: str, domain: str) -> None:
        """Count one CDP event (called from a page bridge per event frame)."""
        self._events[(browser_uuid, target_id, domain)] += 1

    # -- lifecycle --------------------------------------------------------- #

    async def start(self) -> None:
        self._refresh_task = asyncio.create_task(self._refresh_loop())

    async def stop(self) -> None:
        if self._refresh_task is not None:
            self._refresh_task.cancel()
            try:
                await self._refresh_task
            except asyncio.CancelledError:
                pass
            self._refresh_task = None

    async def handle(self, request: web.Request) -> web.Response:
        """``GET /metrics`` -- render the registry in the Prometheus text format.

        Rendered synchronously on the event loop (not via ``to_thread``) so that
        ``collect`` reading ``_events`` cannot race with :meth:`record_event`
        mutating it from the same loop -- the registry is small, so this is cheap.
        """
        body = generate_latest(self._registry)
        return web.Response(body=body, content_type=CONTENT_TYPE_LATEST.split(";")[0],
                            charset="utf-8")

    # -- snapshot refresh -------------------------------------------------- #

    async def _refresh_loop(self) -> None:
        while True:
            try:
                await self._refresh_once()
            except Exception:
                logger.exception("metrics refresh failed")
            await asyncio.sleep(self._refresh_interval)

    async def _refresh_once(self) -> None:
        snapshot: Dict[str, _BrowserSnapshot] = {}
        live_targets: Set[Tuple[str, str]] = set()
        for browser_uuid, supervisor in list(self._server.supervisors.items()):
            # Only active (READY) browsers contribute metrics; skipping the rest
            # keeps their targets out of ``live_targets`` so their event series
            # are pruned below instead of lingering.
            if not supervisor.is_active:
                continue
            snap = _BrowserSnapshot()
            origin = supervisor.http_origin
            if origin is not None:
                await self._sample_targets(origin, snap)
            if supervisor.pid is not None:
                await asyncio.to_thread(self._sample_resources, supervisor.pid, snap)
            snapshot[browser_uuid] = snap
            live_targets.update((browser_uuid, tid) for tid in snap.target_ids)
        self._snapshot = snapshot
        self._prune_events(live_targets)

    async def _sample_targets(self, http_origin: str, snap: _BrowserSnapshot) -> None:
        """Fill ``snap`` from ``{http_origin}/json/list`` (excludes the browser target)."""
        try:
            targets = await asyncio.to_thread(self._read_json, f"{http_origin}/json/list")
        except (urllib.error.URLError, OSError, ValueError):
            return
        by_type: Dict[str, int] = defaultdict(int)
        for target in targets:
            by_type[target.get("type", "other")] += 1
            tid = target.get("id")
            if tid:
                snap.target_ids.add(tid)
            if target.get("parentId"):
                snap.nested += 1
        snap.targets_by_type = dict(by_type)

    def _sample_resources(self, pid: int, snap: _BrowserSnapshot) -> None:
        """Sum CPU% and RSS over the browser process tree (renderers, gpu, ...)."""
        try:
            root = self._proc(pid)
            procs = [root] + root.children(recursive=True)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            return
        cpu = 0.0
        rss = 0
        for proc in procs:
            try:
                cpu += self._proc(proc.pid).cpu_percent(None)
                rss += proc.memory_info().rss
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue
        snap.cpu_percent = cpu
        snap.memory_bytes = rss

    def _proc(self, pid: int) -> psutil.Process:
        """Return a cached :class:`psutil.Process` so cpu_percent() deltas persist."""
        proc = self._proc_cache.get(pid)
        if proc is None or not proc.is_running():
            proc = psutil.Process(pid)
            proc.cpu_percent(None)  # prime the delta baseline
            self._proc_cache[pid] = proc
        return proc

    def _prune_events(self, live: Set[Tuple[str, str]]) -> None:
        """Drop event series for targets no longer present (bounds cardinality)."""
        stale = [k for k in self._events if (k[0], k[1]) not in live]
        for key in stale:
            del self._events[key]

    @staticmethod
    def _read_json(url: str) -> list:
        with urllib.request.urlopen(url, timeout=2) as resp:
            return json.loads(resp.read())


class _Collector:
    """Bridges :class:`ServerMetrics` state into Prometheus metric families."""

    def __init__(self, metrics: ServerMetrics) -> None:
        self._metrics = metrics

    def collect(self):
        m = self._metrics
        snapshot = m._snapshot

        browsers = GaugeMetricFamily("parsek_browsers", "Number of active (READY) browsers")
        browsers.add_metric([], float(len(snapshot)))
        yield browsers

        targets = GaugeMetricFamily(
            "parsek_targets", "Targets per browser by type", labels=["browser", "type"]
        )
        nested = GaugeMetricFamily(
            "parsek_nested_targets", "Targets with a parent (nested)", labels=["browser"]
        )
        cpu = GaugeMetricFamily(
            "parsek_browser_cpu_percent", "CPU%% of the browser process tree",
            labels=["browser"],
        )
        mem = GaugeMetricFamily(
            "parsek_browser_memory_bytes", "RSS of the browser process tree",
            labels=["browser"],
        )
        for browser_uuid, snap in snapshot.items():
            for type_, count in snap.targets_by_type.items():
                targets.add_metric([browser_uuid, type_], float(count))
            nested.add_metric([browser_uuid], float(snap.nested))
            cpu.add_metric([browser_uuid], snap.cpu_percent)
            mem.add_metric([browser_uuid], float(snap.memory_bytes))
        yield targets
        yield nested
        yield cpu
        yield mem

        events = CounterMetricFamily(
            "parsek_cdp_events", "CDP events seen, by target and domain",
            labels=["browser", "target", "domain"],
        )
        for (browser_uuid, target_id, domain), count in list(m._events.items()):
            events.add_metric([browser_uuid, target_id, domain], float(count))
        yield events