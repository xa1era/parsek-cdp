"""Commands for the IndexedDB domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode

if TYPE_CHECKING:
    from .types import (
        DataEntry,
        DatabaseWithObjectStores,
        KeyRange,
    )
    from ..storage.types import StorageBucket as Storage_StorageBucket

@dataclass
class RequestDataReturn(DataType):
    """Return value of :meth:`IndexedDB.request_data`."""
    object_store_data_entries: List[DataEntry]
    has_more: bool
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('object_store_data_entries', 'objectStoreDataEntries', False, 'array', inner=FieldMeta('', '', False, 'object', ref='IndexedDB.DataEntry')),
        FieldMeta('has_more', 'hasMore', False, 'primitive'),
    )


@dataclass
class GetMetadataReturn(DataType):
    """Return value of :meth:`IndexedDB.get_metadata`."""
    entries_count: float
    key_generator_value: float
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('entries_count', 'entriesCount', False, 'primitive'),
        FieldMeta('key_generator_value', 'keyGeneratorValue', False, 'primitive'),
    )


@dataclass
class RequestDatabaseReturn(DataType):
    """Return value of :meth:`IndexedDB.request_database`."""
    database_with_object_stores: DatabaseWithObjectStores
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('database_with_object_stores', 'databaseWithObjectStores', False, 'object', ref='IndexedDB.DatabaseWithObjectStores'),
    )


@dataclass
class RequestDatabaseNamesReturn(DataType):
    """Return value of :meth:`IndexedDB.request_database_names`."""
    database_names: List[str]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('database_names', 'databaseNames', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


class IndexedDB:
    """Commands of the IndexedDB domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def clear_object_store(self, *, database_name: str, object_store_name: str, security_origin: Optional[str] = None, storage_key: Optional[str] = None, storage_bucket: Optional[Storage_StorageBucket] = None) -> None:
        """
        Clears all entries from an object store.
        :param security_origin: At least and at most one of securityOrigin, storageKey, or storageBucket must be specified.
        Security origin.
        :param storage_key: Storage key.
        :param storage_bucket: Storage bucket. If not specified, it uses the default bucket.
        :param database_name: Database name.
        :param object_store_name: Object store name.
        """
        _params: Dict[str, Any] = {}
        _params['databaseName'] = encode(FieldMeta('', '', False, 'primitive'), database_name)
        _params['objectStoreName'] = encode(FieldMeta('', '', False, 'primitive'), object_store_name)
        if security_origin is not None:
            _params['securityOrigin'] = encode(FieldMeta('', '', False, 'primitive'), security_origin)
        if storage_key is not None:
            _params['storageKey'] = encode(FieldMeta('', '', False, 'primitive'), storage_key)
        if storage_bucket is not None:
            _params['storageBucket'] = encode(FieldMeta('', '', False, 'object', ref='Storage.StorageBucket'), storage_bucket)
        _result = await self._target.send('IndexedDB.clearObjectStore', _params)
        return None

    async def delete_database(self, *, database_name: str, security_origin: Optional[str] = None, storage_key: Optional[str] = None, storage_bucket: Optional[Storage_StorageBucket] = None) -> None:
        """
        Deletes a database.
        :param security_origin: At least and at most one of securityOrigin, storageKey, or storageBucket must be specified.
        Security origin.
        :param storage_key: Storage key.
        :param storage_bucket: Storage bucket. If not specified, it uses the default bucket.
        :param database_name: Database name.
        """
        _params: Dict[str, Any] = {}
        _params['databaseName'] = encode(FieldMeta('', '', False, 'primitive'), database_name)
        if security_origin is not None:
            _params['securityOrigin'] = encode(FieldMeta('', '', False, 'primitive'), security_origin)
        if storage_key is not None:
            _params['storageKey'] = encode(FieldMeta('', '', False, 'primitive'), storage_key)
        if storage_bucket is not None:
            _params['storageBucket'] = encode(FieldMeta('', '', False, 'object', ref='Storage.StorageBucket'), storage_bucket)
        _result = await self._target.send('IndexedDB.deleteDatabase', _params)
        return None

    async def delete_object_store_entries(self, *, database_name: str, object_store_name: str, key_range: KeyRange, security_origin: Optional[str] = None, storage_key: Optional[str] = None, storage_bucket: Optional[Storage_StorageBucket] = None) -> None:
        """
        Delete a range of entries from an object store
        :param security_origin: At least and at most one of securityOrigin, storageKey, or storageBucket must be specified.
        Security origin.
        :param storage_key: Storage key.
        :param storage_bucket: Storage bucket. If not specified, it uses the default bucket.
        :param database_name:
        :param object_store_name:
        :param key_range: Range of entry keys to delete
        """
        _params: Dict[str, Any] = {}
        _params['databaseName'] = encode(FieldMeta('', '', False, 'primitive'), database_name)
        _params['objectStoreName'] = encode(FieldMeta('', '', False, 'primitive'), object_store_name)
        _params['keyRange'] = encode(FieldMeta('', '', False, 'object', ref='IndexedDB.KeyRange'), key_range)
        if security_origin is not None:
            _params['securityOrigin'] = encode(FieldMeta('', '', False, 'primitive'), security_origin)
        if storage_key is not None:
            _params['storageKey'] = encode(FieldMeta('', '', False, 'primitive'), storage_key)
        if storage_bucket is not None:
            _params['storageBucket'] = encode(FieldMeta('', '', False, 'object', ref='Storage.StorageBucket'), storage_bucket)
        _result = await self._target.send('IndexedDB.deleteObjectStoreEntries', _params)
        return None

    async def disable(self) -> None:
        """Disables events from backend."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('IndexedDB.disable', _params)
        return None

    async def enable(self) -> None:
        """Enables events from backend."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('IndexedDB.enable', _params)
        return None

    async def request_data(self, *, database_name: str, object_store_name: str, skip_count: int, page_size: int, security_origin: Optional[str] = None, storage_key: Optional[str] = None, storage_bucket: Optional[Storage_StorageBucket] = None, index_name: Optional[str] = None, key_range: Optional[KeyRange] = None) -> RequestDataReturn:
        """
        Requests data from object store or index.
        :param security_origin: At least and at most one of securityOrigin, storageKey, or storageBucket must be specified.
        Security origin.
        :param storage_key: Storage key.
        :param storage_bucket: Storage bucket. If not specified, it uses the default bucket.
        :param database_name: Database name.
        :param object_store_name: Object store name.
        :param index_name: Index name. If not specified, it performs an object store data request.
        :param skip_count: Number of records to skip.
        :param page_size: Number of records to fetch.
        :param key_range: Key range.
        """
        _params: Dict[str, Any] = {}
        _params['databaseName'] = encode(FieldMeta('', '', False, 'primitive'), database_name)
        _params['objectStoreName'] = encode(FieldMeta('', '', False, 'primitive'), object_store_name)
        _params['skipCount'] = encode(FieldMeta('', '', False, 'primitive'), skip_count)
        _params['pageSize'] = encode(FieldMeta('', '', False, 'primitive'), page_size)
        if security_origin is not None:
            _params['securityOrigin'] = encode(FieldMeta('', '', False, 'primitive'), security_origin)
        if storage_key is not None:
            _params['storageKey'] = encode(FieldMeta('', '', False, 'primitive'), storage_key)
        if storage_bucket is not None:
            _params['storageBucket'] = encode(FieldMeta('', '', False, 'object', ref='Storage.StorageBucket'), storage_bucket)
        if index_name is not None:
            _params['indexName'] = encode(FieldMeta('', '', False, 'primitive'), index_name)
        if key_range is not None:
            _params['keyRange'] = encode(FieldMeta('', '', False, 'object', ref='IndexedDB.KeyRange'), key_range)
        _result = await self._target.send('IndexedDB.requestData', _params)
        return RequestDataReturn.from_json(_result)

    async def get_metadata(self, *, database_name: str, object_store_name: str, security_origin: Optional[str] = None, storage_key: Optional[str] = None, storage_bucket: Optional[Storage_StorageBucket] = None) -> GetMetadataReturn:
        """
        Gets metadata of an object store.
        :param security_origin: At least and at most one of securityOrigin, storageKey, or storageBucket must be specified.
        Security origin.
        :param storage_key: Storage key.
        :param storage_bucket: Storage bucket. If not specified, it uses the default bucket.
        :param database_name: Database name.
        :param object_store_name: Object store name.
        """
        _params: Dict[str, Any] = {}
        _params['databaseName'] = encode(FieldMeta('', '', False, 'primitive'), database_name)
        _params['objectStoreName'] = encode(FieldMeta('', '', False, 'primitive'), object_store_name)
        if security_origin is not None:
            _params['securityOrigin'] = encode(FieldMeta('', '', False, 'primitive'), security_origin)
        if storage_key is not None:
            _params['storageKey'] = encode(FieldMeta('', '', False, 'primitive'), storage_key)
        if storage_bucket is not None:
            _params['storageBucket'] = encode(FieldMeta('', '', False, 'object', ref='Storage.StorageBucket'), storage_bucket)
        _result = await self._target.send('IndexedDB.getMetadata', _params)
        return GetMetadataReturn.from_json(_result)

    async def request_database(self, *, database_name: str, security_origin: Optional[str] = None, storage_key: Optional[str] = None, storage_bucket: Optional[Storage_StorageBucket] = None) -> RequestDatabaseReturn:
        """
        Requests database with given name in given frame.
        :param security_origin: At least and at most one of securityOrigin, storageKey, or storageBucket must be specified.
        Security origin.
        :param storage_key: Storage key.
        :param storage_bucket: Storage bucket. If not specified, it uses the default bucket.
        :param database_name: Database name.
        """
        _params: Dict[str, Any] = {}
        _params['databaseName'] = encode(FieldMeta('', '', False, 'primitive'), database_name)
        if security_origin is not None:
            _params['securityOrigin'] = encode(FieldMeta('', '', False, 'primitive'), security_origin)
        if storage_key is not None:
            _params['storageKey'] = encode(FieldMeta('', '', False, 'primitive'), storage_key)
        if storage_bucket is not None:
            _params['storageBucket'] = encode(FieldMeta('', '', False, 'object', ref='Storage.StorageBucket'), storage_bucket)
        _result = await self._target.send('IndexedDB.requestDatabase', _params)
        return RequestDatabaseReturn.from_json(_result)

    async def request_database_names(self, *, security_origin: Optional[str] = None, storage_key: Optional[str] = None, storage_bucket: Optional[Storage_StorageBucket] = None) -> RequestDatabaseNamesReturn:
        """
        Requests database names for given security origin.
        :param security_origin: At least and at most one of securityOrigin, storageKey, or storageBucket must be specified.
        Security origin.
        :param storage_key: Storage key.
        :param storage_bucket: Storage bucket. If not specified, it uses the default bucket.
        """
        _params: Dict[str, Any] = {}
        if security_origin is not None:
            _params['securityOrigin'] = encode(FieldMeta('', '', False, 'primitive'), security_origin)
        if storage_key is not None:
            _params['storageKey'] = encode(FieldMeta('', '', False, 'primitive'), storage_key)
        if storage_bucket is not None:
            _params['storageBucket'] = encode(FieldMeta('', '', False, 'object', ref='Storage.StorageBucket'), storage_bucket)
        _result = await self._target.send('IndexedDB.requestDatabaseNames', _params)
        return RequestDatabaseNamesReturn.from_json(_result)
