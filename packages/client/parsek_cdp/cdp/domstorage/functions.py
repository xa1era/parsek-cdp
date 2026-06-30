"""Commands for the DOMStorage domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode

if TYPE_CHECKING:
    from .types import (
        Item,
        StorageId,
    )

@dataclass
class GetDOMStorageItemsReturn(DataType):
    """Return value of :meth:`DOMStorage.get_dom_storage_items`."""
    entries: List[Item]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('entries', 'entries', False, 'array', inner=FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'primitive'))),
    )


class DOMStorage:
    """Commands of the DOMStorage domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def clear(self, *, storage_id: StorageId) -> None:
        """:param storage_id:"""
        _params: Dict[str, Any] = {}
        _params['storageId'] = encode(FieldMeta('', '', False, 'object', ref='DOMStorage.StorageId'), storage_id)
        _result = await self._target.send('DOMStorage.clear', _params)
        return None

    async def disable(self) -> None:
        """Disables storage tracking, prevents storage events from being sent to the client."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('DOMStorage.disable', _params)
        return None

    async def enable(self) -> None:
        """Enables storage tracking, storage events will now be delivered to the client."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('DOMStorage.enable', _params)
        return None

    async def get_dom_storage_items(self, *, storage_id: StorageId) -> GetDOMStorageItemsReturn:
        """:param storage_id:"""
        _params: Dict[str, Any] = {}
        _params['storageId'] = encode(FieldMeta('', '', False, 'object', ref='DOMStorage.StorageId'), storage_id)
        _result = await self._target.send('DOMStorage.getDOMStorageItems', _params)
        return GetDOMStorageItemsReturn.from_json(_result)

    async def remove_dom_storage_item(self, *, storage_id: StorageId, key: str) -> None:
        """
        :param storage_id:
        :param key:
        """
        _params: Dict[str, Any] = {}
        _params['storageId'] = encode(FieldMeta('', '', False, 'object', ref='DOMStorage.StorageId'), storage_id)
        _params['key'] = encode(FieldMeta('', '', False, 'primitive'), key)
        _result = await self._target.send('DOMStorage.removeDOMStorageItem', _params)
        return None

    async def set_dom_storage_item(self, *, storage_id: StorageId, key: str, value: str) -> None:
        """
        :param storage_id:
        :param key:
        :param value:
        """
        _params: Dict[str, Any] = {}
        _params['storageId'] = encode(FieldMeta('', '', False, 'object', ref='DOMStorage.StorageId'), storage_id)
        _params['key'] = encode(FieldMeta('', '', False, 'primitive'), key)
        _params['value'] = encode(FieldMeta('', '', False, 'primitive'), value)
        _result = await self._target.send('DOMStorage.setDOMStorageItem', _params)
        return None
