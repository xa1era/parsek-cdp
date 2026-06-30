"""Commands for the DOM domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode

if TYPE_CHECKING:
    from .types import (
        BackendNodeId,
        BoxModel,
        CSSComputedStyleProperty,
        DetachedElementInfo,
        LogicalAxes,
        Node,
        NodeId,
        PhysicalAxes,
        Quad,
        Rect,
    )
    from ..page.types import FrameId as Page_FrameId
    from ..runtime.types import ExecutionContextId as Runtime_ExecutionContextId
    from ..runtime.types import RemoteObject as Runtime_RemoteObject
    from ..runtime.types import RemoteObjectId as Runtime_RemoteObjectId
    from ..runtime.types import StackTrace as Runtime_StackTrace

@dataclass
class CollectClassNamesFromSubtreeReturn(DataType):
    """Return value of :meth:`DOM.collect_class_names_from_subtree`."""
    class_names: List[str]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('class_names', 'classNames', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


@dataclass
class CopyToReturn(DataType):
    """Return value of :meth:`DOM.copy_to`."""
    node_id: NodeId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('node_id', 'nodeId', False, 'primitive'),
    )


@dataclass
class DescribeNodeReturn(DataType):
    """Return value of :meth:`DOM.describe_node`."""
    node: Node
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('node', 'node', False, 'object', ref='DOM.Node'),
    )


@dataclass
class GetAttributesReturn(DataType):
    """Return value of :meth:`DOM.get_attributes`."""
    attributes: List[str]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('attributes', 'attributes', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


@dataclass
class GetBoxModelReturn(DataType):
    """Return value of :meth:`DOM.get_box_model`."""
    model: BoxModel
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('model', 'model', False, 'object', ref='DOM.BoxModel'),
    )


@dataclass
class GetContentQuadsReturn(DataType):
    """Return value of :meth:`DOM.get_content_quads`."""
    quads: List[Quad]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('quads', 'quads', False, 'array', inner=FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'primitive'))),
    )


@dataclass
class GetDocumentReturn(DataType):
    """Return value of :meth:`DOM.get_document`."""
    root: Node
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('root', 'root', False, 'object', ref='DOM.Node'),
    )


@dataclass
class GetFlattenedDocumentReturn(DataType):
    """Return value of :meth:`DOM.get_flattened_document`."""
    nodes: List[Node]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('nodes', 'nodes', False, 'array', inner=FieldMeta('', '', False, 'object', ref='DOM.Node')),
    )


@dataclass
class GetNodesForSubtreeByStyleReturn(DataType):
    """Return value of :meth:`DOM.get_nodes_for_subtree_by_style`."""
    node_ids: List[NodeId]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('node_ids', 'nodeIds', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


@dataclass
class GetNodeForLocationReturn(DataType):
    """Return value of :meth:`DOM.get_node_for_location`."""
    backend_node_id: BackendNodeId
    frame_id: Page_FrameId
    node_id: Optional[NodeId] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('backend_node_id', 'backendNodeId', False, 'primitive'),
        FieldMeta('frame_id', 'frameId', False, 'primitive'),
        FieldMeta('node_id', 'nodeId', True, 'primitive'),
    )


@dataclass
class GetOuterHTMLReturn(DataType):
    """Return value of :meth:`DOM.get_outer_html`."""
    outer_html: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('outer_html', 'outerHTML', False, 'primitive'),
    )


@dataclass
class GetRelayoutBoundaryReturn(DataType):
    """Return value of :meth:`DOM.get_relayout_boundary`."""
    node_id: NodeId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('node_id', 'nodeId', False, 'primitive'),
    )


@dataclass
class GetSearchResultsReturn(DataType):
    """Return value of :meth:`DOM.get_search_results`."""
    node_ids: List[NodeId]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('node_ids', 'nodeIds', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


@dataclass
class MoveToReturn(DataType):
    """Return value of :meth:`DOM.move_to`."""
    node_id: NodeId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('node_id', 'nodeId', False, 'primitive'),
    )


@dataclass
class PerformSearchReturn(DataType):
    """Return value of :meth:`DOM.perform_search`."""
    search_id: str
    result_count: int
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('search_id', 'searchId', False, 'primitive'),
        FieldMeta('result_count', 'resultCount', False, 'primitive'),
    )


@dataclass
class PushNodeByPathToFrontendReturn(DataType):
    """Return value of :meth:`DOM.push_node_by_path_to_frontend`."""
    node_id: NodeId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('node_id', 'nodeId', False, 'primitive'),
    )


@dataclass
class PushNodesByBackendIdsToFrontendReturn(DataType):
    """Return value of :meth:`DOM.push_nodes_by_backend_ids_to_frontend`."""
    node_ids: List[NodeId]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('node_ids', 'nodeIds', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


@dataclass
class QuerySelectorReturn(DataType):
    """Return value of :meth:`DOM.query_selector`."""
    node_id: NodeId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('node_id', 'nodeId', False, 'primitive'),
    )


@dataclass
class QuerySelectorAllReturn(DataType):
    """Return value of :meth:`DOM.query_selector_all`."""
    node_ids: List[NodeId]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('node_ids', 'nodeIds', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


@dataclass
class GetTopLayerElementsReturn(DataType):
    """Return value of :meth:`DOM.get_top_layer_elements`."""
    node_ids: List[NodeId]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('node_ids', 'nodeIds', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


@dataclass
class GetElementByRelationReturn(DataType):
    """Return value of :meth:`DOM.get_element_by_relation`."""
    node_id: NodeId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('node_id', 'nodeId', False, 'primitive'),
    )


@dataclass
class RequestNodeReturn(DataType):
    """Return value of :meth:`DOM.request_node`."""
    node_id: NodeId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('node_id', 'nodeId', False, 'primitive'),
    )


@dataclass
class ResolveNodeReturn(DataType):
    """Return value of :meth:`DOM.resolve_node`."""
    object: Runtime_RemoteObject
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('object', 'object', False, 'object', ref='Runtime.RemoteObject'),
    )


@dataclass
class GetNodeStackTracesReturn(DataType):
    """Return value of :meth:`DOM.get_node_stack_traces`."""
    creation: Optional[Runtime_StackTrace] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('creation', 'creation', True, 'object', ref='Runtime.StackTrace'),
    )


@dataclass
class GetFileInfoReturn(DataType):
    """Return value of :meth:`DOM.get_file_info`."""
    path: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('path', 'path', False, 'primitive'),
    )


@dataclass
class GetDetachedDomNodesReturn(DataType):
    """Return value of :meth:`DOM.get_detached_dom_nodes`."""
    detached_nodes: List[DetachedElementInfo]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('detached_nodes', 'detachedNodes', False, 'array', inner=FieldMeta('', '', False, 'object', ref='DOM.DetachedElementInfo')),
    )


@dataclass
class SetNodeNameReturn(DataType):
    """Return value of :meth:`DOM.set_node_name`."""
    node_id: NodeId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('node_id', 'nodeId', False, 'primitive'),
    )


@dataclass
class GetFrameOwnerReturn(DataType):
    """Return value of :meth:`DOM.get_frame_owner`."""
    backend_node_id: BackendNodeId
    node_id: Optional[NodeId] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('backend_node_id', 'backendNodeId', False, 'primitive'),
        FieldMeta('node_id', 'nodeId', True, 'primitive'),
    )


@dataclass
class GetContainerForNodeReturn(DataType):
    """Return value of :meth:`DOM.get_container_for_node`."""
    node_id: Optional[NodeId] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('node_id', 'nodeId', True, 'primitive'),
    )


@dataclass
class GetQueryingDescendantsForContainerReturn(DataType):
    """Return value of :meth:`DOM.get_querying_descendants_for_container`."""
    node_ids: List[NodeId]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('node_ids', 'nodeIds', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


@dataclass
class GetAnchorElementReturn(DataType):
    """Return value of :meth:`DOM.get_anchor_element`."""
    node_id: NodeId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('node_id', 'nodeId', False, 'primitive'),
    )


@dataclass
class ForceShowPopoverReturn(DataType):
    """Return value of :meth:`DOM.force_show_popover`."""
    node_ids: List[NodeId]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('node_ids', 'nodeIds', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


class DOM:
    """Commands of the DOM domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def collect_class_names_from_subtree(self, *, node_id: NodeId) -> CollectClassNamesFromSubtreeReturn:
        """
        Collects class names for the node with given id and all of it's child nodes.
        :param node_id: Id of the node to collect class names.
        """
        _params: Dict[str, Any] = {}
        _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        _result = await self._target.send('DOM.collectClassNamesFromSubtree', _params)
        return CollectClassNamesFromSubtreeReturn.from_json(_result)

    async def copy_to(self, *, node_id: NodeId, target_node_id: NodeId, insert_before_node_id: Optional[NodeId] = None) -> CopyToReturn:
        """
        Creates a deep copy of the specified node and places it into the target container before the
        given anchor.
        :param node_id: Id of the node to copy.
        :param target_node_id: Id of the element to drop the copy into.
        :param insert_before_node_id: Drop the copy before this node (if absent, the copy becomes the last child of
        `targetNodeId`).
        """
        _params: Dict[str, Any] = {}
        _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        _params['targetNodeId'] = encode(FieldMeta('', '', False, 'primitive'), target_node_id)
        if insert_before_node_id is not None:
            _params['insertBeforeNodeId'] = encode(FieldMeta('', '', False, 'primitive'), insert_before_node_id)
        _result = await self._target.send('DOM.copyTo', _params)
        return CopyToReturn.from_json(_result)

    async def describe_node(self, *, node_id: Optional[NodeId] = None, backend_node_id: Optional[BackendNodeId] = None, object_id: Optional[Runtime_RemoteObjectId] = None, depth: Optional[int] = None, pierce: Optional[bool] = None) -> DescribeNodeReturn:
        """
        Describes node given its id, does not require domain to be enabled. Does not start tracking any
        objects, can be used for automation.
        :param node_id: Identifier of the node.
        :param backend_node_id: Identifier of the backend node.
        :param object_id: JavaScript object id of the node wrapper.
        :param depth: The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the
        entire subtree or provide an integer larger than 0.
        :param pierce: Whether or not iframes and shadow roots should be traversed when returning the subtree
        (default is false).
        """
        _params: Dict[str, Any] = {}
        if node_id is not None:
            _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        if backend_node_id is not None:
            _params['backendNodeId'] = encode(FieldMeta('', '', False, 'primitive'), backend_node_id)
        if object_id is not None:
            _params['objectId'] = encode(FieldMeta('', '', False, 'primitive'), object_id)
        if depth is not None:
            _params['depth'] = encode(FieldMeta('', '', False, 'primitive'), depth)
        if pierce is not None:
            _params['pierce'] = encode(FieldMeta('', '', False, 'primitive'), pierce)
        _result = await self._target.send('DOM.describeNode', _params)
        return DescribeNodeReturn.from_json(_result)

    async def scroll_into_view_if_needed(self, *, node_id: Optional[NodeId] = None, backend_node_id: Optional[BackendNodeId] = None, object_id: Optional[Runtime_RemoteObjectId] = None, rect: Optional[Rect] = None) -> None:
        """
        Scrolls the specified rect of the given node into view if not already visible.
        Note: exactly one between nodeId, backendNodeId and objectId should be passed
        to identify the node.
        :param node_id: Identifier of the node.
        :param backend_node_id: Identifier of the backend node.
        :param object_id: JavaScript object id of the node wrapper.
        :param rect: The rect to be scrolled into view, relative to the node's border box, in CSS pixels.
        When omitted, center of the node will be used, similar to Element.scrollIntoView.
        """
        _params: Dict[str, Any] = {}
        if node_id is not None:
            _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        if backend_node_id is not None:
            _params['backendNodeId'] = encode(FieldMeta('', '', False, 'primitive'), backend_node_id)
        if object_id is not None:
            _params['objectId'] = encode(FieldMeta('', '', False, 'primitive'), object_id)
        if rect is not None:
            _params['rect'] = encode(FieldMeta('', '', False, 'object', ref='DOM.Rect'), rect)
        _result = await self._target.send('DOM.scrollIntoViewIfNeeded', _params)
        return None

    async def disable(self) -> None:
        """Disables DOM agent for the given page."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('DOM.disable', _params)
        return None

    async def discard_search_results(self, *, search_id: str) -> None:
        """
        Discards search results from the session with the given id. `getSearchResults` should no longer
        be called for that search.
        :param search_id: Unique search session identifier.
        """
        _params: Dict[str, Any] = {}
        _params['searchId'] = encode(FieldMeta('', '', False, 'primitive'), search_id)
        _result = await self._target.send('DOM.discardSearchResults', _params)
        return None

    async def enable(self, *, include_whitespace: Optional[Literal['none', 'all']] = None) -> None:
        """
        Enables DOM agent for the given page.
        :param include_whitespace: Whether to include whitespaces in the children array of returned Nodes.
        """
        _params: Dict[str, Any] = {}
        if include_whitespace is not None:
            _params['includeWhitespace'] = encode(FieldMeta('', '', False, 'primitive'), include_whitespace)
        _result = await self._target.send('DOM.enable', _params)
        return None

    async def focus(self, *, node_id: Optional[NodeId] = None, backend_node_id: Optional[BackendNodeId] = None, object_id: Optional[Runtime_RemoteObjectId] = None) -> None:
        """
        Focuses the given element.
        :param node_id: Identifier of the node.
        :param backend_node_id: Identifier of the backend node.
        :param object_id: JavaScript object id of the node wrapper.
        """
        _params: Dict[str, Any] = {}
        if node_id is not None:
            _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        if backend_node_id is not None:
            _params['backendNodeId'] = encode(FieldMeta('', '', False, 'primitive'), backend_node_id)
        if object_id is not None:
            _params['objectId'] = encode(FieldMeta('', '', False, 'primitive'), object_id)
        _result = await self._target.send('DOM.focus', _params)
        return None

    async def get_attributes(self, *, node_id: NodeId) -> GetAttributesReturn:
        """
        Returns attributes for the specified node.
        :param node_id: Id of the node to retrieve attributes for.
        """
        _params: Dict[str, Any] = {}
        _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        _result = await self._target.send('DOM.getAttributes', _params)
        return GetAttributesReturn.from_json(_result)

    async def get_box_model(self, *, node_id: Optional[NodeId] = None, backend_node_id: Optional[BackendNodeId] = None, object_id: Optional[Runtime_RemoteObjectId] = None) -> GetBoxModelReturn:
        """
        Returns boxes for the given node.
        :param node_id: Identifier of the node.
        :param backend_node_id: Identifier of the backend node.
        :param object_id: JavaScript object id of the node wrapper.
        """
        _params: Dict[str, Any] = {}
        if node_id is not None:
            _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        if backend_node_id is not None:
            _params['backendNodeId'] = encode(FieldMeta('', '', False, 'primitive'), backend_node_id)
        if object_id is not None:
            _params['objectId'] = encode(FieldMeta('', '', False, 'primitive'), object_id)
        _result = await self._target.send('DOM.getBoxModel', _params)
        return GetBoxModelReturn.from_json(_result)

    async def get_content_quads(self, *, node_id: Optional[NodeId] = None, backend_node_id: Optional[BackendNodeId] = None, object_id: Optional[Runtime_RemoteObjectId] = None) -> GetContentQuadsReturn:
        """
        Returns quads that describe node position on the page. This method
        might return multiple quads for inline nodes.
        :param node_id: Identifier of the node.
        :param backend_node_id: Identifier of the backend node.
        :param object_id: JavaScript object id of the node wrapper.
        """
        _params: Dict[str, Any] = {}
        if node_id is not None:
            _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        if backend_node_id is not None:
            _params['backendNodeId'] = encode(FieldMeta('', '', False, 'primitive'), backend_node_id)
        if object_id is not None:
            _params['objectId'] = encode(FieldMeta('', '', False, 'primitive'), object_id)
        _result = await self._target.send('DOM.getContentQuads', _params)
        return GetContentQuadsReturn.from_json(_result)

    async def get_document(self, *, depth: Optional[int] = None, pierce: Optional[bool] = None) -> GetDocumentReturn:
        """
        Returns the root DOM node (and optionally the subtree) to the caller.
        Implicitly enables the DOM domain events for the current target.
        :param depth: The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the
        entire subtree or provide an integer larger than 0.
        :param pierce: Whether or not iframes and shadow roots should be traversed when returning the subtree
        (default is false).
        """
        _params: Dict[str, Any] = {}
        if depth is not None:
            _params['depth'] = encode(FieldMeta('', '', False, 'primitive'), depth)
        if pierce is not None:
            _params['pierce'] = encode(FieldMeta('', '', False, 'primitive'), pierce)
        _result = await self._target.send('DOM.getDocument', _params)
        return GetDocumentReturn.from_json(_result)

    async def get_flattened_document(self, *, depth: Optional[int] = None, pierce: Optional[bool] = None) -> GetFlattenedDocumentReturn:
        """
        Returns the root DOM node (and optionally the subtree) to the caller.
        Deprecated, as it is not designed to work well with the rest of the DOM agent.
        Use DOMSnapshot.captureSnapshot instead.
        
        .. deprecated::
        :param depth: The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the
        entire subtree or provide an integer larger than 0.
        :param pierce: Whether or not iframes and shadow roots should be traversed when returning the subtree
        (default is false).
        """
        _params: Dict[str, Any] = {}
        if depth is not None:
            _params['depth'] = encode(FieldMeta('', '', False, 'primitive'), depth)
        if pierce is not None:
            _params['pierce'] = encode(FieldMeta('', '', False, 'primitive'), pierce)
        _result = await self._target.send('DOM.getFlattenedDocument', _params)
        return GetFlattenedDocumentReturn.from_json(_result)

    async def get_nodes_for_subtree_by_style(self, *, node_id: NodeId, computed_styles: List[CSSComputedStyleProperty], pierce: Optional[bool] = None) -> GetNodesForSubtreeByStyleReturn:
        """
        Finds nodes with a given computed style in a subtree.
        :param node_id: Node ID pointing to the root of a subtree.
        :param computed_styles: The style to filter nodes by (includes nodes if any of properties matches).
        :param pierce: Whether or not iframes and shadow roots in the same target should be traversed when returning the
        results (default is false).
        """
        _params: Dict[str, Any] = {}
        _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        _params['computedStyles'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'object', ref='DOM.CSSComputedStyleProperty')), computed_styles)
        if pierce is not None:
            _params['pierce'] = encode(FieldMeta('', '', False, 'primitive'), pierce)
        _result = await self._target.send('DOM.getNodesForSubtreeByStyle', _params)
        return GetNodesForSubtreeByStyleReturn.from_json(_result)

    async def get_node_for_location(self, *, x: int, y: int, include_user_agent_shadow_dom: Optional[bool] = None, ignore_pointer_events_none: Optional[bool] = None) -> GetNodeForLocationReturn:
        """
        Returns node id at given location. Depending on whether DOM domain is enabled, nodeId is
        either returned or not.
        :param x: X coordinate.
        :param y: Y coordinate.
        :param include_user_agent_shadow_dom: False to skip to the nearest non-UA shadow root ancestor (default: false).
        :param ignore_pointer_events_none: Whether to ignore pointer-events: none on elements and hit test them.
        """
        _params: Dict[str, Any] = {}
        _params['x'] = encode(FieldMeta('', '', False, 'primitive'), x)
        _params['y'] = encode(FieldMeta('', '', False, 'primitive'), y)
        if include_user_agent_shadow_dom is not None:
            _params['includeUserAgentShadowDOM'] = encode(FieldMeta('', '', False, 'primitive'), include_user_agent_shadow_dom)
        if ignore_pointer_events_none is not None:
            _params['ignorePointerEventsNone'] = encode(FieldMeta('', '', False, 'primitive'), ignore_pointer_events_none)
        _result = await self._target.send('DOM.getNodeForLocation', _params)
        return GetNodeForLocationReturn.from_json(_result)

    async def get_outer_html(self, *, node_id: Optional[NodeId] = None, backend_node_id: Optional[BackendNodeId] = None, object_id: Optional[Runtime_RemoteObjectId] = None, include_shadow_dom: Optional[bool] = None) -> GetOuterHTMLReturn:
        """
        Returns node's HTML markup.
        :param node_id: Identifier of the node.
        :param backend_node_id: Identifier of the backend node.
        :param object_id: JavaScript object id of the node wrapper.
        :param include_shadow_dom: Include all shadow roots. Equals to false if not specified.
        """
        _params: Dict[str, Any] = {}
        if node_id is not None:
            _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        if backend_node_id is not None:
            _params['backendNodeId'] = encode(FieldMeta('', '', False, 'primitive'), backend_node_id)
        if object_id is not None:
            _params['objectId'] = encode(FieldMeta('', '', False, 'primitive'), object_id)
        if include_shadow_dom is not None:
            _params['includeShadowDOM'] = encode(FieldMeta('', '', False, 'primitive'), include_shadow_dom)
        _result = await self._target.send('DOM.getOuterHTML', _params)
        return GetOuterHTMLReturn.from_json(_result)

    async def get_relayout_boundary(self, *, node_id: NodeId) -> GetRelayoutBoundaryReturn:
        """
        Returns the id of the nearest ancestor that is a relayout boundary.
        :param node_id: Id of the node.
        """
        _params: Dict[str, Any] = {}
        _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        _result = await self._target.send('DOM.getRelayoutBoundary', _params)
        return GetRelayoutBoundaryReturn.from_json(_result)

    async def get_search_results(self, *, search_id: str, from_index: int, to_index: int) -> GetSearchResultsReturn:
        """
        Returns search results from given `fromIndex` to given `toIndex` from the search with the given
        identifier.
        :param search_id: Unique search session identifier.
        :param from_index: Start index of the search result to be returned.
        :param to_index: End index of the search result to be returned.
        """
        _params: Dict[str, Any] = {}
        _params['searchId'] = encode(FieldMeta('', '', False, 'primitive'), search_id)
        _params['fromIndex'] = encode(FieldMeta('', '', False, 'primitive'), from_index)
        _params['toIndex'] = encode(FieldMeta('', '', False, 'primitive'), to_index)
        _result = await self._target.send('DOM.getSearchResults', _params)
        return GetSearchResultsReturn.from_json(_result)

    async def hide_highlight(self) -> None:
        """Hides any highlight."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('DOM.hideHighlight', _params)
        return None

    async def highlight_node(self) -> None:
        """Highlights DOM node."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('DOM.highlightNode', _params)
        return None

    async def highlight_rect(self) -> None:
        """Highlights given rectangle."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('DOM.highlightRect', _params)
        return None

    async def mark_undoable_state(self) -> None:
        """Marks last undoable state."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('DOM.markUndoableState', _params)
        return None

    async def move_to(self, *, node_id: NodeId, target_node_id: NodeId, insert_before_node_id: Optional[NodeId] = None) -> MoveToReturn:
        """
        Moves node into the new container, places it before the given anchor.
        :param node_id: Id of the node to move.
        :param target_node_id: Id of the element to drop the moved node into.
        :param insert_before_node_id: Drop node before this one (if absent, the moved node becomes the last child of
        `targetNodeId`).
        """
        _params: Dict[str, Any] = {}
        _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        _params['targetNodeId'] = encode(FieldMeta('', '', False, 'primitive'), target_node_id)
        if insert_before_node_id is not None:
            _params['insertBeforeNodeId'] = encode(FieldMeta('', '', False, 'primitive'), insert_before_node_id)
        _result = await self._target.send('DOM.moveTo', _params)
        return MoveToReturn.from_json(_result)

    async def perform_search(self, *, query: str, include_user_agent_shadow_dom: Optional[bool] = None) -> PerformSearchReturn:
        """
        Searches for a given string in the DOM tree. Use `getSearchResults` to access search results or
        `cancelSearch` to end this search session.
        :param query: Plain text or query selector or XPath search query.
        :param include_user_agent_shadow_dom: True to search in user agent shadow DOM.
        """
        _params: Dict[str, Any] = {}
        _params['query'] = encode(FieldMeta('', '', False, 'primitive'), query)
        if include_user_agent_shadow_dom is not None:
            _params['includeUserAgentShadowDOM'] = encode(FieldMeta('', '', False, 'primitive'), include_user_agent_shadow_dom)
        _result = await self._target.send('DOM.performSearch', _params)
        return PerformSearchReturn.from_json(_result)

    async def push_node_by_path_to_frontend(self, *, path: str) -> PushNodeByPathToFrontendReturn:
        """
        Requests that the node is sent to the caller given its path. // FIXME, use XPath
        :param path: Path to node in the proprietary format.
        """
        _params: Dict[str, Any] = {}
        _params['path'] = encode(FieldMeta('', '', False, 'primitive'), path)
        _result = await self._target.send('DOM.pushNodeByPathToFrontend', _params)
        return PushNodeByPathToFrontendReturn.from_json(_result)

    async def push_nodes_by_backend_ids_to_frontend(self, *, backend_node_ids: List[BackendNodeId]) -> PushNodesByBackendIdsToFrontendReturn:
        """
        Requests that a batch of nodes is sent to the caller given their backend node ids.
        :param backend_node_ids: The array of backend node ids.
        """
        _params: Dict[str, Any] = {}
        _params['backendNodeIds'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'primitive')), backend_node_ids)
        _result = await self._target.send('DOM.pushNodesByBackendIdsToFrontend', _params)
        return PushNodesByBackendIdsToFrontendReturn.from_json(_result)

    async def query_selector(self, *, node_id: NodeId, selector: str) -> QuerySelectorReturn:
        """
        Executes `querySelector` on a given node.
        :param node_id: Id of the node to query upon.
        :param selector: Selector string.
        """
        _params: Dict[str, Any] = {}
        _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        _params['selector'] = encode(FieldMeta('', '', False, 'primitive'), selector)
        _result = await self._target.send('DOM.querySelector', _params)
        return QuerySelectorReturn.from_json(_result)

    async def query_selector_all(self, *, node_id: NodeId, selector: str) -> QuerySelectorAllReturn:
        """
        Executes `querySelectorAll` on a given node.
        :param node_id: Id of the node to query upon.
        :param selector: Selector string.
        """
        _params: Dict[str, Any] = {}
        _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        _params['selector'] = encode(FieldMeta('', '', False, 'primitive'), selector)
        _result = await self._target.send('DOM.querySelectorAll', _params)
        return QuerySelectorAllReturn.from_json(_result)

    async def get_top_layer_elements(self) -> GetTopLayerElementsReturn:
        """
        Returns NodeIds of current top layer elements.
        Top layer is rendered closest to the user within a viewport, therefore its elements always
        appear on top of all other content.
        """
        _params: Dict[str, Any] = {}
        _result = await self._target.send('DOM.getTopLayerElements', _params)
        return GetTopLayerElementsReturn.from_json(_result)

    async def get_element_by_relation(self, *, node_id: NodeId, relation: Literal['PopoverTarget', 'InterestTarget', 'CommandFor']) -> GetElementByRelationReturn:
        """
        Returns the NodeId of the matched element according to certain relations.
        :param node_id: Id of the node from which to query the relation.
        :param relation: Type of relation to get.
        """
        _params: Dict[str, Any] = {}
        _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        _params['relation'] = encode(FieldMeta('', '', False, 'primitive'), relation)
        _result = await self._target.send('DOM.getElementByRelation', _params)
        return GetElementByRelationReturn.from_json(_result)

    async def redo(self) -> None:
        """Re-does the last undone action."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('DOM.redo', _params)
        return None

    async def remove_attribute(self, *, node_id: NodeId, name: str) -> None:
        """
        Removes attribute with given name from an element with given id.
        :param node_id: Id of the element to remove attribute from.
        :param name: Name of the attribute to remove.
        """
        _params: Dict[str, Any] = {}
        _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        _params['name'] = encode(FieldMeta('', '', False, 'primitive'), name)
        _result = await self._target.send('DOM.removeAttribute', _params)
        return None

    async def remove_node(self, *, node_id: NodeId) -> None:
        """
        Removes node with given id.
        :param node_id: Id of the node to remove.
        """
        _params: Dict[str, Any] = {}
        _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        _result = await self._target.send('DOM.removeNode', _params)
        return None

    async def request_child_nodes(self, *, node_id: NodeId, depth: Optional[int] = None, pierce: Optional[bool] = None) -> None:
        """
        Requests that children of the node with given id are returned to the caller in form of
        `setChildNodes` events where not only immediate children are retrieved, but all children down to
        the specified depth.
        :param node_id: Id of the node to get children for.
        :param depth: The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the
        entire subtree or provide an integer larger than 0.
        :param pierce: Whether or not iframes and shadow roots should be traversed when returning the sub-tree
        (default is false).
        """
        _params: Dict[str, Any] = {}
        _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        if depth is not None:
            _params['depth'] = encode(FieldMeta('', '', False, 'primitive'), depth)
        if pierce is not None:
            _params['pierce'] = encode(FieldMeta('', '', False, 'primitive'), pierce)
        _result = await self._target.send('DOM.requestChildNodes', _params)
        return None

    async def request_node(self, *, object_id: Runtime_RemoteObjectId) -> RequestNodeReturn:
        """
        Requests that the node is sent to the caller given the JavaScript node object reference. All
        nodes that form the path from the node to the root are also sent to the client as a series of
        `setChildNodes` notifications.
        :param object_id: JavaScript object id to convert into node.
        """
        _params: Dict[str, Any] = {}
        _params['objectId'] = encode(FieldMeta('', '', False, 'primitive'), object_id)
        _result = await self._target.send('DOM.requestNode', _params)
        return RequestNodeReturn.from_json(_result)

    async def resolve_node(self, *, node_id: Optional[NodeId] = None, backend_node_id: Optional[BackendNodeId] = None, object_group: Optional[str] = None, execution_context_id: Optional[Runtime_ExecutionContextId] = None) -> ResolveNodeReturn:
        """
        Resolves the JavaScript node object for a given NodeId or BackendNodeId.
        :param node_id: Id of the node to resolve.
        :param backend_node_id: Backend identifier of the node to resolve.
        :param object_group: Symbolic group name that can be used to release multiple objects.
        :param execution_context_id: Execution context in which to resolve the node.
        """
        _params: Dict[str, Any] = {}
        if node_id is not None:
            _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        if backend_node_id is not None:
            _params['backendNodeId'] = encode(FieldMeta('', '', False, 'primitive'), backend_node_id)
        if object_group is not None:
            _params['objectGroup'] = encode(FieldMeta('', '', False, 'primitive'), object_group)
        if execution_context_id is not None:
            _params['executionContextId'] = encode(FieldMeta('', '', False, 'primitive'), execution_context_id)
        _result = await self._target.send('DOM.resolveNode', _params)
        return ResolveNodeReturn.from_json(_result)

    async def set_attribute_value(self, *, node_id: NodeId, name: str, value: str) -> None:
        """
        Sets attribute for an element with given id.
        :param node_id: Id of the element to set attribute for.
        :param name: Attribute name.
        :param value: Attribute value.
        """
        _params: Dict[str, Any] = {}
        _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        _params['name'] = encode(FieldMeta('', '', False, 'primitive'), name)
        _params['value'] = encode(FieldMeta('', '', False, 'primitive'), value)
        _result = await self._target.send('DOM.setAttributeValue', _params)
        return None

    async def set_attributes_as_text(self, *, node_id: NodeId, text: str, name: Optional[str] = None) -> None:
        """
        Sets attributes on element with given id. This method is useful when user edits some existing
        attribute value and types in several attribute name/value pairs.
        :param node_id: Id of the element to set attributes for.
        :param text: Text with a number of attributes. Will parse this text using HTML parser.
        :param name: Attribute name to replace with new attributes derived from text in case text parsed
        successfully.
        """
        _params: Dict[str, Any] = {}
        _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        _params['text'] = encode(FieldMeta('', '', False, 'primitive'), text)
        if name is not None:
            _params['name'] = encode(FieldMeta('', '', False, 'primitive'), name)
        _result = await self._target.send('DOM.setAttributesAsText', _params)
        return None

    async def set_file_input_files(self, *, files: List[str], node_id: Optional[NodeId] = None, backend_node_id: Optional[BackendNodeId] = None, object_id: Optional[Runtime_RemoteObjectId] = None) -> None:
        """
        Sets files for the given file input element.
        :param files: Array of file paths to set.
        :param node_id: Identifier of the node.
        :param backend_node_id: Identifier of the backend node.
        :param object_id: JavaScript object id of the node wrapper.
        """
        _params: Dict[str, Any] = {}
        _params['files'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'primitive')), files)
        if node_id is not None:
            _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        if backend_node_id is not None:
            _params['backendNodeId'] = encode(FieldMeta('', '', False, 'primitive'), backend_node_id)
        if object_id is not None:
            _params['objectId'] = encode(FieldMeta('', '', False, 'primitive'), object_id)
        _result = await self._target.send('DOM.setFileInputFiles', _params)
        return None

    async def set_node_stack_traces_enabled(self, *, enable: bool) -> None:
        """
        Sets if stack traces should be captured for Nodes. See `Node.getNodeStackTraces`. Default is disabled.
        :param enable: Enable or disable.
        """
        _params: Dict[str, Any] = {}
        _params['enable'] = encode(FieldMeta('', '', False, 'primitive'), enable)
        _result = await self._target.send('DOM.setNodeStackTracesEnabled', _params)
        return None

    async def get_node_stack_traces(self, *, node_id: NodeId) -> GetNodeStackTracesReturn:
        """
        Gets stack traces associated with a Node. As of now, only provides stack trace for Node creation.
        :param node_id: Id of the node to get stack traces for.
        """
        _params: Dict[str, Any] = {}
        _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        _result = await self._target.send('DOM.getNodeStackTraces', _params)
        return GetNodeStackTracesReturn.from_json(_result)

    async def get_file_info(self, *, object_id: Runtime_RemoteObjectId) -> GetFileInfoReturn:
        """
        Returns file information for the given
        File wrapper.
        :param object_id: JavaScript object id of the node wrapper.
        """
        _params: Dict[str, Any] = {}
        _params['objectId'] = encode(FieldMeta('', '', False, 'primitive'), object_id)
        _result = await self._target.send('DOM.getFileInfo', _params)
        return GetFileInfoReturn.from_json(_result)

    async def get_detached_dom_nodes(self) -> GetDetachedDomNodesReturn:
        """Returns list of detached nodes"""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('DOM.getDetachedDomNodes', _params)
        return GetDetachedDomNodesReturn.from_json(_result)

    async def set_inspected_node(self, *, node_id: NodeId) -> None:
        """
        Enables console to refer to the node with given id via $x (see Command Line API for more details
        $x functions).
        :param node_id: DOM node id to be accessible by means of $x command line API.
        """
        _params: Dict[str, Any] = {}
        _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        _result = await self._target.send('DOM.setInspectedNode', _params)
        return None

    async def set_node_name(self, *, node_id: NodeId, name: str) -> SetNodeNameReturn:
        """
        Sets node name for a node with given id.
        :param node_id: Id of the node to set name for.
        :param name: New node's name.
        """
        _params: Dict[str, Any] = {}
        _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        _params['name'] = encode(FieldMeta('', '', False, 'primitive'), name)
        _result = await self._target.send('DOM.setNodeName', _params)
        return SetNodeNameReturn.from_json(_result)

    async def set_node_value(self, *, node_id: NodeId, value: str) -> None:
        """
        Sets node value for a node with given id.
        :param node_id: Id of the node to set value for.
        :param value: New node's value.
        """
        _params: Dict[str, Any] = {}
        _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        _params['value'] = encode(FieldMeta('', '', False, 'primitive'), value)
        _result = await self._target.send('DOM.setNodeValue', _params)
        return None

    async def set_outer_html(self, *, node_id: NodeId, outer_html: str) -> None:
        """
        Sets node HTML markup, returns new node id.
        :param node_id: Id of the node to set markup for.
        :param outer_html: Outer HTML markup to set.
        """
        _params: Dict[str, Any] = {}
        _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        _params['outerHTML'] = encode(FieldMeta('', '', False, 'primitive'), outer_html)
        _result = await self._target.send('DOM.setOuterHTML', _params)
        return None

    async def undo(self) -> None:
        """Undoes the last performed action."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('DOM.undo', _params)
        return None

    async def get_frame_owner(self, *, frame_id: Page_FrameId) -> GetFrameOwnerReturn:
        """
        Returns iframe node that owns iframe with the given domain.
        :param frame_id:
        """
        _params: Dict[str, Any] = {}
        _params['frameId'] = encode(FieldMeta('', '', False, 'primitive'), frame_id)
        _result = await self._target.send('DOM.getFrameOwner', _params)
        return GetFrameOwnerReturn.from_json(_result)

    async def get_container_for_node(self, *, node_id: NodeId, container_name: Optional[str] = None, physical_axes: Optional[PhysicalAxes] = None, logical_axes: Optional[LogicalAxes] = None, queries_scroll_state: Optional[bool] = None, queries_anchored: Optional[bool] = None) -> GetContainerForNodeReturn:
        """
        Returns the query container of the given node based on container query
        conditions: containerName, physical and logical axes, and whether it queries
        scroll-state or anchored elements. If no axes are provided and
        queriesScrollState is false, the style container is returned, which is the
        direct parent or the closest element with a matching container-name.
        :param node_id:
        :param container_name:
        :param physical_axes:
        :param logical_axes:
        :param queries_scroll_state:
        :param queries_anchored:
        """
        _params: Dict[str, Any] = {}
        _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        if container_name is not None:
            _params['containerName'] = encode(FieldMeta('', '', False, 'primitive'), container_name)
        if physical_axes is not None:
            _params['physicalAxes'] = encode(FieldMeta('', '', False, 'enum', ref='DOM.PhysicalAxes'), physical_axes)
        if logical_axes is not None:
            _params['logicalAxes'] = encode(FieldMeta('', '', False, 'enum', ref='DOM.LogicalAxes'), logical_axes)
        if queries_scroll_state is not None:
            _params['queriesScrollState'] = encode(FieldMeta('', '', False, 'primitive'), queries_scroll_state)
        if queries_anchored is not None:
            _params['queriesAnchored'] = encode(FieldMeta('', '', False, 'primitive'), queries_anchored)
        _result = await self._target.send('DOM.getContainerForNode', _params)
        return GetContainerForNodeReturn.from_json(_result)

    async def get_querying_descendants_for_container(self, *, node_id: NodeId) -> GetQueryingDescendantsForContainerReturn:
        """
        Returns the descendants of a container query container that have
        container queries against this container.
        :param node_id: Id of the container node to find querying descendants from.
        """
        _params: Dict[str, Any] = {}
        _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        _result = await self._target.send('DOM.getQueryingDescendantsForContainer', _params)
        return GetQueryingDescendantsForContainerReturn.from_json(_result)

    async def get_anchor_element(self, *, node_id: NodeId, anchor_specifier: Optional[str] = None) -> GetAnchorElementReturn:
        """
        Returns the target anchor element of the given anchor query according to
        https://www.w3.org/TR/css-anchor-position-1/#target.
        :param node_id: Id of the positioned element from which to find the anchor.
        :param anchor_specifier: An optional anchor specifier, as defined in
        https://www.w3.org/TR/css-anchor-position-1/#anchor-specifier.
        If not provided, it will return the implicit anchor element for
        the given positioned element.
        """
        _params: Dict[str, Any] = {}
        _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        if anchor_specifier is not None:
            _params['anchorSpecifier'] = encode(FieldMeta('', '', False, 'primitive'), anchor_specifier)
        _result = await self._target.send('DOM.getAnchorElement', _params)
        return GetAnchorElementReturn.from_json(_result)

    async def force_show_popover(self, *, node_id: NodeId, enable: bool) -> ForceShowPopoverReturn:
        """
        When enabling, this API force-opens the popover identified by nodeId
        and keeps it open until disabled.
        :param node_id: Id of the popover HTMLElement
        :param enable: If true, opens the popover and keeps it open. If false, closes the
        popover if it was previously force-opened.
        """
        _params: Dict[str, Any] = {}
        _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        _params['enable'] = encode(FieldMeta('', '', False, 'primitive'), enable)
        _result = await self._target.send('DOM.forceShowPopover', _params)
        return ForceShowPopoverReturn.from_json(_result)
