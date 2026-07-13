"""The browser lifecycle loop -- the genuinely new value of the server scope.

One :class:`BrowserSupervisor` owns one browser (= one "task"): it launches it
via :class:`~parsek_cdp_server.launcher.ChromeLauncher`, watches its health, and
restarts it on a crash.  Every state transition is broadcast (through the
``on_state`` callbacks the proxy registers) so a parser can react -- re-attach
its contexts, re-navigate -- instead of hanging on a dead socket.

The proxy is a *transparent pipe*: it opens a fresh websocket to the browser per
client connection, so the supervisor does not hold a persistent CDP connection.
It only needs to expose where the browser lives (:attr:`ws_url` / :attr:`host`)
and whether it is alive, and to drive relaunch.  On restart the websocket origin
changes and the proxy's pipes simply reconnect against the new :attr:`host`.
"""

from __future__ import annotations

import asyncio
from typing import Callable, List, Optional

from parsek_cdp._logging import get_logger
from parsek_cdp.core.target import ws_origin
from parsek_cdp.parsek import BrowserState

from .launcher import ChromeLauncher, LaunchOptions

logger = get_logger(__name__)

#: Notified on every lifecycle transition (the proxy turns this into a broadcast).
StateCallback = Callable[[BrowserState, Optional[str]], None]


class BrowserSupervisor:
    """Owns and supervises a single browser instance (one task)."""

    def __init__(
        self,
        browser_uuid: str,
        *,
        options: Optional[LaunchOptions] = None,
        restart_on_crash: bool = True,
        max_restarts: int = 5,
        poll_interval: float = 1.0,
        idle_timeout: Optional[float] = None,
    ) -> None:
        self.browser_uuid = browser_uuid
        self.launcher = ChromeLauncher(options)
        self.restart_on_crash = restart_on_crash
        self.max_restarts = max_restarts
        self.poll_interval = poll_interval
        #: When set, the browser closes itself after this many seconds with no
        #: client connection (``None`` disables the idle shutdown entirely).
        self.idle_timeout = idle_timeout
        self.state: BrowserState = BrowserState.STARTING
        #: Browser-level DevTools websocket url and its origin (set after start).
        self.ws_url: Optional[str] = None
        self.host: Optional[str] = None
        self._restarts = 0
        self._watch_task: Optional[asyncio.Task] = None
        self._shutting_down = False
        self._state_callbacks: List[StateCallback] = []
        #: Number of live client connections (control + page pipes).
        self._connections = 0
        #: Loop time the browser went idle (no connections), or ``None``.
        self._idle_since: Optional[float] = None
        #: Armed by :meth:`expect_exit` when the client sent a command that
        #: *might* make the browser quit on its own (closing the last target /
        #: browser context); tells :meth:`_watch` to record the next observed
        #: exit as a graceful close instead of a crash to relaunch. Cleared the
        #: moment the browser is next seen alive, so it only covers the poll
        #: right after such a command.
        self._expect_exit = False

    def on_state(self, callback: StateCallback) -> StateCallback:
        """Register a lifecycle-transition listener (proxy uses this to broadcast)."""
        self._state_callbacks.append(callback)
        return callback

    def client_connected(self) -> None:
        """Register a new client connection (cancels any pending idle shutdown)."""
        self._connections += 1
        self._idle_since = None

    def client_disconnected(self) -> None:
        """Register a client disconnecting; the idle clock restarts when it hits 0."""
        self._connections = max(0, self._connections - 1)

    def expect_exit(self) -> None:
        """Arm the watchdog to treat the next observed exit as a graceful close.

        Unlike ``Browser.close`` (which reliably quits the process, so it drives
        an immediate deliberate :meth:`shutdown`), commands like
        ``Target.closeTarget``/``Target.disposeBrowserContext`` only *might*
        end up closing the last target or context -- the browser may well keep
        running for other clients, so we can't force it down here. This just
        makes sure that *if* it turns out to have been the last one and the
        process exits on its own, :meth:`_watch` doesn't mistake that for a
        crash and restart it.
        """
        self._expect_exit = True

    def _set_state(self, state: BrowserState, reason: Optional[str] = None) -> None:
        logger.info("browser %s -> %s%s", self.browser_uuid, state.value,
                    f" ({reason})" if reason else "")
        self.state = state
        for cb in list(self._state_callbacks):
            try:
                cb(state, reason)
            except Exception:
                logger.exception("browser state callback failed")

    async def start(self) -> None:
        """Launch the browser, record where it lives, and start the watchdog."""
        self._set_state(BrowserState.STARTING)
        self.ws_url = await self.launcher.launch()
        self.host = ws_origin(self.ws_url)
        self._set_state(BrowserState.READY)
        self._watch_task = asyncio.create_task(self._watch())

    async def _watch(self) -> None:
        """Poll the process; on death drive a restart (or give up)."""
        try:
            while not self._shutting_down:
                await asyncio.sleep(self.poll_interval)
                if self._shutting_down:
                    return
                if self.launcher.is_alive():
                    self._expect_exit = False
                    if self._idle_expired():
                        await self._close_idle()
                        return
                    continue
                if self._expect_exit:
                    self._shutting_down = True
                    await self.launcher.terminate()
                    self._set_state(BrowserState.CLOSED, "closed by client")
                    return
                self._set_state(BrowserState.CRASHED, "process exited")
                if not self.restart_on_crash or self._restarts >= self.max_restarts:
                    return
                self._restarts += 1
                self._set_state(
                    BrowserState.RESTARTING,
                    f"attempt {self._restarts}/{self.max_restarts}",
                )
                try:
                    await self.restart()
                except Exception as exc:
                    self._set_state(BrowserState.CRASHED, f"restart failed: {exc}")
                    return
        except asyncio.CancelledError:
            raise

    async def restart(self) -> None:
        """Tear down and relaunch the browser, refreshing :attr:`ws_url`/:attr:`host`."""
        await self.launcher.terminate()
        self.launcher = ChromeLauncher(self.launcher.options)
        self.ws_url = await self.launcher.launch()
        self.host = ws_origin(self.ws_url)
        self._set_state(BrowserState.READY, "restarted")

    def _idle_expired(self) -> bool:
        """Whether the browser has had no connection for ``idle_timeout`` seconds.

        The clock starts the first poll the connection count is zero and resets
        whenever a client (re)connects, so an idle browser closes after the
        configured grace period -- including one nobody ever connected to.
        """
        if self.idle_timeout is None or self._connections > 0:
            self._idle_since = None
            return False
        now = asyncio.get_running_loop().time()
        if self._idle_since is None:
            self._idle_since = now
            return False
        return now - self._idle_since >= self.idle_timeout

    async def _close_idle(self) -> None:
        """Terminate the browser because it sat idle past :attr:`idle_timeout`."""
        self._shutting_down = True
        await self.launcher.terminate()
        self._set_state(BrowserState.CLOSED, "idle timeout")

    async def shutdown(self) -> None:
        """Stop supervising and terminate the browser (``BrowserState.CLOSED``)."""
        self._shutting_down = True
        if self._watch_task is not None:
            self._watch_task.cancel()
            try:
                await self._watch_task
            except asyncio.CancelledError:
                pass
            self._watch_task = None
        await self.launcher.terminate()
        self._set_state(BrowserState.CLOSED)

    def target_ws_url(self, target_id: str) -> str:
        """Build the browser's per-target DevTools websocket url for ``target_id``."""
        if self.host is None:
            raise RuntimeError("supervisor not started")
        return f"{self.host}/devtools/page/{target_id}"

    @property
    def is_active(self) -> bool:
        """Whether the browser is up and serving (state ``READY``).

        Metrics report only active browsers, so a starting / crashed / restarting
        / closed browser contributes no series (and its stale event counters are
        pruned), preventing leftover data from lingering.
        """
        return self.state is BrowserState.READY

    @property
    def pid(self) -> Optional[int]:
        """PID of the supervised browser process (``None`` before launch)."""
        return self.launcher.pid

    @property
    def http_origin(self) -> Optional[str]:
        """HTTP origin of the browser's DevTools endpoint (for ``/json/list``).

        Derived from :attr:`host` (``ws://127.0.0.1:PORT`` -> ``http://...``); the
        metrics collector polls ``{http_origin}/json/list`` to enumerate targets.
        """
        if self.host is None:
            return None
        return "http" + self.host[2:] if self.host.startswith("ws") else self.host
