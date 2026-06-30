"""Custom types and enums for the Memory domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, register


@register("Memory.PressureLevel")
class PressureLevel(str, Enum):
    """Memory pressure level."""
    MODERATE = 'moderate'
    CRITICAL = 'critical'


@register("Memory.SamplingProfileNode")
@dataclass
class SamplingProfileNode(DataType):
    """Heap profile sample."""
    size: float
    total: float
    stack: List[str]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('size', 'size', False, 'primitive'),
        FieldMeta('total', 'total', False, 'primitive'),
        FieldMeta('stack', 'stack', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


@register("Memory.SamplingProfile")
@dataclass
class SamplingProfile(DataType):
    """Array of heap profile samples."""
    samples: List[SamplingProfileNode]
    modules: List[Module]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('samples', 'samples', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Memory.SamplingProfileNode')),
        FieldMeta('modules', 'modules', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Memory.Module')),
    )


@register("Memory.Module")
@dataclass
class Module(DataType):
    """Executable module information"""
    name: str
    uuid: str
    base_address: str
    size: float
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('name', 'name', False, 'primitive'),
        FieldMeta('uuid', 'uuid', False, 'primitive'),
        FieldMeta('base_address', 'baseAddress', False, 'primitive'),
        FieldMeta('size', 'size', False, 'primitive'),
    )


@register("Memory.DOMCounter")
@dataclass
class DOMCounter(DataType):
    """DOM object counter data."""
    name: str
    count: int
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('name', 'name', False, 'primitive'),
        FieldMeta('count', 'count', False, 'primitive'),
    )

__all__ = ["DOMCounter", "Module", "PressureLevel", "SamplingProfile", "SamplingProfileNode"]
