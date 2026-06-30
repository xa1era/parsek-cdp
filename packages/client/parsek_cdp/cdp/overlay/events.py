"""Events for the Overlay domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import FieldMeta
from ..mixins.event import Event, register_event

if TYPE_CHECKING:
    from ..dom.types import BackendNodeId as DOM_BackendNodeId
    from ..dom.types import NodeId as DOM_NodeId
    from ..page.types import Viewport as Page_Viewport

@register_event("Overlay.inspectNodeRequested")
@dataclass
class InspectNodeRequested(Event):
    """
    Fired when the node should be inspected. This happens after call to `setInspectMode` or when
    user manually inspects an element.
    """
    backend_node_id: DOM_BackendNodeId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('backend_node_id', 'backendNodeId', False, 'primitive'),
    )


@register_event("Overlay.nodeHighlightRequested")
@dataclass
class NodeHighlightRequested(Event):
    """Fired when the node should be highlighted. This happens after call to `setInspectMode`."""
    node_id: DOM_NodeId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('node_id', 'nodeId', False, 'primitive'),
    )


@register_event("Overlay.screenshotRequested")
@dataclass
class ScreenshotRequested(Event):
    """Fired when user asks to capture screenshot of some area on the page."""
    viewport: Page_Viewport
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('viewport', 'viewport', False, 'object', ref='Page.Viewport'),
    )


@register_event("Overlay.inspectModeCanceled")
@dataclass
class InspectModeCanceled(Event):
    """Fired when user cancels the inspect mode."""
    __FIELDS__: ClassVar[tuple] = ()

__all__ = ["InspectModeCanceled", "InspectNodeRequested", "NodeHighlightRequested", "ScreenshotRequested"]
