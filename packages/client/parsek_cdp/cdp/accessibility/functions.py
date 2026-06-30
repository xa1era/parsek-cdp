"""Commands for the Accessibility domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode

if TYPE_CHECKING:
    from .types import (
        AXNode,
        AXNodeId,
    )
    from ..dom.types import BackendNodeId as DOM_BackendNodeId
    from ..dom.types import NodeId as DOM_NodeId
    from ..page.types import FrameId as Page_FrameId
    from ..runtime.types import RemoteObjectId as Runtime_RemoteObjectId

@dataclass
class GetPartialAXTreeReturn(DataType):
    """Return value of :meth:`Accessibility.get_partial_ax_tree`."""
    nodes: List[AXNode]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('nodes', 'nodes', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Accessibility.AXNode')),
    )


@dataclass
class GetFullAXTreeReturn(DataType):
    """Return value of :meth:`Accessibility.get_full_ax_tree`."""
    nodes: List[AXNode]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('nodes', 'nodes', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Accessibility.AXNode')),
    )


@dataclass
class GetRootAXNodeReturn(DataType):
    """Return value of :meth:`Accessibility.get_root_ax_node`."""
    node: AXNode
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('node', 'node', False, 'object', ref='Accessibility.AXNode'),
    )


@dataclass
class GetAXNodeAndAncestorsReturn(DataType):
    """Return value of :meth:`Accessibility.get_ax_node_and_ancestors`."""
    nodes: List[AXNode]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('nodes', 'nodes', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Accessibility.AXNode')),
    )


@dataclass
class GetChildAXNodesReturn(DataType):
    """Return value of :meth:`Accessibility.get_child_ax_nodes`."""
    nodes: List[AXNode]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('nodes', 'nodes', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Accessibility.AXNode')),
    )


@dataclass
class QueryAXTreeReturn(DataType):
    """Return value of :meth:`Accessibility.query_ax_tree`."""
    nodes: List[AXNode]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('nodes', 'nodes', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Accessibility.AXNode')),
    )


class Accessibility:
    """Commands of the Accessibility domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def disable(self) -> None:
        """Disables the accessibility domain."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Accessibility.disable', _params)
        return None

    async def enable(self) -> None:
        """
        Enables the accessibility domain which causes `AXNodeId`s to remain consistent between method calls.
        This turns on accessibility for the page, which can impact performance until accessibility is disabled.
        """
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Accessibility.enable', _params)
        return None

    async def get_partial_ax_tree(self, *, node_id: Optional[DOM_NodeId] = None, backend_node_id: Optional[DOM_BackendNodeId] = None, object_id: Optional[Runtime_RemoteObjectId] = None, fetch_relatives: Optional[bool] = None) -> GetPartialAXTreeReturn:
        """
        Fetches the accessibility node and partial accessibility tree for this DOM node, if it exists.
        :param node_id: Identifier of the node to get the partial accessibility tree for.
        :param backend_node_id: Identifier of the backend node to get the partial accessibility tree for.
        :param object_id: JavaScript object id of the node wrapper to get the partial accessibility tree for.
        :param fetch_relatives: Whether to fetch this node's ancestors, siblings and children. Defaults to true.
        """
        _params: Dict[str, Any] = {}
        if node_id is not None:
            _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        if backend_node_id is not None:
            _params['backendNodeId'] = encode(FieldMeta('', '', False, 'primitive'), backend_node_id)
        if object_id is not None:
            _params['objectId'] = encode(FieldMeta('', '', False, 'primitive'), object_id)
        if fetch_relatives is not None:
            _params['fetchRelatives'] = encode(FieldMeta('', '', False, 'primitive'), fetch_relatives)
        _result = await self._target.send('Accessibility.getPartialAXTree', _params)
        return GetPartialAXTreeReturn.from_json(_result)

    async def get_full_ax_tree(self, *, depth: Optional[int] = None, frame_id: Optional[Page_FrameId] = None) -> GetFullAXTreeReturn:
        """
        Fetches the entire accessibility tree for the root Document
        :param depth: The maximum depth at which descendants of the root node should be retrieved.
        If omitted, the full tree is returned.
        :param frame_id: The frame for whose document the AX tree should be retrieved.
        If omitted, the root frame is used.
        """
        _params: Dict[str, Any] = {}
        if depth is not None:
            _params['depth'] = encode(FieldMeta('', '', False, 'primitive'), depth)
        if frame_id is not None:
            _params['frameId'] = encode(FieldMeta('', '', False, 'primitive'), frame_id)
        _result = await self._target.send('Accessibility.getFullAXTree', _params)
        return GetFullAXTreeReturn.from_json(_result)

    async def get_root_ax_node(self, *, frame_id: Optional[Page_FrameId] = None) -> GetRootAXNodeReturn:
        """
        Fetches the root node.
        Requires `enable()` to have been called previously.
        :param frame_id: The frame in whose document the node resides.
        If omitted, the root frame is used.
        """
        _params: Dict[str, Any] = {}
        if frame_id is not None:
            _params['frameId'] = encode(FieldMeta('', '', False, 'primitive'), frame_id)
        _result = await self._target.send('Accessibility.getRootAXNode', _params)
        return GetRootAXNodeReturn.from_json(_result)

    async def get_ax_node_and_ancestors(self, *, node_id: Optional[DOM_NodeId] = None, backend_node_id: Optional[DOM_BackendNodeId] = None, object_id: Optional[Runtime_RemoteObjectId] = None) -> GetAXNodeAndAncestorsReturn:
        """
        Fetches a node and all ancestors up to and including the root.
        Requires `enable()` to have been called previously.
        :param node_id: Identifier of the node to get.
        :param backend_node_id: Identifier of the backend node to get.
        :param object_id: JavaScript object id of the node wrapper to get.
        """
        _params: Dict[str, Any] = {}
        if node_id is not None:
            _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        if backend_node_id is not None:
            _params['backendNodeId'] = encode(FieldMeta('', '', False, 'primitive'), backend_node_id)
        if object_id is not None:
            _params['objectId'] = encode(FieldMeta('', '', False, 'primitive'), object_id)
        _result = await self._target.send('Accessibility.getAXNodeAndAncestors', _params)
        return GetAXNodeAndAncestorsReturn.from_json(_result)

    async def get_child_ax_nodes(self, *, id: AXNodeId, frame_id: Optional[Page_FrameId] = None) -> GetChildAXNodesReturn:
        """
        Fetches a particular accessibility node by AXNodeId.
        Requires `enable()` to have been called previously.
        :param id:
        :param frame_id: The frame in whose document the node resides.
        If omitted, the root frame is used.
        """
        _params: Dict[str, Any] = {}
        _params['id'] = encode(FieldMeta('', '', False, 'primitive'), id)
        if frame_id is not None:
            _params['frameId'] = encode(FieldMeta('', '', False, 'primitive'), frame_id)
        _result = await self._target.send('Accessibility.getChildAXNodes', _params)
        return GetChildAXNodesReturn.from_json(_result)

    async def query_ax_tree(self, *, node_id: Optional[DOM_NodeId] = None, backend_node_id: Optional[DOM_BackendNodeId] = None, object_id: Optional[Runtime_RemoteObjectId] = None, accessible_name: Optional[str] = None, role: Optional[str] = None) -> QueryAXTreeReturn:
        """
        Query a DOM node's accessibility subtree for accessible name and role.
        This command computes the name and role for all nodes in the subtree, including those that are
        ignored for accessibility, and returns those that match the specified name and role. If no DOM
        node is specified, or the DOM node does not exist, the command returns an error. If neither
        `accessibleName` or `role` is specified, it returns all the accessibility nodes in the subtree.
        :param node_id: Identifier of the node for the root to query.
        :param backend_node_id: Identifier of the backend node for the root to query.
        :param object_id: JavaScript object id of the node wrapper for the root to query.
        :param accessible_name: Find nodes with this computed name.
        :param role: Find nodes with this computed role.
        """
        _params: Dict[str, Any] = {}
        if node_id is not None:
            _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        if backend_node_id is not None:
            _params['backendNodeId'] = encode(FieldMeta('', '', False, 'primitive'), backend_node_id)
        if object_id is not None:
            _params['objectId'] = encode(FieldMeta('', '', False, 'primitive'), object_id)
        if accessible_name is not None:
            _params['accessibleName'] = encode(FieldMeta('', '', False, 'primitive'), accessible_name)
        if role is not None:
            _params['role'] = encode(FieldMeta('', '', False, 'primitive'), role)
        _result = await self._target.send('Accessibility.queryAXTree', _params)
        return QueryAXTreeReturn.from_json(_result)
