"""Custom types and enums for the Profiler domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, register

if TYPE_CHECKING:
    from ..runtime.types import CallFrame as Runtime_CallFrame
    from ..runtime.types import ScriptId as Runtime_ScriptId

@register("Profiler.ProfileNode")
@dataclass
class ProfileNode(DataType):
    """Profile node. Holds callsite information, execution statistics and child nodes."""
    id: int
    call_frame: Runtime_CallFrame
    hit_count: Optional[int] = None
    children: Optional[List[int]] = None
    deopt_reason: Optional[str] = None
    position_ticks: Optional[List[PositionTickInfo]] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('id', 'id', False, 'primitive'),
        FieldMeta('call_frame', 'callFrame', False, 'object', ref='Runtime.CallFrame'),
        FieldMeta('hit_count', 'hitCount', True, 'primitive'),
        FieldMeta('children', 'children', True, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('deopt_reason', 'deoptReason', True, 'primitive'),
        FieldMeta('position_ticks', 'positionTicks', True, 'array', inner=FieldMeta('', '', False, 'object', ref='Profiler.PositionTickInfo')),
    )


@register("Profiler.Profile")
@dataclass
class Profile(DataType):
    """Profile."""
    nodes: List[ProfileNode]
    start_time: float
    end_time: float
    samples: Optional[List[int]] = None
    time_deltas: Optional[List[int]] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('nodes', 'nodes', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Profiler.ProfileNode')),
        FieldMeta('start_time', 'startTime', False, 'primitive'),
        FieldMeta('end_time', 'endTime', False, 'primitive'),
        FieldMeta('samples', 'samples', True, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('time_deltas', 'timeDeltas', True, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


@register("Profiler.PositionTickInfo")
@dataclass
class PositionTickInfo(DataType):
    """Specifies a number of samples attributed to a certain source position."""
    line: int
    ticks: int
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('line', 'line', False, 'primitive'),
        FieldMeta('ticks', 'ticks', False, 'primitive'),
    )


@register("Profiler.CoverageRange")
@dataclass
class CoverageRange(DataType):
    """Coverage data for a source range."""
    start_offset: int
    end_offset: int
    count: int
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('start_offset', 'startOffset', False, 'primitive'),
        FieldMeta('end_offset', 'endOffset', False, 'primitive'),
        FieldMeta('count', 'count', False, 'primitive'),
    )


@register("Profiler.FunctionCoverage")
@dataclass
class FunctionCoverage(DataType):
    """Coverage data for a JavaScript function."""
    function_name: str
    ranges: List[CoverageRange]
    is_block_coverage: bool
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('function_name', 'functionName', False, 'primitive'),
        FieldMeta('ranges', 'ranges', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Profiler.CoverageRange')),
        FieldMeta('is_block_coverage', 'isBlockCoverage', False, 'primitive'),
    )


@register("Profiler.ScriptCoverage")
@dataclass
class ScriptCoverage(DataType):
    """Coverage data for a JavaScript script."""
    script_id: Runtime_ScriptId
    url: str
    functions: List[FunctionCoverage]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('script_id', 'scriptId', False, 'primitive'),
        FieldMeta('url', 'url', False, 'primitive'),
        FieldMeta('functions', 'functions', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Profiler.FunctionCoverage')),
    )

__all__ = ["CoverageRange", "FunctionCoverage", "PositionTickInfo", "Profile", "ProfileNode", "ScriptCoverage"]
