"""Custom types and enums for the CacheStorage domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, register

if TYPE_CHECKING:
    from ..storage.types import StorageBucket as Storage_StorageBucket

type CacheId = str  # Unique identifier of the Cache object.


@register("CacheStorage.CachedResponseType")
class CachedResponseType(str, Enum):
    """type of HTTP response cached"""
    BASIC = 'basic'
    CORS = 'cors'
    DEFAULT = 'default'
    ERROR = 'error'
    OPAQUERESPONSE = 'opaqueResponse'
    OPAQUEREDIRECT = 'opaqueRedirect'


@register("CacheStorage.DataEntry")
@dataclass
class DataEntry(DataType):
    """Data entry."""
    request_url: str
    request_method: str
    request_headers: List[Header]
    response_time: float
    response_status: int
    response_status_text: str
    response_type: CachedResponseType
    response_headers: List[Header]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('request_url', 'requestURL', False, 'primitive'),
        FieldMeta('request_method', 'requestMethod', False, 'primitive'),
        FieldMeta('request_headers', 'requestHeaders', False, 'array', inner=FieldMeta('', '', False, 'object', ref='CacheStorage.Header')),
        FieldMeta('response_time', 'responseTime', False, 'primitive'),
        FieldMeta('response_status', 'responseStatus', False, 'primitive'),
        FieldMeta('response_status_text', 'responseStatusText', False, 'primitive'),
        FieldMeta('response_type', 'responseType', False, 'enum', ref='CacheStorage.CachedResponseType'),
        FieldMeta('response_headers', 'responseHeaders', False, 'array', inner=FieldMeta('', '', False, 'object', ref='CacheStorage.Header')),
    )


@register("CacheStorage.Cache")
@dataclass
class Cache(DataType):
    """Cache identifier."""
    cache_id: CacheId
    security_origin: str
    storage_key: str
    cache_name: str
    storage_bucket: Optional[Storage_StorageBucket] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('cache_id', 'cacheId', False, 'primitive'),
        FieldMeta('security_origin', 'securityOrigin', False, 'primitive'),
        FieldMeta('storage_key', 'storageKey', False, 'primitive'),
        FieldMeta('cache_name', 'cacheName', False, 'primitive'),
        FieldMeta('storage_bucket', 'storageBucket', True, 'object', ref='Storage.StorageBucket'),
    )


@register("CacheStorage.Header")
@dataclass
class Header(DataType):
    name: str
    value: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('name', 'name', False, 'primitive'),
        FieldMeta('value', 'value', False, 'primitive'),
    )


@register("CacheStorage.CachedResponse")
@dataclass
class CachedResponse(DataType):
    """Cached response"""
    body: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('body', 'body', False, 'primitive'),
    )

__all__ = ["Cache", "CacheId", "CachedResponse", "CachedResponseType", "DataEntry", "Header"]
