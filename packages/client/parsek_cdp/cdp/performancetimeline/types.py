"""Custom types and enums for the PerformanceTimeline domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, register

if TYPE_CHECKING:
    from ..dom.types import BackendNodeId as DOM_BackendNodeId
    from ..dom.types import Rect as DOM_Rect
    from ..network.types import TimeSinceEpoch as Network_TimeSinceEpoch
    from ..page.types import FrameId as Page_FrameId

@register("PerformanceTimeline.LargestContentfulPaint")
@dataclass
class LargestContentfulPaint(DataType):
    """See https://github.com/WICG/LargestContentfulPaint and largest_contentful_paint.idl"""
    render_time: Network_TimeSinceEpoch
    load_time: Network_TimeSinceEpoch
    size: float
    element_id: Optional[str] = None
    url: Optional[str] = None
    node_id: Optional[DOM_BackendNodeId] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('render_time', 'renderTime', False, 'primitive'),
        FieldMeta('load_time', 'loadTime', False, 'primitive'),
        FieldMeta('size', 'size', False, 'primitive'),
        FieldMeta('element_id', 'elementId', True, 'primitive'),
        FieldMeta('url', 'url', True, 'primitive'),
        FieldMeta('node_id', 'nodeId', True, 'primitive'),
    )


@register("PerformanceTimeline.LayoutShiftAttribution")
@dataclass
class LayoutShiftAttribution(DataType):
    previous_rect: DOM_Rect
    current_rect: DOM_Rect
    node_id: Optional[DOM_BackendNodeId] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('previous_rect', 'previousRect', False, 'object', ref='DOM.Rect'),
        FieldMeta('current_rect', 'currentRect', False, 'object', ref='DOM.Rect'),
        FieldMeta('node_id', 'nodeId', True, 'primitive'),
    )


@register("PerformanceTimeline.LayoutShift")
@dataclass
class LayoutShift(DataType):
    """See https://wicg.github.io/layout-instability/#sec-layout-shift and layout_shift.idl"""
    value: float
    had_recent_input: bool
    last_input_time: Network_TimeSinceEpoch
    sources: List[LayoutShiftAttribution]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('value', 'value', False, 'primitive'),
        FieldMeta('had_recent_input', 'hadRecentInput', False, 'primitive'),
        FieldMeta('last_input_time', 'lastInputTime', False, 'primitive'),
        FieldMeta('sources', 'sources', False, 'array', inner=FieldMeta('', '', False, 'object', ref='PerformanceTimeline.LayoutShiftAttribution')),
    )


@register("PerformanceTimeline.TimelineEvent")
@dataclass
class TimelineEvent(DataType):
    frame_id: Page_FrameId
    type_: str
    name: str
    time: Network_TimeSinceEpoch
    duration: Optional[float] = None
    lcp_details: Optional[LargestContentfulPaint] = None
    layout_shift_details: Optional[LayoutShift] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('frame_id', 'frameId', False, 'primitive'),
        FieldMeta('type_', 'type', False, 'primitive'),
        FieldMeta('name', 'name', False, 'primitive'),
        FieldMeta('time', 'time', False, 'primitive'),
        FieldMeta('duration', 'duration', True, 'primitive'),
        FieldMeta('lcp_details', 'lcpDetails', True, 'object', ref='PerformanceTimeline.LargestContentfulPaint'),
        FieldMeta('layout_shift_details', 'layoutShiftDetails', True, 'object', ref='PerformanceTimeline.LayoutShift'),
    )

__all__ = ["LargestContentfulPaint", "LayoutShift", "LayoutShiftAttribution", "TimelineEvent"]
