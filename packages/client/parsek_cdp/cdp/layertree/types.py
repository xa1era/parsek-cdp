"""Custom types and enums for the LayerTree domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, register

if TYPE_CHECKING:
    from ..dom.types import BackendNodeId as DOM_BackendNodeId
    from ..dom.types import Rect as DOM_Rect

type LayerId = str  # Unique Layer identifier.


type SnapshotId = str  # Unique snapshot identifier.


@register("LayerTree.ScrollRect")
@dataclass
class ScrollRect(DataType):
    """Rectangle where scrolling happens on the main thread."""
    rect: DOM_Rect
    type_: Literal['RepaintsOnScroll', 'TouchEventHandler', 'WheelEventHandler']
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('rect', 'rect', False, 'object', ref='DOM.Rect'),
        FieldMeta('type_', 'type', False, 'primitive'),
    )


@register("LayerTree.StickyPositionConstraint")
@dataclass
class StickyPositionConstraint(DataType):
    """Sticky position constraints."""
    sticky_box_rect: DOM_Rect
    containing_block_rect: DOM_Rect
    nearest_layer_shifting_sticky_box: Optional[LayerId] = None
    nearest_layer_shifting_containing_block: Optional[LayerId] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('sticky_box_rect', 'stickyBoxRect', False, 'object', ref='DOM.Rect'),
        FieldMeta('containing_block_rect', 'containingBlockRect', False, 'object', ref='DOM.Rect'),
        FieldMeta('nearest_layer_shifting_sticky_box', 'nearestLayerShiftingStickyBox', True, 'primitive'),
        FieldMeta('nearest_layer_shifting_containing_block', 'nearestLayerShiftingContainingBlock', True, 'primitive'),
    )


@register("LayerTree.PictureTile")
@dataclass
class PictureTile(DataType):
    """Serialized fragment of layer picture along with its offset within the layer."""
    x: float
    y: float
    picture: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('x', 'x', False, 'primitive'),
        FieldMeta('y', 'y', False, 'primitive'),
        FieldMeta('picture', 'picture', False, 'primitive'),
    )


@register("LayerTree.Layer")
@dataclass
class Layer(DataType):
    """Information about a compositing layer."""
    layer_id: LayerId
    offset_x: float
    offset_y: float
    width: float
    height: float
    paint_count: int
    draws_content: bool
    parent_layer_id: Optional[LayerId] = None
    backend_node_id: Optional[DOM_BackendNodeId] = None
    transform: Optional[List[float]] = None
    anchor_x: Optional[float] = None
    anchor_y: Optional[float] = None
    anchor_z: Optional[float] = None
    invisible: Optional[bool] = None
    scroll_rects: Optional[List[ScrollRect]] = None
    sticky_position_constraint: Optional[StickyPositionConstraint] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('layer_id', 'layerId', False, 'primitive'),
        FieldMeta('offset_x', 'offsetX', False, 'primitive'),
        FieldMeta('offset_y', 'offsetY', False, 'primitive'),
        FieldMeta('width', 'width', False, 'primitive'),
        FieldMeta('height', 'height', False, 'primitive'),
        FieldMeta('paint_count', 'paintCount', False, 'primitive'),
        FieldMeta('draws_content', 'drawsContent', False, 'primitive'),
        FieldMeta('parent_layer_id', 'parentLayerId', True, 'primitive'),
        FieldMeta('backend_node_id', 'backendNodeId', True, 'primitive'),
        FieldMeta('transform', 'transform', True, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('anchor_x', 'anchorX', True, 'primitive'),
        FieldMeta('anchor_y', 'anchorY', True, 'primitive'),
        FieldMeta('anchor_z', 'anchorZ', True, 'primitive'),
        FieldMeta('invisible', 'invisible', True, 'primitive'),
        FieldMeta('scroll_rects', 'scrollRects', True, 'array', inner=FieldMeta('', '', False, 'object', ref='LayerTree.ScrollRect')),
        FieldMeta('sticky_position_constraint', 'stickyPositionConstraint', True, 'object', ref='LayerTree.StickyPositionConstraint'),
    )


type PaintProfile = List[float]  # Array of timings, one per paint step.

__all__ = ["Layer", "LayerId", "PaintProfile", "PictureTile", "ScrollRect", "SnapshotId", "StickyPositionConstraint"]
