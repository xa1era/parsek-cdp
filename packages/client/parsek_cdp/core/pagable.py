"""``PagableTarget`` -- shared management of pages (the page/tab handling).

Both :class:`Browser` (all pages) and :class:`BrowserContext` (pages of one
context) manage a collection of pages with identical bookkeeping, so the whole
page/tab lifecycle -- *including reacting to the ``Target.*`` discovery events*
-- lives here:

* :meth:`watch` registers the discovery handlers on the connection that delivers
  them (the browser's own websocket);
* :meth:`_on_target_created` / :meth:`_on_target_destroyed` /
  :meth:`_on_target_info_changed` react to the protocol events;
* :meth:`new_page` issues ``Target.createTarget`` and waits for the matching
  target to be discovered;
* :meth:`_ensure_page` builds a :class:`Page` (via ``self.page_class``), connects
  its own websocket, binds it and registers it.

Pages are keyed by their **target id** (each target has its own websocket, so
there is no multiplexing ``sessionId``).  A page registered in a scope *bubbles*
to its :attr:`_parent` (a context's parent is its browser), so a page created in
a context also lands in the browser's global registry -- one :class:`Page`
instance shared by both.  The only browser-specific bit is resolving which
context owns a target, exposed through :meth:`_context_for` (defaults to
``self``; the browser overrides it).
"""

from __future__ import annotations

import asyncio
import functools
from typing import TYPE_CHECKING, Callable, Dict, List, Optional, cast

from ..cdp import Target as TargetDomain

if TYPE_CHECKING:
    from ..cdp import CDP
    from .browser import Browser
    from .page import Page
    from .target import Target

PageCallback = Callable[["Page"], None]


class PagableTarget[T: Page]:
    """Mixin managing a collection of pages within a scope."""

    _cdp: CDP
    page_class: type[T]
    _parent: PagableTarget[T] | None = None

    def __init__(self) -> None:
        self._pages: Dict[TargetDomain.TargetID, T] = {}
        self._page_callbacks: List[PageCallback] = []
        self._page_waiters: List[list] = []

    @property
    def pages(self):
        return list(self._pages.values())

    @property
    def _scope_context_id(self) -> Optional[str]:
        """Browser-context id new pages are created in (``None`` = default)."""
        raise NotImplementedError

    def _bind_page(self, page: T) -> None:
        """Set ``page.browser`` / ``page.browser_context``. Overridden per scope."""

    def _context_for(self, context_id: Optional[str]) -> "PagableTarget[T]":
        """Resolve the scope that owns a target. Browser overrides; else self."""
        return self

    def watch(self, connection: "Target") -> None:
        """Register the page-discovery handlers on ``connection``'s websocket.

        Only the browser calls this (its websocket is where ``Target.*`` events
        arrive); contexts are driven by the browser routing through
        :meth:`_context_for`.
        """
        connection.on(TargetDomain.TargetCreated, self.__on_target_created)
        connection.on(TargetDomain.TargetDestroyed, self.__on_target_destroyed)
        connection.on(TargetDomain.TargetInfoChanged, self.__on_target_info_changed)

    def __on_target_created(self, event: TargetDomain.TargetCreated) -> None:
        info = event.target_info
        if info.type_ in ("page", "tab"):
            scope = self._context_for(info.browser_context_id)
            asyncio.ensure_future(scope._ensure_page(info))

    def __on_target_destroyed(self, event: TargetDomain.TargetDestroyed) -> None:
        self._drop_page(event.target_id)

    def __on_target_info_changed(self, event: TargetDomain.TargetInfoChanged) -> None:
        page = self.get_page(target_id=event.target_info.target_id)
        if page is not None:
            page._target = event.target_info

    def on_page(self, callback: PageCallback) -> PageCallback:
        """Register a callback invoked for every page added to this scope."""
        self._page_callbacks.append(callback)

        @functools.wraps(callback)
        def wrapper(page: Page):
            callback(page)

        return wrapper

    @property
    def page_list(self) -> List[T]:
        return list(self._pages.values())

    def get_page(self, *, target_id: Optional[str] = None) -> Optional[T]:
        """Look a page up by target id."""
        if target_id is not None:
            return self._pages.get(target_id)
        return None

    async def new_page(self, url: str = "about:blank", *, timeout: float = 30) -> T:
        """Create a new page/tab in this scope and return it once connected.

        Relies on target discovery to deliver the new target, build the page and
        open its own websocket.
        """
        loop = asyncio.get_running_loop()
        future: asyncio.Future = loop.create_future()
        waiter: list = [None, future]
        self._page_waiters.append(waiter)
        try:
            created = await self._cdp.Target.create_target(
                url=url,
                browser_context_id=self._scope_context_id,
            )
            waiter[0] = created.target_id
            existing = self.get_page(target_id=created.target_id)
            if existing is not None and not future.done():
                future.set_result(existing)
            page: T = await asyncio.wait_for(future, timeout)
            await page.wait_features_ready()
            return page
        finally:
            if waiter in self._page_waiters:
                self._page_waiters.remove(waiter)

    async def _ensure_page(self, target_info: TargetDomain.TargetInfo) -> T:
        """Build, connect + register a page in this scope (once per target)."""
        page = self._pages.get(target_info.target_id)
        if page is None:
            owner = cast("Browser[T]", self._parent or self)
            page = self.page_class(owner, target_info)
            self._bind_page(page)
            await page.connect()
            await page.wait_features_ready()
            self._add_page(page)
        return page

    def _add_page(self, page: T) -> None:
        if page.id is not None:
            self._pages[page.id] = page
        for callback in list(self._page_callbacks):
            callback(page)
        for waiter in list(self._page_waiters):
            target_id, future = waiter
            if target_id == page.id and not future.done():
                future.set_result(page)
        if self._parent is not None:
            self._parent._add_page(page)  # bubble to the global registry

    def _drop_page(self, target_id: Optional[str]) -> None:
        page = self._pages.pop(target_id or "", None)
        if page is None:
            return
        context = getattr(page, "browser_context", None)
        if context is not None and context is not self:
            context._remove_page(page.id)

    def _remove_page(self, target_id: Optional[str]) -> None:
        self._pages.pop(target_id or "", None)
