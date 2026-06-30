"""Events for the CSS domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import FieldMeta
from ..mixins.event import Event, register_event

if TYPE_CHECKING:
    from .types import (
        CSSStyleSheetHeader,
        FontFace,
    )
    from ..dom.types import NodeId as DOM_NodeId
    from ..dom.types import StyleSheetId as DOM_StyleSheetId

@register_event("CSS.fontsUpdated")
@dataclass
class FontsUpdated(Event):
    """
    Fires whenever a web font is updated.  A non-empty font parameter indicates a successfully loaded
    web font.
    """
    font: Optional[FontFace] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('font', 'font', True, 'object', ref='CSS.FontFace'),
    )


@register_event("CSS.mediaQueryResultChanged")
@dataclass
class MediaQueryResultChanged(Event):
    """
    Fires whenever a MediaQuery result changes (for example, after a browser window has been
    resized.) The current implementation considers only viewport-dependent media features.
    """
    __FIELDS__: ClassVar[tuple] = ()


@register_event("CSS.styleSheetAdded")
@dataclass
class StyleSheetAdded(Event):
    """Fired whenever an active document stylesheet is added."""
    header: CSSStyleSheetHeader
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('header', 'header', False, 'object', ref='CSS.CSSStyleSheetHeader'),
    )


@register_event("CSS.styleSheetChanged")
@dataclass
class StyleSheetChanged(Event):
    """Fired whenever a stylesheet is changed as a result of the client operation."""
    style_sheet_id: DOM_StyleSheetId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('style_sheet_id', 'styleSheetId', False, 'primitive'),
    )


@register_event("CSS.styleSheetRemoved")
@dataclass
class StyleSheetRemoved(Event):
    """Fired whenever an active document stylesheet is removed."""
    style_sheet_id: DOM_StyleSheetId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('style_sheet_id', 'styleSheetId', False, 'primitive'),
    )


@register_event("CSS.computedStyleUpdated")
@dataclass
class ComputedStyleUpdated(Event):
    node_id: DOM_NodeId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('node_id', 'nodeId', False, 'primitive'),
    )

__all__ = ["ComputedStyleUpdated", "FontsUpdated", "MediaQueryResultChanged", "StyleSheetAdded", "StyleSheetChanged", "StyleSheetRemoved"]
