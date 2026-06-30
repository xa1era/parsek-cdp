"""Custom types and enums for the DOM domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, register

if TYPE_CHECKING:
    from ..page.types import FrameId as Page_FrameId

type NodeId = int  # Unique DOM node identifier.


type BackendNodeId = int  # Unique DOM node identifier used to reference a node that may not have been pushed to the


type StyleSheetId = str  # Unique identifier for a CSS stylesheet.


@register("DOM.BackendNode")
@dataclass
class BackendNode(DataType):
    """Backend node with a friendly name."""
    node_type: int
    node_name: str
    backend_node_id: BackendNodeId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('node_type', 'nodeType', False, 'primitive'),
        FieldMeta('node_name', 'nodeName', False, 'primitive'),
        FieldMeta('backend_node_id', 'backendNodeId', False, 'primitive'),
    )


@register("DOM.PseudoType")
class PseudoType(str, Enum):
    """Pseudo element type."""
    FIRST_LINE = 'first-line'
    FIRST_LETTER = 'first-letter'
    CHECKMARK = 'checkmark'
    BEFORE = 'before'
    AFTER = 'after'
    PICKER_ICON = 'picker-icon'
    INTEREST_HINT = 'interest-hint'
    MARKER = 'marker'
    BACKDROP = 'backdrop'
    COLUMN = 'column'
    SELECTION = 'selection'
    SEARCH_TEXT = 'search-text'
    TARGET_TEXT = 'target-text'
    SPELLING_ERROR = 'spelling-error'
    GRAMMAR_ERROR = 'grammar-error'
    HIGHLIGHT = 'highlight'
    FIRST_LINE_INHERITED = 'first-line-inherited'
    SCROLL_MARKER = 'scroll-marker'
    SCROLL_MARKER_GROUP = 'scroll-marker-group'
    SCROLL_BUTTON = 'scroll-button'
    SCROLLBAR = 'scrollbar'
    SCROLLBAR_THUMB = 'scrollbar-thumb'
    SCROLLBAR_BUTTON = 'scrollbar-button'
    SCROLLBAR_TRACK = 'scrollbar-track'
    SCROLLBAR_TRACK_PIECE = 'scrollbar-track-piece'
    SCROLLBAR_CORNER = 'scrollbar-corner'
    RESIZER = 'resizer'
    INPUT_LIST_BUTTON = 'input-list-button'
    VIEW_TRANSITION = 'view-transition'
    VIEW_TRANSITION_GROUP = 'view-transition-group'
    VIEW_TRANSITION_IMAGE_PAIR = 'view-transition-image-pair'
    VIEW_TRANSITION_GROUP_CHILDREN = 'view-transition-group-children'
    VIEW_TRANSITION_OLD = 'view-transition-old'
    VIEW_TRANSITION_NEW = 'view-transition-new'
    PLACEHOLDER = 'placeholder'
    FILE_SELECTOR_BUTTON = 'file-selector-button'
    DETAILS_CONTENT = 'details-content'
    PICKER = 'picker'
    PERMISSION_ICON = 'permission-icon'
    OVERSCROLL_AREA_PARENT = 'overscroll-area-parent'
    OVERSCROLL_CLIENT_AREA = 'overscroll-client-area'


@register("DOM.ShadowRootType")
class ShadowRootType(str, Enum):
    """Shadow root type."""
    USER_AGENT = 'user-agent'
    OPEN = 'open'
    CLOSED = 'closed'


@register("DOM.CompatibilityMode")
class CompatibilityMode(str, Enum):
    """Document compatibility mode."""
    QUIRKSMODE = 'QuirksMode'
    LIMITEDQUIRKSMODE = 'LimitedQuirksMode'
    NOQUIRKSMODE = 'NoQuirksMode'


@register("DOM.PhysicalAxes")
class PhysicalAxes(str, Enum):
    """ContainerSelector physical axes"""
    HORIZONTAL = 'Horizontal'
    VERTICAL = 'Vertical'
    BOTH = 'Both'


@register("DOM.LogicalAxes")
class LogicalAxes(str, Enum):
    """ContainerSelector logical axes"""
    INLINE = 'Inline'
    BLOCK = 'Block'
    BOTH = 'Both'


@register("DOM.ScrollOrientation")
class ScrollOrientation(str, Enum):
    """Physical scroll orientation"""
    HORIZONTAL = 'horizontal'
    VERTICAL = 'vertical'


@register("DOM.Node")
@dataclass
class Node(DataType):
    """
    DOM interaction is implemented in terms of mirror objects that represent the actual DOM nodes.
    DOMNode is a base node mirror type.
    """
    node_id: NodeId
    backend_node_id: BackendNodeId
    node_type: int
    node_name: str
    local_name: str
    node_value: str
    parent_id: Optional[NodeId] = None
    child_node_count: Optional[int] = None
    children: Optional[List[Node]] = None
    attributes: Optional[List[str]] = None
    document_url: Optional[str] = None
    base_url: Optional[str] = None
    public_id: Optional[str] = None
    system_id: Optional[str] = None
    internal_subset: Optional[str] = None
    xml_version: Optional[str] = None
    name: Optional[str] = None
    value: Optional[str] = None
    pseudo_type: Optional[PseudoType] = None
    pseudo_identifier: Optional[str] = None
    shadow_root_type: Optional[ShadowRootType] = None
    frame_id: Optional[Page_FrameId] = None
    content_document: Optional[Node] = None
    shadow_roots: Optional[List[Node]] = None
    template_content: Optional[Node] = None
    pseudo_elements: Optional[List[Node]] = None
    imported_document: Optional[Node] = None
    distributed_nodes: Optional[List[BackendNode]] = None
    is_svg: Optional[bool] = None
    compatibility_mode: Optional[CompatibilityMode] = None
    assigned_slot: Optional[BackendNode] = None
    is_scrollable: Optional[bool] = None
    affected_by_starting_styles: Optional[bool] = None
    adopted_style_sheets: Optional[List[StyleSheetId]] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('node_id', 'nodeId', False, 'primitive'),
        FieldMeta('backend_node_id', 'backendNodeId', False, 'primitive'),
        FieldMeta('node_type', 'nodeType', False, 'primitive'),
        FieldMeta('node_name', 'nodeName', False, 'primitive'),
        FieldMeta('local_name', 'localName', False, 'primitive'),
        FieldMeta('node_value', 'nodeValue', False, 'primitive'),
        FieldMeta('parent_id', 'parentId', True, 'primitive'),
        FieldMeta('child_node_count', 'childNodeCount', True, 'primitive'),
        FieldMeta('children', 'children', True, 'array', inner=FieldMeta('', '', False, 'object', ref='DOM.Node')),
        FieldMeta('attributes', 'attributes', True, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('document_url', 'documentURL', True, 'primitive'),
        FieldMeta('base_url', 'baseURL', True, 'primitive'),
        FieldMeta('public_id', 'publicId', True, 'primitive'),
        FieldMeta('system_id', 'systemId', True, 'primitive'),
        FieldMeta('internal_subset', 'internalSubset', True, 'primitive'),
        FieldMeta('xml_version', 'xmlVersion', True, 'primitive'),
        FieldMeta('name', 'name', True, 'primitive'),
        FieldMeta('value', 'value', True, 'primitive'),
        FieldMeta('pseudo_type', 'pseudoType', True, 'enum', ref='DOM.PseudoType'),
        FieldMeta('pseudo_identifier', 'pseudoIdentifier', True, 'primitive'),
        FieldMeta('shadow_root_type', 'shadowRootType', True, 'enum', ref='DOM.ShadowRootType'),
        FieldMeta('frame_id', 'frameId', True, 'primitive'),
        FieldMeta('content_document', 'contentDocument', True, 'object', ref='DOM.Node'),
        FieldMeta('shadow_roots', 'shadowRoots', True, 'array', inner=FieldMeta('', '', False, 'object', ref='DOM.Node')),
        FieldMeta('template_content', 'templateContent', True, 'object', ref='DOM.Node'),
        FieldMeta('pseudo_elements', 'pseudoElements', True, 'array', inner=FieldMeta('', '', False, 'object', ref='DOM.Node')),
        FieldMeta('imported_document', 'importedDocument', True, 'object', ref='DOM.Node'),
        FieldMeta('distributed_nodes', 'distributedNodes', True, 'array', inner=FieldMeta('', '', False, 'object', ref='DOM.BackendNode')),
        FieldMeta('is_svg', 'isSVG', True, 'primitive'),
        FieldMeta('compatibility_mode', 'compatibilityMode', True, 'enum', ref='DOM.CompatibilityMode'),
        FieldMeta('assigned_slot', 'assignedSlot', True, 'object', ref='DOM.BackendNode'),
        FieldMeta('is_scrollable', 'isScrollable', True, 'primitive'),
        FieldMeta('affected_by_starting_styles', 'affectedByStartingStyles', True, 'primitive'),
        FieldMeta('adopted_style_sheets', 'adoptedStyleSheets', True, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


@register("DOM.DetachedElementInfo")
@dataclass
class DetachedElementInfo(DataType):
    """A structure to hold the top-level node of a detached tree and an array of its retained descendants."""
    tree_node: Node
    retained_node_ids: List[NodeId]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('tree_node', 'treeNode', False, 'object', ref='DOM.Node'),
        FieldMeta('retained_node_ids', 'retainedNodeIds', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


@register("DOM.RGBA")
@dataclass
class RGBA(DataType):
    """A structure holding an RGBA color."""
    r: int
    g: int
    b: int
    a: Optional[float] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('r', 'r', False, 'primitive'),
        FieldMeta('g', 'g', False, 'primitive'),
        FieldMeta('b', 'b', False, 'primitive'),
        FieldMeta('a', 'a', True, 'primitive'),
    )


type Quad = List[float]  # An array of quad vertices, x immediately followed by y for each point, points clock-wise.


@register("DOM.BoxModel")
@dataclass
class BoxModel(DataType):
    """Box model."""
    content: Quad
    padding: Quad
    border: Quad
    margin: Quad
    width: int
    height: int
    shape_outside: Optional[ShapeOutsideInfo] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('content', 'content', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('padding', 'padding', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('border', 'border', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('margin', 'margin', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('width', 'width', False, 'primitive'),
        FieldMeta('height', 'height', False, 'primitive'),
        FieldMeta('shape_outside', 'shapeOutside', True, 'object', ref='DOM.ShapeOutsideInfo'),
    )


@register("DOM.ShapeOutsideInfo")
@dataclass
class ShapeOutsideInfo(DataType):
    """CSS Shape Outside details."""
    bounds: Quad
    shape: List[Any]
    margin_shape: List[Any]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('bounds', 'bounds', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('shape', 'shape', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('margin_shape', 'marginShape', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


@register("DOM.Rect")
@dataclass
class Rect(DataType):
    """Rectangle."""
    x: float
    y: float
    width: float
    height: float
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('x', 'x', False, 'primitive'),
        FieldMeta('y', 'y', False, 'primitive'),
        FieldMeta('width', 'width', False, 'primitive'),
        FieldMeta('height', 'height', False, 'primitive'),
    )


@register("DOM.CSSComputedStyleProperty")
@dataclass
class CSSComputedStyleProperty(DataType):
    name: str
    value: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('name', 'name', False, 'primitive'),
        FieldMeta('value', 'value', False, 'primitive'),
    )

__all__ = ["BackendNode", "BackendNodeId", "BoxModel", "CSSComputedStyleProperty", "CompatibilityMode", "DetachedElementInfo", "LogicalAxes", "Node", "NodeId", "PhysicalAxes", "PseudoType", "Quad", "RGBA", "Rect", "ScrollOrientation", "ShadowRootType", "ShapeOutsideInfo", "StyleSheetId"]
