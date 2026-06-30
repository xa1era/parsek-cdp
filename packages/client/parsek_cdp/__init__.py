"""parsek_cdp -- a Chrome DevTools Protocol client.

``cdp`` is the generated protocol layer (one module per domain); ``core`` is the
hand-written runtime (connection, browser, page, request tracking).

Quickstart::

    import asyncio
    from parsek_cdp import Browser, Page, RequestListener

    async def main():
        browser = await Browser.connect_http(
            "http://127.0.0.1:9222", page_class=Page[RequestListener]
        )
        page = await browser.new_page("https://example.com")
        await page.navigate("https://example.com", wait_load=True)
        print(len(page.request_listener.requests), "requests captured")

    asyncio.run(main())
"""

import logging

from ._logging import TRACE, get_logger
from .core import (
    Browser,
    BrowserContext,
    Element,
    Feature,
    Page,
    ProtocolError,
    Target,
)
from .core.frame import ElementState, Frame, LoadState
from .core.page import NavigationError
from .features import RequestListener

# Library best practice: stay silent unless the application configures logging.
get_logger(__name__).addHandler(logging.NullHandler())

__all__ = [
    "TRACE",
    "Browser",
    "BrowserContext",
    "Element",
    "ElementState",
    "Feature",
    "Frame",
    "LoadState",
    "NavigationError",
    "Page",
    "ProtocolError",
    "RequestListener",
    "Target",
]
