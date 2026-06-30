"""Custom types and enums for the Performance domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, register


@register("Performance.Metric")
@dataclass
class Metric(DataType):
    """Run-time execution metric."""
    name: str
    value: float
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('name', 'name', False, 'primitive'),
        FieldMeta('value', 'value', False, 'primitive'),
    )

__all__ = ["Metric"]
