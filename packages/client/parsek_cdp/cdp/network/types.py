"""Custom types and enums for the Network domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, register

if TYPE_CHECKING:
    from ..io.types import StreamHandle as IO_StreamHandle
    from ..runtime.types import StackTrace as Runtime_StackTrace
    from ..security.types import CertificateId as Security_CertificateId
    from ..security.types import MixedContentType as Security_MixedContentType
    from ..security.types import SecurityState as Security_SecurityState

@register("Network.ResourceType")
class ResourceType(str, Enum):
    """Resource type as it was perceived by the rendering engine."""
    DOCUMENT = 'Document'
    STYLESHEET = 'Stylesheet'
    IMAGE = 'Image'
    MEDIA = 'Media'
    FONT = 'Font'
    SCRIPT = 'Script'
    TEXTTRACK = 'TextTrack'
    XHR = 'XHR'
    FETCH = 'Fetch'
    PREFETCH = 'Prefetch'
    EVENTSOURCE = 'EventSource'
    WEBSOCKET = 'WebSocket'
    MANIFEST = 'Manifest'
    SIGNEDEXCHANGE = 'SignedExchange'
    PING = 'Ping'
    CSPVIOLATIONREPORT = 'CSPViolationReport'
    PREFLIGHT = 'Preflight'
    FEDCM = 'FedCM'
    OTHER = 'Other'


type LoaderId = str  # Unique loader identifier.


type RequestId = str  # Unique network request identifier.


type InterceptionId = str  # Unique intercepted request identifier.


@register("Network.ErrorReason")
class ErrorReason(str, Enum):
    """Network level fetch failure reason."""
    FAILED = 'Failed'
    ABORTED = 'Aborted'
    TIMEDOUT = 'TimedOut'
    ACCESSDENIED = 'AccessDenied'
    CONNECTIONCLOSED = 'ConnectionClosed'
    CONNECTIONRESET = 'ConnectionReset'
    CONNECTIONREFUSED = 'ConnectionRefused'
    CONNECTIONABORTED = 'ConnectionAborted'
    CONNECTIONFAILED = 'ConnectionFailed'
    NAMENOTRESOLVED = 'NameNotResolved'
    INTERNETDISCONNECTED = 'InternetDisconnected'
    ADDRESSUNREACHABLE = 'AddressUnreachable'
    BLOCKEDBYCLIENT = 'BlockedByClient'
    BLOCKEDBYRESPONSE = 'BlockedByResponse'


type TimeSinceEpoch = float  # UTC time in seconds, counted from January 1, 1970.


type MonotonicTime = float  # Monotonically increasing time in seconds since an arbitrary point in the past.


type Headers = Dict[str, Any]  # Request / response headers as keys / values of JSON object.


@register("Network.ConnectionType")
class ConnectionType(str, Enum):
    """The underlying connection technology that the browser is supposedly using."""
    NONE = 'none'
    CELLULAR2G = 'cellular2g'
    CELLULAR3G = 'cellular3g'
    CELLULAR4G = 'cellular4g'
    BLUETOOTH = 'bluetooth'
    ETHERNET = 'ethernet'
    WIFI = 'wifi'
    WIMAX = 'wimax'
    OTHER = 'other'


@register("Network.CookieSameSite")
class CookieSameSite(str, Enum):
    """
    Represents the cookie's 'SameSite' status:
    https://tools.ietf.org/html/draft-west-first-party-cookies
    """
    STRICT = 'Strict'
    LAX = 'Lax'
    NONE = 'None'


@register("Network.CookiePriority")
class CookiePriority(str, Enum):
    """
    Represents the cookie's 'Priority' status:
    https://tools.ietf.org/html/draft-west-cookie-priority-00
    """
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'


@register("Network.CookieSourceScheme")
class CookieSourceScheme(str, Enum):
    """
    Represents the source scheme of the origin that originally set the cookie.
    A value of "Unset" allows protocol clients to emulate legacy cookie scope for the scheme.
    This is a temporary ability and it will be removed in the future.
    """
    UNSET = 'Unset'
    NONSECURE = 'NonSecure'
    SECURE = 'Secure'


@register("Network.ResourceTiming")
@dataclass
class ResourceTiming(DataType):
    """Timing information for the request."""
    request_time: float
    proxy_start: float
    proxy_end: float
    dns_start: float
    dns_end: float
    connect_start: float
    connect_end: float
    ssl_start: float
    ssl_end: float
    worker_start: float
    worker_ready: float
    worker_fetch_start: float
    worker_respond_with_settled: float
    send_start: float
    send_end: float
    push_start: float
    push_end: float
    receive_headers_start: float
    receive_headers_end: float
    worker_router_evaluation_start: Optional[float] = None
    worker_cache_lookup_start: Optional[float] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('request_time', 'requestTime', False, 'primitive'),
        FieldMeta('proxy_start', 'proxyStart', False, 'primitive'),
        FieldMeta('proxy_end', 'proxyEnd', False, 'primitive'),
        FieldMeta('dns_start', 'dnsStart', False, 'primitive'),
        FieldMeta('dns_end', 'dnsEnd', False, 'primitive'),
        FieldMeta('connect_start', 'connectStart', False, 'primitive'),
        FieldMeta('connect_end', 'connectEnd', False, 'primitive'),
        FieldMeta('ssl_start', 'sslStart', False, 'primitive'),
        FieldMeta('ssl_end', 'sslEnd', False, 'primitive'),
        FieldMeta('worker_start', 'workerStart', False, 'primitive'),
        FieldMeta('worker_ready', 'workerReady', False, 'primitive'),
        FieldMeta('worker_fetch_start', 'workerFetchStart', False, 'primitive'),
        FieldMeta('worker_respond_with_settled', 'workerRespondWithSettled', False, 'primitive'),
        FieldMeta('send_start', 'sendStart', False, 'primitive'),
        FieldMeta('send_end', 'sendEnd', False, 'primitive'),
        FieldMeta('push_start', 'pushStart', False, 'primitive'),
        FieldMeta('push_end', 'pushEnd', False, 'primitive'),
        FieldMeta('receive_headers_start', 'receiveHeadersStart', False, 'primitive'),
        FieldMeta('receive_headers_end', 'receiveHeadersEnd', False, 'primitive'),
        FieldMeta('worker_router_evaluation_start', 'workerRouterEvaluationStart', True, 'primitive'),
        FieldMeta('worker_cache_lookup_start', 'workerCacheLookupStart', True, 'primitive'),
    )


@register("Network.ResourcePriority")
class ResourcePriority(str, Enum):
    """Loading priority of a resource request."""
    VERYLOW = 'VeryLow'
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'
    VERYHIGH = 'VeryHigh'


@register("Network.PostDataEntry")
@dataclass
class PostDataEntry(DataType):
    """Post data entry for HTTP request"""
    bytes: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('bytes', 'bytes', True, 'primitive'),
    )


@register("Network.Request")
@dataclass
class Request(DataType):
    """HTTP request data."""
    url: str
    method: str
    headers: Headers
    initial_priority: ResourcePriority
    referrer_policy: Literal['unsafe-url', 'no-referrer-when-downgrade', 'no-referrer', 'origin', 'origin-when-cross-origin', 'same-origin', 'strict-origin', 'strict-origin-when-cross-origin']
    url_fragment: Optional[str] = None
    post_data: Optional[str] = None
    has_post_data: Optional[bool] = None
    post_data_entries: Optional[List[PostDataEntry]] = None
    mixed_content_type: Optional[Security_MixedContentType] = None
    is_link_preload: Optional[bool] = None
    trust_token_params: Optional[TrustTokenParams] = None
    is_same_site: Optional[bool] = None
    is_ad_related: Optional[bool] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('url', 'url', False, 'primitive'),
        FieldMeta('method', 'method', False, 'primitive'),
        FieldMeta('headers', 'headers', False, 'primitive'),
        FieldMeta('initial_priority', 'initialPriority', False, 'enum', ref='Network.ResourcePriority'),
        FieldMeta('referrer_policy', 'referrerPolicy', False, 'primitive'),
        FieldMeta('url_fragment', 'urlFragment', True, 'primitive'),
        FieldMeta('post_data', 'postData', True, 'primitive'),
        FieldMeta('has_post_data', 'hasPostData', True, 'primitive'),
        FieldMeta('post_data_entries', 'postDataEntries', True, 'array', inner=FieldMeta('', '', False, 'object', ref='Network.PostDataEntry')),
        FieldMeta('mixed_content_type', 'mixedContentType', True, 'enum', ref='Security.MixedContentType'),
        FieldMeta('is_link_preload', 'isLinkPreload', True, 'primitive'),
        FieldMeta('trust_token_params', 'trustTokenParams', True, 'object', ref='Network.TrustTokenParams'),
        FieldMeta('is_same_site', 'isSameSite', True, 'primitive'),
        FieldMeta('is_ad_related', 'isAdRelated', True, 'primitive'),
    )


@register("Network.SignedCertificateTimestamp")
@dataclass
class SignedCertificateTimestamp(DataType):
    """Details of a signed certificate timestamp (SCT)."""
    status: str
    origin: str
    log_description: str
    log_id: str
    timestamp: float
    hash_algorithm: str
    signature_algorithm: str
    signature_data: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('status', 'status', False, 'primitive'),
        FieldMeta('origin', 'origin', False, 'primitive'),
        FieldMeta('log_description', 'logDescription', False, 'primitive'),
        FieldMeta('log_id', 'logId', False, 'primitive'),
        FieldMeta('timestamp', 'timestamp', False, 'primitive'),
        FieldMeta('hash_algorithm', 'hashAlgorithm', False, 'primitive'),
        FieldMeta('signature_algorithm', 'signatureAlgorithm', False, 'primitive'),
        FieldMeta('signature_data', 'signatureData', False, 'primitive'),
    )


@register("Network.SecurityDetails")
@dataclass
class SecurityDetails(DataType):
    """Security details about a request."""
    protocol: str
    key_exchange: str
    cipher: str
    certificate_id: Security_CertificateId
    subject_name: str
    san_list: List[str]
    issuer: str
    valid_from: TimeSinceEpoch
    valid_to: TimeSinceEpoch
    signed_certificate_timestamp_list: List[SignedCertificateTimestamp]
    certificate_transparency_compliance: CertificateTransparencyCompliance
    encrypted_client_hello: bool
    key_exchange_group: Optional[str] = None
    mac: Optional[str] = None
    server_signature_algorithm: Optional[int] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('protocol', 'protocol', False, 'primitive'),
        FieldMeta('key_exchange', 'keyExchange', False, 'primitive'),
        FieldMeta('cipher', 'cipher', False, 'primitive'),
        FieldMeta('certificate_id', 'certificateId', False, 'primitive'),
        FieldMeta('subject_name', 'subjectName', False, 'primitive'),
        FieldMeta('san_list', 'sanList', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('issuer', 'issuer', False, 'primitive'),
        FieldMeta('valid_from', 'validFrom', False, 'primitive'),
        FieldMeta('valid_to', 'validTo', False, 'primitive'),
        FieldMeta('signed_certificate_timestamp_list', 'signedCertificateTimestampList', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Network.SignedCertificateTimestamp')),
        FieldMeta('certificate_transparency_compliance', 'certificateTransparencyCompliance', False, 'enum', ref='Network.CertificateTransparencyCompliance'),
        FieldMeta('encrypted_client_hello', 'encryptedClientHello', False, 'primitive'),
        FieldMeta('key_exchange_group', 'keyExchangeGroup', True, 'primitive'),
        FieldMeta('mac', 'mac', True, 'primitive'),
        FieldMeta('server_signature_algorithm', 'serverSignatureAlgorithm', True, 'primitive'),
    )


@register("Network.CertificateTransparencyCompliance")
class CertificateTransparencyCompliance(str, Enum):
    """Whether the request complied with Certificate Transparency policy."""
    UNKNOWN = 'unknown'
    NOT_COMPLIANT = 'not-compliant'
    COMPLIANT = 'compliant'


@register("Network.BlockedReason")
class BlockedReason(str, Enum):
    """The reason why request was blocked."""
    OTHER = 'other'
    CSP = 'csp'
    MIXED_CONTENT = 'mixed-content'
    ORIGIN = 'origin'
    INSPECTOR = 'inspector'
    INTEGRITY = 'integrity'
    SUBRESOURCE_FILTER = 'subresource-filter'
    CONTENT_TYPE = 'content-type'
    COEP_FRAME_RESOURCE_NEEDS_COEP_HEADER = 'coep-frame-resource-needs-coep-header'
    COOP_SANDBOXED_IFRAME_CANNOT_NAVIGATE_TO_COOP_PAGE = 'coop-sandboxed-iframe-cannot-navigate-to-coop-page'
    CORP_NOT_SAME_ORIGIN = 'corp-not-same-origin'
    CORP_NOT_SAME_ORIGIN_AFTER_DEFAULTED_TO_SAME_ORIGIN_BY_COEP = 'corp-not-same-origin-after-defaulted-to-same-origin-by-coep'
    CORP_NOT_SAME_ORIGIN_AFTER_DEFAULTED_TO_SAME_ORIGIN_BY_DIP = 'corp-not-same-origin-after-defaulted-to-same-origin-by-dip'
    CORP_NOT_SAME_ORIGIN_AFTER_DEFAULTED_TO_SAME_ORIGIN_BY_COEP_AND_DIP = 'corp-not-same-origin-after-defaulted-to-same-origin-by-coep-and-dip'
    CORP_NOT_SAME_SITE = 'corp-not-same-site'
    SRI_MESSAGE_SIGNATURE_MISMATCH = 'sri-message-signature-mismatch'


@register("Network.CorsError")
class CorsError(str, Enum):
    """The reason why request was blocked."""
    DISALLOWEDBYMODE = 'DisallowedByMode'
    INVALIDRESPONSE = 'InvalidResponse'
    WILDCARDORIGINNOTALLOWED = 'WildcardOriginNotAllowed'
    MISSINGALLOWORIGINHEADER = 'MissingAllowOriginHeader'
    MULTIPLEALLOWORIGINVALUES = 'MultipleAllowOriginValues'
    INVALIDALLOWORIGINVALUE = 'InvalidAllowOriginValue'
    ALLOWORIGINMISMATCH = 'AllowOriginMismatch'
    INVALIDALLOWCREDENTIALS = 'InvalidAllowCredentials'
    CORSDISABLEDSCHEME = 'CorsDisabledScheme'
    PREFLIGHTINVALIDSTATUS = 'PreflightInvalidStatus'
    PREFLIGHTDISALLOWEDREDIRECT = 'PreflightDisallowedRedirect'
    PREFLIGHTWILDCARDORIGINNOTALLOWED = 'PreflightWildcardOriginNotAllowed'
    PREFLIGHTMISSINGALLOWORIGINHEADER = 'PreflightMissingAllowOriginHeader'
    PREFLIGHTMULTIPLEALLOWORIGINVALUES = 'PreflightMultipleAllowOriginValues'
    PREFLIGHTINVALIDALLOWORIGINVALUE = 'PreflightInvalidAllowOriginValue'
    PREFLIGHTALLOWORIGINMISMATCH = 'PreflightAllowOriginMismatch'
    PREFLIGHTINVALIDALLOWCREDENTIALS = 'PreflightInvalidAllowCredentials'
    PREFLIGHTMISSINGALLOWEXTERNAL = 'PreflightMissingAllowExternal'
    PREFLIGHTINVALIDALLOWEXTERNAL = 'PreflightInvalidAllowExternal'
    PREFLIGHTMISSINGALLOWPRIVATENETWORK = 'PreflightMissingAllowPrivateNetwork'
    PREFLIGHTINVALIDALLOWPRIVATENETWORK = 'PreflightInvalidAllowPrivateNetwork'
    INVALIDALLOWMETHODSPREFLIGHTRESPONSE = 'InvalidAllowMethodsPreflightResponse'
    INVALIDALLOWHEADERSPREFLIGHTRESPONSE = 'InvalidAllowHeadersPreflightResponse'
    METHODDISALLOWEDBYPREFLIGHTRESPONSE = 'MethodDisallowedByPreflightResponse'
    HEADERDISALLOWEDBYPREFLIGHTRESPONSE = 'HeaderDisallowedByPreflightResponse'
    REDIRECTCONTAINSCREDENTIALS = 'RedirectContainsCredentials'
    INSECUREPRIVATENETWORK = 'InsecurePrivateNetwork'
    INVALIDPRIVATENETWORKACCESS = 'InvalidPrivateNetworkAccess'
    UNEXPECTEDPRIVATENETWORKACCESS = 'UnexpectedPrivateNetworkAccess'
    NOCORSREDIRECTMODENOTFOLLOW = 'NoCorsRedirectModeNotFollow'
    PREFLIGHTMISSINGPRIVATENETWORKACCESSID = 'PreflightMissingPrivateNetworkAccessId'
    PREFLIGHTMISSINGPRIVATENETWORKACCESSNAME = 'PreflightMissingPrivateNetworkAccessName'
    PRIVATENETWORKACCESSPERMISSIONUNAVAILABLE = 'PrivateNetworkAccessPermissionUnavailable'
    PRIVATENETWORKACCESSPERMISSIONDENIED = 'PrivateNetworkAccessPermissionDenied'
    LOCALNETWORKACCESSPERMISSIONDENIED = 'LocalNetworkAccessPermissionDenied'


@register("Network.CorsErrorStatus")
@dataclass
class CorsErrorStatus(DataType):
    cors_error: CorsError
    failed_parameter: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('cors_error', 'corsError', False, 'enum', ref='Network.CorsError'),
        FieldMeta('failed_parameter', 'failedParameter', False, 'primitive'),
    )


@register("Network.ServiceWorkerResponseSource")
class ServiceWorkerResponseSource(str, Enum):
    """Source of serviceworker response."""
    CACHE_STORAGE = 'cache-storage'
    HTTP_CACHE = 'http-cache'
    FALLBACK_CODE = 'fallback-code'
    NETWORK = 'network'


@register("Network.TrustTokenParams")
@dataclass
class TrustTokenParams(DataType):
    """
    Determines what type of Trust Token operation is executed and
    depending on the type, some additional parameters. The values
    are specified in third_party/blink/renderer/core/fetch/trust_token.idl.
    """
    operation: TrustTokenOperationType
    refresh_policy: Literal['UseCached', 'Refresh']
    issuers: Optional[List[str]] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('operation', 'operation', False, 'enum', ref='Network.TrustTokenOperationType'),
        FieldMeta('refresh_policy', 'refreshPolicy', False, 'primitive'),
        FieldMeta('issuers', 'issuers', True, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


@register("Network.TrustTokenOperationType")
class TrustTokenOperationType(str, Enum):
    ISSUANCE = 'Issuance'
    REDEMPTION = 'Redemption'
    SIGNING = 'Signing'


@register("Network.AlternateProtocolUsage")
class AlternateProtocolUsage(str, Enum):
    """The reason why Chrome uses a specific transport protocol for HTTP semantics."""
    ALTERNATIVEJOBWONWITHOUTRACE = 'alternativeJobWonWithoutRace'
    ALTERNATIVEJOBWONRACE = 'alternativeJobWonRace'
    MAINJOBWONRACE = 'mainJobWonRace'
    MAPPINGMISSING = 'mappingMissing'
    BROKEN = 'broken'
    DNSALPNH3JOBWONWITHOUTRACE = 'dnsAlpnH3JobWonWithoutRace'
    DNSALPNH3JOBWONRACE = 'dnsAlpnH3JobWonRace'
    UNSPECIFIEDREASON = 'unspecifiedReason'


@register("Network.ServiceWorkerRouterSource")
class ServiceWorkerRouterSource(str, Enum):
    """Source of service worker router."""
    NETWORK = 'network'
    CACHE = 'cache'
    FETCH_EVENT = 'fetch-event'
    RACE_NETWORK_AND_FETCH_HANDLER = 'race-network-and-fetch-handler'
    RACE_NETWORK_AND_CACHE = 'race-network-and-cache'


@register("Network.ServiceWorkerRouterInfo")
@dataclass
class ServiceWorkerRouterInfo(DataType):
    rule_id_matched: Optional[int] = None
    matched_source_type: Optional[ServiceWorkerRouterSource] = None
    actual_source_type: Optional[ServiceWorkerRouterSource] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('rule_id_matched', 'ruleIdMatched', True, 'primitive'),
        FieldMeta('matched_source_type', 'matchedSourceType', True, 'enum', ref='Network.ServiceWorkerRouterSource'),
        FieldMeta('actual_source_type', 'actualSourceType', True, 'enum', ref='Network.ServiceWorkerRouterSource'),
    )


@register("Network.Response")
@dataclass
class Response(DataType):
    """HTTP response data."""
    url: str
    status: int
    status_text: str
    headers: Headers
    mime_type: str
    charset: str
    connection_reused: bool
    connection_id: float
    encoded_data_length: float
    security_state: Security_SecurityState
    headers_text: Optional[str] = None
    request_headers: Optional[Headers] = None
    request_headers_text: Optional[str] = None
    remote_ip_address: Optional[str] = None
    remote_port: Optional[int] = None
    from_disk_cache: Optional[bool] = None
    from_service_worker: Optional[bool] = None
    from_prefetch_cache: Optional[bool] = None
    from_early_hints: Optional[bool] = None
    service_worker_router_info: Optional[ServiceWorkerRouterInfo] = None
    timing: Optional[ResourceTiming] = None
    service_worker_response_source: Optional[ServiceWorkerResponseSource] = None
    response_time: Optional[TimeSinceEpoch] = None
    cache_storage_cache_name: Optional[str] = None
    protocol: Optional[str] = None
    alternate_protocol_usage: Optional[AlternateProtocolUsage] = None
    security_details: Optional[SecurityDetails] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('url', 'url', False, 'primitive'),
        FieldMeta('status', 'status', False, 'primitive'),
        FieldMeta('status_text', 'statusText', False, 'primitive'),
        FieldMeta('headers', 'headers', False, 'primitive'),
        FieldMeta('mime_type', 'mimeType', False, 'primitive'),
        FieldMeta('charset', 'charset', False, 'primitive'),
        FieldMeta('connection_reused', 'connectionReused', False, 'primitive'),
        FieldMeta('connection_id', 'connectionId', False, 'primitive'),
        FieldMeta('encoded_data_length', 'encodedDataLength', False, 'primitive'),
        FieldMeta('security_state', 'securityState', False, 'enum', ref='Security.SecurityState'),
        FieldMeta('headers_text', 'headersText', True, 'primitive'),
        FieldMeta('request_headers', 'requestHeaders', True, 'primitive'),
        FieldMeta('request_headers_text', 'requestHeadersText', True, 'primitive'),
        FieldMeta('remote_ip_address', 'remoteIPAddress', True, 'primitive'),
        FieldMeta('remote_port', 'remotePort', True, 'primitive'),
        FieldMeta('from_disk_cache', 'fromDiskCache', True, 'primitive'),
        FieldMeta('from_service_worker', 'fromServiceWorker', True, 'primitive'),
        FieldMeta('from_prefetch_cache', 'fromPrefetchCache', True, 'primitive'),
        FieldMeta('from_early_hints', 'fromEarlyHints', True, 'primitive'),
        FieldMeta('service_worker_router_info', 'serviceWorkerRouterInfo', True, 'object', ref='Network.ServiceWorkerRouterInfo'),
        FieldMeta('timing', 'timing', True, 'object', ref='Network.ResourceTiming'),
        FieldMeta('service_worker_response_source', 'serviceWorkerResponseSource', True, 'enum', ref='Network.ServiceWorkerResponseSource'),
        FieldMeta('response_time', 'responseTime', True, 'primitive'),
        FieldMeta('cache_storage_cache_name', 'cacheStorageCacheName', True, 'primitive'),
        FieldMeta('protocol', 'protocol', True, 'primitive'),
        FieldMeta('alternate_protocol_usage', 'alternateProtocolUsage', True, 'enum', ref='Network.AlternateProtocolUsage'),
        FieldMeta('security_details', 'securityDetails', True, 'object', ref='Network.SecurityDetails'),
    )


@register("Network.WebSocketRequest")
@dataclass
class WebSocketRequest(DataType):
    """WebSocket request data."""
    headers: Headers
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('headers', 'headers', False, 'primitive'),
    )


@register("Network.WebSocketResponse")
@dataclass
class WebSocketResponse(DataType):
    """WebSocket response data."""
    status: int
    status_text: str
    headers: Headers
    headers_text: Optional[str] = None
    request_headers: Optional[Headers] = None
    request_headers_text: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('status', 'status', False, 'primitive'),
        FieldMeta('status_text', 'statusText', False, 'primitive'),
        FieldMeta('headers', 'headers', False, 'primitive'),
        FieldMeta('headers_text', 'headersText', True, 'primitive'),
        FieldMeta('request_headers', 'requestHeaders', True, 'primitive'),
        FieldMeta('request_headers_text', 'requestHeadersText', True, 'primitive'),
    )


@register("Network.WebSocketFrame")
@dataclass
class WebSocketFrame(DataType):
    """WebSocket message data. This represents an entire WebSocket message, not just a fragmented frame as the name suggests."""
    opcode: float
    mask: bool
    payload_data: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('opcode', 'opcode', False, 'primitive'),
        FieldMeta('mask', 'mask', False, 'primitive'),
        FieldMeta('payload_data', 'payloadData', False, 'primitive'),
    )


@register("Network.CachedResource")
@dataclass
class CachedResource(DataType):
    """Information about the cached resource."""
    url: str
    type_: ResourceType
    body_size: float
    response: Optional[Response] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('url', 'url', False, 'primitive'),
        FieldMeta('type_', 'type', False, 'enum', ref='Network.ResourceType'),
        FieldMeta('body_size', 'bodySize', False, 'primitive'),
        FieldMeta('response', 'response', True, 'object', ref='Network.Response'),
    )


@register("Network.Initiator")
@dataclass
class Initiator(DataType):
    """Information about the request initiator."""
    type_: Literal['parser', 'script', 'preload', 'SignedExchange', 'preflight', 'FedCM', 'other']
    stack: Optional[Runtime_StackTrace] = None
    url: Optional[str] = None
    line_number: Optional[float] = None
    column_number: Optional[float] = None
    request_id: Optional[RequestId] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('type_', 'type', False, 'primitive'),
        FieldMeta('stack', 'stack', True, 'object', ref='Runtime.StackTrace'),
        FieldMeta('url', 'url', True, 'primitive'),
        FieldMeta('line_number', 'lineNumber', True, 'primitive'),
        FieldMeta('column_number', 'columnNumber', True, 'primitive'),
        FieldMeta('request_id', 'requestId', True, 'primitive'),
    )


@register("Network.CookiePartitionKey")
@dataclass
class CookiePartitionKey(DataType):
    """
    cookiePartitionKey object
    The representation of the components of the key that are created by the cookiePartitionKey class contained in net/cookies/cookie_partition_key.h.
    """
    top_level_site: str
    has_cross_site_ancestor: bool
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('top_level_site', 'topLevelSite', False, 'primitive'),
        FieldMeta('has_cross_site_ancestor', 'hasCrossSiteAncestor', False, 'primitive'),
    )


@register("Network.Cookie")
@dataclass
class Cookie(DataType):
    """Cookie object"""
    name: str
    value: str
    domain: str
    path: str
    expires: float
    size: int
    http_only: bool
    secure: bool
    session: bool
    priority: CookiePriority
    same_party: bool
    source_scheme: CookieSourceScheme
    source_port: int
    same_site: Optional[CookieSameSite] = None
    partition_key: Optional[CookiePartitionKey] = None
    partition_key_opaque: Optional[bool] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('name', 'name', False, 'primitive'),
        FieldMeta('value', 'value', False, 'primitive'),
        FieldMeta('domain', 'domain', False, 'primitive'),
        FieldMeta('path', 'path', False, 'primitive'),
        FieldMeta('expires', 'expires', False, 'primitive'),
        FieldMeta('size', 'size', False, 'primitive'),
        FieldMeta('http_only', 'httpOnly', False, 'primitive'),
        FieldMeta('secure', 'secure', False, 'primitive'),
        FieldMeta('session', 'session', False, 'primitive'),
        FieldMeta('priority', 'priority', False, 'enum', ref='Network.CookiePriority'),
        FieldMeta('same_party', 'sameParty', False, 'primitive'),
        FieldMeta('source_scheme', 'sourceScheme', False, 'enum', ref='Network.CookieSourceScheme'),
        FieldMeta('source_port', 'sourcePort', False, 'primitive'),
        FieldMeta('same_site', 'sameSite', True, 'enum', ref='Network.CookieSameSite'),
        FieldMeta('partition_key', 'partitionKey', True, 'object', ref='Network.CookiePartitionKey'),
        FieldMeta('partition_key_opaque', 'partitionKeyOpaque', True, 'primitive'),
    )


@register("Network.SetCookieBlockedReason")
class SetCookieBlockedReason(str, Enum):
    """Types of reasons why a cookie may not be stored from a response."""
    SECUREONLY = 'SecureOnly'
    SAMESITESTRICT = 'SameSiteStrict'
    SAMESITELAX = 'SameSiteLax'
    SAMESITEUNSPECIFIEDTREATEDASLAX = 'SameSiteUnspecifiedTreatedAsLax'
    SAMESITENONEINSECURE = 'SameSiteNoneInsecure'
    USERPREFERENCES = 'UserPreferences'
    THIRDPARTYPHASEOUT = 'ThirdPartyPhaseout'
    THIRDPARTYBLOCKEDINFIRSTPARTYSET = 'ThirdPartyBlockedInFirstPartySet'
    SYNTAXERROR = 'SyntaxError'
    SCHEMENOTSUPPORTED = 'SchemeNotSupported'
    OVERWRITESECURE = 'OverwriteSecure'
    INVALIDDOMAIN = 'InvalidDomain'
    INVALIDPREFIX = 'InvalidPrefix'
    UNKNOWNERROR = 'UnknownError'
    SCHEMEFULSAMESITESTRICT = 'SchemefulSameSiteStrict'
    SCHEMEFULSAMESITELAX = 'SchemefulSameSiteLax'
    SCHEMEFULSAMESITEUNSPECIFIEDTREATEDASLAX = 'SchemefulSameSiteUnspecifiedTreatedAsLax'
    SAMEPARTYFROMCROSSPARTYCONTEXT = 'SamePartyFromCrossPartyContext'
    SAMEPARTYCONFLICTSWITHOTHERATTRIBUTES = 'SamePartyConflictsWithOtherAttributes'
    NAMEVALUEPAIREXCEEDSMAXSIZE = 'NameValuePairExceedsMaxSize'
    DISALLOWEDCHARACTER = 'DisallowedCharacter'
    NOCOOKIECONTENT = 'NoCookieContent'


@register("Network.CookieBlockedReason")
class CookieBlockedReason(str, Enum):
    """Types of reasons why a cookie may not be sent with a request."""
    SECUREONLY = 'SecureOnly'
    NOTONPATH = 'NotOnPath'
    DOMAINMISMATCH = 'DomainMismatch'
    SAMESITESTRICT = 'SameSiteStrict'
    SAMESITELAX = 'SameSiteLax'
    SAMESITEUNSPECIFIEDTREATEDASLAX = 'SameSiteUnspecifiedTreatedAsLax'
    SAMESITENONEINSECURE = 'SameSiteNoneInsecure'
    USERPREFERENCES = 'UserPreferences'
    THIRDPARTYPHASEOUT = 'ThirdPartyPhaseout'
    THIRDPARTYBLOCKEDINFIRSTPARTYSET = 'ThirdPartyBlockedInFirstPartySet'
    UNKNOWNERROR = 'UnknownError'
    SCHEMEFULSAMESITESTRICT = 'SchemefulSameSiteStrict'
    SCHEMEFULSAMESITELAX = 'SchemefulSameSiteLax'
    SCHEMEFULSAMESITEUNSPECIFIEDTREATEDASLAX = 'SchemefulSameSiteUnspecifiedTreatedAsLax'
    SAMEPARTYFROMCROSSPARTYCONTEXT = 'SamePartyFromCrossPartyContext'
    NAMEVALUEPAIREXCEEDSMAXSIZE = 'NameValuePairExceedsMaxSize'
    PORTMISMATCH = 'PortMismatch'
    SCHEMEMISMATCH = 'SchemeMismatch'
    ANONYMOUSCONTEXT = 'AnonymousContext'


@register("Network.CookieExemptionReason")
class CookieExemptionReason(str, Enum):
    """Types of reasons why a cookie should have been blocked by 3PCD but is exempted for the request."""
    NONE = 'None'
    USERSETTING = 'UserSetting'
    TPCDMETADATA = 'TPCDMetadata'
    TPCDDEPRECATIONTRIAL = 'TPCDDeprecationTrial'
    TOPLEVELTPCDDEPRECATIONTRIAL = 'TopLevelTPCDDeprecationTrial'
    TPCDHEURISTICS = 'TPCDHeuristics'
    ENTERPRISEPOLICY = 'EnterprisePolicy'
    STORAGEACCESS = 'StorageAccess'
    TOPLEVELSTORAGEACCESS = 'TopLevelStorageAccess'
    SCHEME = 'Scheme'
    SAMESITENONECOOKIESINSANDBOX = 'SameSiteNoneCookiesInSandbox'


@register("Network.BlockedSetCookieWithReason")
@dataclass
class BlockedSetCookieWithReason(DataType):
    """A cookie which was not stored from a response with the corresponding reason."""
    blocked_reasons: List[SetCookieBlockedReason]
    cookie_line: str
    cookie: Optional[Cookie] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('blocked_reasons', 'blockedReasons', False, 'array', inner=FieldMeta('', '', False, 'enum', ref='Network.SetCookieBlockedReason')),
        FieldMeta('cookie_line', 'cookieLine', False, 'primitive'),
        FieldMeta('cookie', 'cookie', True, 'object', ref='Network.Cookie'),
    )


@register("Network.ExemptedSetCookieWithReason")
@dataclass
class ExemptedSetCookieWithReason(DataType):
    """
    A cookie should have been blocked by 3PCD but is exempted and stored from a response with the
    corresponding reason. A cookie could only have at most one exemption reason.
    """
    exemption_reason: CookieExemptionReason
    cookie_line: str
    cookie: Cookie
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('exemption_reason', 'exemptionReason', False, 'enum', ref='Network.CookieExemptionReason'),
        FieldMeta('cookie_line', 'cookieLine', False, 'primitive'),
        FieldMeta('cookie', 'cookie', False, 'object', ref='Network.Cookie'),
    )


@register("Network.AssociatedCookie")
@dataclass
class AssociatedCookie(DataType):
    """
    A cookie associated with the request which may or may not be sent with it.
    Includes the cookies itself and reasons for blocking or exemption.
    """
    cookie: Cookie
    blocked_reasons: List[CookieBlockedReason]
    exemption_reason: Optional[CookieExemptionReason] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('cookie', 'cookie', False, 'object', ref='Network.Cookie'),
        FieldMeta('blocked_reasons', 'blockedReasons', False, 'array', inner=FieldMeta('', '', False, 'enum', ref='Network.CookieBlockedReason')),
        FieldMeta('exemption_reason', 'exemptionReason', True, 'enum', ref='Network.CookieExemptionReason'),
    )


@register("Network.CookieParam")
@dataclass
class CookieParam(DataType):
    """Cookie parameter object"""
    name: str
    value: str
    url: Optional[str] = None
    domain: Optional[str] = None
    path: Optional[str] = None
    secure: Optional[bool] = None
    http_only: Optional[bool] = None
    same_site: Optional[CookieSameSite] = None
    expires: Optional[TimeSinceEpoch] = None
    priority: Optional[CookiePriority] = None
    same_party: Optional[bool] = None
    source_scheme: Optional[CookieSourceScheme] = None
    source_port: Optional[int] = None
    partition_key: Optional[CookiePartitionKey] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('name', 'name', False, 'primitive'),
        FieldMeta('value', 'value', False, 'primitive'),
        FieldMeta('url', 'url', True, 'primitive'),
        FieldMeta('domain', 'domain', True, 'primitive'),
        FieldMeta('path', 'path', True, 'primitive'),
        FieldMeta('secure', 'secure', True, 'primitive'),
        FieldMeta('http_only', 'httpOnly', True, 'primitive'),
        FieldMeta('same_site', 'sameSite', True, 'enum', ref='Network.CookieSameSite'),
        FieldMeta('expires', 'expires', True, 'primitive'),
        FieldMeta('priority', 'priority', True, 'enum', ref='Network.CookiePriority'),
        FieldMeta('same_party', 'sameParty', True, 'primitive'),
        FieldMeta('source_scheme', 'sourceScheme', True, 'enum', ref='Network.CookieSourceScheme'),
        FieldMeta('source_port', 'sourcePort', True, 'primitive'),
        FieldMeta('partition_key', 'partitionKey', True, 'object', ref='Network.CookiePartitionKey'),
    )


@register("Network.AuthChallenge")
@dataclass
class AuthChallenge(DataType):
    """Authorization challenge for HTTP status code 401 or 407."""
    origin: str
    scheme: str
    realm: str
    source: Optional[Literal['Server', 'Proxy']] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('origin', 'origin', False, 'primitive'),
        FieldMeta('scheme', 'scheme', False, 'primitive'),
        FieldMeta('realm', 'realm', False, 'primitive'),
        FieldMeta('source', 'source', True, 'primitive'),
    )


@register("Network.AuthChallengeResponse")
@dataclass
class AuthChallengeResponse(DataType):
    """Response to an AuthChallenge."""
    response: Literal['Default', 'CancelAuth', 'ProvideCredentials']
    username: Optional[str] = None
    password: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('response', 'response', False, 'primitive'),
        FieldMeta('username', 'username', True, 'primitive'),
        FieldMeta('password', 'password', True, 'primitive'),
    )


@register("Network.InterceptionStage")
class InterceptionStage(str, Enum):
    """
    Stages of the interception to begin intercepting. Request will intercept before the request is
    sent. Response will intercept after the response is received.
    """
    REQUEST = 'Request'
    HEADERSRECEIVED = 'HeadersReceived'


@register("Network.RequestPattern")
@dataclass
class RequestPattern(DataType):
    """Request pattern for interception."""
    url_pattern: Optional[str] = None
    resource_type: Optional[ResourceType] = None
    interception_stage: Optional[InterceptionStage] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('url_pattern', 'urlPattern', True, 'primitive'),
        FieldMeta('resource_type', 'resourceType', True, 'enum', ref='Network.ResourceType'),
        FieldMeta('interception_stage', 'interceptionStage', True, 'enum', ref='Network.InterceptionStage'),
    )


@register("Network.SignedExchangeSignature")
@dataclass
class SignedExchangeSignature(DataType):
    """
    Information about a signed exchange signature.
    https://wicg.github.io/webpackage/draft-yasskin-httpbis-origin-signed-exchanges-impl.html#rfc.section.3.1
    """
    label: str
    signature: str
    integrity: str
    validity_url: str
    date: int
    expires: int
    cert_url: Optional[str] = None
    cert_sha256: Optional[str] = None
    certificates: Optional[List[str]] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('label', 'label', False, 'primitive'),
        FieldMeta('signature', 'signature', False, 'primitive'),
        FieldMeta('integrity', 'integrity', False, 'primitive'),
        FieldMeta('validity_url', 'validityUrl', False, 'primitive'),
        FieldMeta('date', 'date', False, 'primitive'),
        FieldMeta('expires', 'expires', False, 'primitive'),
        FieldMeta('cert_url', 'certUrl', True, 'primitive'),
        FieldMeta('cert_sha256', 'certSha256', True, 'primitive'),
        FieldMeta('certificates', 'certificates', True, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


@register("Network.SignedExchangeHeader")
@dataclass
class SignedExchangeHeader(DataType):
    """
    Information about a signed exchange header.
    https://wicg.github.io/webpackage/draft-yasskin-httpbis-origin-signed-exchanges-impl.html#cbor-representation
    """
    request_url: str
    response_code: int
    response_headers: Headers
    signatures: List[SignedExchangeSignature]
    header_integrity: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('request_url', 'requestUrl', False, 'primitive'),
        FieldMeta('response_code', 'responseCode', False, 'primitive'),
        FieldMeta('response_headers', 'responseHeaders', False, 'primitive'),
        FieldMeta('signatures', 'signatures', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Network.SignedExchangeSignature')),
        FieldMeta('header_integrity', 'headerIntegrity', False, 'primitive'),
    )


@register("Network.SignedExchangeErrorField")
class SignedExchangeErrorField(str, Enum):
    """Field type for a signed exchange related error."""
    SIGNATURESIG = 'signatureSig'
    SIGNATUREINTEGRITY = 'signatureIntegrity'
    SIGNATURECERTURL = 'signatureCertUrl'
    SIGNATURECERTSHA256 = 'signatureCertSha256'
    SIGNATUREVALIDITYURL = 'signatureValidityUrl'
    SIGNATURETIMESTAMPS = 'signatureTimestamps'


@register("Network.SignedExchangeError")
@dataclass
class SignedExchangeError(DataType):
    """Information about a signed exchange response."""
    message: str
    signature_index: Optional[int] = None
    error_field: Optional[SignedExchangeErrorField] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('message', 'message', False, 'primitive'),
        FieldMeta('signature_index', 'signatureIndex', True, 'primitive'),
        FieldMeta('error_field', 'errorField', True, 'enum', ref='Network.SignedExchangeErrorField'),
    )


@register("Network.SignedExchangeInfo")
@dataclass
class SignedExchangeInfo(DataType):
    """Information about a signed exchange response."""
    outer_response: Response
    has_extra_info: bool
    header: Optional[SignedExchangeHeader] = None
    security_details: Optional[SecurityDetails] = None
    errors: Optional[List[SignedExchangeError]] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('outer_response', 'outerResponse', False, 'object', ref='Network.Response'),
        FieldMeta('has_extra_info', 'hasExtraInfo', False, 'primitive'),
        FieldMeta('header', 'header', True, 'object', ref='Network.SignedExchangeHeader'),
        FieldMeta('security_details', 'securityDetails', True, 'object', ref='Network.SecurityDetails'),
        FieldMeta('errors', 'errors', True, 'array', inner=FieldMeta('', '', False, 'object', ref='Network.SignedExchangeError')),
    )


@register("Network.ContentEncoding")
class ContentEncoding(str, Enum):
    """List of content encodings supported by the backend."""
    DEFLATE = 'deflate'
    GZIP = 'gzip'
    BR = 'br'
    ZSTD = 'zstd'


@register("Network.NetworkConditions")
@dataclass
class NetworkConditions(DataType):
    url_pattern: str
    latency: float
    download_throughput: float
    upload_throughput: float
    connection_type: Optional[ConnectionType] = None
    packet_loss: Optional[float] = None
    packet_queue_length: Optional[int] = None
    packet_reordering: Optional[bool] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('url_pattern', 'urlPattern', False, 'primitive'),
        FieldMeta('latency', 'latency', False, 'primitive'),
        FieldMeta('download_throughput', 'downloadThroughput', False, 'primitive'),
        FieldMeta('upload_throughput', 'uploadThroughput', False, 'primitive'),
        FieldMeta('connection_type', 'connectionType', True, 'enum', ref='Network.ConnectionType'),
        FieldMeta('packet_loss', 'packetLoss', True, 'primitive'),
        FieldMeta('packet_queue_length', 'packetQueueLength', True, 'primitive'),
        FieldMeta('packet_reordering', 'packetReordering', True, 'primitive'),
    )


@register("Network.BlockPattern")
@dataclass
class BlockPattern(DataType):
    url_pattern: str
    block: bool
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('url_pattern', 'urlPattern', False, 'primitive'),
        FieldMeta('block', 'block', False, 'primitive'),
    )


@register("Network.DirectSocketDnsQueryType")
class DirectSocketDnsQueryType(str, Enum):
    IPV4 = 'ipv4'
    IPV6 = 'ipv6'


@register("Network.DirectTCPSocketOptions")
@dataclass
class DirectTCPSocketOptions(DataType):
    no_delay: bool
    keep_alive_delay: Optional[float] = None
    send_buffer_size: Optional[float] = None
    receive_buffer_size: Optional[float] = None
    dns_query_type: Optional[DirectSocketDnsQueryType] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('no_delay', 'noDelay', False, 'primitive'),
        FieldMeta('keep_alive_delay', 'keepAliveDelay', True, 'primitive'),
        FieldMeta('send_buffer_size', 'sendBufferSize', True, 'primitive'),
        FieldMeta('receive_buffer_size', 'receiveBufferSize', True, 'primitive'),
        FieldMeta('dns_query_type', 'dnsQueryType', True, 'enum', ref='Network.DirectSocketDnsQueryType'),
    )


@register("Network.DirectUDPSocketOptions")
@dataclass
class DirectUDPSocketOptions(DataType):
    remote_addr: Optional[str] = None
    remote_port: Optional[int] = None
    local_addr: Optional[str] = None
    local_port: Optional[int] = None
    dns_query_type: Optional[DirectSocketDnsQueryType] = None
    send_buffer_size: Optional[float] = None
    receive_buffer_size: Optional[float] = None
    multicast_loopback: Optional[bool] = None
    multicast_time_to_live: Optional[int] = None
    multicast_allow_address_sharing: Optional[bool] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('remote_addr', 'remoteAddr', True, 'primitive'),
        FieldMeta('remote_port', 'remotePort', True, 'primitive'),
        FieldMeta('local_addr', 'localAddr', True, 'primitive'),
        FieldMeta('local_port', 'localPort', True, 'primitive'),
        FieldMeta('dns_query_type', 'dnsQueryType', True, 'enum', ref='Network.DirectSocketDnsQueryType'),
        FieldMeta('send_buffer_size', 'sendBufferSize', True, 'primitive'),
        FieldMeta('receive_buffer_size', 'receiveBufferSize', True, 'primitive'),
        FieldMeta('multicast_loopback', 'multicastLoopback', True, 'primitive'),
        FieldMeta('multicast_time_to_live', 'multicastTimeToLive', True, 'primitive'),
        FieldMeta('multicast_allow_address_sharing', 'multicastAllowAddressSharing', True, 'primitive'),
    )


@register("Network.DirectUDPMessage")
@dataclass
class DirectUDPMessage(DataType):
    data: str
    remote_addr: Optional[str] = None
    remote_port: Optional[int] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('data', 'data', False, 'primitive'),
        FieldMeta('remote_addr', 'remoteAddr', True, 'primitive'),
        FieldMeta('remote_port', 'remotePort', True, 'primitive'),
    )


@register("Network.PrivateNetworkRequestPolicy")
class PrivateNetworkRequestPolicy(str, Enum):
    ALLOW = 'Allow'
    BLOCKFROMINSECURETOMOREPRIVATE = 'BlockFromInsecureToMorePrivate'
    WARNFROMINSECURETOMOREPRIVATE = 'WarnFromInsecureToMorePrivate'
    PERMISSIONBLOCK = 'PermissionBlock'
    PERMISSIONWARN = 'PermissionWarn'


@register("Network.IPAddressSpace")
class IPAddressSpace(str, Enum):
    LOOPBACK = 'Loopback'
    LOCAL = 'Local'
    PUBLIC = 'Public'
    UNKNOWN = 'Unknown'


@register("Network.ConnectTiming")
@dataclass
class ConnectTiming(DataType):
    request_time: float
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('request_time', 'requestTime', False, 'primitive'),
    )


@register("Network.ClientSecurityState")
@dataclass
class ClientSecurityState(DataType):
    initiator_is_secure_context: bool
    initiator_ip_address_space: IPAddressSpace
    private_network_request_policy: PrivateNetworkRequestPolicy
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('initiator_is_secure_context', 'initiatorIsSecureContext', False, 'primitive'),
        FieldMeta('initiator_ip_address_space', 'initiatorIPAddressSpace', False, 'enum', ref='Network.IPAddressSpace'),
        FieldMeta('private_network_request_policy', 'privateNetworkRequestPolicy', False, 'enum', ref='Network.PrivateNetworkRequestPolicy'),
    )


@register("Network.CrossOriginOpenerPolicyValue")
class CrossOriginOpenerPolicyValue(str, Enum):
    SAMEORIGIN = 'SameOrigin'
    SAMEORIGINALLOWPOPUPS = 'SameOriginAllowPopups'
    RESTRICTPROPERTIES = 'RestrictProperties'
    UNSAFENONE = 'UnsafeNone'
    SAMEORIGINPLUSCOEP = 'SameOriginPlusCoep'
    RESTRICTPROPERTIESPLUSCOEP = 'RestrictPropertiesPlusCoep'
    NOOPENERALLOWPOPUPS = 'NoopenerAllowPopups'


@register("Network.CrossOriginOpenerPolicyStatus")
@dataclass
class CrossOriginOpenerPolicyStatus(DataType):
    value: CrossOriginOpenerPolicyValue
    report_only_value: CrossOriginOpenerPolicyValue
    reporting_endpoint: Optional[str] = None
    report_only_reporting_endpoint: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('value', 'value', False, 'enum', ref='Network.CrossOriginOpenerPolicyValue'),
        FieldMeta('report_only_value', 'reportOnlyValue', False, 'enum', ref='Network.CrossOriginOpenerPolicyValue'),
        FieldMeta('reporting_endpoint', 'reportingEndpoint', True, 'primitive'),
        FieldMeta('report_only_reporting_endpoint', 'reportOnlyReportingEndpoint', True, 'primitive'),
    )


@register("Network.CrossOriginEmbedderPolicyValue")
class CrossOriginEmbedderPolicyValue(str, Enum):
    NONE = 'None'
    CREDENTIALLESS = 'Credentialless'
    REQUIRECORP = 'RequireCorp'


@register("Network.CrossOriginEmbedderPolicyStatus")
@dataclass
class CrossOriginEmbedderPolicyStatus(DataType):
    value: CrossOriginEmbedderPolicyValue
    report_only_value: CrossOriginEmbedderPolicyValue
    reporting_endpoint: Optional[str] = None
    report_only_reporting_endpoint: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('value', 'value', False, 'enum', ref='Network.CrossOriginEmbedderPolicyValue'),
        FieldMeta('report_only_value', 'reportOnlyValue', False, 'enum', ref='Network.CrossOriginEmbedderPolicyValue'),
        FieldMeta('reporting_endpoint', 'reportingEndpoint', True, 'primitive'),
        FieldMeta('report_only_reporting_endpoint', 'reportOnlyReportingEndpoint', True, 'primitive'),
    )


@register("Network.ContentSecurityPolicySource")
class ContentSecurityPolicySource(str, Enum):
    HTTP = 'HTTP'
    META = 'Meta'


@register("Network.ContentSecurityPolicyStatus")
@dataclass
class ContentSecurityPolicyStatus(DataType):
    effective_directives: str
    is_enforced: bool
    source: ContentSecurityPolicySource
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('effective_directives', 'effectiveDirectives', False, 'primitive'),
        FieldMeta('is_enforced', 'isEnforced', False, 'primitive'),
        FieldMeta('source', 'source', False, 'enum', ref='Network.ContentSecurityPolicySource'),
    )


@register("Network.SecurityIsolationStatus")
@dataclass
class SecurityIsolationStatus(DataType):
    coop: Optional[CrossOriginOpenerPolicyStatus] = None
    coep: Optional[CrossOriginEmbedderPolicyStatus] = None
    csp: Optional[List[ContentSecurityPolicyStatus]] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('coop', 'coop', True, 'object', ref='Network.CrossOriginOpenerPolicyStatus'),
        FieldMeta('coep', 'coep', True, 'object', ref='Network.CrossOriginEmbedderPolicyStatus'),
        FieldMeta('csp', 'csp', True, 'array', inner=FieldMeta('', '', False, 'object', ref='Network.ContentSecurityPolicyStatus')),
    )


@register("Network.ReportStatus")
class ReportStatus(str, Enum):
    """The status of a Reporting API report."""
    QUEUED = 'Queued'
    PENDING = 'Pending'
    MARKEDFORREMOVAL = 'MarkedForRemoval'
    SUCCESS = 'Success'


type ReportId = str


@register("Network.ReportingApiReport")
@dataclass
class ReportingApiReport(DataType):
    """An object representing a report generated by the Reporting API."""
    id: ReportId
    initiator_url: str
    destination: str
    type_: str
    timestamp: TimeSinceEpoch
    depth: int
    completed_attempts: int
    body: Dict[str, Any]
    status: ReportStatus
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('id', 'id', False, 'primitive'),
        FieldMeta('initiator_url', 'initiatorUrl', False, 'primitive'),
        FieldMeta('destination', 'destination', False, 'primitive'),
        FieldMeta('type_', 'type', False, 'primitive'),
        FieldMeta('timestamp', 'timestamp', False, 'primitive'),
        FieldMeta('depth', 'depth', False, 'primitive'),
        FieldMeta('completed_attempts', 'completedAttempts', False, 'primitive'),
        FieldMeta('body', 'body', False, 'primitive'),
        FieldMeta('status', 'status', False, 'enum', ref='Network.ReportStatus'),
    )


@register("Network.ReportingApiEndpoint")
@dataclass
class ReportingApiEndpoint(DataType):
    url: str
    group_name: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('url', 'url', False, 'primitive'),
        FieldMeta('group_name', 'groupName', False, 'primitive'),
    )


@register("Network.LoadNetworkResourcePageResult")
@dataclass
class LoadNetworkResourcePageResult(DataType):
    """An object providing the result of a network resource load."""
    success: bool
    net_error: Optional[float] = None
    net_error_name: Optional[str] = None
    http_status_code: Optional[float] = None
    stream: Optional[IO_StreamHandle] = None
    headers: Optional[Headers] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('success', 'success', False, 'primitive'),
        FieldMeta('net_error', 'netError', True, 'primitive'),
        FieldMeta('net_error_name', 'netErrorName', True, 'primitive'),
        FieldMeta('http_status_code', 'httpStatusCode', True, 'primitive'),
        FieldMeta('stream', 'stream', True, 'primitive'),
        FieldMeta('headers', 'headers', True, 'primitive'),
    )


@register("Network.LoadNetworkResourceOptions")
@dataclass
class LoadNetworkResourceOptions(DataType):
    """
    An options object that may be extended later to better support CORS,
    CORB and streaming.
    """
    disable_cache: bool
    include_credentials: bool
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('disable_cache', 'disableCache', False, 'primitive'),
        FieldMeta('include_credentials', 'includeCredentials', False, 'primitive'),
    )

__all__ = ["AlternateProtocolUsage", "AssociatedCookie", "AuthChallenge", "AuthChallengeResponse", "BlockPattern", "BlockedReason", "BlockedSetCookieWithReason", "CachedResource", "CertificateTransparencyCompliance", "ClientSecurityState", "ConnectTiming", "ConnectionType", "ContentEncoding", "ContentSecurityPolicySource", "ContentSecurityPolicyStatus", "Cookie", "CookieBlockedReason", "CookieExemptionReason", "CookieParam", "CookiePartitionKey", "CookiePriority", "CookieSameSite", "CookieSourceScheme", "CorsError", "CorsErrorStatus", "CrossOriginEmbedderPolicyStatus", "CrossOriginEmbedderPolicyValue", "CrossOriginOpenerPolicyStatus", "CrossOriginOpenerPolicyValue", "DirectSocketDnsQueryType", "DirectTCPSocketOptions", "DirectUDPMessage", "DirectUDPSocketOptions", "ErrorReason", "ExemptedSetCookieWithReason", "Headers", "IPAddressSpace", "Initiator", "InterceptionId", "InterceptionStage", "LoadNetworkResourceOptions", "LoadNetworkResourcePageResult", "LoaderId", "MonotonicTime", "NetworkConditions", "PostDataEntry", "PrivateNetworkRequestPolicy", "ReportId", "ReportStatus", "ReportingApiEndpoint", "ReportingApiReport", "Request", "RequestId", "RequestPattern", "ResourcePriority", "ResourceTiming", "ResourceType", "Response", "SecurityDetails", "SecurityIsolationStatus", "ServiceWorkerResponseSource", "ServiceWorkerRouterInfo", "ServiceWorkerRouterSource", "SetCookieBlockedReason", "SignedCertificateTimestamp", "SignedExchangeError", "SignedExchangeErrorField", "SignedExchangeHeader", "SignedExchangeInfo", "SignedExchangeSignature", "TimeSinceEpoch", "TrustTokenOperationType", "TrustTokenParams", "WebSocketFrame", "WebSocketRequest", "WebSocketResponse"]
