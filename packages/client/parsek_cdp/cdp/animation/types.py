"""Custom types and enums for the Animation domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, register

if TYPE_CHECKING:
    from ..dom.types import BackendNodeId as DOM_BackendNodeId
    from ..dom.types import ScrollOrientation as DOM_ScrollOrientation

@register("Animation.Animation")
@dataclass
class Animation(DataType):
    """Animation instance."""
    id: str
    name: str
    paused_state: bool
    play_state: str
    playback_rate: float
    start_time: float
    current_time: float
    type_: Literal['CSSTransition', 'CSSAnimation', 'WebAnimation']
    source: Optional[AnimationEffect] = None
    css_id: Optional[str] = None
    view_or_scroll_timeline: Optional[ViewOrScrollTimeline] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('id', 'id', False, 'primitive'),
        FieldMeta('name', 'name', False, 'primitive'),
        FieldMeta('paused_state', 'pausedState', False, 'primitive'),
        FieldMeta('play_state', 'playState', False, 'primitive'),
        FieldMeta('playback_rate', 'playbackRate', False, 'primitive'),
        FieldMeta('start_time', 'startTime', False, 'primitive'),
        FieldMeta('current_time', 'currentTime', False, 'primitive'),
        FieldMeta('type_', 'type', False, 'primitive'),
        FieldMeta('source', 'source', True, 'object', ref='Animation.AnimationEffect'),
        FieldMeta('css_id', 'cssId', True, 'primitive'),
        FieldMeta('view_or_scroll_timeline', 'viewOrScrollTimeline', True, 'object', ref='Animation.ViewOrScrollTimeline'),
    )


@register("Animation.ViewOrScrollTimeline")
@dataclass
class ViewOrScrollTimeline(DataType):
    """Timeline instance"""
    axis: DOM_ScrollOrientation
    source_node_id: Optional[DOM_BackendNodeId] = None
    start_offset: Optional[float] = None
    end_offset: Optional[float] = None
    subject_node_id: Optional[DOM_BackendNodeId] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('axis', 'axis', False, 'enum', ref='DOM.ScrollOrientation'),
        FieldMeta('source_node_id', 'sourceNodeId', True, 'primitive'),
        FieldMeta('start_offset', 'startOffset', True, 'primitive'),
        FieldMeta('end_offset', 'endOffset', True, 'primitive'),
        FieldMeta('subject_node_id', 'subjectNodeId', True, 'primitive'),
    )


@register("Animation.AnimationEffect")
@dataclass
class AnimationEffect(DataType):
    """AnimationEffect instance"""
    delay: float
    end_delay: float
    iteration_start: float
    duration: float
    direction: str
    fill: str
    easing: str
    iterations: Optional[float] = None
    backend_node_id: Optional[DOM_BackendNodeId] = None
    keyframes_rule: Optional[KeyframesRule] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('delay', 'delay', False, 'primitive'),
        FieldMeta('end_delay', 'endDelay', False, 'primitive'),
        FieldMeta('iteration_start', 'iterationStart', False, 'primitive'),
        FieldMeta('duration', 'duration', False, 'primitive'),
        FieldMeta('direction', 'direction', False, 'primitive'),
        FieldMeta('fill', 'fill', False, 'primitive'),
        FieldMeta('easing', 'easing', False, 'primitive'),
        FieldMeta('iterations', 'iterations', True, 'primitive'),
        FieldMeta('backend_node_id', 'backendNodeId', True, 'primitive'),
        FieldMeta('keyframes_rule', 'keyframesRule', True, 'object', ref='Animation.KeyframesRule'),
    )


@register("Animation.KeyframesRule")
@dataclass
class KeyframesRule(DataType):
    """Keyframes Rule"""
    keyframes: List[KeyframeStyle]
    name: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('keyframes', 'keyframes', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Animation.KeyframeStyle')),
        FieldMeta('name', 'name', True, 'primitive'),
    )


@register("Animation.KeyframeStyle")
@dataclass
class KeyframeStyle(DataType):
    """Keyframe Style"""
    offset: str
    easing: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('offset', 'offset', False, 'primitive'),
        FieldMeta('easing', 'easing', False, 'primitive'),
    )

__all__ = ["Animation", "AnimationEffect", "KeyframeStyle", "KeyframesRule", "ViewOrScrollTimeline"]
