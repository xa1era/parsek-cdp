"""Custom types and enums for the FileSystem domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, register

if TYPE_CHECKING:
    from ..network.types import TimeSinceEpoch as Network_TimeSinceEpoch
    from ..storage.types import SerializedStorageKey as Storage_SerializedStorageKey

@register("FileSystem.File")
@dataclass
class File(DataType):
    name: str
    last_modified: Network_TimeSinceEpoch
    size: float
    type_: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('name', 'name', False, 'primitive'),
        FieldMeta('last_modified', 'lastModified', False, 'primitive'),
        FieldMeta('size', 'size', False, 'primitive'),
        FieldMeta('type_', 'type', False, 'primitive'),
    )


@register("FileSystem.Directory")
@dataclass
class Directory(DataType):
    name: str
    nested_directories: List[str]
    nested_files: List[File]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('name', 'name', False, 'primitive'),
        FieldMeta('nested_directories', 'nestedDirectories', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('nested_files', 'nestedFiles', False, 'array', inner=FieldMeta('', '', False, 'object', ref='FileSystem.File')),
    )


@register("FileSystem.BucketFileSystemLocator")
@dataclass
class BucketFileSystemLocator(DataType):
    storage_key: Storage_SerializedStorageKey
    path_components: List[str]
    bucket_name: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('storage_key', 'storageKey', False, 'primitive'),
        FieldMeta('path_components', 'pathComponents', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('bucket_name', 'bucketName', True, 'primitive'),
    )

__all__ = ["BucketFileSystemLocator", "Directory", "File"]
