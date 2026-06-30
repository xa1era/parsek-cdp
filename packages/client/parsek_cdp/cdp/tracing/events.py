"""Events for the Tracing domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import FieldMeta
from ..mixins.event import Event, register_event

if TYPE_CHECKING:
    from .types import (
        StreamCompression,
        StreamFormat,
    )
    from ..io.types import StreamHandle as IO_StreamHandle

@register_event("Tracing.bufferUsage")
@dataclass
class BufferUsage(Event):
    percent_full: Optional[float] = None
    event_count: Optional[float] = None
    value: Optional[float] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('percent_full', 'percentFull', True, 'primitive'),
        FieldMeta('event_count', 'eventCount', True, 'primitive'),
        FieldMeta('value', 'value', True, 'primitive'),
    )


@register_event("Tracing.dataCollected")
@dataclass
class DataCollected(Event):
    """
    Contains a bucket of collected trace events. When tracing is stopped collected events will be
    sent as a sequence of dataCollected events followed by tracingComplete event.
    """
    value: List[Dict[str, Any]]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('value', 'value', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


@register_event("Tracing.tracingComplete")
@dataclass
class TracingComplete(Event):
    """
    Signals that tracing is stopped and there is no trace buffers pending flush, all data were
    delivered via dataCollected events.
    """
    data_loss_occurred: bool
    stream: Optional[IO_StreamHandle] = None
    trace_format: Optional[StreamFormat] = None
    stream_compression: Optional[StreamCompression] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('data_loss_occurred', 'dataLossOccurred', False, 'primitive'),
        FieldMeta('stream', 'stream', True, 'primitive'),
        FieldMeta('trace_format', 'traceFormat', True, 'enum', ref='Tracing.StreamFormat'),
        FieldMeta('stream_compression', 'streamCompression', True, 'enum', ref='Tracing.StreamCompression'),
    )

__all__ = ["BufferUsage", "DataCollected", "TracingComplete"]
