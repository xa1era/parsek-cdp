"""Custom types and enums for the Input domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, register


@register("Input.TouchPoint")
@dataclass
class TouchPoint(DataType):
    x: float
    y: float
    radius_x: Optional[float] = None
    radius_y: Optional[float] = None
    rotation_angle: Optional[float] = None
    force: Optional[float] = None
    tangential_pressure: Optional[float] = None
    tilt_x: Optional[float] = None
    tilt_y: Optional[float] = None
    twist: Optional[int] = None
    id: Optional[float] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('x', 'x', False, 'primitive'),
        FieldMeta('y', 'y', False, 'primitive'),
        FieldMeta('radius_x', 'radiusX', True, 'primitive'),
        FieldMeta('radius_y', 'radiusY', True, 'primitive'),
        FieldMeta('rotation_angle', 'rotationAngle', True, 'primitive'),
        FieldMeta('force', 'force', True, 'primitive'),
        FieldMeta('tangential_pressure', 'tangentialPressure', True, 'primitive'),
        FieldMeta('tilt_x', 'tiltX', True, 'primitive'),
        FieldMeta('tilt_y', 'tiltY', True, 'primitive'),
        FieldMeta('twist', 'twist', True, 'primitive'),
        FieldMeta('id', 'id', True, 'primitive'),
    )


@register("Input.GestureSourceType")
class GestureSourceType(str, Enum):
    DEFAULT = 'default'
    TOUCH = 'touch'
    MOUSE = 'mouse'


@register("Input.MouseButton")
class MouseButton(str, Enum):
    NONE = 'none'
    LEFT = 'left'
    MIDDLE = 'middle'
    RIGHT = 'right'
    BACK = 'back'
    FORWARD = 'forward'


type TimeSinceEpoch = float  # UTC time in seconds, counted from January 1, 1970.


@register("Input.DragDataItem")
@dataclass
class DragDataItem(DataType):
    mime_type: str
    data: str
    title: Optional[str] = None
    base_url: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('mime_type', 'mimeType', False, 'primitive'),
        FieldMeta('data', 'data', False, 'primitive'),
        FieldMeta('title', 'title', True, 'primitive'),
        FieldMeta('base_url', 'baseURL', True, 'primitive'),
    )


@register("Input.DragData")
@dataclass
class DragData(DataType):
    items: List[DragDataItem]
    drag_operations_mask: int
    files: Optional[List[str]] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('items', 'items', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Input.DragDataItem')),
        FieldMeta('drag_operations_mask', 'dragOperationsMask', False, 'primitive'),
        FieldMeta('files', 'files', True, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )

__all__ = ["DragData", "DragDataItem", "GestureSourceType", "MouseButton", "TimeSinceEpoch", "TouchPoint"]
