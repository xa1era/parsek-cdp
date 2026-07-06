"""The proxy: a transparent CDP pipe between clients and the browser.

Each client connection (a parser flow's browser / context / page) gets its own
websocket, mirroring how the client library connects one socket per target.  The
proxy relays raw CDP frames 1:1 to the browser and back -- it does *not*
multiplex by ``sessionId`` and does *not* remap message ids, because each pipe
carries exactly one client's traffic.

Two things are *not* pure passthrough:

* **lifecycle** -- the control channel also pushes ``Parsek.browserStateChanged``
  so a parser learns when its browser crashed/restarted instead of hanging;
* **feature aggregation** -- on a page pipe the server-side feature *producers*
  digest the raw CDP burst (e.g. all of ``Network.*``) into a couple of
  aggregated ``Parsek.*`` events and *suppress* the raw events they consumed, so
  the channel is not flooded.  ``?raw=1`` opts out of suppression.

Endpoints::

    POST /browsers                                create a task -> browser_uuid
    GET  /metrics                                 Prometheus metrics (browsers/targets/...)
    ws   /cdp/{browser}/control                   pipe to the browser endpoint + Parsek.*
    ws   /cdp/{browser}/page/{target_id}          pipe to one target + feature aggregation
"""

from __future__ import annotations

import asyncio
import itertools
import json
import subprocess
import uuid
from typing import Awaitable, Callable, Dict, List, Optional, Set, Tuple, Type

import websockets
from aiohttp import web
from parsek_cdp._logging import get_logger
from parsek_cdp.core.browser import LaunchOptions
from parsek_cdp.core.feature import Feature
from parsek_cdp.core.target import ProtocolError
from parsek_cdp.parsek import BrowserState
from parsek_cdp.parsek.events import BrowserStateChanged

from .metrics import ServerMetrics
from .reaper import spawn_reaper
from .supervisor import BrowserSupervisor

logger = get_logger(__name__)

#: Server-injected commands (feature enables, body fetches) get ids from this
#: range so they never collide with the client's ids on the same socket.
_SERVER_ID_BASE = 1 << 30


async def _close_pending(pending) -> None:
    for task in pending:
        task.cancel()
    for task in pending:
        try:
            await task
        except asyncio.CancelledError:
            pass


class PageBridge:
    """One client websocket bridged 1:1 to one browser target websocket.

    Relays raw CDP both ways and hosts the server-side feature producers, which
    aggregate the raw event burst into ``Parsek.*`` events and suppress the raw
    events they digest.  Acts as the feature ``host`` (``send_cdp`` /
    ``emit_parsek``), keeping its server-injected commands on a disjoint id range.
    """

    def __init__(
        self,
        client_ws: web.WebSocketResponse,
        chrome_url: str,
        feature_classes: Tuple[Type[Feature], ...],
        *,
        raw_passthrough: bool = False,
        on_event: Optional[Callable[[str], None]] = None,
    ) -> None:
        self.client_ws = client_ws
        self.chrome_url = chrome_url
        self.feature_classes = feature_classes
        self.raw_passthrough = raw_passthrough
        self._on_event = on_event
        self._chrome: Optional[websockets.ClientConnection] = None
        self._server_ids = itertools.count(_SERVER_ID_BASE)
        self._server_pending: Dict[int, asyncio.Future] = {}
        self._features: List[Feature] = []
        self._suppress: Tuple[str, ...] = ()

    async def run(self) -> None:
        async with websockets.connect(
            self.chrome_url, max_size=None, ping_interval=None
        ) as chrome:
            self._chrome = chrome
            self._features = [fc(self, role="server") for fc in self.feature_classes]
            self._suppress = tuple(
                prefix
                for fc in self.feature_classes
                for prefix in fc.suppressed_prefixes()
            )
            # The receive loop must run before features enable their domains, so
            # their send_cdp responses can be matched.
            recv = asyncio.ensure_future(self._chrome_to_client())
            for feature in self._features:
                await feature.start()
            send = asyncio.ensure_future(self._client_to_chrome())
            _done, pending = await asyncio.wait(
                {recv, send}, return_when=asyncio.FIRST_COMPLETED
            )
            await _close_pending(pending)

    # -- feature host interface ------------------------------------------- #

    async def send_cdp(self, method: str, params: dict) -> dict:
        """Issue a server-originated CDP command and await its result."""
        if self._chrome is None:
            raise ConnectionError("chrome connection not open")
        message_id = next(self._server_ids)
        future: asyncio.Future = asyncio.get_running_loop().create_future()
        self._server_pending[message_id] = future
        await self._chrome.send(
            json.dumps({"id": message_id, "method": method, "params": params})
        )
        return await future

    async def emit_parsek(
        self, method: str, params: dict, session_id: Optional[str] = None
    ) -> None:
        """Send an aggregated ``Parsek.*`` event to the client."""
        await self._send_client(json.dumps({"method": method, "params": params}))

    # -- pumps ------------------------------------------------------------- #

    async def _chrome_to_client(self) -> None:
        assert self._chrome is not None
        try:
            await self._pump_chrome()
        except (websockets.ConnectionClosed, ConnectionError):
            pass  # socket dropped -- the other pump tears the bridge down

    async def _pump_chrome(self) -> None:
        assert self._chrome is not None
        async for raw in self._chrome:
            msg = json.loads(raw)
            if "id" in msg:
                future = self._server_pending.pop(msg["id"], None)
                if future is not None:  # our own command -> consume, don't relay
                    if not future.done():
                        if "error" in msg:
                            err = msg["error"]
                            future.set_exception(
                                ProtocolError(
                                    err.get("code", -1),
                                    err.get("message", ""),
                                    err.get("data"),
                                )
                            )
                        else:
                            future.set_result(msg.get("result", {}))
                    continue
                await self._send_client(raw)  # the client's own response
                continue
            method = msg.get("method", "")
            params = msg.get("params", {})
            if self._on_event and method:
                self._on_event(method.split(".", 1)[0])
            for feature in self._features:
                try:
                    await feature.handle_cdp_event(method, params, "")
                except Exception:
                    logger.exception("feature failed on %s", method)
            if self.raw_passthrough or not method.startswith(self._suppress):
                await self._send_client(raw)

    async def _client_to_chrome(self) -> None:
        assert self._chrome is not None
        try:
            async for msg in self.client_ws:
                if msg.type is not web.WSMsgType.TEXT:
                    break
                frame = json.loads(msg.data)
                if str(frame.get("method", "")).startswith("Parsek."):
                    await self._handle_parsek(frame)
                else:
                    await self._chrome.send(msg.data)
        except (websockets.ConnectionClosed, ConnectionError):
            pass

    async def _handle_parsek(self, frame: dict) -> None:
        """Handle a page-scoped ``Parsek.*`` command locally and reply."""
        method = frame.get("method")
        params = frame.get("params", {})
        result: dict = {}
        if method == "Parsek.setRawPassthrough":
            self.raw_passthrough = bool(params.get("enabled"))
        elif method == "Parsek.getRequests":
            for feature in self._features:
                snap = await feature.snapshot()
                if snap:
                    result = snap
                    break
        else:
            logger.warning("unhandled Parsek command %r", method)
        if frame.get("id") is not None:
            await self._send_client(json.dumps({"id": frame["id"], "result": result}))

    async def _send_client(self, data: str) -> None:
        try:
            await self.client_ws.send_str(data)
        except Exception:
            pass


class ParsekServer:
    """The HTTP/ws front door: routes connections to supervisors and bridges."""

    def __init__(
        self,
        *,
        launch_options: Optional[LaunchOptions] = None,
        idle_timeout: Optional[float] = None,
        enable_metrics: bool = True,
        metrics_refresh: float = 5.0,
        reap_zombies: bool = True,
        reap_interval: float = 30.0,
    ) -> None:
        self.supervisors: Dict[str, BrowserSupervisor] = {}
        #: Feature producers hosted on pages.  The proxy is a pure CDP
        #: passthrough by default; register features with :meth:`register_feature`
        #: to make them selectable per browser via ``?feature=``.
        self.features: Tuple[Type[Feature], ...] = ()
        self.launch_options = launch_options
        self.idle_timeout = idle_timeout
        self._feature_registry: Dict[str, Type[Feature]] = {}
        self._browser_features: Dict[str, Tuple[Type[Feature], ...]] = {}
        self._control_clients: Dict[str, Set[web.WebSocketResponse]] = {}
        self._runner: Optional[web.AppRunner] = None
        self.metrics: Optional[ServerMetrics] = (
            ServerMetrics(self, refresh_interval=metrics_refresh)
            if enable_metrics
            else None
        )
        self._reap_zombies = reap_zombies
        self._reap_interval = reap_interval
        self._reaper = None

    def register_feature(self, feature: Type[Feature]) -> None:
        """Make ``feature`` selectable by clients via ``?feature=<name>``."""
        self._feature_registry[feature.__name__] = feature

    async def start(self, host: str = "127.0.0.1", port: int = 9333) -> None:
        """Start the aiohttp app serving the endpoints documented above."""
        app = web.Application()
        app.router.add_post("/browsers", self.create_browser)
        app.router.add_get("/cdp/{browser}/control", self.control_ws)
        app.router.add_get("/cdp/{browser}/page/{target}", self.page_ws)
        if self.metrics is not None:
            app.router.add_get("/metrics", self.metrics.handle)
        self._runner = web.AppRunner(app)
        await self._runner.setup()
        await web.TCPSite(self._runner, host, port).start()
        if self.metrics is not None:
            await self.metrics.start()
        if self._reap_zombies:
            self._reaper = spawn_reaper(self._reap_interval)
        logger.info("ParsekServer listening on http://%s:%d", host, port)

    async def stop(self) -> None:
        """Shut down every supervised browser and the HTTP server."""
        for supervisor in list(self.supervisors.values()):
            await supervisor.shutdown()
        self.supervisors.clear()
        self._browser_features.clear()
        self._control_clients.clear()
        if self.metrics is not None:
            await self.metrics.stop()
        if self._reaper is not None:
            self._reaper.terminate()
            try:
                self._reaper.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self._reaper.kill()
            self._reaper = None
        if self._runner is not None:
            await self._runner.cleanup()
            self._runner = None

    # -- endpoint handlers ------------------------------------------------- #

    async def create_browser(self, request: web.Request) -> web.Response:
        """``POST /browsers?feature=...``: spawn a supervisor, return its endpoint.

        ``?feature=`` query params (repeatable) select which registered features
        are hosted on this browser's pages (none by default -- pure passthrough);
        the JSON body carries the launch settings (``headless``, ``executable``,
        ``extra_args``, ...).  Returns ``{browserUuid, wsUrl}`` where ``wsUrl`` is
        the control-channel endpoint.
        """
        names = request.query.getall("feature", [])
        unknown = [n for n in names if n not in self._feature_registry]
        if unknown:
            logger.warning("ignoring unknown features: %s", unknown)
        feats = tuple(
            self._feature_registry[n] for n in names if n in self._feature_registry
        )
        if not feats:
            feats = self.features

        options = await self._launch_options(request)
        idle_timeout = await self._idle_timeout(request)
        browser_uuid = uuid.uuid4().hex
        supervisor = BrowserSupervisor(
            browser_uuid, options=options, idle_timeout=idle_timeout
        )
        supervisor.on_state(self._state_broadcaster(browser_uuid))
        # Registered after the broadcaster so clients still receive the CLOSED
        # frame before the registries are dropped.
        supervisor.on_state(self._forget_on_close(browser_uuid))
        self.supervisors[browser_uuid] = supervisor
        self._browser_features[browser_uuid] = feats
        self._control_clients[browser_uuid] = set()
        await supervisor.start()
        ws_url = f"ws://{request.host}/cdp/{browser_uuid}/control"
        return web.json_response({"browserUuid": browser_uuid, "wsUrl": ws_url})

    async def _launch_options(self, request: web.Request) -> Optional[LaunchOptions]:
        """Build :class:`LaunchOptions` from the request body, else the server default."""
        try:
            body = await request.json() if request.can_read_body else {}
        except Exception:
            body = {}
        if body:
            return LaunchOptions.from_json(body)
        return self.launch_options

    async def _idle_timeout(self, request: web.Request) -> Optional[float]:
        """Seconds-with-no-connection before the browser self-closes.

        Read from the request body's ``idle_timeout`` (falling back to the
        server default); a non-positive or unparseable value disables it.
        """
        try:
            body = await request.json() if request.can_read_body else {}
        except Exception:
            body = {}
        if "idle_timeout" in body:
            try:
                value = float(body["idle_timeout"])
            except (TypeError, ValueError):
                return self.idle_timeout
            return value if value > 0 else None
        return self.idle_timeout

    async def control_ws(self, request: web.Request) -> web.WebSocketResponse:
        """``ws /cdp/{browser}/control``: pipe to the browser endpoint + state."""
        browser_uuid = request.match_info["browser"]
        supervisor = self.supervisors.get(browser_uuid)
        ws = web.WebSocketResponse(max_msg_size=0)
        await ws.prepare(request)
        if supervisor is None or supervisor.ws_url is None:
            await ws.close(code=4040, message=b"unknown browser")
            return ws
        clients = self._control_clients.setdefault(browser_uuid, set())
        clients.add(ws)
        supervisor.client_connected()
        await self._send(
            ws,
            json.dumps(
                {
                    "method": BrowserStateChanged.EVENT_METHOD,
                    "params": BrowserStateChanged(
                        state=supervisor.state, browser_uuid=browser_uuid
                    ).to_json(),
                }
            ),
        )
        try:
            await self._pipe(
                ws,
                supervisor.ws_url,
                on_client_frame=self._on_control_frame(browser_uuid),
            )
        finally:
            clients.discard(ws)
            supervisor.client_disconnected()
        return ws

    def _on_control_frame(self, browser_uuid: str):
        """Watch a control channel for the client's ``Browser.close`` request.

        The frame is still forwarded to the browser (it closes itself gracefully);
        this handler additionally shuts the *supervisor* down so the resulting
        process exit is recorded as an intentional ``CLOSED`` rather than a crash
        to be relaunched.
        """

        async def handle(data: str) -> None:
            # Cheap substring gate first -- only bother parsing the frame that
            # could actually be the close request, not every control message.
            if "Browser.close" not in data:
                return
            try:
                method = json.loads(data).get("method")
            except Exception:
                return
            if method == "Browser.close":
                await self._graceful_close(browser_uuid)

        return handle

    async def _graceful_close(self, browser_uuid: str) -> None:
        """Stop supervising ``browser_uuid`` and terminate it (idempotent)."""
        supervisor = self.supervisors.pop(browser_uuid, None)
        self._browser_features.pop(browser_uuid, None)
        self._control_clients.pop(browser_uuid, None)
        if supervisor is not None:
            await supervisor.shutdown()

    async def page_ws(self, request: web.Request) -> web.WebSocketResponse:
        """``ws /cdp/{browser}/page/{target}``: pipe to a target + aggregation."""
        browser_uuid = request.match_info["browser"]
        target_id = request.match_info["target"]
        supervisor = self.supervisors.get(browser_uuid)
        ws = web.WebSocketResponse(max_msg_size=0)
        await ws.prepare(request)
        if supervisor is None or supervisor.host is None:
            await ws.close(code=4040, message=b"unknown browser")
            return ws
        raw = request.query.get("raw") in ("1", "true", "yes")
        feats = self._browser_features.get(browser_uuid, self.features)
        on_event = None
        if self.metrics is not None:

            def on_event(domain: str) -> None:
                self.metrics.record_event(browser_uuid, target_id, domain)

        bridge = PageBridge(
            ws,
            supervisor.target_ws_url(target_id),
            feats,
            raw_passthrough=raw,
            on_event=on_event,
        )
        supervisor.client_connected()
        try:
            await bridge.run()
        except Exception:
            logger.exception("page bridge for %s crashed", target_id)
        finally:
            supervisor.client_disconnected()
        return ws

    # -- helpers ----------------------------------------------------------- #

    async def _pipe(
        self,
        client_ws: web.WebSocketResponse,
        chrome_url: str,
        on_client_frame: Optional[Callable[[str], Awaitable[None]]] = None,
    ) -> None:
        """Relay raw frames both ways between a client socket and Chrome.

        ``on_client_frame`` (if given) is invoked with each text frame *after* it
        has been forwarded, letting the caller react to specific commands (e.g.
        ``Browser.close``) without disturbing the passthrough.
        """
        async with websockets.connect(
            chrome_url, max_size=None, ping_interval=None
        ) as chrome:

            async def client_to_chrome() -> None:
                try:
                    async for msg in client_ws:
                        if msg.type is not web.WSMsgType.TEXT:
                            break
                        await chrome.send(msg.data)
                        if on_client_frame is not None:
                            await on_client_frame(msg.data)
                except (websockets.ConnectionClosed, ConnectionError):
                    pass

            async def chrome_to_client() -> None:
                try:
                    async for raw in chrome:
                        await self._send(client_ws, raw)
                except (websockets.ConnectionClosed, ConnectionError):
                    pass

            c2b = asyncio.ensure_future(client_to_chrome())
            b2c = asyncio.ensure_future(chrome_to_client())
            _done, pending = await asyncio.wait(
                {c2b, b2c}, return_when=asyncio.FIRST_COMPLETED
            )
            await _close_pending(pending)

    def _forget_on_close(self, browser_uuid: str):
        """Drop a browser from the registries once it reaches ``CLOSED``.

        This is how a self-initiated shutdown -- notably the supervisor's idle
        timeout (:meth:`BrowserSupervisor._close_idle`) -- gets its supervisor
        removed from :attr:`supervisors` (and the sibling registries), without the
        supervisor needing a back-reference to the server.  Idempotent, so a
        ``CLOSED`` also driven by :meth:`_graceful_close`/:meth:`stop` is harmless.
        """

        def callback(state, reason=None) -> None:
            if state is BrowserState.CLOSED:
                self.supervisors.pop(browser_uuid, None)
                self._browser_features.pop(browser_uuid, None)
                self._control_clients.pop(browser_uuid, None)

        return callback

    def _state_broadcaster(self, browser_uuid: str):
        def callback(state, reason) -> None:
            frame = json.dumps(
                {
                    "method": BrowserStateChanged.EVENT_METHOD,
                    "params": BrowserStateChanged(
                        state=state, reason=reason, browser_uuid=browser_uuid
                    ).to_json(),
                }
            )
            for ws in list(self._control_clients.get(browser_uuid, ())):
                asyncio.ensure_future(self._send(ws, frame))

        return callback

    @staticmethod
    async def _send(ws: web.WebSocketResponse, data: str) -> None:
        try:
            await ws.send_str(data)
        except Exception:
            pass
