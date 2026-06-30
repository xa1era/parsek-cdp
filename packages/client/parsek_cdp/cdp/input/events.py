"""Events for the Input domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import FieldMeta
from ..mixins.event import Event, register_event

if TYPE_CHECKING:
    from .types import DragData

@register_event("Input.dragIntercepted")
@dataclass
class DragIntercepted(Event):
    """
    Emitted only when `Input.setInterceptDrags` is enabled. Use this data with `Input.dispatchDragEvent` to
    restore normal drag and drop behavior.
    """
    data: DragData
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('data', 'data', False, 'object', ref='Input.DragData'),
    )

__all__ = ["DragIntercepted"]
