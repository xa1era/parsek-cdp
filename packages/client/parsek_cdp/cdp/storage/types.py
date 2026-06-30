"""Custom types and enums for the Storage domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, register

if TYPE_CHECKING:
    from ..network.types import TimeSinceEpoch as Network_TimeSinceEpoch
    from ..target.types import TargetID as Target_TargetID

type SerializedStorageKey = str


@register("Storage.StorageType")
class StorageType(str, Enum):
    """Enum of possible storage types."""
    COOKIES = 'cookies'
    FILE_SYSTEMS = 'file_systems'
    INDEXEDDB = 'indexeddb'
    LOCAL_STORAGE = 'local_storage'
    SHADER_CACHE = 'shader_cache'
    WEBSQL = 'websql'
    SERVICE_WORKERS = 'service_workers'
    CACHE_STORAGE = 'cache_storage'
    INTEREST_GROUPS = 'interest_groups'
    SHARED_STORAGE = 'shared_storage'
    STORAGE_BUCKETS = 'storage_buckets'
    ALL = 'all'
    OTHER = 'other'


@register("Storage.UsageForType")
@dataclass
class UsageForType(DataType):
    """Usage for a storage type."""
    storage_type: StorageType
    usage: float
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('storage_type', 'storageType', False, 'enum', ref='Storage.StorageType'),
        FieldMeta('usage', 'usage', False, 'primitive'),
    )


@register("Storage.TrustTokens")
@dataclass
class TrustTokens(DataType):
    """
    Pair of issuer origin and number of available (signed, but not used) Trust
    Tokens from that issuer.
    """
    issuer_origin: str
    count: float
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('issuer_origin', 'issuerOrigin', False, 'primitive'),
        FieldMeta('count', 'count', False, 'primitive'),
    )


type InterestGroupAuctionId = str  # Protected audience interest group auction identifier.


@register("Storage.InterestGroupAccessType")
class InterestGroupAccessType(str, Enum):
    """Enum of interest group access types."""
    JOIN = 'join'
    LEAVE = 'leave'
    UPDATE = 'update'
    LOADED = 'loaded'
    BID = 'bid'
    WIN = 'win'
    ADDITIONALBID = 'additionalBid'
    ADDITIONALBIDWIN = 'additionalBidWin'
    TOPLEVELBID = 'topLevelBid'
    TOPLEVELADDITIONALBID = 'topLevelAdditionalBid'
    CLEAR = 'clear'


@register("Storage.InterestGroupAuctionEventType")
class InterestGroupAuctionEventType(str, Enum):
    """Enum of auction events."""
    STARTED = 'started'
    CONFIGRESOLVED = 'configResolved'


@register("Storage.InterestGroupAuctionFetchType")
class InterestGroupAuctionFetchType(str, Enum):
    """Enum of network fetches auctions can do."""
    BIDDERJS = 'bidderJs'
    BIDDERWASM = 'bidderWasm'
    SELLERJS = 'sellerJs'
    BIDDERTRUSTEDSIGNALS = 'bidderTrustedSignals'
    SELLERTRUSTEDSIGNALS = 'sellerTrustedSignals'


@register("Storage.SharedStorageAccessScope")
class SharedStorageAccessScope(str, Enum):
    """Enum of shared storage access scopes."""
    WINDOW = 'window'
    SHAREDSTORAGEWORKLET = 'sharedStorageWorklet'
    PROTECTEDAUDIENCEWORKLET = 'protectedAudienceWorklet'
    HEADER = 'header'


@register("Storage.SharedStorageAccessMethod")
class SharedStorageAccessMethod(str, Enum):
    """Enum of shared storage access methods."""
    ADDMODULE = 'addModule'
    CREATEWORKLET = 'createWorklet'
    SELECTURL = 'selectURL'
    RUN = 'run'
    BATCHUPDATE = 'batchUpdate'
    SET = 'set'
    APPEND = 'append'
    DELETE = 'delete'
    CLEAR = 'clear'
    GET = 'get'
    KEYS = 'keys'
    VALUES = 'values'
    ENTRIES = 'entries'
    LENGTH = 'length'
    REMAININGBUDGET = 'remainingBudget'


@register("Storage.SharedStorageEntry")
@dataclass
class SharedStorageEntry(DataType):
    """Struct for a single key-value pair in an origin's shared storage."""
    key: str
    value: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('key', 'key', False, 'primitive'),
        FieldMeta('value', 'value', False, 'primitive'),
    )


@register("Storage.SharedStorageMetadata")
@dataclass
class SharedStorageMetadata(DataType):
    """Details for an origin's shared storage."""
    creation_time: Network_TimeSinceEpoch
    length: int
    remaining_budget: float
    bytes_used: int
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('creation_time', 'creationTime', False, 'primitive'),
        FieldMeta('length', 'length', False, 'primitive'),
        FieldMeta('remaining_budget', 'remainingBudget', False, 'primitive'),
        FieldMeta('bytes_used', 'bytesUsed', False, 'primitive'),
    )


@register("Storage.SharedStoragePrivateAggregationConfig")
@dataclass
class SharedStoragePrivateAggregationConfig(DataType):
    """
    Represents a dictionary object passed in as privateAggregationConfig to
    run or selectURL.
    """
    filtering_id_max_bytes: int
    aggregation_coordinator_origin: Optional[str] = None
    context_id: Optional[str] = None
    max_contributions: Optional[int] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('filtering_id_max_bytes', 'filteringIdMaxBytes', False, 'primitive'),
        FieldMeta('aggregation_coordinator_origin', 'aggregationCoordinatorOrigin', True, 'primitive'),
        FieldMeta('context_id', 'contextId', True, 'primitive'),
        FieldMeta('max_contributions', 'maxContributions', True, 'primitive'),
    )


@register("Storage.SharedStorageReportingMetadata")
@dataclass
class SharedStorageReportingMetadata(DataType):
    """Pair of reporting metadata details for a candidate URL for `selectURL()`."""
    event_type: str
    reporting_url: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('event_type', 'eventType', False, 'primitive'),
        FieldMeta('reporting_url', 'reportingUrl', False, 'primitive'),
    )


@register("Storage.SharedStorageUrlWithMetadata")
@dataclass
class SharedStorageUrlWithMetadata(DataType):
    """Bundles a candidate URL with its reporting metadata."""
    url: str
    reporting_metadata: List[SharedStorageReportingMetadata]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('url', 'url', False, 'primitive'),
        FieldMeta('reporting_metadata', 'reportingMetadata', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Storage.SharedStorageReportingMetadata')),
    )


@register("Storage.SharedStorageAccessParams")
@dataclass
class SharedStorageAccessParams(DataType):
    """
    Bundles the parameters for shared storage access events whose
    presence/absence can vary according to SharedStorageAccessType.
    """
    script_source_url: Optional[str] = None
    data_origin: Optional[str] = None
    operation_name: Optional[str] = None
    operation_id: Optional[str] = None
    keep_alive: Optional[bool] = None
    private_aggregation_config: Optional[SharedStoragePrivateAggregationConfig] = None
    serialized_data: Optional[str] = None
    urls_with_metadata: Optional[List[SharedStorageUrlWithMetadata]] = None
    urn_uuid: Optional[str] = None
    key: Optional[str] = None
    value: Optional[str] = None
    ignore_if_present: Optional[bool] = None
    worklet_ordinal: Optional[int] = None
    worklet_target_id: Optional[Target_TargetID] = None
    with_lock: Optional[str] = None
    batch_update_id: Optional[str] = None
    batch_size: Optional[int] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('script_source_url', 'scriptSourceUrl', True, 'primitive'),
        FieldMeta('data_origin', 'dataOrigin', True, 'primitive'),
        FieldMeta('operation_name', 'operationName', True, 'primitive'),
        FieldMeta('operation_id', 'operationId', True, 'primitive'),
        FieldMeta('keep_alive', 'keepAlive', True, 'primitive'),
        FieldMeta('private_aggregation_config', 'privateAggregationConfig', True, 'object', ref='Storage.SharedStoragePrivateAggregationConfig'),
        FieldMeta('serialized_data', 'serializedData', True, 'primitive'),
        FieldMeta('urls_with_metadata', 'urlsWithMetadata', True, 'array', inner=FieldMeta('', '', False, 'object', ref='Storage.SharedStorageUrlWithMetadata')),
        FieldMeta('urn_uuid', 'urnUuid', True, 'primitive'),
        FieldMeta('key', 'key', True, 'primitive'),
        FieldMeta('value', 'value', True, 'primitive'),
        FieldMeta('ignore_if_present', 'ignoreIfPresent', True, 'primitive'),
        FieldMeta('worklet_ordinal', 'workletOrdinal', True, 'primitive'),
        FieldMeta('worklet_target_id', 'workletTargetId', True, 'primitive'),
        FieldMeta('with_lock', 'withLock', True, 'primitive'),
        FieldMeta('batch_update_id', 'batchUpdateId', True, 'primitive'),
        FieldMeta('batch_size', 'batchSize', True, 'primitive'),
    )


@register("Storage.StorageBucketsDurability")
class StorageBucketsDurability(str, Enum):
    RELAXED = 'relaxed'
    STRICT = 'strict'


@register("Storage.StorageBucket")
@dataclass
class StorageBucket(DataType):
    storage_key: SerializedStorageKey
    name: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('storage_key', 'storageKey', False, 'primitive'),
        FieldMeta('name', 'name', True, 'primitive'),
    )


@register("Storage.StorageBucketInfo")
@dataclass
class StorageBucketInfo(DataType):
    bucket: StorageBucket
    id: str
    expiration: Network_TimeSinceEpoch
    quota: float
    persistent: bool
    durability: StorageBucketsDurability
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('bucket', 'bucket', False, 'object', ref='Storage.StorageBucket'),
        FieldMeta('id', 'id', False, 'primitive'),
        FieldMeta('expiration', 'expiration', False, 'primitive'),
        FieldMeta('quota', 'quota', False, 'primitive'),
        FieldMeta('persistent', 'persistent', False, 'primitive'),
        FieldMeta('durability', 'durability', False, 'enum', ref='Storage.StorageBucketsDurability'),
    )


@register("Storage.AttributionReportingSourceType")
class AttributionReportingSourceType(str, Enum):
    NAVIGATION = 'navigation'
    EVENT = 'event'


type UnsignedInt64AsBase10 = str


type UnsignedInt128AsBase16 = str


type SignedInt64AsBase10 = str


@register("Storage.AttributionReportingFilterDataEntry")
@dataclass
class AttributionReportingFilterDataEntry(DataType):
    key: str
    values: List[str]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('key', 'key', False, 'primitive'),
        FieldMeta('values', 'values', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


@register("Storage.AttributionReportingFilterConfig")
@dataclass
class AttributionReportingFilterConfig(DataType):
    filter_values: List[AttributionReportingFilterDataEntry]
    lookback_window: Optional[int] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('filter_values', 'filterValues', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Storage.AttributionReportingFilterDataEntry')),
        FieldMeta('lookback_window', 'lookbackWindow', True, 'primitive'),
    )


@register("Storage.AttributionReportingFilterPair")
@dataclass
class AttributionReportingFilterPair(DataType):
    filters: List[AttributionReportingFilterConfig]
    not_filters: List[AttributionReportingFilterConfig]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('filters', 'filters', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Storage.AttributionReportingFilterConfig')),
        FieldMeta('not_filters', 'notFilters', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Storage.AttributionReportingFilterConfig')),
    )


@register("Storage.AttributionReportingAggregationKeysEntry")
@dataclass
class AttributionReportingAggregationKeysEntry(DataType):
    key: str
    value: UnsignedInt128AsBase16
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('key', 'key', False, 'primitive'),
        FieldMeta('value', 'value', False, 'primitive'),
    )


@register("Storage.AttributionReportingEventReportWindows")
@dataclass
class AttributionReportingEventReportWindows(DataType):
    start: int
    ends: List[int]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('start', 'start', False, 'primitive'),
        FieldMeta('ends', 'ends', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


@register("Storage.AttributionReportingTriggerDataMatching")
class AttributionReportingTriggerDataMatching(str, Enum):
    EXACT = 'exact'
    MODULUS = 'modulus'


@register("Storage.AttributionReportingAggregatableDebugReportingData")
@dataclass
class AttributionReportingAggregatableDebugReportingData(DataType):
    key_piece: UnsignedInt128AsBase16
    value: float
    types: List[str]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('key_piece', 'keyPiece', False, 'primitive'),
        FieldMeta('value', 'value', False, 'primitive'),
        FieldMeta('types', 'types', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


@register("Storage.AttributionReportingAggregatableDebugReportingConfig")
@dataclass
class AttributionReportingAggregatableDebugReportingConfig(DataType):
    key_piece: UnsignedInt128AsBase16
    debug_data: List[AttributionReportingAggregatableDebugReportingData]
    budget: Optional[float] = None
    aggregation_coordinator_origin: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('key_piece', 'keyPiece', False, 'primitive'),
        FieldMeta('debug_data', 'debugData', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Storage.AttributionReportingAggregatableDebugReportingData')),
        FieldMeta('budget', 'budget', True, 'primitive'),
        FieldMeta('aggregation_coordinator_origin', 'aggregationCoordinatorOrigin', True, 'primitive'),
    )


@register("Storage.AttributionScopesData")
@dataclass
class AttributionScopesData(DataType):
    values: List[str]
    limit: float
    max_event_states: float
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('values', 'values', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('limit', 'limit', False, 'primitive'),
        FieldMeta('max_event_states', 'maxEventStates', False, 'primitive'),
    )


@register("Storage.AttributionReportingNamedBudgetDef")
@dataclass
class AttributionReportingNamedBudgetDef(DataType):
    name: str
    budget: int
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('name', 'name', False, 'primitive'),
        FieldMeta('budget', 'budget', False, 'primitive'),
    )


@register("Storage.AttributionReportingSourceRegistration")
@dataclass
class AttributionReportingSourceRegistration(DataType):
    time: Network_TimeSinceEpoch
    expiry: int
    trigger_data: List[float]
    event_report_windows: AttributionReportingEventReportWindows
    aggregatable_report_window: int
    type_: AttributionReportingSourceType
    source_origin: str
    reporting_origin: str
    destination_sites: List[str]
    event_id: UnsignedInt64AsBase10
    priority: SignedInt64AsBase10
    filter_data: List[AttributionReportingFilterDataEntry]
    aggregation_keys: List[AttributionReportingAggregationKeysEntry]
    trigger_data_matching: AttributionReportingTriggerDataMatching
    destination_limit_priority: SignedInt64AsBase10
    aggregatable_debug_reporting_config: AttributionReportingAggregatableDebugReportingConfig
    max_event_level_reports: int
    named_budgets: List[AttributionReportingNamedBudgetDef]
    debug_reporting: bool
    event_level_epsilon: float
    debug_key: Optional[UnsignedInt64AsBase10] = None
    scopes_data: Optional[AttributionScopesData] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('time', 'time', False, 'primitive'),
        FieldMeta('expiry', 'expiry', False, 'primitive'),
        FieldMeta('trigger_data', 'triggerData', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('event_report_windows', 'eventReportWindows', False, 'object', ref='Storage.AttributionReportingEventReportWindows'),
        FieldMeta('aggregatable_report_window', 'aggregatableReportWindow', False, 'primitive'),
        FieldMeta('type_', 'type', False, 'enum', ref='Storage.AttributionReportingSourceType'),
        FieldMeta('source_origin', 'sourceOrigin', False, 'primitive'),
        FieldMeta('reporting_origin', 'reportingOrigin', False, 'primitive'),
        FieldMeta('destination_sites', 'destinationSites', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('event_id', 'eventId', False, 'primitive'),
        FieldMeta('priority', 'priority', False, 'primitive'),
        FieldMeta('filter_data', 'filterData', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Storage.AttributionReportingFilterDataEntry')),
        FieldMeta('aggregation_keys', 'aggregationKeys', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Storage.AttributionReportingAggregationKeysEntry')),
        FieldMeta('trigger_data_matching', 'triggerDataMatching', False, 'enum', ref='Storage.AttributionReportingTriggerDataMatching'),
        FieldMeta('destination_limit_priority', 'destinationLimitPriority', False, 'primitive'),
        FieldMeta('aggregatable_debug_reporting_config', 'aggregatableDebugReportingConfig', False, 'object', ref='Storage.AttributionReportingAggregatableDebugReportingConfig'),
        FieldMeta('max_event_level_reports', 'maxEventLevelReports', False, 'primitive'),
        FieldMeta('named_budgets', 'namedBudgets', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Storage.AttributionReportingNamedBudgetDef')),
        FieldMeta('debug_reporting', 'debugReporting', False, 'primitive'),
        FieldMeta('event_level_epsilon', 'eventLevelEpsilon', False, 'primitive'),
        FieldMeta('debug_key', 'debugKey', True, 'primitive'),
        FieldMeta('scopes_data', 'scopesData', True, 'object', ref='Storage.AttributionScopesData'),
    )


@register("Storage.AttributionReportingSourceRegistrationResult")
class AttributionReportingSourceRegistrationResult(str, Enum):
    SUCCESS = 'success'
    INTERNALERROR = 'internalError'
    INSUFFICIENTSOURCECAPACITY = 'insufficientSourceCapacity'
    INSUFFICIENTUNIQUEDESTINATIONCAPACITY = 'insufficientUniqueDestinationCapacity'
    EXCESSIVEREPORTINGORIGINS = 'excessiveReportingOrigins'
    PROHIBITEDBYBROWSERPOLICY = 'prohibitedByBrowserPolicy'
    SUCCESSNOISED = 'successNoised'
    DESTINATIONREPORTINGLIMITREACHED = 'destinationReportingLimitReached'
    DESTINATIONGLOBALLIMITREACHED = 'destinationGlobalLimitReached'
    DESTINATIONBOTHLIMITSREACHED = 'destinationBothLimitsReached'
    REPORTINGORIGINSPERSITELIMITREACHED = 'reportingOriginsPerSiteLimitReached'
    EXCEEDSMAXCHANNELCAPACITY = 'exceedsMaxChannelCapacity'
    EXCEEDSMAXSCOPESCHANNELCAPACITY = 'exceedsMaxScopesChannelCapacity'
    EXCEEDSMAXTRIGGERSTATECARDINALITY = 'exceedsMaxTriggerStateCardinality'
    EXCEEDSMAXEVENTSTATESLIMIT = 'exceedsMaxEventStatesLimit'
    DESTINATIONPERDAYREPORTINGLIMITREACHED = 'destinationPerDayReportingLimitReached'


@register("Storage.AttributionReportingSourceRegistrationTimeConfig")
class AttributionReportingSourceRegistrationTimeConfig(str, Enum):
    INCLUDE = 'include'
    EXCLUDE = 'exclude'


@register("Storage.AttributionReportingAggregatableValueDictEntry")
@dataclass
class AttributionReportingAggregatableValueDictEntry(DataType):
    key: str
    value: float
    filtering_id: UnsignedInt64AsBase10
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('key', 'key', False, 'primitive'),
        FieldMeta('value', 'value', False, 'primitive'),
        FieldMeta('filtering_id', 'filteringId', False, 'primitive'),
    )


@register("Storage.AttributionReportingAggregatableValueEntry")
@dataclass
class AttributionReportingAggregatableValueEntry(DataType):
    values: List[AttributionReportingAggregatableValueDictEntry]
    filters: AttributionReportingFilterPair
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('values', 'values', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Storage.AttributionReportingAggregatableValueDictEntry')),
        FieldMeta('filters', 'filters', False, 'object', ref='Storage.AttributionReportingFilterPair'),
    )


@register("Storage.AttributionReportingEventTriggerData")
@dataclass
class AttributionReportingEventTriggerData(DataType):
    data: UnsignedInt64AsBase10
    priority: SignedInt64AsBase10
    filters: AttributionReportingFilterPair
    dedup_key: Optional[UnsignedInt64AsBase10] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('data', 'data', False, 'primitive'),
        FieldMeta('priority', 'priority', False, 'primitive'),
        FieldMeta('filters', 'filters', False, 'object', ref='Storage.AttributionReportingFilterPair'),
        FieldMeta('dedup_key', 'dedupKey', True, 'primitive'),
    )


@register("Storage.AttributionReportingAggregatableTriggerData")
@dataclass
class AttributionReportingAggregatableTriggerData(DataType):
    key_piece: UnsignedInt128AsBase16
    source_keys: List[str]
    filters: AttributionReportingFilterPair
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('key_piece', 'keyPiece', False, 'primitive'),
        FieldMeta('source_keys', 'sourceKeys', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('filters', 'filters', False, 'object', ref='Storage.AttributionReportingFilterPair'),
    )


@register("Storage.AttributionReportingAggregatableDedupKey")
@dataclass
class AttributionReportingAggregatableDedupKey(DataType):
    filters: AttributionReportingFilterPair
    dedup_key: Optional[UnsignedInt64AsBase10] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('filters', 'filters', False, 'object', ref='Storage.AttributionReportingFilterPair'),
        FieldMeta('dedup_key', 'dedupKey', True, 'primitive'),
    )


@register("Storage.AttributionReportingNamedBudgetCandidate")
@dataclass
class AttributionReportingNamedBudgetCandidate(DataType):
    filters: AttributionReportingFilterPair
    name: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('filters', 'filters', False, 'object', ref='Storage.AttributionReportingFilterPair'),
        FieldMeta('name', 'name', True, 'primitive'),
    )


@register("Storage.AttributionReportingTriggerRegistration")
@dataclass
class AttributionReportingTriggerRegistration(DataType):
    filters: AttributionReportingFilterPair
    aggregatable_dedup_keys: List[AttributionReportingAggregatableDedupKey]
    event_trigger_data: List[AttributionReportingEventTriggerData]
    aggregatable_trigger_data: List[AttributionReportingAggregatableTriggerData]
    aggregatable_values: List[AttributionReportingAggregatableValueEntry]
    aggregatable_filtering_id_max_bytes: int
    debug_reporting: bool
    source_registration_time_config: AttributionReportingSourceRegistrationTimeConfig
    aggregatable_debug_reporting_config: AttributionReportingAggregatableDebugReportingConfig
    scopes: List[str]
    named_budgets: List[AttributionReportingNamedBudgetCandidate]
    debug_key: Optional[UnsignedInt64AsBase10] = None
    aggregation_coordinator_origin: Optional[str] = None
    trigger_context_id: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('filters', 'filters', False, 'object', ref='Storage.AttributionReportingFilterPair'),
        FieldMeta('aggregatable_dedup_keys', 'aggregatableDedupKeys', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Storage.AttributionReportingAggregatableDedupKey')),
        FieldMeta('event_trigger_data', 'eventTriggerData', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Storage.AttributionReportingEventTriggerData')),
        FieldMeta('aggregatable_trigger_data', 'aggregatableTriggerData', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Storage.AttributionReportingAggregatableTriggerData')),
        FieldMeta('aggregatable_values', 'aggregatableValues', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Storage.AttributionReportingAggregatableValueEntry')),
        FieldMeta('aggregatable_filtering_id_max_bytes', 'aggregatableFilteringIdMaxBytes', False, 'primitive'),
        FieldMeta('debug_reporting', 'debugReporting', False, 'primitive'),
        FieldMeta('source_registration_time_config', 'sourceRegistrationTimeConfig', False, 'enum', ref='Storage.AttributionReportingSourceRegistrationTimeConfig'),
        FieldMeta('aggregatable_debug_reporting_config', 'aggregatableDebugReportingConfig', False, 'object', ref='Storage.AttributionReportingAggregatableDebugReportingConfig'),
        FieldMeta('scopes', 'scopes', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('named_budgets', 'namedBudgets', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Storage.AttributionReportingNamedBudgetCandidate')),
        FieldMeta('debug_key', 'debugKey', True, 'primitive'),
        FieldMeta('aggregation_coordinator_origin', 'aggregationCoordinatorOrigin', True, 'primitive'),
        FieldMeta('trigger_context_id', 'triggerContextId', True, 'primitive'),
    )


@register("Storage.AttributionReportingEventLevelResult")
class AttributionReportingEventLevelResult(str, Enum):
    SUCCESS = 'success'
    SUCCESSDROPPEDLOWERPRIORITY = 'successDroppedLowerPriority'
    INTERNALERROR = 'internalError'
    NOCAPACITYFORATTRIBUTIONDESTINATION = 'noCapacityForAttributionDestination'
    NOMATCHINGSOURCES = 'noMatchingSources'
    DEDUPLICATED = 'deduplicated'
    EXCESSIVEATTRIBUTIONS = 'excessiveAttributions'
    PRIORITYTOOLOW = 'priorityTooLow'
    NEVERATTRIBUTEDSOURCE = 'neverAttributedSource'
    EXCESSIVEREPORTINGORIGINS = 'excessiveReportingOrigins'
    NOMATCHINGSOURCEFILTERDATA = 'noMatchingSourceFilterData'
    PROHIBITEDBYBROWSERPOLICY = 'prohibitedByBrowserPolicy'
    NOMATCHINGCONFIGURATIONS = 'noMatchingConfigurations'
    EXCESSIVEREPORTS = 'excessiveReports'
    FALSELYATTRIBUTEDSOURCE = 'falselyAttributedSource'
    REPORTWINDOWPASSED = 'reportWindowPassed'
    NOTREGISTERED = 'notRegistered'
    REPORTWINDOWNOTSTARTED = 'reportWindowNotStarted'
    NOMATCHINGTRIGGERDATA = 'noMatchingTriggerData'


@register("Storage.AttributionReportingAggregatableResult")
class AttributionReportingAggregatableResult(str, Enum):
    SUCCESS = 'success'
    INTERNALERROR = 'internalError'
    NOCAPACITYFORATTRIBUTIONDESTINATION = 'noCapacityForAttributionDestination'
    NOMATCHINGSOURCES = 'noMatchingSources'
    EXCESSIVEATTRIBUTIONS = 'excessiveAttributions'
    EXCESSIVEREPORTINGORIGINS = 'excessiveReportingOrigins'
    NOHISTOGRAMS = 'noHistograms'
    INSUFFICIENTBUDGET = 'insufficientBudget'
    INSUFFICIENTNAMEDBUDGET = 'insufficientNamedBudget'
    NOMATCHINGSOURCEFILTERDATA = 'noMatchingSourceFilterData'
    NOTREGISTERED = 'notRegistered'
    PROHIBITEDBYBROWSERPOLICY = 'prohibitedByBrowserPolicy'
    DEDUPLICATED = 'deduplicated'
    REPORTWINDOWPASSED = 'reportWindowPassed'
    EXCESSIVEREPORTS = 'excessiveReports'


@register("Storage.AttributionReportingReportResult")
class AttributionReportingReportResult(str, Enum):
    SENT = 'sent'
    PROHIBITED = 'prohibited'
    FAILEDTOASSEMBLE = 'failedToAssemble'
    EXPIRED = 'expired'


@register("Storage.RelatedWebsiteSet")
@dataclass
class RelatedWebsiteSet(DataType):
    """A single Related Website Set object."""
    primary_sites: List[str]
    associated_sites: List[str]
    service_sites: List[str]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('primary_sites', 'primarySites', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('associated_sites', 'associatedSites', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('service_sites', 'serviceSites', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )

__all__ = ["AttributionReportingAggregatableDebugReportingConfig", "AttributionReportingAggregatableDebugReportingData", "AttributionReportingAggregatableDedupKey", "AttributionReportingAggregatableResult", "AttributionReportingAggregatableTriggerData", "AttributionReportingAggregatableValueDictEntry", "AttributionReportingAggregatableValueEntry", "AttributionReportingAggregationKeysEntry", "AttributionReportingEventLevelResult", "AttributionReportingEventReportWindows", "AttributionReportingEventTriggerData", "AttributionReportingFilterConfig", "AttributionReportingFilterDataEntry", "AttributionReportingFilterPair", "AttributionReportingNamedBudgetCandidate", "AttributionReportingNamedBudgetDef", "AttributionReportingReportResult", "AttributionReportingSourceRegistration", "AttributionReportingSourceRegistrationResult", "AttributionReportingSourceRegistrationTimeConfig", "AttributionReportingSourceType", "AttributionReportingTriggerDataMatching", "AttributionReportingTriggerRegistration", "AttributionScopesData", "InterestGroupAccessType", "InterestGroupAuctionEventType", "InterestGroupAuctionFetchType", "InterestGroupAuctionId", "RelatedWebsiteSet", "SerializedStorageKey", "SharedStorageAccessMethod", "SharedStorageAccessParams", "SharedStorageAccessScope", "SharedStorageEntry", "SharedStorageMetadata", "SharedStoragePrivateAggregationConfig", "SharedStorageReportingMetadata", "SharedStorageUrlWithMetadata", "SignedInt64AsBase10", "StorageBucket", "StorageBucketInfo", "StorageBucketsDurability", "StorageType", "TrustTokens", "UnsignedInt128AsBase16", "UnsignedInt64AsBase10", "UsageForType"]
