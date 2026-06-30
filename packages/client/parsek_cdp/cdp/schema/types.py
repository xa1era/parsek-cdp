"""Custom types and enums for the Schema domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, register


@register("Schema.Domain")
@dataclass
class Domain(DataType):
    """Description of the protocol domain."""
    name: str
    version: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('name', 'name', False, 'primitive'),
        FieldMeta('version', 'version', False, 'primitive'),
    )

__all__ = ["Domain"]
