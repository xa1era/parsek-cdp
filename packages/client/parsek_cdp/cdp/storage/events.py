"""Events for the Storage domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import FieldMeta
from ..mixins.event import Event, register_event

if TYPE_CHECKING:
    from .types import (
        AttributionReportingAggregatableResult,
        AttributionReportingEventLevelResult,
        AttributionReportingReportResult,
        AttributionReportingSourceRegistration,
        AttributionReportingSourceRegistrationResult,
        AttributionReportingTriggerRegistration,
        InterestGroupAccessType,
        InterestGroupAuctionEventType,
        InterestGroupAuctionFetchType,
        InterestGroupAuctionId,
        SharedStorageAccessMethod,
        SharedStorageAccessParams,
        SharedStorageAccessScope,
        StorageBucketInfo,
    )
    from ..network.types import RequestId as Network_RequestId
    from ..network.types import TimeSinceEpoch as Network_TimeSinceEpoch
    from ..page.types import FrameId as Page_FrameId
    from ..target.types import TargetID as Target_TargetID

@register_event("Storage.cacheStorageContentUpdated")
@dataclass
class CacheStorageContentUpdated(Event):
    """A cache's contents have been modified."""
    origin: str
    storage_key: str
    bucket_id: str
    cache_name: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('origin', 'origin', False, 'primitive'),
        FieldMeta('storage_key', 'storageKey', False, 'primitive'),
        FieldMeta('bucket_id', 'bucketId', False, 'primitive'),
        FieldMeta('cache_name', 'cacheName', False, 'primitive'),
    )


@register_event("Storage.cacheStorageListUpdated")
@dataclass
class CacheStorageListUpdated(Event):
    """A cache has been added/deleted."""
    origin: str
    storage_key: str
    bucket_id: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('origin', 'origin', False, 'primitive'),
        FieldMeta('storage_key', 'storageKey', False, 'primitive'),
        FieldMeta('bucket_id', 'bucketId', False, 'primitive'),
    )


@register_event("Storage.indexedDBContentUpdated")
@dataclass
class IndexedDBContentUpdated(Event):
    """The origin's IndexedDB object store has been modified."""
    origin: str
    storage_key: str
    bucket_id: str
    database_name: str
    object_store_name: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('origin', 'origin', False, 'primitive'),
        FieldMeta('storage_key', 'storageKey', False, 'primitive'),
        FieldMeta('bucket_id', 'bucketId', False, 'primitive'),
        FieldMeta('database_name', 'databaseName', False, 'primitive'),
        FieldMeta('object_store_name', 'objectStoreName', False, 'primitive'),
    )


@register_event("Storage.indexedDBListUpdated")
@dataclass
class IndexedDBListUpdated(Event):
    """The origin's IndexedDB database list has been modified."""
    origin: str
    storage_key: str
    bucket_id: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('origin', 'origin', False, 'primitive'),
        FieldMeta('storage_key', 'storageKey', False, 'primitive'),
        FieldMeta('bucket_id', 'bucketId', False, 'primitive'),
    )


@register_event("Storage.interestGroupAccessed")
@dataclass
class InterestGroupAccessed(Event):
    """
    One of the interest groups was accessed. Note that these events are global
    to all targets sharing an interest group store.
    """
    access_time: Network_TimeSinceEpoch
    type_: InterestGroupAccessType
    owner_origin: str
    name: str
    component_seller_origin: Optional[str] = None
    bid: Optional[float] = None
    bid_currency: Optional[str] = None
    unique_auction_id: Optional[InterestGroupAuctionId] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('access_time', 'accessTime', False, 'primitive'),
        FieldMeta('type_', 'type', False, 'enum', ref='Storage.InterestGroupAccessType'),
        FieldMeta('owner_origin', 'ownerOrigin', False, 'primitive'),
        FieldMeta('name', 'name', False, 'primitive'),
        FieldMeta('component_seller_origin', 'componentSellerOrigin', True, 'primitive'),
        FieldMeta('bid', 'bid', True, 'primitive'),
        FieldMeta('bid_currency', 'bidCurrency', True, 'primitive'),
        FieldMeta('unique_auction_id', 'uniqueAuctionId', True, 'primitive'),
    )


@register_event("Storage.interestGroupAuctionEventOccurred")
@dataclass
class InterestGroupAuctionEventOccurred(Event):
    """
    An auction involving interest groups is taking place. These events are
    target-specific.
    """
    event_time: Network_TimeSinceEpoch
    type_: InterestGroupAuctionEventType
    unique_auction_id: InterestGroupAuctionId
    parent_auction_id: Optional[InterestGroupAuctionId] = None
    auction_config: Optional[Dict[str, Any]] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('event_time', 'eventTime', False, 'primitive'),
        FieldMeta('type_', 'type', False, 'enum', ref='Storage.InterestGroupAuctionEventType'),
        FieldMeta('unique_auction_id', 'uniqueAuctionId', False, 'primitive'),
        FieldMeta('parent_auction_id', 'parentAuctionId', True, 'primitive'),
        FieldMeta('auction_config', 'auctionConfig', True, 'primitive'),
    )


@register_event("Storage.interestGroupAuctionNetworkRequestCreated")
@dataclass
class InterestGroupAuctionNetworkRequestCreated(Event):
    """
    Specifies which auctions a particular network fetch may be related to, and
    in what role. Note that it is not ordered with respect to
    Network.requestWillBeSent (but will happen before loadingFinished
    loadingFailed).
    """
    type_: InterestGroupAuctionFetchType
    request_id: Network_RequestId
    auctions: List[InterestGroupAuctionId]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('type_', 'type', False, 'enum', ref='Storage.InterestGroupAuctionFetchType'),
        FieldMeta('request_id', 'requestId', False, 'primitive'),
        FieldMeta('auctions', 'auctions', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


@register_event("Storage.sharedStorageAccessed")
@dataclass
class SharedStorageAccessed(Event):
    """
    Shared storage was accessed by the associated page.
    The following parameters are included in all events.
    """
    access_time: Network_TimeSinceEpoch
    scope: SharedStorageAccessScope
    method: SharedStorageAccessMethod
    main_frame_id: Page_FrameId
    owner_origin: str
    owner_site: str
    params: SharedStorageAccessParams
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('access_time', 'accessTime', False, 'primitive'),
        FieldMeta('scope', 'scope', False, 'enum', ref='Storage.SharedStorageAccessScope'),
        FieldMeta('method', 'method', False, 'enum', ref='Storage.SharedStorageAccessMethod'),
        FieldMeta('main_frame_id', 'mainFrameId', False, 'primitive'),
        FieldMeta('owner_origin', 'ownerOrigin', False, 'primitive'),
        FieldMeta('owner_site', 'ownerSite', False, 'primitive'),
        FieldMeta('params', 'params', False, 'object', ref='Storage.SharedStorageAccessParams'),
    )


@register_event("Storage.sharedStorageWorkletOperationExecutionFinished")
@dataclass
class SharedStorageWorkletOperationExecutionFinished(Event):
    """
    A shared storage run or selectURL operation finished its execution.
    The following parameters are included in all events.
    """
    finished_time: Network_TimeSinceEpoch
    execution_time: int
    method: SharedStorageAccessMethod
    operation_id: str
    worklet_target_id: Target_TargetID
    main_frame_id: Page_FrameId
    owner_origin: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('finished_time', 'finishedTime', False, 'primitive'),
        FieldMeta('execution_time', 'executionTime', False, 'primitive'),
        FieldMeta('method', 'method', False, 'enum', ref='Storage.SharedStorageAccessMethod'),
        FieldMeta('operation_id', 'operationId', False, 'primitive'),
        FieldMeta('worklet_target_id', 'workletTargetId', False, 'primitive'),
        FieldMeta('main_frame_id', 'mainFrameId', False, 'primitive'),
        FieldMeta('owner_origin', 'ownerOrigin', False, 'primitive'),
    )


@register_event("Storage.storageBucketCreatedOrUpdated")
@dataclass
class StorageBucketCreatedOrUpdated(Event):
    bucket_info: StorageBucketInfo
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('bucket_info', 'bucketInfo', False, 'object', ref='Storage.StorageBucketInfo'),
    )


@register_event("Storage.storageBucketDeleted")
@dataclass
class StorageBucketDeleted(Event):
    bucket_id: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('bucket_id', 'bucketId', False, 'primitive'),
    )


@register_event("Storage.attributionReportingSourceRegistered")
@dataclass
class AttributionReportingSourceRegistered(Event):
    registration: AttributionReportingSourceRegistration
    result: AttributionReportingSourceRegistrationResult
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('registration', 'registration', False, 'object', ref='Storage.AttributionReportingSourceRegistration'),
        FieldMeta('result', 'result', False, 'enum', ref='Storage.AttributionReportingSourceRegistrationResult'),
    )


@register_event("Storage.attributionReportingTriggerRegistered")
@dataclass
class AttributionReportingTriggerRegistered(Event):
    registration: AttributionReportingTriggerRegistration
    event_level: AttributionReportingEventLevelResult
    aggregatable: AttributionReportingAggregatableResult
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('registration', 'registration', False, 'object', ref='Storage.AttributionReportingTriggerRegistration'),
        FieldMeta('event_level', 'eventLevel', False, 'enum', ref='Storage.AttributionReportingEventLevelResult'),
        FieldMeta('aggregatable', 'aggregatable', False, 'enum', ref='Storage.AttributionReportingAggregatableResult'),
    )


@register_event("Storage.attributionReportingReportSent")
@dataclass
class AttributionReportingReportSent(Event):
    url: str
    body: Dict[str, Any]
    result: AttributionReportingReportResult
    net_error: Optional[int] = None
    net_error_name: Optional[str] = None
    http_status_code: Optional[int] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('url', 'url', False, 'primitive'),
        FieldMeta('body', 'body', False, 'primitive'),
        FieldMeta('result', 'result', False, 'enum', ref='Storage.AttributionReportingReportResult'),
        FieldMeta('net_error', 'netError', True, 'primitive'),
        FieldMeta('net_error_name', 'netErrorName', True, 'primitive'),
        FieldMeta('http_status_code', 'httpStatusCode', True, 'primitive'),
    )


@register_event("Storage.attributionReportingVerboseDebugReportSent")
@dataclass
class AttributionReportingVerboseDebugReportSent(Event):
    url: str
    body: Optional[List[Dict[str, Any]]] = None
    net_error: Optional[int] = None
    net_error_name: Optional[str] = None
    http_status_code: Optional[int] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('url', 'url', False, 'primitive'),
        FieldMeta('body', 'body', True, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('net_error', 'netError', True, 'primitive'),
        FieldMeta('net_error_name', 'netErrorName', True, 'primitive'),
        FieldMeta('http_status_code', 'httpStatusCode', True, 'primitive'),
    )

__all__ = ["AttributionReportingReportSent", "AttributionReportingSourceRegistered", "AttributionReportingTriggerRegistered", "AttributionReportingVerboseDebugReportSent", "CacheStorageContentUpdated", "CacheStorageListUpdated", "IndexedDBContentUpdated", "IndexedDBListUpdated", "InterestGroupAccessed", "InterestGroupAuctionEventOccurred", "InterestGroupAuctionNetworkRequestCreated", "SharedStorageAccessed", "SharedStorageWorkletOperationExecutionFinished", "StorageBucketCreatedOrUpdated", "StorageBucketDeleted"]
