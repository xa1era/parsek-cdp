"""Events for the Accessibility domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import FieldMeta
from ..mixins.event import Event, register_event

if TYPE_CHECKING:
    from .types import AXNode

@register_event("Accessibility.loadComplete")
@dataclass
class LoadComplete(Event):
    """
    The loadComplete event mirrors the load complete event sent by the browser to assistive
    technology when the web page has finished loading.
    """
    root: AXNode
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('root', 'root', False, 'object', ref='Accessibility.AXNode'),
    )


@register_event("Accessibility.nodesUpdated")
@dataclass
class NodesUpdated(Event):
    """The nodesUpdated event is sent every time a previously requested node has changed the in tree."""
    nodes: List[AXNode]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('nodes', 'nodes', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Accessibility.AXNode')),
    )

__all__ = ["LoadComplete", "NodesUpdated"]
