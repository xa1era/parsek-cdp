"""Events for the Log domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import FieldMeta
from ..mixins.event import Event, register_event

if TYPE_CHECKING:
    from .types import LogEntry

@register_event("Log.entryAdded")
@dataclass
class EntryAdded(Event):
    """Issued when new message was logged."""
    entry: LogEntry
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('entry', 'entry', False, 'object', ref='Log.LogEntry'),
    )

__all__ = ["EntryAdded"]
