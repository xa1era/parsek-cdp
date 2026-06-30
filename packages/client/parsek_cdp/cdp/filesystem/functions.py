"""Commands for the FileSystem domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode

if TYPE_CHECKING:
    from .types import (
        BucketFileSystemLocator,
        Directory,
    )

@dataclass
class GetDirectoryReturn(DataType):
    """Return value of :meth:`FileSystem.get_directory`."""
    directory: Directory
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('directory', 'directory', False, 'object', ref='FileSystem.Directory'),
    )


class FileSystem:
    """Commands of the FileSystem domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def get_directory(self, *, bucket_file_system_locator: BucketFileSystemLocator) -> GetDirectoryReturn:
        """:param bucket_file_system_locator:"""
        _params: Dict[str, Any] = {}
        _params['bucketFileSystemLocator'] = encode(FieldMeta('', '', False, 'object', ref='FileSystem.BucketFileSystemLocator'), bucket_file_system_locator)
        _result = await self._target.send('FileSystem.getDirectory', _params)
        return GetDirectoryReturn.from_json(_result)
