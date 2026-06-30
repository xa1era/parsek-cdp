"""Wire types of the Parsek contract -- the protocol *between* client and server.

This is deliberately tiny: browser *control* goes over plain CDP (the server is
a transparent proxy), so the only thing that needs its own contract is what CDP
cannot express -- the **lifecycle** of a server-supervised browser.  These types
are shipped in the client distribution and reused by the server, built on the
same :class:`~parsek_cdp.cdp.mixins.datatype` machinery as the generated CDP
types so they (de)serialize identically.
"""

from __future__ import annotations

from enum import Enum

from ..cdp.mixins.datatype import register


class BrowserState(str, Enum):
    """Lifecycle state of a supervised browser.

    Broadcast to control-channel clients as
    :class:`~parsek_cdp.parsek.events.BrowserStateChanged` so a parser can react
    (re-attach, re-navigate) instead of hanging on a dead socket.  ``str`` mixin
    so the value serializes directly to JSON.
    """

    STARTING = "starting"
    READY = "ready"
    CRASHED = "crashed"
    RESTARTING = "restarting"
    CLOSED = "closed"


# Referenced by ``ref`` from the event field below, so it must be resolvable in
# the TYPE_REGISTRY.
register("Parsek.BrowserState")(BrowserState)
