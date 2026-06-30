"""Commands for the Extensions domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode

if TYPE_CHECKING:
    from .types import StorageArea

@dataclass
class LoadUnpackedReturn(DataType):
    """Return value of :meth:`Extensions.load_unpacked`."""
    id: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('id', 'id', False, 'primitive'),
    )


@dataclass
class GetStorageItemsReturn(DataType):
    """Return value of :meth:`Extensions.get_storage_items`."""
    data: Dict[str, Any]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('data', 'data', False, 'primitive'),
    )


class Extensions:
    """Commands of the Extensions domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def load_unpacked(self, *, path: str) -> LoadUnpackedReturn:
        """
        Installs an unpacked extension from the filesystem similar to
        --load-extension CLI flags. Returns extension ID once the extension
        has been installed. Available if the client is connected using the
        --remote-debugging-pipe flag and the --enable-unsafe-extension-debugging
        flag is set.
        :param path: Absolute file path.
        """
        _params: Dict[str, Any] = {}
        _params['path'] = encode(FieldMeta('', '', False, 'primitive'), path)
        _result = await self._target.send('Extensions.loadUnpacked', _params)
        return LoadUnpackedReturn.from_json(_result)

    async def uninstall(self, *, id: str) -> None:
        """
        Uninstalls an unpacked extension (others not supported) from the profile.
        Available if the client is connected using the --remote-debugging-pipe flag
        and the --enable-unsafe-extension-debugging.
        :param id: Extension id.
        """
        _params: Dict[str, Any] = {}
        _params['id'] = encode(FieldMeta('', '', False, 'primitive'), id)
        _result = await self._target.send('Extensions.uninstall', _params)
        return None

    async def get_storage_items(self, *, id: str, storage_area: StorageArea, keys: Optional[List[str]] = None) -> GetStorageItemsReturn:
        """
        Gets data from extension storage in the given `storageArea`. If `keys` is
        specified, these are used to filter the result.
        :param id: ID of extension.
        :param storage_area: StorageArea to retrieve data from.
        :param keys: Keys to retrieve.
        """
        _params: Dict[str, Any] = {}
        _params['id'] = encode(FieldMeta('', '', False, 'primitive'), id)
        _params['storageArea'] = encode(FieldMeta('', '', False, 'enum', ref='Extensions.StorageArea'), storage_area)
        if keys is not None:
            _params['keys'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'primitive')), keys)
        _result = await self._target.send('Extensions.getStorageItems', _params)
        return GetStorageItemsReturn.from_json(_result)

    async def remove_storage_items(self, *, id: str, storage_area: StorageArea, keys: List[str]) -> None:
        """
        Removes `keys` from extension storage in the given `storageArea`.
        :param id: ID of extension.
        :param storage_area: StorageArea to remove data from.
        :param keys: Keys to remove.
        """
        _params: Dict[str, Any] = {}
        _params['id'] = encode(FieldMeta('', '', False, 'primitive'), id)
        _params['storageArea'] = encode(FieldMeta('', '', False, 'enum', ref='Extensions.StorageArea'), storage_area)
        _params['keys'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'primitive')), keys)
        _result = await self._target.send('Extensions.removeStorageItems', _params)
        return None

    async def clear_storage_items(self, *, id: str, storage_area: StorageArea) -> None:
        """
        Clears extension storage in the given `storageArea`.
        :param id: ID of extension.
        :param storage_area: StorageArea to remove data from.
        """
        _params: Dict[str, Any] = {}
        _params['id'] = encode(FieldMeta('', '', False, 'primitive'), id)
        _params['storageArea'] = encode(FieldMeta('', '', False, 'enum', ref='Extensions.StorageArea'), storage_area)
        _result = await self._target.send('Extensions.clearStorageItems', _params)
        return None

    async def set_storage_items(self, *, id: str, storage_area: StorageArea, values: Dict[str, Any]) -> None:
        """
        Sets `values` in extension storage in the given `storageArea`. The provided `values`
        will be merged with existing values in the storage area.
        :param id: ID of extension.
        :param storage_area: StorageArea to set data in.
        :param values: Values to set.
        """
        _params: Dict[str, Any] = {}
        _params['id'] = encode(FieldMeta('', '', False, 'primitive'), id)
        _params['storageArea'] = encode(FieldMeta('', '', False, 'enum', ref='Extensions.StorageArea'), storage_area)
        _params['values'] = encode(FieldMeta('', '', False, 'primitive'), values)
        _result = await self._target.send('Extensions.setStorageItems', _params)
        return None
