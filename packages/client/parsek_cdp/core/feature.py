"""Unified feature framework -- one feature class, two roles (server / client),
plus the host mixin that composes features onto targets/pages.

A feature is written **once** and runs in either role:

* **server (producer)** -- enables the CDP ``domains`` it declares, receives their
  raw events, and runs the ``@on(<CdpEvent>)`` handlers.  A handler marked
  ``@emit(<ParsekEvent>)`` has its return value sent to the client *and* fed
  through the feature's own reducers, so state is built by the same code paths;
* **client (view)** -- receives the ``Parsek.*`` events off the wire and runs the
  ``@on(<ParsekEvent>)`` reducers, which build the exact same state.

Because the reducers run in both roles, the feature's public API (properties /
methods reading that state) is identical client- and server-side -- and the
embedded/local mode just runs the server role in-process.

Three building blocks:

* ``domains``           -- CDP domains the feature owns; auto-enabled, and their
  raw events are suppressed from client passthrough (the proxy reads
  :meth:`Feature.suppressed_prefixes`);
* ``@on(Event, ...)``   -- register a method as a handler.  A CDP event makes it a
  *producer* (server only); a ``Parsek.*`` event makes it a *reducer* (both);
* ``@emit(Event)``      -- the handler's return (an event instance, or a list of
  them, or ``None`` to skip) is published: emitted to the client and reduced
  locally;
* ``@parsek_type(name)``-- declare a wire type whose ``__FIELDS__`` are derived
  from its annotations (no hand-written ``FieldMeta``).

:class:`FeatureHost` is the mixin that targets/pages use to compose features
declaratively (``Page[RequestListener]``) or attach them imperatively
(:meth:`FeatureHost.attach` / :meth:`FeatureHost.get_feature`).  Hosted features
are created in the host's :attr:`_feature_role` (``"local"`` -- direct to the
browser -- for a plain :class:`~parsek_cdp.core.page.Page`) and their async
:meth:`Feature.start` is scheduled, then awaited together by
:meth:`wait_features_ready`.
"""

from __future__ import annotations

import asyncio
import dataclasses
import typing
from enum import Enum
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    ClassVar,
    Dict,
    List,
    Optional,
    Tuple,
    Type,
    get_args,
    get_origin,
)

from ..cdp.mixins.datatype import DataType, FieldMeta, register

if TYPE_CHECKING:
    from .page import Page

__all__ = ["Feature", "FeatureHost", "parsek_type", "on", "emit"]

# python class -> its registered qualified protocol name, for nested-ref resolution.
_QUALNAME: dict[type, str] = {}


# --------------------------------------------------------------------------- #
# custom-type decorator: __FIELDS__ from annotations
# --------------------------------------------------------------------------- #


def _camel(name: str) -> str:
    head, *tail = name.split("_")
    return head + "".join(p[:1].upper() + p[1:] for p in tail)


def _meta_for(py: str, json: str, hint: Any, optional: bool) -> FieldMeta:
    origin = get_origin(hint)
    if origin is typing.Union:  # Optional[X] / Union[X, None]
        args = [a for a in get_args(hint) if a is not type(None)]  # noqa: E721
        return _meta_for(py, json, args[0], True)
    if origin in (list, typing.List):
        inner = _meta_for("", "", get_args(hint)[0], False)
        return FieldMeta(py, json, optional, "array", inner=inner)
    if isinstance(hint, type) and issubclass(hint, Enum):
        return FieldMeta(py, json, optional, "enum", ref=_QUALNAME[hint])
    if isinstance(hint, type) and issubclass(hint, DataType):
        return FieldMeta(py, json, optional, "object", ref=_QUALNAME[hint])
    return FieldMeta(py, json, optional, "primitive")  # str/int/float/bool/dict/Any


def parsek_type(name: str) -> Callable[[type], type]:
    """Register ``cls`` as a wire type and synthesize ``__FIELDS__`` from its hints.

    The class must subclass :class:`~parsek_cdp.cdp.mixins.datatype.DataType`.
    ``@dataclass`` is applied if not already.  ``snake_case`` fields map to
    ``camelCase`` wire keys; a field is optional iff it has a default.  Nested
    enum/``DataType`` references resolve by qualified name, so declare leaf types
    before the types that reference them.
    """

    def deco(cls: type) -> type:
        if not dataclasses.is_dataclass(cls):
            cls = dataclasses.dataclass(cls)
        register(name)(cls)
        _QUALNAME[cls] = name
        if not cls.__dict__.get("__FIELDS__"):
            hints = typing.get_type_hints(cls)
            fields = tuple(
                _meta_for(
                    f.name,
                    _camel(f.name),
                    hints.get(f.name, f.type),
                    f.default is not dataclasses.MISSING
                    or f.default_factory is not dataclasses.MISSING,
                )
                for f in dataclasses.fields(cls)
            )
            cls.__FIELDS__ = fields  # type: ignore[attr-defined]
        return cls

    return deco


# --------------------------------------------------------------------------- #
# handler decorators
# --------------------------------------------------------------------------- #


def on(*events: type) -> Callable[[Callable], Callable]:
    """Register a method as a handler for one or more events (CDP or Parsek)."""

    def deco(fn: Callable) -> Callable:
        fn._handles = tuple(getattr(fn, "_handles", ())) + events  # type: ignore[attr-defined]
        return fn

    return deco


def emit(event_cls: type) -> Callable[[Callable], Callable]:
    """Mark a handler whose return value is published as ``event_cls``.

    Return an instance (or a list of instances) to publish, or ``None`` to skip.
    """

    def deco(fn: Callable) -> Callable:
        fn._emits = event_cls  # type: ignore[attr-defined]
        return fn

    return deco


# --------------------------------------------------------------------------- #
# the feature base
# --------------------------------------------------------------------------- #


class Feature:
    """A behaviour bound to a host, runnable in one of three roles.

    * ``"local"`` -- direct to the browser, no Parsek server: the producers
      (``@on(<CdpEvent>)``) subscribe to raw CDP on the host target and feed the
      reducers in-process; nothing is sent over a wire.  This is what a plain
      :class:`~parsek_cdp.core.page.Page` uses.
    * ``"server"`` -- the proxy feeds raw CDP via :meth:`handle_cdp_event`; a
      produced event is emitted to the client *and* reduced locally (for the
      snapshot).  ``host`` exposes ``send_cdp`` / ``emit_parsek``.
    * ``"client"`` -- only the reducers run, fed by ``Parsek.*`` events arriving
      off the wire on the host target.

    The reducers run in every role, so the public API (state they build) is
    identical regardless of where the feature runs.
    """

    #: CDP domains this feature owns, as the namespaces imported from
    #: :mod:`parsek_cdp.cdp` -- e.g. ``domains = (Network, Page)``.  They are
    #: auto-enabled on the server and their raw events are suppressed from
    #: client passthrough.
    domains: tuple = ()

    def __init__(self, host: Page, *, role: str = "client") -> None:
        self.host = host
        self.role = role
        #: cdp method -> (event class, bound handler, emits class | None)
        self._producers: dict[str, tuple[type, Callable, Optional[type]]] = {}
        #: parsek method -> list[(event class, bound handler)]
        self._reducers: dict[str, list[tuple[type, Callable]]] = {}
        self._scan()

    def _scan(self) -> None:
        for name in dir(type(self)):
            func = getattr(type(self), name, None)
            handles = getattr(func, "_handles", ())
            if not handles:
                continue
            bound = getattr(self, name)
            for ev in handles:
                method = ev.EVENT_METHOD
                if method.startswith("Parsek."):
                    self._reducers.setdefault(method, []).append((ev, bound))
                else:
                    self._producers[method] = (ev, bound, getattr(func, "_emits", None))

    @classmethod
    def suppressed_prefixes(cls) -> tuple[str, ...]:
        """Raw CDP method prefixes the proxy must not pass through (server)."""
        return tuple(f"{d.DOMAIN}." for d in cls.domains)

    # -- lifecycle --------------------------------------------------------- #

    async def start(self) -> None:
        """Wire the feature for its role (enable domains and/or bind handlers)."""
        if self.role == "server":
            for domain in self.domains:
                await self.host.send_cdp(f"{domain.DOMAIN}.enable", {})
        elif self.role == "local":
            # Direct to the browser: enable domains on the target, subscribe the
            # producers to raw CDP, and reduce their output in-process.
            for domain in self.domains:
                await self.host.send(f"{domain.DOMAIN}.enable", {})
            for ev_cls, fn, emits in self._producers.values():
                self.host.on(ev_cls, self._local_producer(fn, emits))
        else:  # client
            for handlers in self._reducers.values():
                for ev_cls, fn in handlers:
                    self.host.on(ev_cls, fn)  # connection dispatch routes Parsek.*

    # -- server: raw CDP in (fed by the proxy) ----------------------------- #

    async def handle_cdp_event(
        self, method: str, params: dict, session_id: str
    ) -> None:
        """Feed one raw CDP event to its producer (called by the proxy, server)."""
        entry = self._producers.get(method)
        if entry is None:
            return
        ev_cls, fn, emits = entry
        result = fn(ev_cls.parse(params))
        if asyncio.iscoroutine(result):
            result = await result
        if emits is not None and result is not None:
            events = result if isinstance(result, (list, tuple)) else (result,)
            for event in events:
                await self._publish(event, session_id)

    async def _publish(self, event: Any, session_id: str) -> None:
        """Emit a produced event to the client and reduce it locally (server)."""
        await self.host.emit_parsek(event.EVENT_METHOD, event.to_json(), session_id)
        self._reduce(event)

    # -- local: raw CDP in (subscribed directly on the target) ------------- #

    def _local_producer(self, fn: Callable, emits: Optional[type]) -> Callable:
        """Wrap a producer so its return is reduced in-process (no wire emit)."""

        def handler(event: Any) -> None:
            result = fn(event)
            if asyncio.iscoroutine(result):
                asyncio.ensure_future(self._reduce_async(result, emits))
            elif emits is not None:
                self._reduce_result(result, emits)

        return handler

    async def _reduce_async(self, coro: Any, emits: Optional[type]) -> None:
        if emits is not None:
            self._reduce_result(await coro, emits)

    def _reduce_result(self, result: Any, emits: Optional[type]) -> None:
        if result is None:
            return
        for event in result if isinstance(result, (list, tuple)) else (result,):
            self._reduce(event)

    def _reduce(self, event: Any) -> None:
        """Run every reducer registered for ``event`` (builds feature state)."""
        for _ev_cls, fn in self._reducers.get(event.EVENT_METHOD, ()):
            fn(event)

    # -- snapshot ---------------------------------------------------------- #

    async def snapshot(self) -> dict:
        """State for this feature's ``get*`` command (override in stateful features)."""
        return {}


# --------------------------------------------------------------------------- #
# the host mixin
# --------------------------------------------------------------------------- #


class FeatureHost[T: Feature = Feature]:
    """Mixin giving a class the ``[Feat]`` composition + ``attach``/``get_feature`` API."""

    #: Role given to features hosted here ("local" = direct to the browser).
    _feature_role: ClassVar[str] = "local"
    #: Feature classes auto-attached on construction (extended by ``cls[Feat]``).
    _feature_classes: ClassVar[Tuple[Type[Feature], ...]] = ()
    # Cache of composed subclasses so ``Cls[Feat] is Cls[Feat]``.
    _composed_cache: ClassVar[Dict[Tuple[type, ...], type]] = {}

    #: Flipped on by :meth:`wait_features_ready` once the host's connection is
    #: live; until then every ``start()`` is deferred (it would otherwise send
    #: CDP commands before the websocket is open).
    _features_connected: bool = False

    def _init_features(self) -> None:
        """Instantiate every declared feature. Call once from ``__init__``."""
        self._features: Dict[Type[Feature], Feature] = {}
        self._pending_starts: List = []  # start() coroutines awaiting connect
        self._start_tasks: List[asyncio.Task] = []
        self._features_connected = False
        for feat_cls in self._feature_classes:
            self.attach(feat_cls)

    def attach[FeatT: Feature](self, feat_cls: Type[FeatT]) -> FeatT:
        """Instantiate ``feat_cls`` for this host's role and schedule its start.

        Access an attached feature via :meth:`get_feature` (no magic attribute is
        bound on the host).
        """
        feat = feat_cls(self, role=self._feature_role)  # type: ignore[arg-type]
        self._features[feat_cls] = feat
        self._schedule_coro(feat.start())
        return feat

    def _schedule_coro(self, coro) -> None:
        """Start ``coro`` once the host is connected, else defer it.

        Shared by feature ``start()`` and built-in page setup (e.g. frame
        tracking), so everything that must be enabled is awaited at one point
        (:meth:`wait_features_ready`) -- and never before the websocket is open.
        """
        if not self._features_connected:
            self._pending_starts.append(coro)  # not connected yet -- defer
            return
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            self._pending_starts.append(coro)  # no loop yet -- defer
            return
        self._start_tasks.append(loop.create_task(coro))

    async def wait_features_ready(self) -> None:
        """Await every feature's :meth:`Feature.start` (and any deferred coros)."""
        self._features_connected = True
        for coro in self._pending_starts:
            self._start_tasks.append(asyncio.ensure_future(coro))
        self._pending_starts.clear()
        if self._start_tasks:
            await asyncio.gather(*self._start_tasks)
            self._start_tasks.clear()

    def get_feature[FeatT: Feature](self, feat_cls: Type[FeatT]) -> FeatT:
        """Return the attached ``feat_cls`` instance, attaching it on first use."""
        feat = self._features.get(feat_cls)
        if feat is None:
            feat = self.attach(feat_cls)
        return feat  # type: ignore[return-value]

    def has_feature(self, feat_cls: Type[Feature]) -> bool:
        return feat_cls in self._features

    def __class_getitem__(cls, item):
        feats = item if isinstance(item, tuple) else (item,)
        if feats and all(isinstance(f, type) and issubclass(f, Feature) for f in feats):
            key = (cls, *feats)
            cached = FeatureHost._composed_cache.get(key)
            if cached is not None:
                return cached
            name = f"{cls.__name__}[{', '.join(f.__name__ for f in feats)}]"
            composed = type(
                name, (cls,), {"_feature_classes": (*cls._feature_classes, *feats)}
            )
            FeatureHost._composed_cache[key] = composed
            return composed
        return super().__class_getitem__(item)  # type: ignore[misc]
