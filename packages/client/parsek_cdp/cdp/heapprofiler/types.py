"""Custom types and enums for the HeapProfiler domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, register

if TYPE_CHECKING:
    from ..runtime.types import CallFrame as Runtime_CallFrame

type HeapSnapshotObjectId = str  # Heap snapshot object id.


@register("HeapProfiler.SamplingHeapProfileNode")
@dataclass
class SamplingHeapProfileNode(DataType):
    """Sampling Heap Profile node. Holds callsite information, allocation statistics and child nodes."""
    call_frame: Runtime_CallFrame
    self_size: float
    id: int
    children: List[SamplingHeapProfileNode]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('call_frame', 'callFrame', False, 'object', ref='Runtime.CallFrame'),
        FieldMeta('self_size', 'selfSize', False, 'primitive'),
        FieldMeta('id', 'id', False, 'primitive'),
        FieldMeta('children', 'children', False, 'array', inner=FieldMeta('', '', False, 'object', ref='HeapProfiler.SamplingHeapProfileNode')),
    )


@register("HeapProfiler.SamplingHeapProfileSample")
@dataclass
class SamplingHeapProfileSample(DataType):
    """A single sample from a sampling profile."""
    size: float
    node_id: int
    ordinal: float
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('size', 'size', False, 'primitive'),
        FieldMeta('node_id', 'nodeId', False, 'primitive'),
        FieldMeta('ordinal', 'ordinal', False, 'primitive'),
    )


@register("HeapProfiler.SamplingHeapProfile")
@dataclass
class SamplingHeapProfile(DataType):
    """Sampling profile."""
    head: SamplingHeapProfileNode
    samples: List[SamplingHeapProfileSample]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('head', 'head', False, 'object', ref='HeapProfiler.SamplingHeapProfileNode'),
        FieldMeta('samples', 'samples', False, 'array', inner=FieldMeta('', '', False, 'object', ref='HeapProfiler.SamplingHeapProfileSample')),
    )

__all__ = ["HeapSnapshotObjectId", "SamplingHeapProfile", "SamplingHeapProfileNode", "SamplingHeapProfileSample"]
