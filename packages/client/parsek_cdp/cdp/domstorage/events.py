"""Events for the DOMStorage domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import FieldMeta
from ..mixins.event import Event, register_event

if TYPE_CHECKING:
    from .types import StorageId

@register_event("DOMStorage.domStorageItemAdded")
@dataclass
class DomStorageItemAdded(Event):
    storage_id: StorageId
    key: str
    new_value: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('storage_id', 'storageId', False, 'object', ref='DOMStorage.StorageId'),
        FieldMeta('key', 'key', False, 'primitive'),
        FieldMeta('new_value', 'newValue', False, 'primitive'),
    )


@register_event("DOMStorage.domStorageItemRemoved")
@dataclass
class DomStorageItemRemoved(Event):
    storage_id: StorageId
    key: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('storage_id', 'storageId', False, 'object', ref='DOMStorage.StorageId'),
        FieldMeta('key', 'key', False, 'primitive'),
    )


@register_event("DOMStorage.domStorageItemUpdated")
@dataclass
class DomStorageItemUpdated(Event):
    storage_id: StorageId
    key: str
    old_value: str
    new_value: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('storage_id', 'storageId', False, 'object', ref='DOMStorage.StorageId'),
        FieldMeta('key', 'key', False, 'primitive'),
        FieldMeta('old_value', 'oldValue', False, 'primitive'),
        FieldMeta('new_value', 'newValue', False, 'primitive'),
    )


@register_event("DOMStorage.domStorageItemsCleared")
@dataclass
class DomStorageItemsCleared(Event):
    storage_id: StorageId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('storage_id', 'storageId', False, 'object', ref='DOMStorage.StorageId'),
    )

__all__ = ["DomStorageItemAdded", "DomStorageItemRemoved", "DomStorageItemUpdated", "DomStorageItemsCleared"]
