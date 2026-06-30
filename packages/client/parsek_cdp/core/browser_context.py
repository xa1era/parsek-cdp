"""Browser contexts -- isolated, incognito-like profiles within one browser.

A :class:`BrowserContext` groups pages that share cookies/storage and are
isolated from other contexts.  The context with ``id is None`` is the browser's
default context.

A context is *not* a separate CDP session: its commands go through the browser
session, so :attr:`cdp` and :attr:`connection` delegate to the browser.  All the
page/tab handling is inherited from :class:`PagableTarget`; pages added here
bubble to the browser via :attr:`_parent`.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from .pagable import PagableTarget

if TYPE_CHECKING:
    from .browser import Browser
    from .page import Page


class BrowserContext[T: Page](PagableTarget[T]):
    """A browser context (incognito-like profile)."""

    def __init__(self, browser: "Browser[T]", context_id: Optional[str] = None):
        super().__init__()
        self.browser = browser
        self.id = context_id
        self.page_class: type[T] = browser.page_class
        self._parent = browser
        self._cdp = browser.cdp

    @property
    def _scope_context_id(self) -> Optional[str]:
        return self.id

    @property
    def is_default(self) -> bool:
        return self.id is None

    def _bind_page(self, page: T) -> None:
        page.browser = self.browser
        page.browser_context = self

    async def close(self) -> None:
        """Dispose the context (and its pages). No-op for the default context."""
        if self.id is None:
            return
        await self.browser.cdp.Target.dispose_browser_context(
            browser_context_id=self.id
        )
        self.browser._forget_context(self.id)

    def __repr__(self) -> str:
        kind = "default" if self.is_default else self.id
        return f"<BrowserContext {kind} pages={len(self.pages)}>"
