"""Events for the Performance domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import FieldMeta
from ..mixins.event import Event, register_event

if TYPE_CHECKING:
    from .types import Metric

@register_event("Performance.metrics")
@dataclass
class Metrics(Event):
    """Current values of the metrics."""
    metrics: List[Metric]
    title: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('metrics', 'metrics', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Performance.Metric')),
        FieldMeta('title', 'title', False, 'primitive'),
    )

__all__ = ["Metrics"]
