"""Custom types and enums for the Overlay domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, register

if TYPE_CHECKING:
    from ..dom.types import NodeId as DOM_NodeId
    from ..dom.types import RGBA as DOM_RGBA
    from ..dom.types import Rect as DOM_Rect

@register("Overlay.SourceOrderConfig")
@dataclass
class SourceOrderConfig(DataType):
    """Configuration data for drawing the source order of an elements children."""
    parent_outline_color: DOM_RGBA
    child_outline_color: DOM_RGBA
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('parent_outline_color', 'parentOutlineColor', False, 'object', ref='DOM.RGBA'),
        FieldMeta('child_outline_color', 'childOutlineColor', False, 'object', ref='DOM.RGBA'),
    )


@register("Overlay.GridHighlightConfig")
@dataclass
class GridHighlightConfig(DataType):
    """Configuration data for the highlighting of Grid elements."""
    show_grid_extension_lines: Optional[bool] = None
    show_positive_line_numbers: Optional[bool] = None
    show_negative_line_numbers: Optional[bool] = None
    show_area_names: Optional[bool] = None
    show_line_names: Optional[bool] = None
    show_track_sizes: Optional[bool] = None
    grid_border_color: Optional[DOM_RGBA] = None
    cell_border_color: Optional[DOM_RGBA] = None
    row_line_color: Optional[DOM_RGBA] = None
    column_line_color: Optional[DOM_RGBA] = None
    grid_border_dash: Optional[bool] = None
    cell_border_dash: Optional[bool] = None
    row_line_dash: Optional[bool] = None
    column_line_dash: Optional[bool] = None
    row_gap_color: Optional[DOM_RGBA] = None
    row_hatch_color: Optional[DOM_RGBA] = None
    column_gap_color: Optional[DOM_RGBA] = None
    column_hatch_color: Optional[DOM_RGBA] = None
    area_border_color: Optional[DOM_RGBA] = None
    grid_background_color: Optional[DOM_RGBA] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('show_grid_extension_lines', 'showGridExtensionLines', True, 'primitive'),
        FieldMeta('show_positive_line_numbers', 'showPositiveLineNumbers', True, 'primitive'),
        FieldMeta('show_negative_line_numbers', 'showNegativeLineNumbers', True, 'primitive'),
        FieldMeta('show_area_names', 'showAreaNames', True, 'primitive'),
        FieldMeta('show_line_names', 'showLineNames', True, 'primitive'),
        FieldMeta('show_track_sizes', 'showTrackSizes', True, 'primitive'),
        FieldMeta('grid_border_color', 'gridBorderColor', True, 'object', ref='DOM.RGBA'),
        FieldMeta('cell_border_color', 'cellBorderColor', True, 'object', ref='DOM.RGBA'),
        FieldMeta('row_line_color', 'rowLineColor', True, 'object', ref='DOM.RGBA'),
        FieldMeta('column_line_color', 'columnLineColor', True, 'object', ref='DOM.RGBA'),
        FieldMeta('grid_border_dash', 'gridBorderDash', True, 'primitive'),
        FieldMeta('cell_border_dash', 'cellBorderDash', True, 'primitive'),
        FieldMeta('row_line_dash', 'rowLineDash', True, 'primitive'),
        FieldMeta('column_line_dash', 'columnLineDash', True, 'primitive'),
        FieldMeta('row_gap_color', 'rowGapColor', True, 'object', ref='DOM.RGBA'),
        FieldMeta('row_hatch_color', 'rowHatchColor', True, 'object', ref='DOM.RGBA'),
        FieldMeta('column_gap_color', 'columnGapColor', True, 'object', ref='DOM.RGBA'),
        FieldMeta('column_hatch_color', 'columnHatchColor', True, 'object', ref='DOM.RGBA'),
        FieldMeta('area_border_color', 'areaBorderColor', True, 'object', ref='DOM.RGBA'),
        FieldMeta('grid_background_color', 'gridBackgroundColor', True, 'object', ref='DOM.RGBA'),
    )


@register("Overlay.FlexContainerHighlightConfig")
@dataclass
class FlexContainerHighlightConfig(DataType):
    """Configuration data for the highlighting of Flex container elements."""
    container_border: Optional[LineStyle] = None
    line_separator: Optional[LineStyle] = None
    item_separator: Optional[LineStyle] = None
    main_distributed_space: Optional[BoxStyle] = None
    cross_distributed_space: Optional[BoxStyle] = None
    row_gap_space: Optional[BoxStyle] = None
    column_gap_space: Optional[BoxStyle] = None
    cross_alignment: Optional[LineStyle] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('container_border', 'containerBorder', True, 'object', ref='Overlay.LineStyle'),
        FieldMeta('line_separator', 'lineSeparator', True, 'object', ref='Overlay.LineStyle'),
        FieldMeta('item_separator', 'itemSeparator', True, 'object', ref='Overlay.LineStyle'),
        FieldMeta('main_distributed_space', 'mainDistributedSpace', True, 'object', ref='Overlay.BoxStyle'),
        FieldMeta('cross_distributed_space', 'crossDistributedSpace', True, 'object', ref='Overlay.BoxStyle'),
        FieldMeta('row_gap_space', 'rowGapSpace', True, 'object', ref='Overlay.BoxStyle'),
        FieldMeta('column_gap_space', 'columnGapSpace', True, 'object', ref='Overlay.BoxStyle'),
        FieldMeta('cross_alignment', 'crossAlignment', True, 'object', ref='Overlay.LineStyle'),
    )


@register("Overlay.FlexItemHighlightConfig")
@dataclass
class FlexItemHighlightConfig(DataType):
    """Configuration data for the highlighting of Flex item elements."""
    base_size_box: Optional[BoxStyle] = None
    base_size_border: Optional[LineStyle] = None
    flexibility_arrow: Optional[LineStyle] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('base_size_box', 'baseSizeBox', True, 'object', ref='Overlay.BoxStyle'),
        FieldMeta('base_size_border', 'baseSizeBorder', True, 'object', ref='Overlay.LineStyle'),
        FieldMeta('flexibility_arrow', 'flexibilityArrow', True, 'object', ref='Overlay.LineStyle'),
    )


@register("Overlay.LineStyle")
@dataclass
class LineStyle(DataType):
    """Style information for drawing a line."""
    color: Optional[DOM_RGBA] = None
    pattern: Optional[Literal['dashed', 'dotted']] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('color', 'color', True, 'object', ref='DOM.RGBA'),
        FieldMeta('pattern', 'pattern', True, 'primitive'),
    )


@register("Overlay.BoxStyle")
@dataclass
class BoxStyle(DataType):
    """Style information for drawing a box."""
    fill_color: Optional[DOM_RGBA] = None
    hatch_color: Optional[DOM_RGBA] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('fill_color', 'fillColor', True, 'object', ref='DOM.RGBA'),
        FieldMeta('hatch_color', 'hatchColor', True, 'object', ref='DOM.RGBA'),
    )


@register("Overlay.ContrastAlgorithm")
class ContrastAlgorithm(str, Enum):
    AA = 'aa'
    AAA = 'aaa'
    APCA = 'apca'


@register("Overlay.HighlightConfig")
@dataclass
class HighlightConfig(DataType):
    """Configuration data for the highlighting of page elements."""
    show_info: Optional[bool] = None
    show_styles: Optional[bool] = None
    show_rulers: Optional[bool] = None
    show_accessibility_info: Optional[bool] = None
    show_extension_lines: Optional[bool] = None
    content_color: Optional[DOM_RGBA] = None
    padding_color: Optional[DOM_RGBA] = None
    border_color: Optional[DOM_RGBA] = None
    margin_color: Optional[DOM_RGBA] = None
    event_target_color: Optional[DOM_RGBA] = None
    shape_color: Optional[DOM_RGBA] = None
    shape_margin_color: Optional[DOM_RGBA] = None
    css_grid_color: Optional[DOM_RGBA] = None
    color_format: Optional[ColorFormat] = None
    grid_highlight_config: Optional[GridHighlightConfig] = None
    flex_container_highlight_config: Optional[FlexContainerHighlightConfig] = None
    flex_item_highlight_config: Optional[FlexItemHighlightConfig] = None
    contrast_algorithm: Optional[ContrastAlgorithm] = None
    container_query_container_highlight_config: Optional[ContainerQueryContainerHighlightConfig] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('show_info', 'showInfo', True, 'primitive'),
        FieldMeta('show_styles', 'showStyles', True, 'primitive'),
        FieldMeta('show_rulers', 'showRulers', True, 'primitive'),
        FieldMeta('show_accessibility_info', 'showAccessibilityInfo', True, 'primitive'),
        FieldMeta('show_extension_lines', 'showExtensionLines', True, 'primitive'),
        FieldMeta('content_color', 'contentColor', True, 'object', ref='DOM.RGBA'),
        FieldMeta('padding_color', 'paddingColor', True, 'object', ref='DOM.RGBA'),
        FieldMeta('border_color', 'borderColor', True, 'object', ref='DOM.RGBA'),
        FieldMeta('margin_color', 'marginColor', True, 'object', ref='DOM.RGBA'),
        FieldMeta('event_target_color', 'eventTargetColor', True, 'object', ref='DOM.RGBA'),
        FieldMeta('shape_color', 'shapeColor', True, 'object', ref='DOM.RGBA'),
        FieldMeta('shape_margin_color', 'shapeMarginColor', True, 'object', ref='DOM.RGBA'),
        FieldMeta('css_grid_color', 'cssGridColor', True, 'object', ref='DOM.RGBA'),
        FieldMeta('color_format', 'colorFormat', True, 'enum', ref='Overlay.ColorFormat'),
        FieldMeta('grid_highlight_config', 'gridHighlightConfig', True, 'object', ref='Overlay.GridHighlightConfig'),
        FieldMeta('flex_container_highlight_config', 'flexContainerHighlightConfig', True, 'object', ref='Overlay.FlexContainerHighlightConfig'),
        FieldMeta('flex_item_highlight_config', 'flexItemHighlightConfig', True, 'object', ref='Overlay.FlexItemHighlightConfig'),
        FieldMeta('contrast_algorithm', 'contrastAlgorithm', True, 'enum', ref='Overlay.ContrastAlgorithm'),
        FieldMeta('container_query_container_highlight_config', 'containerQueryContainerHighlightConfig', True, 'object', ref='Overlay.ContainerQueryContainerHighlightConfig'),
    )


@register("Overlay.ColorFormat")
class ColorFormat(str, Enum):
    RGB = 'rgb'
    HSL = 'hsl'
    HWB = 'hwb'
    HEX = 'hex'


@register("Overlay.GridNodeHighlightConfig")
@dataclass
class GridNodeHighlightConfig(DataType):
    """Configurations for Persistent Grid Highlight"""
    grid_highlight_config: GridHighlightConfig
    node_id: DOM_NodeId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('grid_highlight_config', 'gridHighlightConfig', False, 'object', ref='Overlay.GridHighlightConfig'),
        FieldMeta('node_id', 'nodeId', False, 'primitive'),
    )


@register("Overlay.FlexNodeHighlightConfig")
@dataclass
class FlexNodeHighlightConfig(DataType):
    flex_container_highlight_config: FlexContainerHighlightConfig
    node_id: DOM_NodeId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('flex_container_highlight_config', 'flexContainerHighlightConfig', False, 'object', ref='Overlay.FlexContainerHighlightConfig'),
        FieldMeta('node_id', 'nodeId', False, 'primitive'),
    )


@register("Overlay.ScrollSnapContainerHighlightConfig")
@dataclass
class ScrollSnapContainerHighlightConfig(DataType):
    snapport_border: Optional[LineStyle] = None
    snap_area_border: Optional[LineStyle] = None
    scroll_margin_color: Optional[DOM_RGBA] = None
    scroll_padding_color: Optional[DOM_RGBA] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('snapport_border', 'snapportBorder', True, 'object', ref='Overlay.LineStyle'),
        FieldMeta('snap_area_border', 'snapAreaBorder', True, 'object', ref='Overlay.LineStyle'),
        FieldMeta('scroll_margin_color', 'scrollMarginColor', True, 'object', ref='DOM.RGBA'),
        FieldMeta('scroll_padding_color', 'scrollPaddingColor', True, 'object', ref='DOM.RGBA'),
    )


@register("Overlay.ScrollSnapHighlightConfig")
@dataclass
class ScrollSnapHighlightConfig(DataType):
    scroll_snap_container_highlight_config: ScrollSnapContainerHighlightConfig
    node_id: DOM_NodeId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('scroll_snap_container_highlight_config', 'scrollSnapContainerHighlightConfig', False, 'object', ref='Overlay.ScrollSnapContainerHighlightConfig'),
        FieldMeta('node_id', 'nodeId', False, 'primitive'),
    )


@register("Overlay.HingeConfig")
@dataclass
class HingeConfig(DataType):
    """Configuration for dual screen hinge"""
    rect: DOM_Rect
    content_color: Optional[DOM_RGBA] = None
    outline_color: Optional[DOM_RGBA] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('rect', 'rect', False, 'object', ref='DOM.Rect'),
        FieldMeta('content_color', 'contentColor', True, 'object', ref='DOM.RGBA'),
        FieldMeta('outline_color', 'outlineColor', True, 'object', ref='DOM.RGBA'),
    )


@register("Overlay.WindowControlsOverlayConfig")
@dataclass
class WindowControlsOverlayConfig(DataType):
    """Configuration for Window Controls Overlay"""
    show_css: bool
    selected_platform: str
    theme_color: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('show_css', 'showCSS', False, 'primitive'),
        FieldMeta('selected_platform', 'selectedPlatform', False, 'primitive'),
        FieldMeta('theme_color', 'themeColor', False, 'primitive'),
    )


@register("Overlay.ContainerQueryHighlightConfig")
@dataclass
class ContainerQueryHighlightConfig(DataType):
    container_query_container_highlight_config: ContainerQueryContainerHighlightConfig
    node_id: DOM_NodeId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('container_query_container_highlight_config', 'containerQueryContainerHighlightConfig', False, 'object', ref='Overlay.ContainerQueryContainerHighlightConfig'),
        FieldMeta('node_id', 'nodeId', False, 'primitive'),
    )


@register("Overlay.ContainerQueryContainerHighlightConfig")
@dataclass
class ContainerQueryContainerHighlightConfig(DataType):
    container_border: Optional[LineStyle] = None
    descendant_border: Optional[LineStyle] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('container_border', 'containerBorder', True, 'object', ref='Overlay.LineStyle'),
        FieldMeta('descendant_border', 'descendantBorder', True, 'object', ref='Overlay.LineStyle'),
    )


@register("Overlay.IsolatedElementHighlightConfig")
@dataclass
class IsolatedElementHighlightConfig(DataType):
    isolation_mode_highlight_config: IsolationModeHighlightConfig
    node_id: DOM_NodeId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('isolation_mode_highlight_config', 'isolationModeHighlightConfig', False, 'object', ref='Overlay.IsolationModeHighlightConfig'),
        FieldMeta('node_id', 'nodeId', False, 'primitive'),
    )


@register("Overlay.IsolationModeHighlightConfig")
@dataclass
class IsolationModeHighlightConfig(DataType):
    resizer_color: Optional[DOM_RGBA] = None
    resizer_handle_color: Optional[DOM_RGBA] = None
    mask_color: Optional[DOM_RGBA] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('resizer_color', 'resizerColor', True, 'object', ref='DOM.RGBA'),
        FieldMeta('resizer_handle_color', 'resizerHandleColor', True, 'object', ref='DOM.RGBA'),
        FieldMeta('mask_color', 'maskColor', True, 'object', ref='DOM.RGBA'),
    )


@register("Overlay.InspectMode")
class InspectMode(str, Enum):
    SEARCHFORNODE = 'searchForNode'
    SEARCHFORUASHADOWDOM = 'searchForUAShadowDOM'
    CAPTUREAREASCREENSHOT = 'captureAreaScreenshot'
    NONE = 'none'

__all__ = ["BoxStyle", "ColorFormat", "ContainerQueryContainerHighlightConfig", "ContainerQueryHighlightConfig", "ContrastAlgorithm", "FlexContainerHighlightConfig", "FlexItemHighlightConfig", "FlexNodeHighlightConfig", "GridHighlightConfig", "GridNodeHighlightConfig", "HighlightConfig", "HingeConfig", "InspectMode", "IsolatedElementHighlightConfig", "IsolationModeHighlightConfig", "LineStyle", "ScrollSnapContainerHighlightConfig", "ScrollSnapHighlightConfig", "SourceOrderConfig", "WindowControlsOverlayConfig"]
