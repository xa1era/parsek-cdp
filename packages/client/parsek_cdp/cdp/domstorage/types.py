"""Custom types and enums for the DOMStorage domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, register


type SerializedStorageKey = str


@register("DOMStorage.StorageId")
@dataclass
class StorageId(DataType):
    """DOM Storage identifier."""
    is_local_storage: bool
    security_origin: Optional[str] = None
    storage_key: Optional[SerializedStorageKey] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('is_local_storage', 'isLocalStorage', False, 'primitive'),
        FieldMeta('security_origin', 'securityOrigin', True, 'primitive'),
        FieldMeta('storage_key', 'storageKey', True, 'primitive'),
    )


type Item = List[str]  # DOM Storage item.

__all__ = ["Item", "SerializedStorageKey", "StorageId"]
