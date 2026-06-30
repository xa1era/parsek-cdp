"""Events for the LayerTree domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import FieldMeta
from ..mixins.event import Event, register_event

if TYPE_CHECKING:
    from .types import (
        Layer,
        LayerId,
    )
    from ..dom.types import Rect as DOM_Rect

@register_event("LayerTree.layerPainted")
@dataclass
class LayerPainted(Event):
    layer_id: LayerId
    clip: DOM_Rect
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('layer_id', 'layerId', False, 'primitive'),
        FieldMeta('clip', 'clip', False, 'object', ref='DOM.Rect'),
    )


@register_event("LayerTree.layerTreeDidChange")
@dataclass
class LayerTreeDidChange(Event):
    layers: Optional[List[Layer]] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('layers', 'layers', True, 'array', inner=FieldMeta('', '', False, 'object', ref='LayerTree.Layer')),
    )

__all__ = ["LayerPainted", "LayerTreeDidChange"]
