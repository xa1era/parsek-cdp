"""Commands for the Overlay domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode

if TYPE_CHECKING:
    from .types import (
        ColorFormat,
        ContainerQueryHighlightConfig,
        FlexNodeHighlightConfig,
        GridNodeHighlightConfig,
        HighlightConfig,
        HingeConfig,
        InspectMode,
        IsolatedElementHighlightConfig,
        ScrollSnapHighlightConfig,
        SourceOrderConfig,
        WindowControlsOverlayConfig,
    )
    from ..dom.types import BackendNodeId as DOM_BackendNodeId
    from ..dom.types import NodeId as DOM_NodeId
    from ..dom.types import Quad as DOM_Quad
    from ..dom.types import RGBA as DOM_RGBA
    from ..page.types import FrameId as Page_FrameId
    from ..runtime.types import RemoteObjectId as Runtime_RemoteObjectId

@dataclass
class GetHighlightObjectForTestReturn(DataType):
    """Return value of :meth:`Overlay.get_highlight_object_for_test`."""
    highlight: Dict[str, Any]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('highlight', 'highlight', False, 'primitive'),
    )


@dataclass
class GetGridHighlightObjectsForTestReturn(DataType):
    """Return value of :meth:`Overlay.get_grid_highlight_objects_for_test`."""
    highlights: Dict[str, Any]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('highlights', 'highlights', False, 'primitive'),
    )


@dataclass
class GetSourceOrderHighlightObjectForTestReturn(DataType):
    """Return value of :meth:`Overlay.get_source_order_highlight_object_for_test`."""
    highlight: Dict[str, Any]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('highlight', 'highlight', False, 'primitive'),
    )


class Overlay:
    """Commands of the Overlay domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def disable(self) -> None:
        """Disables domain notifications."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Overlay.disable', _params)
        return None

    async def enable(self) -> None:
        """Enables domain notifications."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Overlay.enable', _params)
        return None

    async def get_highlight_object_for_test(self, *, node_id: DOM_NodeId, include_distance: Optional[bool] = None, include_style: Optional[bool] = None, color_format: Optional[ColorFormat] = None, show_accessibility_info: Optional[bool] = None) -> GetHighlightObjectForTestReturn:
        """
        For testing.
        :param node_id: Id of the node to get highlight object for.
        :param include_distance: Whether to include distance info.
        :param include_style: Whether to include style info.
        :param color_format: The color format to get config with (default: hex).
        :param show_accessibility_info: Whether to show accessibility info (default: true).
        """
        _params: Dict[str, Any] = {}
        _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        if include_distance is not None:
            _params['includeDistance'] = encode(FieldMeta('', '', False, 'primitive'), include_distance)
        if include_style is not None:
            _params['includeStyle'] = encode(FieldMeta('', '', False, 'primitive'), include_style)
        if color_format is not None:
            _params['colorFormat'] = encode(FieldMeta('', '', False, 'enum', ref='Overlay.ColorFormat'), color_format)
        if show_accessibility_info is not None:
            _params['showAccessibilityInfo'] = encode(FieldMeta('', '', False, 'primitive'), show_accessibility_info)
        _result = await self._target.send('Overlay.getHighlightObjectForTest', _params)
        return GetHighlightObjectForTestReturn.from_json(_result)

    async def get_grid_highlight_objects_for_test(self, *, node_ids: List[DOM_NodeId]) -> GetGridHighlightObjectsForTestReturn:
        """
        For Persistent Grid testing.
        :param node_ids: Ids of the node to get highlight object for.
        """
        _params: Dict[str, Any] = {}
        _params['nodeIds'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'primitive')), node_ids)
        _result = await self._target.send('Overlay.getGridHighlightObjectsForTest', _params)
        return GetGridHighlightObjectsForTestReturn.from_json(_result)

    async def get_source_order_highlight_object_for_test(self, *, node_id: DOM_NodeId) -> GetSourceOrderHighlightObjectForTestReturn:
        """
        For Source Order Viewer testing.
        :param node_id: Id of the node to highlight.
        """
        _params: Dict[str, Any] = {}
        _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        _result = await self._target.send('Overlay.getSourceOrderHighlightObjectForTest', _params)
        return GetSourceOrderHighlightObjectForTestReturn.from_json(_result)

    async def hide_highlight(self) -> None:
        """Hides any highlight."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Overlay.hideHighlight', _params)
        return None

    async def highlight_frame(self, *, frame_id: Page_FrameId, content_color: Optional[DOM_RGBA] = None, content_outline_color: Optional[DOM_RGBA] = None) -> None:
        """
        Highlights owner element of the frame with given id.
        Deprecated: Doesn't work reliably and cannot be fixed due to process
        separation (the owner node might be in a different process). Determine
        the owner node in the client and use highlightNode.
        
        .. deprecated::
        :param frame_id: Identifier of the frame to highlight.
        :param content_color: The content box highlight fill color (default: transparent).
        :param content_outline_color: The content box highlight outline color (default: transparent).
        """
        _params: Dict[str, Any] = {}
        _params['frameId'] = encode(FieldMeta('', '', False, 'primitive'), frame_id)
        if content_color is not None:
            _params['contentColor'] = encode(FieldMeta('', '', False, 'object', ref='DOM.RGBA'), content_color)
        if content_outline_color is not None:
            _params['contentOutlineColor'] = encode(FieldMeta('', '', False, 'object', ref='DOM.RGBA'), content_outline_color)
        _result = await self._target.send('Overlay.highlightFrame', _params)
        return None

    async def highlight_node(self, *, highlight_config: HighlightConfig, node_id: Optional[DOM_NodeId] = None, backend_node_id: Optional[DOM_BackendNodeId] = None, object_id: Optional[Runtime_RemoteObjectId] = None, selector: Optional[str] = None) -> None:
        """
        Highlights DOM node with given id or with the given JavaScript object wrapper. Either nodeId or
        objectId must be specified.
        :param highlight_config: A descriptor for the highlight appearance.
        :param node_id: Identifier of the node to highlight.
        :param backend_node_id: Identifier of the backend node to highlight.
        :param object_id: JavaScript object id of the node to be highlighted.
        :param selector: Selectors to highlight relevant nodes.
        """
        _params: Dict[str, Any] = {}
        _params['highlightConfig'] = encode(FieldMeta('', '', False, 'object', ref='Overlay.HighlightConfig'), highlight_config)
        if node_id is not None:
            _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        if backend_node_id is not None:
            _params['backendNodeId'] = encode(FieldMeta('', '', False, 'primitive'), backend_node_id)
        if object_id is not None:
            _params['objectId'] = encode(FieldMeta('', '', False, 'primitive'), object_id)
        if selector is not None:
            _params['selector'] = encode(FieldMeta('', '', False, 'primitive'), selector)
        _result = await self._target.send('Overlay.highlightNode', _params)
        return None

    async def highlight_quad(self, *, quad: DOM_Quad, color: Optional[DOM_RGBA] = None, outline_color: Optional[DOM_RGBA] = None) -> None:
        """
        Highlights given quad. Coordinates are absolute with respect to the main frame viewport.
        :param quad: Quad to highlight
        :param color: The highlight fill color (default: transparent).
        :param outline_color: The highlight outline color (default: transparent).
        """
        _params: Dict[str, Any] = {}
        _params['quad'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'primitive')), quad)
        if color is not None:
            _params['color'] = encode(FieldMeta('', '', False, 'object', ref='DOM.RGBA'), color)
        if outline_color is not None:
            _params['outlineColor'] = encode(FieldMeta('', '', False, 'object', ref='DOM.RGBA'), outline_color)
        _result = await self._target.send('Overlay.highlightQuad', _params)
        return None

    async def highlight_rect(self, *, x: int, y: int, width: int, height: int, color: Optional[DOM_RGBA] = None, outline_color: Optional[DOM_RGBA] = None) -> None:
        """
        Highlights given rectangle. Coordinates are absolute with respect to the main frame viewport.
        Issue: the method does not handle device pixel ratio (DPR) correctly.
        The coordinates currently have to be adjusted by the client
        if DPR is not 1 (see crbug.com/437807128).
        :param x: X coordinate
        :param y: Y coordinate
        :param width: Rectangle width
        :param height: Rectangle height
        :param color: The highlight fill color (default: transparent).
        :param outline_color: The highlight outline color (default: transparent).
        """
        _params: Dict[str, Any] = {}
        _params['x'] = encode(FieldMeta('', '', False, 'primitive'), x)
        _params['y'] = encode(FieldMeta('', '', False, 'primitive'), y)
        _params['width'] = encode(FieldMeta('', '', False, 'primitive'), width)
        _params['height'] = encode(FieldMeta('', '', False, 'primitive'), height)
        if color is not None:
            _params['color'] = encode(FieldMeta('', '', False, 'object', ref='DOM.RGBA'), color)
        if outline_color is not None:
            _params['outlineColor'] = encode(FieldMeta('', '', False, 'object', ref='DOM.RGBA'), outline_color)
        _result = await self._target.send('Overlay.highlightRect', _params)
        return None

    async def highlight_source_order(self, *, source_order_config: SourceOrderConfig, node_id: Optional[DOM_NodeId] = None, backend_node_id: Optional[DOM_BackendNodeId] = None, object_id: Optional[Runtime_RemoteObjectId] = None) -> None:
        """
        Highlights the source order of the children of the DOM node with given id or with the given
        JavaScript object wrapper. Either nodeId or objectId must be specified.
        :param source_order_config: A descriptor for the appearance of the overlay drawing.
        :param node_id: Identifier of the node to highlight.
        :param backend_node_id: Identifier of the backend node to highlight.
        :param object_id: JavaScript object id of the node to be highlighted.
        """
        _params: Dict[str, Any] = {}
        _params['sourceOrderConfig'] = encode(FieldMeta('', '', False, 'object', ref='Overlay.SourceOrderConfig'), source_order_config)
        if node_id is not None:
            _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        if backend_node_id is not None:
            _params['backendNodeId'] = encode(FieldMeta('', '', False, 'primitive'), backend_node_id)
        if object_id is not None:
            _params['objectId'] = encode(FieldMeta('', '', False, 'primitive'), object_id)
        _result = await self._target.send('Overlay.highlightSourceOrder', _params)
        return None

    async def set_inspect_mode(self, *, mode: InspectMode, highlight_config: Optional[HighlightConfig] = None) -> None:
        """
        Enters the 'inspect' mode. In this mode, elements that user is hovering over are highlighted.
        Backend then generates 'inspectNodeRequested' event upon element selection.
        :param mode: Set an inspection mode.
        :param highlight_config: A descriptor for the highlight appearance of hovered-over nodes. May be omitted if `enabled
        == false`.
        """
        _params: Dict[str, Any] = {}
        _params['mode'] = encode(FieldMeta('', '', False, 'enum', ref='Overlay.InspectMode'), mode)
        if highlight_config is not None:
            _params['highlightConfig'] = encode(FieldMeta('', '', False, 'object', ref='Overlay.HighlightConfig'), highlight_config)
        _result = await self._target.send('Overlay.setInspectMode', _params)
        return None

    async def set_show_ad_highlights(self, *, show: bool) -> None:
        """
        Highlights owner element of all frames detected to be ads.
        :param show: True for showing ad highlights
        """
        _params: Dict[str, Any] = {}
        _params['show'] = encode(FieldMeta('', '', False, 'primitive'), show)
        _result = await self._target.send('Overlay.setShowAdHighlights', _params)
        return None

    async def set_paused_in_debugger_message(self, *, message: Optional[str] = None) -> None:
        """:param message: The message to display, also triggers resume and step over controls."""
        _params: Dict[str, Any] = {}
        if message is not None:
            _params['message'] = encode(FieldMeta('', '', False, 'primitive'), message)
        _result = await self._target.send('Overlay.setPausedInDebuggerMessage', _params)
        return None

    async def set_show_debug_borders(self, *, show: bool) -> None:
        """
        Requests that backend shows debug borders on layers
        :param show: True for showing debug borders
        """
        _params: Dict[str, Any] = {}
        _params['show'] = encode(FieldMeta('', '', False, 'primitive'), show)
        _result = await self._target.send('Overlay.setShowDebugBorders', _params)
        return None

    async def set_show_fps_counter(self, *, show: bool) -> None:
        """
        Requests that backend shows the FPS counter
        :param show: True for showing the FPS counter
        """
        _params: Dict[str, Any] = {}
        _params['show'] = encode(FieldMeta('', '', False, 'primitive'), show)
        _result = await self._target.send('Overlay.setShowFPSCounter', _params)
        return None

    async def set_show_grid_overlays(self, *, grid_node_highlight_configs: List[GridNodeHighlightConfig]) -> None:
        """
        Highlight multiple elements with the CSS Grid overlay.
        :param grid_node_highlight_configs: An array of node identifiers and descriptors for the highlight appearance.
        """
        _params: Dict[str, Any] = {}
        _params['gridNodeHighlightConfigs'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Overlay.GridNodeHighlightConfig')), grid_node_highlight_configs)
        _result = await self._target.send('Overlay.setShowGridOverlays', _params)
        return None

    async def set_show_flex_overlays(self, *, flex_node_highlight_configs: List[FlexNodeHighlightConfig]) -> None:
        """:param flex_node_highlight_configs: An array of node identifiers and descriptors for the highlight appearance."""
        _params: Dict[str, Any] = {}
        _params['flexNodeHighlightConfigs'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Overlay.FlexNodeHighlightConfig')), flex_node_highlight_configs)
        _result = await self._target.send('Overlay.setShowFlexOverlays', _params)
        return None

    async def set_show_scroll_snap_overlays(self, *, scroll_snap_highlight_configs: List[ScrollSnapHighlightConfig]) -> None:
        """:param scroll_snap_highlight_configs: An array of node identifiers and descriptors for the highlight appearance."""
        _params: Dict[str, Any] = {}
        _params['scrollSnapHighlightConfigs'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Overlay.ScrollSnapHighlightConfig')), scroll_snap_highlight_configs)
        _result = await self._target.send('Overlay.setShowScrollSnapOverlays', _params)
        return None

    async def set_show_container_query_overlays(self, *, container_query_highlight_configs: List[ContainerQueryHighlightConfig]) -> None:
        """:param container_query_highlight_configs: An array of node identifiers and descriptors for the highlight appearance."""
        _params: Dict[str, Any] = {}
        _params['containerQueryHighlightConfigs'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Overlay.ContainerQueryHighlightConfig')), container_query_highlight_configs)
        _result = await self._target.send('Overlay.setShowContainerQueryOverlays', _params)
        return None

    async def set_show_paint_rects(self, *, result: bool) -> None:
        """
        Requests that backend shows paint rectangles
        :param result: True for showing paint rectangles
        """
        _params: Dict[str, Any] = {}
        _params['result'] = encode(FieldMeta('', '', False, 'primitive'), result)
        _result = await self._target.send('Overlay.setShowPaintRects', _params)
        return None

    async def set_show_layout_shift_regions(self, *, result: bool) -> None:
        """
        Requests that backend shows layout shift regions
        :param result: True for showing layout shift regions
        """
        _params: Dict[str, Any] = {}
        _params['result'] = encode(FieldMeta('', '', False, 'primitive'), result)
        _result = await self._target.send('Overlay.setShowLayoutShiftRegions', _params)
        return None

    async def set_show_scroll_bottleneck_rects(self, *, show: bool) -> None:
        """
        Requests that backend shows scroll bottleneck rects
        :param show: True for showing scroll bottleneck rects
        """
        _params: Dict[str, Any] = {}
        _params['show'] = encode(FieldMeta('', '', False, 'primitive'), show)
        _result = await self._target.send('Overlay.setShowScrollBottleneckRects', _params)
        return None

    async def set_show_hit_test_borders(self, *, show: bool) -> None:
        """
        Deprecated, no longer has any effect.
        
        .. deprecated::
        :param show: True for showing hit-test borders
        """
        _params: Dict[str, Any] = {}
        _params['show'] = encode(FieldMeta('', '', False, 'primitive'), show)
        _result = await self._target.send('Overlay.setShowHitTestBorders', _params)
        return None

    async def set_show_web_vitals(self, *, show: bool) -> None:
        """
        Deprecated, no longer has any effect.
        
        .. deprecated::
        :param show:
        """
        _params: Dict[str, Any] = {}
        _params['show'] = encode(FieldMeta('', '', False, 'primitive'), show)
        _result = await self._target.send('Overlay.setShowWebVitals', _params)
        return None

    async def set_show_viewport_size_on_resize(self, *, show: bool) -> None:
        """
        Paints viewport size upon main frame resize.
        :param show: Whether to paint size or not.
        """
        _params: Dict[str, Any] = {}
        _params['show'] = encode(FieldMeta('', '', False, 'primitive'), show)
        _result = await self._target.send('Overlay.setShowViewportSizeOnResize', _params)
        return None

    async def set_show_hinge(self, *, hinge_config: Optional[HingeConfig] = None) -> None:
        """
        Add a dual screen device hinge
        :param hinge_config: hinge data, null means hideHinge
        """
        _params: Dict[str, Any] = {}
        if hinge_config is not None:
            _params['hingeConfig'] = encode(FieldMeta('', '', False, 'object', ref='Overlay.HingeConfig'), hinge_config)
        _result = await self._target.send('Overlay.setShowHinge', _params)
        return None

    async def set_show_isolated_elements(self, *, isolated_element_highlight_configs: List[IsolatedElementHighlightConfig]) -> None:
        """
        Show elements in isolation mode with overlays.
        :param isolated_element_highlight_configs: An array of node identifiers and descriptors for the highlight appearance.
        """
        _params: Dict[str, Any] = {}
        _params['isolatedElementHighlightConfigs'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Overlay.IsolatedElementHighlightConfig')), isolated_element_highlight_configs)
        _result = await self._target.send('Overlay.setShowIsolatedElements', _params)
        return None

    async def set_show_window_controls_overlay(self, *, window_controls_overlay_config: Optional[WindowControlsOverlayConfig] = None) -> None:
        """
        Show Window Controls Overlay for PWA
        :param window_controls_overlay_config: Window Controls Overlay data, null means hide Window Controls Overlay
        """
        _params: Dict[str, Any] = {}
        if window_controls_overlay_config is not None:
            _params['windowControlsOverlayConfig'] = encode(FieldMeta('', '', False, 'object', ref='Overlay.WindowControlsOverlayConfig'), window_controls_overlay_config)
        _result = await self._target.send('Overlay.setShowWindowControlsOverlay', _params)
        return None
