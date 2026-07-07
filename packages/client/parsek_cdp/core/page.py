"""A page target: a CDP session attached to a page/tab.

``Page`` is a bare host -- it attaches **no** features by default; every feature
(frame-tree tracking, request listening, ...) is optional and opted into:

* declaratively -- ``Page[Frames]`` / ``Page[Frames, RequestListener]`` (or
  chained ``Page[A][B]``); each is attached on construction;
* imperatively + type-safely -- ``page.get_feature(Frames)`` returns the feature
  typed as ``Frames`` (attaching it on first use).

A page *is its own main frame*: it subclasses :class:`Frame` (the main frame's id
equals the page's target id), so ``page.select(...)`` / ``page.evaluate(...)``
work on the top frame without any feature.  The frame *tree* (subframes, OOPIFs)
lives in the optional :class:`Frames` feature.
"""

from __future__ import annotations

import asyncio
from contextlib import asynccontextmanager
from typing import TYPE_CHECKING, AsyncIterator

from ..cdp import Target as TargetDomain
from .feature import Feature, FeatureHost
from .frame import Frame
from .target import Target

if TYPE_CHECKING:
    from .browser import Browser
    from .browser_context import BrowserContext


class NavigationError(Exception):
    """Raised by :meth:`Page.no_navigation` when the guarded block was cut short
    by a main-frame navigation (only when ``raise_=True``)."""


class _NavGuard:
    """Handle yielded by :meth:`Page.no_navigation`; ``navigated`` flips on nav."""

    navigated: bool = False


class Page[T: Feature](Target, FeatureHost[T], Frame):
    """A page (tab) target exposing every CDP domain through :attr:`cdp`.

    A page *is its own main frame*: it subclasses :class:`Frame` (in CDP the
    main frame's id equals the page's target id), so ``page.url`` and
    ``page.evaluate(...)`` operate on the top frame, while the full frame tree
    (and navigation like ``page.frames.children_of(page)``) lives in
    :attr:`frames`.

    Generic over the feature type so ``Page[RequestListener]`` is accepted by
    type checkers (the runtime composition is handled by ``FeatureHost``).
    """

    browser: "Browser"
    browser_context: "BrowserContext"

    def __init__(
        self,
        browser: Browser,
        target_info: TargetDomain.TargetInfo,
    ):
        Target.__init__(self, target_info, browser)
        self._init_features()
        self.browser = browser
        self.browser._targets[self.id] = self

    @property
    def frame_id(self):
        return self._frame.id

    async def connect(self) -> "Page[T]":
        """Open the page's own websocket, learn its main frame, start features."""
        await super().connect()
        tree = await self.cdp.Page.get_frame_tree()
        Frame.__init__(self, self, tree.frame_tree.frame, None)
        await self.wait_features_ready()
        return self

    async def navigate(self, url: str, *, wait_load: bool = False, timeout: float = 30):
        """Navigate to ``url``; optionally wait for the load event.

        ``Page.loadEventFired`` only arrives while the ``Page`` domain is enabled,
        so ``wait_load`` enables it for the duration here.  The waiter is armed
        *before* navigating, so a fast load that fires before the command returns
        is not missed.
        """
        from ..cdp.page.events import LoadEventFired

        if not wait_load:
            return await self.cdp.Page.navigate(url=url)

        async with self.domain_enabled(self.cdp.Page):
            loop = asyncio.get_running_loop()
            loaded: asyncio.Future = loop.create_future()

            def _on_load(_event: object) -> None:
                if not loaded.done():
                    loaded.set_result(None)

            self.on(LoadEventFired, _on_load)
            try:
                data = await self.cdp.Page.navigate(url=url)
                await asyncio.wait_for(loaded, timeout)
            finally:
                self.off(LoadEventFired, _on_load)
        return data

    @asynccontextmanager
    async def with_same_navigation(
        self, *, raise_: bool = True
    ) -> AsyncIterator[_NavGuard]:
        """Run the block only while the document stays the same.

        Guards a block of work against a main-frame navigation: if the page
        navigates (the main frame commits a new ``loaderId``) while the body
        runs, the body is cancelled at its next ``await`` -- so logic never keeps
        operating on a document that has been replaced underneath it::

            async with page.with_same_navigation():
                el = await page.select(selector="#row")
                await el.click()          # cut short if navigation happens here

        With ``raise_=True`` (default) a :class:`NavigationError` is raised when
        the block is cut short; with ``raise_=False`` it is swallowed and the
        yielded guard's ``navigated`` flag lets the caller decide (e.g. retry)::

            async with page.with_same_navigation(raise_=False) as guard:
                ...
            if guard.navigated:
                ...  # the block was interrupted by a navigation
        """
        from ..cdp.page.events import FrameNavigated

        guard = _NavGuard()
        baseline = self.loader_id
        task = asyncio.current_task()

        def _on(e: "FrameNavigated") -> None:
            if (
                e.frame.parent_id is None
                and e.frame.loader_id != baseline
                and not guard.navigated
            ):
                guard.navigated = True
                if task is not None:
                    task.cancel()

        self.on(FrameNavigated, _on)
        try:
            async with self.domain_enabled(self.cdp.Page):
                yield guard
                if guard.navigated and raise_:
                    raise NavigationError(
                        f"navigation away from {self.url!r} cut the block short"
                    )
        except asyncio.CancelledError:
            if not guard.navigated:
                raise  # a genuine external cancellation -- propagate untouched
            if raise_:
                raise NavigationError(
                    f"navigation away from {self.url!r} cut the block short"
                ) from None
        finally:
            self.off(FrameNavigated, _on)
