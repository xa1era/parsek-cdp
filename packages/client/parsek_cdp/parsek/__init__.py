"""The Parsek contract -- the small slice of protocol that is *not* plain CDP.

Browser control flows over CDP through the transparent proxy, so the only shared
contract is the lifecycle of a server-supervised browser: the :class:`BrowserState`
enum and the :class:`BrowserStateChanged` event the server broadcasts and the
client consumes.  Shipped here in the client distribution so both sides share one
wire definition.
"""

from __future__ import annotations

from .events import BrowserStateChanged
from .types import BrowserState

__all__ = [
    "BrowserState",
    "BrowserStateChanged",
]
