"""Events for the PerformanceTimeline domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import FieldMeta
from ..mixins.event import Event, register_event

if TYPE_CHECKING:
    from .types import TimelineEvent

@register_event("PerformanceTimeline.timelineEventAdded")
@dataclass
class TimelineEventAdded(Event):
    """Sent when a performance timeline event is added. See reportPerformanceTimeline method."""
    event: TimelineEvent
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('event', 'event', False, 'object', ref='PerformanceTimeline.TimelineEvent'),
    )

__all__ = ["TimelineEventAdded"]
