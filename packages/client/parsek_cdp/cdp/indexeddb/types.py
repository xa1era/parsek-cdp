"""Custom types and enums for the IndexedDB domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, register

if TYPE_CHECKING:
    from ..runtime.types import RemoteObject as Runtime_RemoteObject

@register("IndexedDB.DatabaseWithObjectStores")
@dataclass
class DatabaseWithObjectStores(DataType):
    """Database with an array of object stores."""
    name: str
    version: float
    object_stores: List[ObjectStore]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('name', 'name', False, 'primitive'),
        FieldMeta('version', 'version', False, 'primitive'),
        FieldMeta('object_stores', 'objectStores', False, 'array', inner=FieldMeta('', '', False, 'object', ref='IndexedDB.ObjectStore')),
    )


@register("IndexedDB.ObjectStore")
@dataclass
class ObjectStore(DataType):
    """Object store."""
    name: str
    key_path: KeyPath
    auto_increment: bool
    indexes: List[ObjectStoreIndex]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('name', 'name', False, 'primitive'),
        FieldMeta('key_path', 'keyPath', False, 'object', ref='IndexedDB.KeyPath'),
        FieldMeta('auto_increment', 'autoIncrement', False, 'primitive'),
        FieldMeta('indexes', 'indexes', False, 'array', inner=FieldMeta('', '', False, 'object', ref='IndexedDB.ObjectStoreIndex')),
    )


@register("IndexedDB.ObjectStoreIndex")
@dataclass
class ObjectStoreIndex(DataType):
    """Object store index."""
    name: str
    key_path: KeyPath
    unique: bool
    multi_entry: bool
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('name', 'name', False, 'primitive'),
        FieldMeta('key_path', 'keyPath', False, 'object', ref='IndexedDB.KeyPath'),
        FieldMeta('unique', 'unique', False, 'primitive'),
        FieldMeta('multi_entry', 'multiEntry', False, 'primitive'),
    )


@register("IndexedDB.Key")
@dataclass
class Key(DataType):
    """Key."""
    type_: Literal['number', 'string', 'date', 'array']
    number: Optional[float] = None
    string: Optional[str] = None
    date: Optional[float] = None
    array: Optional[List[Key]] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('type_', 'type', False, 'primitive'),
        FieldMeta('number', 'number', True, 'primitive'),
        FieldMeta('string', 'string', True, 'primitive'),
        FieldMeta('date', 'date', True, 'primitive'),
        FieldMeta('array', 'array', True, 'array', inner=FieldMeta('', '', False, 'object', ref='IndexedDB.Key')),
    )


@register("IndexedDB.KeyRange")
@dataclass
class KeyRange(DataType):
    """Key range."""
    lower_open: bool
    upper_open: bool
    lower: Optional[Key] = None
    upper: Optional[Key] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('lower_open', 'lowerOpen', False, 'primitive'),
        FieldMeta('upper_open', 'upperOpen', False, 'primitive'),
        FieldMeta('lower', 'lower', True, 'object', ref='IndexedDB.Key'),
        FieldMeta('upper', 'upper', True, 'object', ref='IndexedDB.Key'),
    )


@register("IndexedDB.DataEntry")
@dataclass
class DataEntry(DataType):
    """Data entry."""
    key: Runtime_RemoteObject
    primary_key: Runtime_RemoteObject
    value: Runtime_RemoteObject
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('key', 'key', False, 'object', ref='Runtime.RemoteObject'),
        FieldMeta('primary_key', 'primaryKey', False, 'object', ref='Runtime.RemoteObject'),
        FieldMeta('value', 'value', False, 'object', ref='Runtime.RemoteObject'),
    )


@register("IndexedDB.KeyPath")
@dataclass
class KeyPath(DataType):
    """Key path."""
    type_: Literal['null', 'string', 'array']
    string: Optional[str] = None
    array: Optional[List[str]] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('type_', 'type', False, 'primitive'),
        FieldMeta('string', 'string', True, 'primitive'),
        FieldMeta('array', 'array', True, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )

__all__ = ["DataEntry", "DatabaseWithObjectStores", "Key", "KeyPath", "KeyRange", "ObjectStore", "ObjectStoreIndex"]
