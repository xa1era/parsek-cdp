"""Commands for the CacheStorage domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode

if TYPE_CHECKING:
    from .types import (
        Cache,
        CacheId,
        CachedResponse,
        DataEntry,
        Header,
    )
    from ..storage.types import StorageBucket as Storage_StorageBucket

@dataclass
class RequestCacheNamesReturn(DataType):
    """Return value of :meth:`CacheStorage.request_cache_names`."""
    caches: List[Cache]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('caches', 'caches', False, 'array', inner=FieldMeta('', '', False, 'object', ref='CacheStorage.Cache')),
    )


@dataclass
class RequestCachedResponseReturn(DataType):
    """Return value of :meth:`CacheStorage.request_cached_response`."""
    response: CachedResponse
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('response', 'response', False, 'object', ref='CacheStorage.CachedResponse'),
    )


@dataclass
class RequestEntriesReturn(DataType):
    """Return value of :meth:`CacheStorage.request_entries`."""
    cache_data_entries: List[DataEntry]
    return_count: float
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('cache_data_entries', 'cacheDataEntries', False, 'array', inner=FieldMeta('', '', False, 'object', ref='CacheStorage.DataEntry')),
        FieldMeta('return_count', 'returnCount', False, 'primitive'),
    )


class CacheStorage:
    """Commands of the CacheStorage domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def delete_cache(self, *, cache_id: CacheId) -> None:
        """
        Deletes a cache.
        :param cache_id: Id of cache for deletion.
        """
        _params: Dict[str, Any] = {}
        _params['cacheId'] = encode(FieldMeta('', '', False, 'primitive'), cache_id)
        _result = await self._target.send('CacheStorage.deleteCache', _params)
        return None

    async def delete_entry(self, *, cache_id: CacheId, request: str) -> None:
        """
        Deletes a cache entry.
        :param cache_id: Id of cache where the entry will be deleted.
        :param request: URL spec of the request.
        """
        _params: Dict[str, Any] = {}
        _params['cacheId'] = encode(FieldMeta('', '', False, 'primitive'), cache_id)
        _params['request'] = encode(FieldMeta('', '', False, 'primitive'), request)
        _result = await self._target.send('CacheStorage.deleteEntry', _params)
        return None

    async def request_cache_names(self, *, security_origin: Optional[str] = None, storage_key: Optional[str] = None, storage_bucket: Optional[Storage_StorageBucket] = None) -> RequestCacheNamesReturn:
        """
        Requests cache names.
        :param security_origin: At least and at most one of securityOrigin, storageKey, storageBucket must be specified.
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
        _result = await self._target.send('CacheStorage.requestCacheNames', _params)
        return RequestCacheNamesReturn.from_json(_result)

    async def request_cached_response(self, *, cache_id: CacheId, request_url: str, request_headers: List[Header]) -> RequestCachedResponseReturn:
        """
        Fetches cache entry.
        :param cache_id: Id of cache that contains the entry.
        :param request_url: URL spec of the request.
        :param request_headers: headers of the request.
        """
        _params: Dict[str, Any] = {}
        _params['cacheId'] = encode(FieldMeta('', '', False, 'primitive'), cache_id)
        _params['requestURL'] = encode(FieldMeta('', '', False, 'primitive'), request_url)
        _params['requestHeaders'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'object', ref='CacheStorage.Header')), request_headers)
        _result = await self._target.send('CacheStorage.requestCachedResponse', _params)
        return RequestCachedResponseReturn.from_json(_result)

    async def request_entries(self, *, cache_id: CacheId, skip_count: Optional[int] = None, page_size: Optional[int] = None, path_filter: Optional[str] = None) -> RequestEntriesReturn:
        """
        Requests data from cache.
        :param cache_id: ID of cache to get entries from.
        :param skip_count: Number of records to skip.
        :param page_size: Number of records to fetch.
        :param path_filter: If present, only return the entries containing this substring in the path
        """
        _params: Dict[str, Any] = {}
        _params['cacheId'] = encode(FieldMeta('', '', False, 'primitive'), cache_id)
        if skip_count is not None:
            _params['skipCount'] = encode(FieldMeta('', '', False, 'primitive'), skip_count)
        if page_size is not None:
            _params['pageSize'] = encode(FieldMeta('', '', False, 'primitive'), page_size)
        if path_filter is not None:
            _params['pathFilter'] = encode(FieldMeta('', '', False, 'primitive'), path_filter)
        _result = await self._target.send('CacheStorage.requestEntries', _params)
        return RequestEntriesReturn.from_json(_result)
