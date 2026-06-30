"""Events for the Console domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import FieldMeta
from ..mixins.event import Event, register_event

if TYPE_CHECKING:
    from .types import ConsoleMessage

@register_event("Console.messageAdded")
@dataclass
class MessageAdded(Event):
    """Issued when new console message is added."""
    message: ConsoleMessage
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('message', 'message', False, 'object', ref='Console.ConsoleMessage'),
    )

__all__ = ["MessageAdded"]
