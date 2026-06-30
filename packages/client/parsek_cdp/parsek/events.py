"""Events of the Parsek contract.

Only the *protocol-level* events live here (browser lifecycle); per-feature
``Parsek.*`` events (e.g. ``Parsek.RequestListener.request``) are declared inside
their own feature package.  Every event is a :class:`~parsek_cdp.cdp.mixins.event.Event`
registered under its ``Parsek.*`` method name, so the client connection dispatch
deserializes and routes it exactly like a CDP event.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar, Optional

from ..cdp.mixins.datatype import FieldMeta
from ..cdp.mixins.event import Event, register_event
from .types import BrowserState


@register_event("Parsek.browserStateChanged")
@dataclass
class BrowserStateChanged(Event):
    """A supervised browser changed lifecycle state.

    Emitted by the supervisor on every transition (started, crashed, restarting,
    closed) and broadcast to the browser's control-channel clients.  ``reason``
    carries a human-readable cause for the abnormal transitions.
    """

    state: BrowserState
    reason: Optional[str] = None
    browser_uuid: Optional[str] = None

    __FIELDS__: ClassVar[tuple] = (
        FieldMeta("state", "state", False, "enum", ref="Parsek.BrowserState"),
        FieldMeta("reason", "reason", True, "primitive"),
        FieldMeta("browser_uuid", "browserUuid", True, "primitive"),
    )
