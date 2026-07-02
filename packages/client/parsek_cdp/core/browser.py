"""Browser-level target: the websocket endpoint and target management."""

from __future__ import annotations

import asyncio
import json
import urllib.parse
import urllib.request
from typing import ClassVar, List, Optional

from ..cdp import CDP
from ..cdp import Target as TargetDomain
from .browser_context import BrowserContext
from .pagable import PagableTarget
from .page import Page
from .target import (
    CDPConnection,
    ProtocolError,
    Target,
    cdp_host,
    cdp_target_path,
    ws_origin,
)


class Browser[T: Page](Target, PagableTarget[T]):
    """The browser endpoint.

    Connects to the browser-level websocket, discovers page targets and exposes
    them as :class:`Page` objects -- each on its own websocket
    (``{host}/devtools/page/{id}``), with the host kept in the :data:`cdp_host`
    context variable.  Pages are grouped into :class:`BrowserContext` profiles;
    the default context holds pages created without an explicit one.

    Generic over the page class: ``page_class`` drives ``T``, so
    ``browser.pages``, ``new_page()`` and contexts are typed to the page type
    you pass (e.g. ``Browser.connect_http(url, page_class=Page[RequestListener])``).
    """

    #: Page class captured from ``Browser[Page[...]]`` subscription, used by
    #: :meth:`get_distant_browser` so the feature set is derived automatically.
    _page_class_override: ClassVar[Optional[type]] = None

    def __class_getitem__(cls, item):
        """``Browser[Page[Feat]]`` -> a real subclass remembering that page class.

        A bare type parameter (``Browser[P]`` inside generic code) falls back to
        the normal typing machinery.
        """
        if isinstance(item, type) and issubclass(item, Page):
            name = f"{cls.__name__}[{item.__name__}]"
            return type(name, (cls,), {"_page_class_override": item})
        return super().__class_getitem__(item)  # type: ignore[misc]

    def __init__(
        self,
        target_info: TargetDomain.TargetInfo,
        *,
        page_class: type[T] = Page,
    ):
        Target.__init__(self, target_info, None)
        PagableTarget.__init__(self)
        self.page_class: type[T] = page_class
        self._contexts: dict[Optional[str], BrowserContext[T]] = {}
        self.default_context: BrowserContext[T] | None = None

    @property
    def contexts(self):
        return list(self._contexts.values())

    @property
    def _scope_context_id(self) -> Optional[str]:
        return None

    @classmethod
    async def connect_http[P: Page = Page](
        cls,
        endpoint: str = "http://127.0.0.1:9222",
        *,
        page_class: type[P] = Page,
    ) -> "Browser[P]":
        """Discover the websocket via ``/json/version`` then connect.

        Binds :data:`cdp_host` to the endpoint's origin so every page connected
        afterwards reaches the browser at the same host without it being passed
        around.
        """
        with urllib.request.urlopen(f"{endpoint.rstrip('/')}/json/version") as resp:
            info = json.loads(resp.read())
        ws_url = info["webSocketDebuggerUrl"]
        cdp_host.set(ws_origin(ws_url))

        boot = CDPConnection()
        await boot._open(ws_url)
        try:
            browser_info = (await CDP(boot).Target.get_target_info()).target_info
        finally:
            await boot.close()

        browser = Browser[P](browser_info, page_class=page_class)
        await browser.connect(ws_url)
        await browser._discover()
        return browser

    @classmethod
    async def get_distant_browser(
        cls,
        server: str = "http://127.0.0.1:9333",
        *,
        features: Optional[tuple] = None,
        page_class: Optional[type] = None,
        **launch,
    ) -> "Browser[T]":
        """Create a browser on a parsek-cdp-server and return it, connected.

        ``Browser[Page[RequestListener]].get_distant_browser("http://host:9333",
        headless=True)`` issues ``POST /browsers?feature=RequestListener`` with the
        launch settings (``headless``, ``executable``, ``extra_args``, ...) in the
        body, then connects to the proxy's control channel.  The returned browser
        drives the *remote* browser exactly like a local one -- pages connect to
        the proxy's per-target endpoints and the named features are aggregated
        server-side.

        The feature set defaults to the ones declared on the subscripted page
        class (``Page[RequestListener]`` -> ``RequestListener``); pass ``features``
        to override.
        """
        resolved_page = page_class or cls._page_class_override or Page
        feats = (
            features
            if features is not None
            else getattr(resolved_page, "_feature_classes", ())
        )
        query = "&".join(f"feature={urllib.parse.quote(f.__name__)}" for f in feats)
        url = f"{server.rstrip('/')}/browsers" + (f"?{query}" if query else "")
        payload = json.dumps(launch).encode()
        # Run the blocking HTTP POST off the event loop so it never stalls it
        # (notably when client and server share one loop in tests).
        info = await asyncio.to_thread(cls._post_json, url, payload)

        control_url = info["wsUrl"]
        suffix = "/control"
        ws_base = (
            control_url[: -len(suffix)] if control_url.endswith(suffix) else control_url
        )
        cdp_host.set(ws_base)
        cdp_target_path.set("/page/")

        boot = CDPConnection()
        await boot._open(control_url)
        try:
            browser_info = (await CDP(boot).Target.get_target_info()).target_info
        finally:
            await boot.close()

        # Pages on a remote browser run their features as *clients* (consuming the
        # server-aggregated ``Parsek.*`` events), not "local" (which would digest
        # raw CDP -- exactly what the server already suppresses).
        remote_page = type(
            resolved_page.__name__,
            (resolved_page,),
            {"_feature_role": "client"},
        )
        browser = cls(browser_info, page_class=remote_page)
        await browser.connect(control_url)
        await browser._discover()
        return browser

    @staticmethod
    def _post_json(url: str, payload: bytes) -> dict:
        request = urllib.request.Request(
            url,
            data=payload,
            method="POST",
            headers={"Content-Type": "application/json"},
        )
        with urllib.request.urlopen(request) as resp:
            return json.loads(resp.read())

    async def _discover(self) -> None:
        """Populate contexts and pages from the live browser (after connect)."""
        contexts = await self.cdp.Target.get_browser_contexts()
        for context_id in contexts.browser_context_ids:
            self._contexts[context_id] = BrowserContext(self, context_id)
        for target in self.targets:
            target_data = target._target
            if target_data.type_ not in ("page", "tab"):
                continue
            page = await self._ensure_page(target_data)
            self._pages[target.id] = page
            if target_data.browser_context_id not in self._contexts:
                context = BrowserContext(self, target_data.browser_context_id)
                self._contexts[target_data.browser_context_id] = context
                self.default_context = context
            self._contexts[target_data.browser_context_id]._pages[target.id] = page

    async def connect(self, url: Optional[str] = None) -> "Browser[T]":
        """Connect the browser websocket and start watching for page targets.

        The browser endpoint's ws path id does not match its ``target_id``, so
        :meth:`connect_http` passes the discovered ``webSocketDebuggerUrl`` as
        ``url``.  Generic target tracking is wired by :meth:`Target.connect`; the
        page-specific discovery handling lives in :class:`PagableTarget` and is
        registered here on the browser's own connection.
        """
        await super().connect(url)
        await self.cdp.Target.set_discover_targets(discover=True)
        await self.refresh_targets()
        self.watch(self)
        return self

    async def create_context(
        self,
        *,
        dispose_on_detach: Optional[bool] = None,
        proxy_server: Optional[str] = None,
        proxy_bypass_list: Optional[str] = None,
    ):
        """Create a fresh, isolated browser context (incognito-like)."""
        result = await self.cdp.Target.create_browser_context(
            dispose_on_detach=dispose_on_detach,
            proxy_server=proxy_server,
            proxy_bypass_list=proxy_bypass_list,
        )
        ctx = BrowserContext[T](self, result.browser_context_id)
        self._contexts[ctx.id] = ctx
        return ctx

    async def fetch_contexts(self) -> List[BrowserContext]:
        """Sync :attr:`contexts` with the browser and return them all."""
        result = await self.cdp.Target.get_browser_contexts()
        for cid in result.browser_context_ids:
            self._contexts.setdefault(cid, BrowserContext(self, cid))
        return list(self._contexts.values())

    def _context_for(self, context_id: Optional[str]) -> BrowserContext[T]:
        ctx = self._contexts.get(context_id)
        if ctx is None:
            ctx = BrowserContext(self, context_id)
            self._contexts[context_id] = ctx
        return ctx

    def _forget_context(self, context_id: str) -> None:
        ctx = self._contexts.pop(context_id, None)
        if ctx is not None:
            for target_id in list(ctx._pages):
                self._drop_page(target_id)

    async def close(self) -> None:
        """Close the browser: quit the process, then tear down the connection.

        :meth:`Target.close` alone only closes the local websocket -- the browser
        stays alive.  We first ask the browser to quit via ``Browser.close``, then
        run the base teardown (recv task, websockets, child targets).

        For a server-managed browser the ``Browser.close`` frame is intercepted on
        the proxy's control channel and turned into a graceful supervisor
        shutdown (so the exit is not mistaken for a crash and relaunched).

        ``Browser.close`` makes the browser drop the connection as it exits, so
        the command's reply may never arrive (the socket closes first); a
        :class:`ConnectionError` here means the browser is already gone, which is
        exactly what we want, so it is swallowed.
        """
        try:
            await self.cdp.Browser.close()
        except (ConnectionError, ProtocolError):
            pass
        await super().close()
