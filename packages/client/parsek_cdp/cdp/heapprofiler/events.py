"""Events for the HeapProfiler domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import FieldMeta
from ..mixins.event import Event, register_event


@register_event("HeapProfiler.addHeapSnapshotChunk")
@dataclass
class AddHeapSnapshotChunk(Event):
    chunk: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('chunk', 'chunk', False, 'primitive'),
    )


@register_event("HeapProfiler.heapStatsUpdate")
@dataclass
class HeapStatsUpdate(Event):
    """If heap objects tracking has been started then backend may send update for one or more fragments"""
    stats_update: List[int]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('stats_update', 'statsUpdate', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


@register_event("HeapProfiler.lastSeenObjectId")
@dataclass
class LastSeenObjectId(Event):
    """
    If heap objects tracking has been started then backend regularly sends a current value for last
    seen object id and corresponding timestamp. If the were changes in the heap since last event
    then one or more heapStatsUpdate events will be sent before a new lastSeenObjectId event.
    """
    last_seen_object_id: int
    timestamp: float
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('last_seen_object_id', 'lastSeenObjectId', False, 'primitive'),
        FieldMeta('timestamp', 'timestamp', False, 'primitive'),
    )


@register_event("HeapProfiler.reportHeapSnapshotProgress")
@dataclass
class ReportHeapSnapshotProgress(Event):
    done: int
    total: int
    finished: Optional[bool] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('done', 'done', False, 'primitive'),
        FieldMeta('total', 'total', False, 'primitive'),
        FieldMeta('finished', 'finished', True, 'primitive'),
    )


@register_event("HeapProfiler.resetProfiles")
@dataclass
class ResetProfiles(Event):
    pass
    __FIELDS__: ClassVar[tuple] = ()

__all__ = ["AddHeapSnapshotChunk", "HeapStatsUpdate", "LastSeenObjectId", "ReportHeapSnapshotProgress", "ResetProfiles"]
