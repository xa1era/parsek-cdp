"""Custom types and enums for the Extensions domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, register


@register("Extensions.StorageArea")
class StorageArea(str, Enum):
    """Storage areas."""
    SESSION = 'session'
    LOCAL = 'local'
    SYNC = 'sync'
    MANAGED = 'managed'

__all__ = ["StorageArea"]
