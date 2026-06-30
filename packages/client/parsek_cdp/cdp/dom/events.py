"""Events for the DOM domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import FieldMeta
from ..mixins.event import Event, register_event

if TYPE_CHECKING:
    from .types import (
        BackendNode,
        Node,
        NodeId,
        StyleSheetId,
    )

@register_event("DOM.attributeModified")
@dataclass
class AttributeModified(Event):
    """Fired when `Element`'s attribute is modified."""
    node_id: NodeId
    name: str
    value: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('node_id', 'nodeId', False, 'primitive'),
        FieldMeta('name', 'name', False, 'primitive'),
        FieldMeta('value', 'value', False, 'primitive'),
    )


@register_event("DOM.adoptedStyleSheetsModified")
@dataclass
class AdoptedStyleSheetsModified(Event):
    """Fired when `Element`'s adoptedStyleSheets are modified."""
    node_id: NodeId
    adopted_style_sheets: List[StyleSheetId]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('node_id', 'nodeId', False, 'primitive'),
        FieldMeta('adopted_style_sheets', 'adoptedStyleSheets', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


@register_event("DOM.attributeRemoved")
@dataclass
class AttributeRemoved(Event):
    """Fired when `Element`'s attribute is removed."""
    node_id: NodeId
    name: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('node_id', 'nodeId', False, 'primitive'),
        FieldMeta('name', 'name', False, 'primitive'),
    )


@register_event("DOM.characterDataModified")
@dataclass
class CharacterDataModified(Event):
    """Mirrors `DOMCharacterDataModified` event."""
    node_id: NodeId
    character_data: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('node_id', 'nodeId', False, 'primitive'),
        FieldMeta('character_data', 'characterData', False, 'primitive'),
    )


@register_event("DOM.childNodeCountUpdated")
@dataclass
class ChildNodeCountUpdated(Event):
    """Fired when `Container`'s child node count has changed."""
    node_id: NodeId
    child_node_count: int
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('node_id', 'nodeId', False, 'primitive'),
        FieldMeta('child_node_count', 'childNodeCount', False, 'primitive'),
    )


@register_event("DOM.childNodeInserted")
@dataclass
class ChildNodeInserted(Event):
    """Mirrors `DOMNodeInserted` event."""
    parent_node_id: NodeId
    previous_node_id: NodeId
    node: Node
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('parent_node_id', 'parentNodeId', False, 'primitive'),
        FieldMeta('previous_node_id', 'previousNodeId', False, 'primitive'),
        FieldMeta('node', 'node', False, 'object', ref='DOM.Node'),
    )


@register_event("DOM.childNodeRemoved")
@dataclass
class ChildNodeRemoved(Event):
    """Mirrors `DOMNodeRemoved` event."""
    parent_node_id: NodeId
    node_id: NodeId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('parent_node_id', 'parentNodeId', False, 'primitive'),
        FieldMeta('node_id', 'nodeId', False, 'primitive'),
    )


@register_event("DOM.distributedNodesUpdated")
@dataclass
class DistributedNodesUpdated(Event):
    """Called when distribution is changed."""
    insertion_point_id: NodeId
    distributed_nodes: List[BackendNode]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('insertion_point_id', 'insertionPointId', False, 'primitive'),
        FieldMeta('distributed_nodes', 'distributedNodes', False, 'array', inner=FieldMeta('', '', False, 'object', ref='DOM.BackendNode')),
    )


@register_event("DOM.documentUpdated")
@dataclass
class DocumentUpdated(Event):
    """Fired when `Document` has been totally updated. Node ids are no longer valid."""
    __FIELDS__: ClassVar[tuple] = ()


@register_event("DOM.inlineStyleInvalidated")
@dataclass
class InlineStyleInvalidated(Event):
    """Fired when `Element`'s inline style is modified via a CSS property modification."""
    node_ids: List[NodeId]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('node_ids', 'nodeIds', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


@register_event("DOM.pseudoElementAdded")
@dataclass
class PseudoElementAdded(Event):
    """Called when a pseudo element is added to an element."""
    parent_id: NodeId
    pseudo_element: Node
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('parent_id', 'parentId', False, 'primitive'),
        FieldMeta('pseudo_element', 'pseudoElement', False, 'object', ref='DOM.Node'),
    )


@register_event("DOM.topLayerElementsUpdated")
@dataclass
class TopLayerElementsUpdated(Event):
    """Called when top layer elements are changed."""
    __FIELDS__: ClassVar[tuple] = ()


@register_event("DOM.scrollableFlagUpdated")
@dataclass
class ScrollableFlagUpdated(Event):
    """Fired when a node's scrollability state changes."""
    node_id: NodeId
    is_scrollable: bool
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('node_id', 'nodeId', False, 'primitive'),
        FieldMeta('is_scrollable', 'isScrollable', False, 'primitive'),
    )


@register_event("DOM.affectedByStartingStylesFlagUpdated")
@dataclass
class AffectedByStartingStylesFlagUpdated(Event):
    """Fired when a node's starting styles changes."""
    node_id: NodeId
    affected_by_starting_styles: bool
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('node_id', 'nodeId', False, 'primitive'),
        FieldMeta('affected_by_starting_styles', 'affectedByStartingStyles', False, 'primitive'),
    )


@register_event("DOM.pseudoElementRemoved")
@dataclass
class PseudoElementRemoved(Event):
    """Called when a pseudo element is removed from an element."""
    parent_id: NodeId
    pseudo_element_id: NodeId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('parent_id', 'parentId', False, 'primitive'),
        FieldMeta('pseudo_element_id', 'pseudoElementId', False, 'primitive'),
    )


@register_event("DOM.setChildNodes")
@dataclass
class SetChildNodes(Event):
    """
    Fired when backend wants to provide client with the missing DOM structure. This happens upon
    most of the calls requesting node ids.
    """
    parent_id: NodeId
    nodes: List[Node]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('parent_id', 'parentId', False, 'primitive'),
        FieldMeta('nodes', 'nodes', False, 'array', inner=FieldMeta('', '', False, 'object', ref='DOM.Node')),
    )


@register_event("DOM.shadowRootPopped")
@dataclass
class ShadowRootPopped(Event):
    """Called when shadow root is popped from the element."""
    host_id: NodeId
    root_id: NodeId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('host_id', 'hostId', False, 'primitive'),
        FieldMeta('root_id', 'rootId', False, 'primitive'),
    )


@register_event("DOM.shadowRootPushed")
@dataclass
class ShadowRootPushed(Event):
    """Called when shadow root is pushed into the element."""
    host_id: NodeId
    root: Node
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('host_id', 'hostId', False, 'primitive'),
        FieldMeta('root', 'root', False, 'object', ref='DOM.Node'),
    )

__all__ = ["AdoptedStyleSheetsModified", "AffectedByStartingStylesFlagUpdated", "AttributeModified", "AttributeRemoved", "CharacterDataModified", "ChildNodeCountUpdated", "ChildNodeInserted", "ChildNodeRemoved", "DistributedNodesUpdated", "DocumentUpdated", "InlineStyleInvalidated", "PseudoElementAdded", "PseudoElementRemoved", "ScrollableFlagUpdated", "SetChildNodes", "ShadowRootPopped", "ShadowRootPushed", "TopLayerElementsUpdated"]
