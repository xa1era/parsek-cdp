"""Connection and target primitives.

A :class:`CDPConnection` owns a single websocket to one DevTools endpoint, runs
the receive loop, matches command responses to their futures and dispatches the
events that arrive on it.

A :class:`Target` *is* such a connection: every target (the browser, a page, a
worker, ...) opens its **own** websocket to ``{host}/devtools/{type_}/{id}``.
The host is not threaded through every call -- it lives in the :data:`cdp_host`
context variable, set once when the browser is reached and inherited by every
target connected from within that context.  Targets dispatch events to handlers
registered either on the target (:meth:`Target.on`) or globally on the event
class (:meth:`Event.add_handler`).
"""

from __future__ import annotations

import asyncio
import contextlib
import contextvars
import itertools
import json
from typing import Any, AsyncIterator, Awaitable, Callable, ClassVar, Iterator, Optional
from urllib.parse import urlsplit, urlunsplit

import websockets
import websockets.asyncio
import websockets.asyncio.client

from .._logging import get_logger
from ..cdp import CDP
from ..cdp import Target as TargetDomain
from ..cdp.mixins.event import EVENT_REGISTRY, Event
from .feature import _camel

logger = get_logger(__name__)

EventHandler = Callable[[Event], Awaitable[Any | None] | Any | None]
#: Handler for a CDP command call: receives the ``params`` dict that was sent.
FunctionHandler = Callable[[dict], Awaitable[Any | None] | Any | None]


#: Origin (or prefix) of the DevTools endpoint every target connects to.  For a
#: direct Chrome connection this is the bare origin (e.g. ``"ws://127.0.0.1:9222"``);
#: for a parsek-cdp-server proxy it carries the per-browser path prefix (e.g.
#: ``"ws://127.0.0.1:9333/cdp/<uuid>"``).  Set once when the browser is reached;
#: each :meth:`Target.connect` reads it to build its own websocket URL.
cdp_host: contextvars.ContextVar[str] = contextvars.ContextVar("cdp_host")

#: Path segment between :data:`cdp_host` and a target id when building a target's
#: websocket URL.  Chrome serves targets at ``/devtools/page/<id>`` (the default);
#: the proxy serves them at ``/page/<id>``.
cdp_target_path: contextvars.ContextVar[str] = contextvars.ContextVar(
    "cdp_target_path", default="/devtools/page/"
)


def ws_origin(ws_url: str) -> str:
    """Strip a full DevTools ws URL down to its ``scheme://host:port`` origin."""
    parts = urlsplit(ws_url)
    return urlunsplit((parts.scheme, parts.netloc, "", "", ""))


@contextlib.contextmanager
def use_host(host: str) -> Iterator[str]:
    """Bind :data:`cdp_host` for the duration of the block (then restore it)."""
    token = cdp_host.set(host)
    try:
        yield host
    finally:
        cdp_host.reset(token)


class ProtocolError(Exception):
    """Raised when the browser returns an error for a command."""

    def __init__(self, code: int, message: str, data: Any = None):
        super().__init__(f"[{code}] {message}" + (f": {data}" if data else ""))
        self.code = code
        self.message = message
        self.data = data


class CDPConnection:
    """A single websocket carrying one DevTools session's commands and events."""

    _ws: Optional[websockets.asyncio.client.ClientConnection]

    def __init__(self) -> None:
        self._ids = itertools.count(1)
        self._pending: dict[int, asyncio.Future] = {}
        self._send_lock = asyncio.Lock()
        self._recv_task: Optional[asyncio.Task] = None
        self._ws = None

    async def _open(self, url: str) -> "CDPConnection":
        """Open the websocket to ``url`` and start serving its receive loop."""
        self._ws = await websockets.connect(url, max_size=None, ping_interval=None)
        self._recv_task = asyncio.create_task(self._receive_loop())
        return self

    async def send(self, method: str, params: dict) -> Any:
        """Send a command and await its result (or raise :class:`ProtocolError`)."""
        if self._ws is None:
            raise ConnectionError("connection is not open")
        future: asyncio.Future = asyncio.get_running_loop().create_future()
        async with self._send_lock:
            message_id = next(self._ids)
            self._pending[message_id] = future
        payload: dict[str, Any] = {"id": message_id, "method": method, "params": params}
        try:
            logger.trace("send %s", payload)
            await self._ws.send(json.dumps(payload))
        except Exception:
            self._pending.pop(message_id, None)
            raise
        return await future

    async def _receive_loop(self) -> None:
        assert self._ws is not None
        closed_by: Optional[BaseException] = None
        try:
            async for raw in self._ws:
                try:
                    await self._handle_message(json.loads(raw))
                except Exception:
                    # A single malformed message or a throwing event handler
                    # must NOT tear down the whole connection -- log and keep
                    # serving every other command/event.
                    logger.exception("error handling CDP message")
        except asyncio.CancelledError:
            raise
        except Exception as exc:
            closed_by = exc
        finally:
            reason = ConnectionError("CDP connection closed")
            if closed_by is not None:
                reason.__cause__ = closed_by  # keep the real cause visible
            for fut in self._pending.values():
                if not fut.done():
                    fut.set_exception(reason)
            self._pending.clear()

    async def _handle_message(self, msg: dict) -> None:
        if "id" in msg:
            logger.trace("recv %s", msg)
            future = self._pending.pop(msg["id"], None)
            if future is None or future.done():
                return
            if "error" in msg:
                err = msg["error"]
                future.set_exception(
                    ProtocolError(
                        err.get("code", -1), err.get("message", ""), err.get("data")
                    )
                )
            else:
                future.set_result(msg.get("result", {}))
            return
        logger.trace("recv %s", msg)
        await self._dispatch(msg["method"], msg.get("params", {}))

    async def _dispatch(self, method: str, params: dict): ...

    async def close(self) -> None:
        if self._recv_task:
            self._recv_task.cancel()
        if self._ws is not None:
            await self._ws.close()


class Target(CDPConnection):
    """A single CDP session (browser, page, worker, ...) on its own websocket."""

    #: Domains enabled on *any* target (process-wide).  Shared by every
    #: ``Target``; a domain lands here as soon as its ``enable`` succeeds on any
    #: session and leaves on ``disable``.
    enabled_domains: ClassVar[set[str]] = set()

    #: Domains enabled on *this* session specifically.  ``cdp.<Domain>.enable``
    #: adds the domain here (and to :attr:`enabled_domains`); ``disable`` removes
    #: it.  This is the set :meth:`domain_enabled` consults to decide whether it
    #: needs to flip the domain at all.
    session_enabled_domains: set[str]

    def __init__(
        self, target_info: TargetDomain.TargetInfo, parent: Target | None = None
    ):
        super().__init__()
        self._target = target_info
        self._parent = parent
        self._cdp = CDP(self)

        self._handlers: dict[str, list[EventHandler]] = {}
        self._functions_handlers: dict[str, list[FunctionHandler]] = {}

        self._targets: dict[TargetDomain.TargetID, Target] = {}
        self.session_enabled_domains = set()

    async def send(self, method: str, params: dict) -> Any:
        """Send a command, then track domain ``enable``/``disable`` calls.

        Every generated ``cdp.<Domain>.enable``/``disable`` routes through here
        as ``"<Domain>.enable"`` / ``"<Domain>.disable"``.  Registering on the
        way out (only once the command has actually succeeded) is how a domain
        "adds itself" to the enabled sets without any per-domain code.
        """
        result = await super().send(method, params)
        domain, _, command = method.partition(".")
        if command == "enable":
            self.session_enabled_domains.add(domain)
            type(self).enabled_domains.add(domain)
        elif command == "disable":
            self.session_enabled_domains.discard(domain)
            type(self).enabled_domains.discard(domain)
        for handler in list(self._functions_handlers.get(method, ())):
            await self._invoke(handler, params)
        return result

    @contextlib.asynccontextmanager
    async def domain_enabled(self, domain: Any) -> AsyncIterator[None]:
        """Ensure ``domain`` is enabled for the block, restoring prior state.

        ``domain`` is a CDP domain command handle (e.g. ``page.cdp.Page``).  If
        the domain is *already* enabled on this session the block runs untouched;
        otherwise it is enabled on entry and disabled again on exit::

            async with page.domain_enabled(page.cdp.Page):
                await page.cdp.Page.navigate(url=...)

        The manager itself never mutates the enabled sets -- it only calls
        ``enable``/``disable``, which register/unregister the domain themselves.
        """
        name = type(domain).__name__
        already_enabled = name in self.session_enabled_domains
        if not already_enabled:
            await domain.enable()
        try:
            yield
        finally:
            if not already_enabled:
                await domain.disable()

    @property
    def cdp(self):
        return self._cdp

    @property
    def parent(self):
        return self._parent

    @property
    def targets(self):
        return list(self._targets.values())

    @property
    def id(self):
        return self._target.target_id

    @property
    def type_(self) -> str:
        return self._target.type_

    @property
    def url(self):
        return self._target.url

    @property
    def raw_target(self):
        return self._target

    @property
    def ws_url(self) -> str:
        """This target's own DevTools websocket URL, from :data:`cdp_host`.

        Holds for page/worker targets, whose ``target_id`` matches the
        ``/devtools/page/<id>`` path.  The *browser* endpoint is the exception
        -- its ws path carries a dedicated id unrelated to the browser target's
        ``target_id`` -- so the browser passes its discovered URL to
        :meth:`connect` explicitly.
        """
        return f"{cdp_host.get()}{cdp_target_path.get()}{self.id}"

    async def connect(self, url: Optional[str] = None) -> "Target":
        """Open this target's own websocket and start tracking its children.

        ``url`` overrides :attr:`ws_url` (used for the browser endpoint, whose
        path id does not match its ``target_id``).
        """
        await self._open(url or self.ws_url)
        self.on(TargetDomain.TargetCreated, self._on_target_created)
        self.on(TargetDomain.TargetDestroyed, self._on_target_destroyed)
        self.on(TargetDomain.TargetInfoChanged, self._on_target_info_changed)
        return self

    async def close(self):
        await super().close()
        self._handlers.clear()
        self._functions_handlers.clear()
        for child in self.targets:
            await child.close()
        self.targets.clear()

    def on[Ev: Event](
        self, event: "type[Ev]", handler: "Callable[[Ev], Any]"
    ) -> "Callable[[Ev], Any]":
        """Register ``handler`` for an event on this target.

        ``event`` may be an :class:`Event` subclass (the handler is then typed to
        that event) or a raw method string.  Returns the handler so it can be
        used as a decorator.
        """
        method = event.EVENT_METHOD
        self._handlers.setdefault(method, []).append(handler)  # type: ignore[arg-type]
        return handler

    def off[Ev: Event](self, event: "type[Ev]", handler: "Callable[[Ev], Any]") -> None:
        method = event.EVENT_METHOD
        if method in self._handlers:
            try:
                self._handlers[method].remove(handler)  # type: ignore[arg-type]
            except ValueError:
                pass

    @staticmethod
    def _function_method(func: "Callable[..., Any]") -> str:
        """Map a generated CDP command method to its protocol method string.

        ``func`` is a bound command handle such as ``cdp.DOM.enable``; the domain
        is its class name and the command is its (snake_case) ``__name__`` turned
        back into the wire's camelCase -- e.g. ``cdp.DOM.enable`` -> ``"DOM.enable"``.
        """
        return f"{type(func.__self__).__name__}.{_camel(func.__name__)}"  # type: ignore[attr-defined]

    def on_function(
        self, func: "Callable[..., Any]", handler: FunctionHandler
    ) -> FunctionHandler:
        """Register ``handler`` to fire whenever a CDP command is sent.

        The analogue of :meth:`on` for *functions*: ``func`` is a generated
        command handle (e.g. ``page.cdp.DOM.disable``), and ``handler`` is called
        with the command's ``params`` dict each time that command completes on
        this target.  Returns the handler so it can be used as a decorator.
        """
        method = self._function_method(func)
        self._functions_handlers.setdefault(method, []).append(handler)
        return handler

    def off_function(
        self, func: "Callable[..., Any]", handler: FunctionHandler
    ) -> None:
        method = self._function_method(func)
        if method in self._functions_handlers:
            try:
                self._functions_handlers[method].remove(handler)
            except ValueError:
                pass

    async def wait_for[Ev: Event](
        self, event: "type[Ev]", *, timeout: Optional[float] = 30
    ) -> "Ev | Event":
        """Suspend until ``event`` fires once and return the deserialized event."""
        loop = asyncio.get_running_loop()
        future: asyncio.Future = loop.create_future()

        def _once(evt: Event) -> None:
            if not future.done():
                future.set_result(evt)

        self.on(event, _once)
        try:
            return await asyncio.wait_for(future, timeout)
        finally:
            self.off(event, _once)

    async def refresh_targets(self) -> list["Target"]:
        """Re-fetch the live target list and rebuild the child tree under self.

        ``Target.targetCreated`` is not reliably delivered for every target
        (iframe/worker targets discovered mid-navigation often arrive only as a
        ``targetInfoChanged``), so the tree is (re)built on demand from an
        authoritative ``Target.getTargets`` snapshot rather than trusting the
        event stream alone.

        Each child is nested under its parent (an iframe under the target of its
        ``parent_frame_id``; a popup under its ``opener_id``), rooting at this
        target.  Existing :class:`Target` objects are reused -- preserving their
        identity and any open websocket -- and targets gone from the snapshot are
        dropped.  Returns this target's direct children.
        """
        infos = (await self.cdp.Target.get_targets()).target_infos
        self._rebuild_tree(infos)
        return self.targets

    def _rebuild_tree(self, infos: list[TargetDomain.TargetInfo]) -> None:
        # ``getTargets`` is browser-wide, so group children by their parent and
        # then walk only the subtree rooted at *this* target -- a page must not
        # adopt unrelated top-level targets (other tabs, extensions, ...).
        children_of: dict[Optional[str], list[TargetDomain.TargetInfo]] = {}
        for info in infos:
            if info.target_id == self.id:
                continue
            parent_id = info.parent_frame_id or info.opener_id
            children_of.setdefault(parent_id, []).append(info)

        # Index existing Target objects across the tree so already-connected
        # nodes are reused (identity + open websocket preserved) rather than
        # recreated.
        known: dict[str, Target] = {}

        def collect(node: Target) -> None:
            for child in node._targets.values():
                known[child.id] = child
                collect(child)

        collect(self)
        for node in known.values():
            node._targets = {}
        self._targets = {}

        root_key = None if self.type_ == "browser" else self.id

        def attach(parent: Target, key: Optional[str], seen: set[str]) -> None:
            for info in children_of.get(key, ()):
                tid = info.target_id
                if tid in seen:  # guard against cyclic parent links
                    continue
                seen.add(tid)
                node = known.get(tid) or Target(info, parent)
                node._target = info
                node._parent = parent
                parent._targets[tid] = node
                attach(node, tid, seen)

        attach(self, root_key, set())

    async def _on_target_created(self, event: TargetDomain.TargetCreated):
        info = event.target_info
        parent_id = info.opener_id or info.parent_frame_id
        if parent_id is None or parent_id == self.id:
            target = Target(info, self)
            self._targets.setdefault(info.target_id, target)
            await target.connect()
        else:
            for target in self.targets:
                await target._on_target_created(event)

    async def _on_target_destroyed(self, event: TargetDomain.TargetDestroyed):
        if event.target_id in self._targets:
            target = self._targets.pop(event.target_id)
            await target.close()
        else:
            for target in self.targets:
                await target._on_target_destroyed(event)

    def _on_target_info_changed(self, event: TargetDomain.TargetInfoChanged):
        if self.id == event.target_info.target_id:
            self._target = event.target_info
        else:
            for target in self.targets:
                target._on_target_info_changed(event)

    async def _dispatch(self, method: str, params: dict) -> None:
        """Decode an incoming event and fan it out to all handlers."""
        cls = EVENT_REGISTRY.get(method)
        event: Any = cls.parse(params) if cls is not None else params
        handlers = list(self._handlers.get(method, ()))
        if cls is not None:
            handlers += list(cls._global_handlers)
        for handler in handlers:
            await self._invoke(handler, event)

    @staticmethod
    async def _invoke(
        handler: Callable[[Any], Awaitable[Any | None] | Any | None], event: Any
    ) -> None:
        # One failing handler must not stop the others (nor the dispatch loop).
        try:
            result = handler(event)
        except Exception:
            logger.exception("event handler %r failed", handler)
            return
        if asyncio.iscoroutine(result):
            asyncio.ensure_future(result)

    def __repr__(self) -> str:
        kind = type(self).__name__
        return f"<{kind}[{self.type_}] target={self.id} url={self._target.url:.25}>"

    __str__ = __repr__
