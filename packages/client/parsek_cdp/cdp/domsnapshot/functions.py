"""Commands for the DOMSnapshot domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode

if TYPE_CHECKING:
    from .types import (
        ComputedStyle,
        DOMNode,
        DocumentSnapshot,
        LayoutTreeNode,
    )

@dataclass
class GetSnapshotReturn(DataType):
    """Return value of :meth:`DOMSnapshot.get_snapshot`."""
    dom_nodes: List[DOMNode]
    layout_tree_nodes: List[LayoutTreeNode]
    computed_styles: List[ComputedStyle]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('dom_nodes', 'domNodes', False, 'array', inner=FieldMeta('', '', False, 'object', ref='DOMSnapshot.DOMNode')),
        FieldMeta('layout_tree_nodes', 'layoutTreeNodes', False, 'array', inner=FieldMeta('', '', False, 'object', ref='DOMSnapshot.LayoutTreeNode')),
        FieldMeta('computed_styles', 'computedStyles', False, 'array', inner=FieldMeta('', '', False, 'object', ref='DOMSnapshot.ComputedStyle')),
    )


@dataclass
class CaptureSnapshotReturn(DataType):
    """Return value of :meth:`DOMSnapshot.capture_snapshot`."""
    documents: List[DocumentSnapshot]
    strings: List[str]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('documents', 'documents', False, 'array', inner=FieldMeta('', '', False, 'object', ref='DOMSnapshot.DocumentSnapshot')),
        FieldMeta('strings', 'strings', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


class DOMSnapshot:
    """Commands of the DOMSnapshot domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def disable(self) -> None:
        """Disables DOM snapshot agent for the given page."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('DOMSnapshot.disable', _params)
        return None

    async def enable(self) -> None:
        """Enables DOM snapshot agent for the given page."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('DOMSnapshot.enable', _params)
        return None

    async def get_snapshot(self, *, computed_style_whitelist: List[str], include_event_listeners: Optional[bool] = None, include_paint_order: Optional[bool] = None, include_user_agent_shadow_tree: Optional[bool] = None) -> GetSnapshotReturn:
        """
        Returns a document snapshot, including the full DOM tree of the root node (including iframes,
        template contents, and imported documents) in a flattened array, as well as layout and
        white-listed computed style information for the nodes. Shadow DOM in the returned DOM tree is
        flattened.
        
        .. deprecated::
        :param computed_style_whitelist: Whitelist of computed styles to return.
        :param include_event_listeners: Whether or not to retrieve details of DOM listeners (default false).
        :param include_paint_order: Whether to determine and include the paint order index of LayoutTreeNodes (default false).
        :param include_user_agent_shadow_tree: Whether to include UA shadow tree in the snapshot (default false).
        """
        _params: Dict[str, Any] = {}
        _params['computedStyleWhitelist'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'primitive')), computed_style_whitelist)
        if include_event_listeners is not None:
            _params['includeEventListeners'] = encode(FieldMeta('', '', False, 'primitive'), include_event_listeners)
        if include_paint_order is not None:
            _params['includePaintOrder'] = encode(FieldMeta('', '', False, 'primitive'), include_paint_order)
        if include_user_agent_shadow_tree is not None:
            _params['includeUserAgentShadowTree'] = encode(FieldMeta('', '', False, 'primitive'), include_user_agent_shadow_tree)
        _result = await self._target.send('DOMSnapshot.getSnapshot', _params)
        return GetSnapshotReturn.from_json(_result)

    async def capture_snapshot(self, *, computed_styles: List[str], include_paint_order: Optional[bool] = None, include_dom_rects: Optional[bool] = None, include_blended_background_colors: Optional[bool] = None, include_text_color_opacities: Optional[bool] = None) -> CaptureSnapshotReturn:
        """
        Returns a document snapshot, including the full DOM tree of the root node (including iframes,
        template contents, and imported documents) in a flattened array, as well as layout and
        white-listed computed style information for the nodes. Shadow DOM in the returned DOM tree is
        flattened.
        :param computed_styles: Whitelist of computed styles to return.
        :param include_paint_order: Whether to include layout object paint orders into the snapshot.
        :param include_dom_rects: Whether to include DOM rectangles (offsetRects, clientRects, scrollRects) into the snapshot
        :param include_blended_background_colors: Whether to include blended background colors in the snapshot (default: false).
        Blended background color is achieved by blending background colors of all elements
        that overlap with the current element.
        :param include_text_color_opacities: Whether to include text color opacity in the snapshot (default: false).
        An element might have the opacity property set that affects the text color of the element.
        The final text color opacity is computed based on the opacity of all overlapping elements.
        """
        _params: Dict[str, Any] = {}
        _params['computedStyles'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'primitive')), computed_styles)
        if include_paint_order is not None:
            _params['includePaintOrder'] = encode(FieldMeta('', '', False, 'primitive'), include_paint_order)
        if include_dom_rects is not None:
            _params['includeDOMRects'] = encode(FieldMeta('', '', False, 'primitive'), include_dom_rects)
        if include_blended_background_colors is not None:
            _params['includeBlendedBackgroundColors'] = encode(FieldMeta('', '', False, 'primitive'), include_blended_background_colors)
        if include_text_color_opacities is not None:
            _params['includeTextColorOpacities'] = encode(FieldMeta('', '', False, 'primitive'), include_text_color_opacities)
        _result = await self._target.send('DOMSnapshot.captureSnapshot', _params)
        return CaptureSnapshotReturn.from_json(_result)
