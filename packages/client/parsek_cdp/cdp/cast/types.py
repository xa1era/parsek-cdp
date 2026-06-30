"""Custom types and enums for the Cast domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, register


@register("Cast.Sink")
@dataclass
class Sink(DataType):
    name: str
    id: str
    session: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('name', 'name', False, 'primitive'),
        FieldMeta('id', 'id', False, 'primitive'),
        FieldMeta('session', 'session', True, 'primitive'),
    )

__all__ = ["Sink"]
