"""Custom types and enums for the DOMSnapshot domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, register

if TYPE_CHECKING:
    from ..dom.types import BackendNodeId as DOM_BackendNodeId
    from ..dom.types import PseudoType as DOM_PseudoType
    from ..dom.types import Rect as DOM_Rect
    from ..dom.types import ShadowRootType as DOM_ShadowRootType
    from ..domdebugger.types import EventListener as DOMDebugger_EventListener
    from ..page.types import FrameId as Page_FrameId

@register("DOMSnapshot.DOMNode")
@dataclass
class DOMNode(DataType):
    """A Node in the DOM tree."""
    node_type: int
    node_name: str
    node_value: str
    backend_node_id: DOM_BackendNodeId
    text_value: Optional[str] = None
    input_value: Optional[str] = None
    input_checked: Optional[bool] = None
    option_selected: Optional[bool] = None
    child_node_indexes: Optional[List[int]] = None
    attributes: Optional[List[NameValue]] = None
    pseudo_element_indexes: Optional[List[int]] = None
    layout_node_index: Optional[int] = None
    document_url: Optional[str] = None
    base_url: Optional[str] = None
    content_language: Optional[str] = None
    document_encoding: Optional[str] = None
    public_id: Optional[str] = None
    system_id: Optional[str] = None
    frame_id: Optional[Page_FrameId] = None
    content_document_index: Optional[int] = None
    pseudo_type: Optional[DOM_PseudoType] = None
    shadow_root_type: Optional[DOM_ShadowRootType] = None
    is_clickable: Optional[bool] = None
    event_listeners: Optional[List[DOMDebugger_EventListener]] = None
    current_source_url: Optional[str] = None
    origin_url: Optional[str] = None
    scroll_offset_x: Optional[float] = None
    scroll_offset_y: Optional[float] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('node_type', 'nodeType', False, 'primitive'),
        FieldMeta('node_name', 'nodeName', False, 'primitive'),
        FieldMeta('node_value', 'nodeValue', False, 'primitive'),
        FieldMeta('backend_node_id', 'backendNodeId', False, 'primitive'),
        FieldMeta('text_value', 'textValue', True, 'primitive'),
        FieldMeta('input_value', 'inputValue', True, 'primitive'),
        FieldMeta('input_checked', 'inputChecked', True, 'primitive'),
        FieldMeta('option_selected', 'optionSelected', True, 'primitive'),
        FieldMeta('child_node_indexes', 'childNodeIndexes', True, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('attributes', 'attributes', True, 'array', inner=FieldMeta('', '', False, 'object', ref='DOMSnapshot.NameValue')),
        FieldMeta('pseudo_element_indexes', 'pseudoElementIndexes', True, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('layout_node_index', 'layoutNodeIndex', True, 'primitive'),
        FieldMeta('document_url', 'documentURL', True, 'primitive'),
        FieldMeta('base_url', 'baseURL', True, 'primitive'),
        FieldMeta('content_language', 'contentLanguage', True, 'primitive'),
        FieldMeta('document_encoding', 'documentEncoding', True, 'primitive'),
        FieldMeta('public_id', 'publicId', True, 'primitive'),
        FieldMeta('system_id', 'systemId', True, 'primitive'),
        FieldMeta('frame_id', 'frameId', True, 'primitive'),
        FieldMeta('content_document_index', 'contentDocumentIndex', True, 'primitive'),
        FieldMeta('pseudo_type', 'pseudoType', True, 'enum', ref='DOM.PseudoType'),
        FieldMeta('shadow_root_type', 'shadowRootType', True, 'enum', ref='DOM.ShadowRootType'),
        FieldMeta('is_clickable', 'isClickable', True, 'primitive'),
        FieldMeta('event_listeners', 'eventListeners', True, 'array', inner=FieldMeta('', '', False, 'object', ref='DOMDebugger.EventListener')),
        FieldMeta('current_source_url', 'currentSourceURL', True, 'primitive'),
        FieldMeta('origin_url', 'originURL', True, 'primitive'),
        FieldMeta('scroll_offset_x', 'scrollOffsetX', True, 'primitive'),
        FieldMeta('scroll_offset_y', 'scrollOffsetY', True, 'primitive'),
    )


@register("DOMSnapshot.InlineTextBox")
@dataclass
class InlineTextBox(DataType):
    """
    Details of post layout rendered text positions. The exact layout should not be regarded as
    stable and may change between versions.
    """
    bounding_box: DOM_Rect
    start_character_index: int
    num_characters: int
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('bounding_box', 'boundingBox', False, 'object', ref='DOM.Rect'),
        FieldMeta('start_character_index', 'startCharacterIndex', False, 'primitive'),
        FieldMeta('num_characters', 'numCharacters', False, 'primitive'),
    )


@register("DOMSnapshot.LayoutTreeNode")
@dataclass
class LayoutTreeNode(DataType):
    """Details of an element in the DOM tree with a LayoutObject."""
    dom_node_index: int
    bounding_box: DOM_Rect
    layout_text: Optional[str] = None
    inline_text_nodes: Optional[List[InlineTextBox]] = None
    style_index: Optional[int] = None
    paint_order: Optional[int] = None
    is_stacking_context: Optional[bool] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('dom_node_index', 'domNodeIndex', False, 'primitive'),
        FieldMeta('bounding_box', 'boundingBox', False, 'object', ref='DOM.Rect'),
        FieldMeta('layout_text', 'layoutText', True, 'primitive'),
        FieldMeta('inline_text_nodes', 'inlineTextNodes', True, 'array', inner=FieldMeta('', '', False, 'object', ref='DOMSnapshot.InlineTextBox')),
        FieldMeta('style_index', 'styleIndex', True, 'primitive'),
        FieldMeta('paint_order', 'paintOrder', True, 'primitive'),
        FieldMeta('is_stacking_context', 'isStackingContext', True, 'primitive'),
    )


@register("DOMSnapshot.ComputedStyle")
@dataclass
class ComputedStyle(DataType):
    """A subset of the full ComputedStyle as defined by the request whitelist."""
    properties: List[NameValue]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('properties', 'properties', False, 'array', inner=FieldMeta('', '', False, 'object', ref='DOMSnapshot.NameValue')),
    )


@register("DOMSnapshot.NameValue")
@dataclass
class NameValue(DataType):
    """A name/value pair."""
    name: str
    value: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('name', 'name', False, 'primitive'),
        FieldMeta('value', 'value', False, 'primitive'),
    )


type StringIndex = int  # Index of the string in the strings table.


type ArrayOfStrings = List[StringIndex]  # Index of the string in the strings table.


@register("DOMSnapshot.RareStringData")
@dataclass
class RareStringData(DataType):
    """Data that is only present on rare nodes."""
    index: List[int]
    value: List[StringIndex]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('index', 'index', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('value', 'value', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


@register("DOMSnapshot.RareBooleanData")
@dataclass
class RareBooleanData(DataType):
    index: List[int]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('index', 'index', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


@register("DOMSnapshot.RareIntegerData")
@dataclass
class RareIntegerData(DataType):
    index: List[int]
    value: List[int]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('index', 'index', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('value', 'value', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


type Rectangle = List[float]


@register("DOMSnapshot.DocumentSnapshot")
@dataclass
class DocumentSnapshot(DataType):
    """Document snapshot."""
    document_url: StringIndex
    title: StringIndex
    base_url: StringIndex
    content_language: StringIndex
    encoding_name: StringIndex
    public_id: StringIndex
    system_id: StringIndex
    frame_id: StringIndex
    nodes: NodeTreeSnapshot
    layout: LayoutTreeSnapshot
    text_boxes: TextBoxSnapshot
    scroll_offset_x: Optional[float] = None
    scroll_offset_y: Optional[float] = None
    content_width: Optional[float] = None
    content_height: Optional[float] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('document_url', 'documentURL', False, 'primitive'),
        FieldMeta('title', 'title', False, 'primitive'),
        FieldMeta('base_url', 'baseURL', False, 'primitive'),
        FieldMeta('content_language', 'contentLanguage', False, 'primitive'),
        FieldMeta('encoding_name', 'encodingName', False, 'primitive'),
        FieldMeta('public_id', 'publicId', False, 'primitive'),
        FieldMeta('system_id', 'systemId', False, 'primitive'),
        FieldMeta('frame_id', 'frameId', False, 'primitive'),
        FieldMeta('nodes', 'nodes', False, 'object', ref='DOMSnapshot.NodeTreeSnapshot'),
        FieldMeta('layout', 'layout', False, 'object', ref='DOMSnapshot.LayoutTreeSnapshot'),
        FieldMeta('text_boxes', 'textBoxes', False, 'object', ref='DOMSnapshot.TextBoxSnapshot'),
        FieldMeta('scroll_offset_x', 'scrollOffsetX', True, 'primitive'),
        FieldMeta('scroll_offset_y', 'scrollOffsetY', True, 'primitive'),
        FieldMeta('content_width', 'contentWidth', True, 'primitive'),
        FieldMeta('content_height', 'contentHeight', True, 'primitive'),
    )


@register("DOMSnapshot.NodeTreeSnapshot")
@dataclass
class NodeTreeSnapshot(DataType):
    """Table containing nodes."""
    parent_index: Optional[List[int]] = None
    node_type: Optional[List[int]] = None
    shadow_root_type: Optional[RareStringData] = None
    node_name: Optional[List[StringIndex]] = None
    node_value: Optional[List[StringIndex]] = None
    backend_node_id: Optional[List[DOM_BackendNodeId]] = None
    attributes: Optional[List[ArrayOfStrings]] = None
    text_value: Optional[RareStringData] = None
    input_value: Optional[RareStringData] = None
    input_checked: Optional[RareBooleanData] = None
    option_selected: Optional[RareBooleanData] = None
    content_document_index: Optional[RareIntegerData] = None
    pseudo_type: Optional[RareStringData] = None
    pseudo_identifier: Optional[RareStringData] = None
    is_clickable: Optional[RareBooleanData] = None
    current_source_url: Optional[RareStringData] = None
    origin_url: Optional[RareStringData] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('parent_index', 'parentIndex', True, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('node_type', 'nodeType', True, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('shadow_root_type', 'shadowRootType', True, 'object', ref='DOMSnapshot.RareStringData'),
        FieldMeta('node_name', 'nodeName', True, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('node_value', 'nodeValue', True, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('backend_node_id', 'backendNodeId', True, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('attributes', 'attributes', True, 'array', inner=FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'primitive'))),
        FieldMeta('text_value', 'textValue', True, 'object', ref='DOMSnapshot.RareStringData'),
        FieldMeta('input_value', 'inputValue', True, 'object', ref='DOMSnapshot.RareStringData'),
        FieldMeta('input_checked', 'inputChecked', True, 'object', ref='DOMSnapshot.RareBooleanData'),
        FieldMeta('option_selected', 'optionSelected', True, 'object', ref='DOMSnapshot.RareBooleanData'),
        FieldMeta('content_document_index', 'contentDocumentIndex', True, 'object', ref='DOMSnapshot.RareIntegerData'),
        FieldMeta('pseudo_type', 'pseudoType', True, 'object', ref='DOMSnapshot.RareStringData'),
        FieldMeta('pseudo_identifier', 'pseudoIdentifier', True, 'object', ref='DOMSnapshot.RareStringData'),
        FieldMeta('is_clickable', 'isClickable', True, 'object', ref='DOMSnapshot.RareBooleanData'),
        FieldMeta('current_source_url', 'currentSourceURL', True, 'object', ref='DOMSnapshot.RareStringData'),
        FieldMeta('origin_url', 'originURL', True, 'object', ref='DOMSnapshot.RareStringData'),
    )


@register("DOMSnapshot.LayoutTreeSnapshot")
@dataclass
class LayoutTreeSnapshot(DataType):
    """Table of details of an element in the DOM tree with a LayoutObject."""
    node_index: List[int]
    styles: List[ArrayOfStrings]
    bounds: List[Rectangle]
    text: List[StringIndex]
    stacking_contexts: RareBooleanData
    paint_orders: Optional[List[int]] = None
    offset_rects: Optional[List[Rectangle]] = None
    scroll_rects: Optional[List[Rectangle]] = None
    client_rects: Optional[List[Rectangle]] = None
    blended_background_colors: Optional[List[StringIndex]] = None
    text_color_opacities: Optional[List[float]] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('node_index', 'nodeIndex', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('styles', 'styles', False, 'array', inner=FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'primitive'))),
        FieldMeta('bounds', 'bounds', False, 'array', inner=FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'primitive'))),
        FieldMeta('text', 'text', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('stacking_contexts', 'stackingContexts', False, 'object', ref='DOMSnapshot.RareBooleanData'),
        FieldMeta('paint_orders', 'paintOrders', True, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('offset_rects', 'offsetRects', True, 'array', inner=FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'primitive'))),
        FieldMeta('scroll_rects', 'scrollRects', True, 'array', inner=FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'primitive'))),
        FieldMeta('client_rects', 'clientRects', True, 'array', inner=FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'primitive'))),
        FieldMeta('blended_background_colors', 'blendedBackgroundColors', True, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('text_color_opacities', 'textColorOpacities', True, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


@register("DOMSnapshot.TextBoxSnapshot")
@dataclass
class TextBoxSnapshot(DataType):
    """
    Table of details of the post layout rendered text positions. The exact layout should not be regarded as
    stable and may change between versions.
    """
    layout_index: List[int]
    bounds: List[Rectangle]
    start: List[int]
    length: List[int]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('layout_index', 'layoutIndex', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('bounds', 'bounds', False, 'array', inner=FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'primitive'))),
        FieldMeta('start', 'start', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('length', 'length', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )

__all__ = ["ArrayOfStrings", "ComputedStyle", "DOMNode", "DocumentSnapshot", "InlineTextBox", "LayoutTreeNode", "LayoutTreeSnapshot", "NameValue", "NodeTreeSnapshot", "RareBooleanData", "RareIntegerData", "RareStringData", "Rectangle", "StringIndex", "TextBoxSnapshot"]
