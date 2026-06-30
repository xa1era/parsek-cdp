"""Events for the Network domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import FieldMeta
from ..mixins.event import Event, register_event

if TYPE_CHECKING:
    from .types import (
        AssociatedCookie,
        AuthChallenge,
        BlockedReason,
        BlockedSetCookieWithReason,
        ClientSecurityState,
        ConnectTiming,
        CookiePartitionKey,
        CorsErrorStatus,
        DirectTCPSocketOptions,
        DirectUDPMessage,
        DirectUDPSocketOptions,
        ErrorReason,
        ExemptedSetCookieWithReason,
        Headers,
        IPAddressSpace,
        Initiator,
        InterceptionId,
        LoaderId,
        MonotonicTime,
        ReportingApiEndpoint,
        ReportingApiReport,
        Request,
        RequestId,
        ResourcePriority,
        ResourceType,
        Response,
        SignedExchangeInfo,
        TimeSinceEpoch,
        TrustTokenOperationType,
        WebSocketFrame,
        WebSocketRequest,
        WebSocketResponse,
    )
    from ..page.types import FrameId as Page_FrameId

@register_event("Network.dataReceived")
@dataclass
class DataReceived(Event):
    """Fired when data chunk was received over the network."""
    request_id: RequestId
    timestamp: MonotonicTime
    data_length: int
    encoded_data_length: int
    data: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('request_id', 'requestId', False, 'primitive'),
        FieldMeta('timestamp', 'timestamp', False, 'primitive'),
        FieldMeta('data_length', 'dataLength', False, 'primitive'),
        FieldMeta('encoded_data_length', 'encodedDataLength', False, 'primitive'),
        FieldMeta('data', 'data', True, 'primitive'),
    )


@register_event("Network.eventSourceMessageReceived")
@dataclass
class EventSourceMessageReceived(Event):
    """Fired when EventSource message is received."""
    request_id: RequestId
    timestamp: MonotonicTime
    event_name: str
    event_id: str
    data: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('request_id', 'requestId', False, 'primitive'),
        FieldMeta('timestamp', 'timestamp', False, 'primitive'),
        FieldMeta('event_name', 'eventName', False, 'primitive'),
        FieldMeta('event_id', 'eventId', False, 'primitive'),
        FieldMeta('data', 'data', False, 'primitive'),
    )


@register_event("Network.loadingFailed")
@dataclass
class LoadingFailed(Event):
    """Fired when HTTP request has failed to load."""
    request_id: RequestId
    timestamp: MonotonicTime
    type_: ResourceType
    error_text: str
    canceled: Optional[bool] = None
    blocked_reason: Optional[BlockedReason] = None
    cors_error_status: Optional[CorsErrorStatus] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('request_id', 'requestId', False, 'primitive'),
        FieldMeta('timestamp', 'timestamp', False, 'primitive'),
        FieldMeta('type_', 'type', False, 'enum', ref='Network.ResourceType'),
        FieldMeta('error_text', 'errorText', False, 'primitive'),
        FieldMeta('canceled', 'canceled', True, 'primitive'),
        FieldMeta('blocked_reason', 'blockedReason', True, 'enum', ref='Network.BlockedReason'),
        FieldMeta('cors_error_status', 'corsErrorStatus', True, 'object', ref='Network.CorsErrorStatus'),
    )


@register_event("Network.loadingFinished")
@dataclass
class LoadingFinished(Event):
    """Fired when HTTP request has finished loading."""
    request_id: RequestId
    timestamp: MonotonicTime
    encoded_data_length: float
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('request_id', 'requestId', False, 'primitive'),
        FieldMeta('timestamp', 'timestamp', False, 'primitive'),
        FieldMeta('encoded_data_length', 'encodedDataLength', False, 'primitive'),
    )


@register_event("Network.requestIntercepted")
@dataclass
class RequestIntercepted(Event):
    """
    Details of an intercepted HTTP request, which must be either allowed, blocked, modified or
    mocked.
    Deprecated, use Fetch.requestPaused instead.
    """
    interception_id: InterceptionId
    request: Request
    frame_id: Page_FrameId
    resource_type: ResourceType
    is_navigation_request: bool
    is_download: Optional[bool] = None
    redirect_url: Optional[str] = None
    auth_challenge: Optional[AuthChallenge] = None
    response_error_reason: Optional[ErrorReason] = None
    response_status_code: Optional[int] = None
    response_headers: Optional[Headers] = None
    request_id: Optional[RequestId] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('interception_id', 'interceptionId', False, 'primitive'),
        FieldMeta('request', 'request', False, 'object', ref='Network.Request'),
        FieldMeta('frame_id', 'frameId', False, 'primitive'),
        FieldMeta('resource_type', 'resourceType', False, 'enum', ref='Network.ResourceType'),
        FieldMeta('is_navigation_request', 'isNavigationRequest', False, 'primitive'),
        FieldMeta('is_download', 'isDownload', True, 'primitive'),
        FieldMeta('redirect_url', 'redirectUrl', True, 'primitive'),
        FieldMeta('auth_challenge', 'authChallenge', True, 'object', ref='Network.AuthChallenge'),
        FieldMeta('response_error_reason', 'responseErrorReason', True, 'enum', ref='Network.ErrorReason'),
        FieldMeta('response_status_code', 'responseStatusCode', True, 'primitive'),
        FieldMeta('response_headers', 'responseHeaders', True, 'primitive'),
        FieldMeta('request_id', 'requestId', True, 'primitive'),
    )


@register_event("Network.requestServedFromCache")
@dataclass
class RequestServedFromCache(Event):
    """Fired if request ended up loading from cache."""
    request_id: RequestId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('request_id', 'requestId', False, 'primitive'),
    )


@register_event("Network.requestWillBeSent")
@dataclass
class RequestWillBeSent(Event):
    """Fired when page is about to send HTTP request."""
    request_id: RequestId
    loader_id: LoaderId
    document_url: str
    request: Request
    timestamp: MonotonicTime
    wall_time: TimeSinceEpoch
    initiator: Initiator
    redirect_has_extra_info: bool
    redirect_response: Optional[Response] = None
    type_: Optional[ResourceType] = None
    frame_id: Optional[Page_FrameId] = None
    has_user_gesture: Optional[bool] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('request_id', 'requestId', False, 'primitive'),
        FieldMeta('loader_id', 'loaderId', False, 'primitive'),
        FieldMeta('document_url', 'documentURL', False, 'primitive'),
        FieldMeta('request', 'request', False, 'object', ref='Network.Request'),
        FieldMeta('timestamp', 'timestamp', False, 'primitive'),
        FieldMeta('wall_time', 'wallTime', False, 'primitive'),
        FieldMeta('initiator', 'initiator', False, 'object', ref='Network.Initiator'),
        FieldMeta('redirect_has_extra_info', 'redirectHasExtraInfo', False, 'primitive'),
        FieldMeta('redirect_response', 'redirectResponse', True, 'object', ref='Network.Response'),
        FieldMeta('type_', 'type', True, 'enum', ref='Network.ResourceType'),
        FieldMeta('frame_id', 'frameId', True, 'primitive'),
        FieldMeta('has_user_gesture', 'hasUserGesture', True, 'primitive'),
    )


@register_event("Network.resourceChangedPriority")
@dataclass
class ResourceChangedPriority(Event):
    """Fired when resource loading priority is changed"""
    request_id: RequestId
    new_priority: ResourcePriority
    timestamp: MonotonicTime
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('request_id', 'requestId', False, 'primitive'),
        FieldMeta('new_priority', 'newPriority', False, 'enum', ref='Network.ResourcePriority'),
        FieldMeta('timestamp', 'timestamp', False, 'primitive'),
    )


@register_event("Network.signedExchangeReceived")
@dataclass
class SignedExchangeReceived(Event):
    """Fired when a signed exchange was received over the network"""
    request_id: RequestId
    info: SignedExchangeInfo
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('request_id', 'requestId', False, 'primitive'),
        FieldMeta('info', 'info', False, 'object', ref='Network.SignedExchangeInfo'),
    )


@register_event("Network.responseReceived")
@dataclass
class ResponseReceived(Event):
    """Fired when HTTP response is available."""
    request_id: RequestId
    loader_id: LoaderId
    timestamp: MonotonicTime
    type_: ResourceType
    response: Response
    has_extra_info: bool
    frame_id: Optional[Page_FrameId] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('request_id', 'requestId', False, 'primitive'),
        FieldMeta('loader_id', 'loaderId', False, 'primitive'),
        FieldMeta('timestamp', 'timestamp', False, 'primitive'),
        FieldMeta('type_', 'type', False, 'enum', ref='Network.ResourceType'),
        FieldMeta('response', 'response', False, 'object', ref='Network.Response'),
        FieldMeta('has_extra_info', 'hasExtraInfo', False, 'primitive'),
        FieldMeta('frame_id', 'frameId', True, 'primitive'),
    )


@register_event("Network.webSocketClosed")
@dataclass
class WebSocketClosed(Event):
    """Fired when WebSocket is closed."""
    request_id: RequestId
    timestamp: MonotonicTime
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('request_id', 'requestId', False, 'primitive'),
        FieldMeta('timestamp', 'timestamp', False, 'primitive'),
    )


@register_event("Network.webSocketCreated")
@dataclass
class WebSocketCreated(Event):
    """Fired upon WebSocket creation."""
    request_id: RequestId
    url: str
    initiator: Optional[Initiator] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('request_id', 'requestId', False, 'primitive'),
        FieldMeta('url', 'url', False, 'primitive'),
        FieldMeta('initiator', 'initiator', True, 'object', ref='Network.Initiator'),
    )


@register_event("Network.webSocketFrameError")
@dataclass
class WebSocketFrameError(Event):
    """Fired when WebSocket message error occurs."""
    request_id: RequestId
    timestamp: MonotonicTime
    error_message: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('request_id', 'requestId', False, 'primitive'),
        FieldMeta('timestamp', 'timestamp', False, 'primitive'),
        FieldMeta('error_message', 'errorMessage', False, 'primitive'),
    )


@register_event("Network.webSocketFrameReceived")
@dataclass
class WebSocketFrameReceived(Event):
    """Fired when WebSocket message is received."""
    request_id: RequestId
    timestamp: MonotonicTime
    response: WebSocketFrame
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('request_id', 'requestId', False, 'primitive'),
        FieldMeta('timestamp', 'timestamp', False, 'primitive'),
        FieldMeta('response', 'response', False, 'object', ref='Network.WebSocketFrame'),
    )


@register_event("Network.webSocketFrameSent")
@dataclass
class WebSocketFrameSent(Event):
    """Fired when WebSocket message is sent."""
    request_id: RequestId
    timestamp: MonotonicTime
    response: WebSocketFrame
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('request_id', 'requestId', False, 'primitive'),
        FieldMeta('timestamp', 'timestamp', False, 'primitive'),
        FieldMeta('response', 'response', False, 'object', ref='Network.WebSocketFrame'),
    )


@register_event("Network.webSocketHandshakeResponseReceived")
@dataclass
class WebSocketHandshakeResponseReceived(Event):
    """Fired when WebSocket handshake response becomes available."""
    request_id: RequestId
    timestamp: MonotonicTime
    response: WebSocketResponse
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('request_id', 'requestId', False, 'primitive'),
        FieldMeta('timestamp', 'timestamp', False, 'primitive'),
        FieldMeta('response', 'response', False, 'object', ref='Network.WebSocketResponse'),
    )


@register_event("Network.webSocketWillSendHandshakeRequest")
@dataclass
class WebSocketWillSendHandshakeRequest(Event):
    """Fired when WebSocket is about to initiate handshake."""
    request_id: RequestId
    timestamp: MonotonicTime
    wall_time: TimeSinceEpoch
    request: WebSocketRequest
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('request_id', 'requestId', False, 'primitive'),
        FieldMeta('timestamp', 'timestamp', False, 'primitive'),
        FieldMeta('wall_time', 'wallTime', False, 'primitive'),
        FieldMeta('request', 'request', False, 'object', ref='Network.WebSocketRequest'),
    )


@register_event("Network.webTransportCreated")
@dataclass
class WebTransportCreated(Event):
    """Fired upon WebTransport creation."""
    transport_id: RequestId
    url: str
    timestamp: MonotonicTime
    initiator: Optional[Initiator] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('transport_id', 'transportId', False, 'primitive'),
        FieldMeta('url', 'url', False, 'primitive'),
        FieldMeta('timestamp', 'timestamp', False, 'primitive'),
        FieldMeta('initiator', 'initiator', True, 'object', ref='Network.Initiator'),
    )


@register_event("Network.webTransportConnectionEstablished")
@dataclass
class WebTransportConnectionEstablished(Event):
    """Fired when WebTransport handshake is finished."""
    transport_id: RequestId
    timestamp: MonotonicTime
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('transport_id', 'transportId', False, 'primitive'),
        FieldMeta('timestamp', 'timestamp', False, 'primitive'),
    )


@register_event("Network.webTransportClosed")
@dataclass
class WebTransportClosed(Event):
    """Fired when WebTransport is disposed."""
    transport_id: RequestId
    timestamp: MonotonicTime
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('transport_id', 'transportId', False, 'primitive'),
        FieldMeta('timestamp', 'timestamp', False, 'primitive'),
    )


@register_event("Network.directTCPSocketCreated")
@dataclass
class DirectTCPSocketCreated(Event):
    """Fired upon direct_socket.TCPSocket creation."""
    identifier: RequestId
    remote_addr: str
    remote_port: int
    options: DirectTCPSocketOptions
    timestamp: MonotonicTime
    initiator: Optional[Initiator] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('identifier', 'identifier', False, 'primitive'),
        FieldMeta('remote_addr', 'remoteAddr', False, 'primitive'),
        FieldMeta('remote_port', 'remotePort', False, 'primitive'),
        FieldMeta('options', 'options', False, 'object', ref='Network.DirectTCPSocketOptions'),
        FieldMeta('timestamp', 'timestamp', False, 'primitive'),
        FieldMeta('initiator', 'initiator', True, 'object', ref='Network.Initiator'),
    )


@register_event("Network.directTCPSocketOpened")
@dataclass
class DirectTCPSocketOpened(Event):
    """Fired when direct_socket.TCPSocket connection is opened."""
    identifier: RequestId
    remote_addr: str
    remote_port: int
    timestamp: MonotonicTime
    local_addr: Optional[str] = None
    local_port: Optional[int] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('identifier', 'identifier', False, 'primitive'),
        FieldMeta('remote_addr', 'remoteAddr', False, 'primitive'),
        FieldMeta('remote_port', 'remotePort', False, 'primitive'),
        FieldMeta('timestamp', 'timestamp', False, 'primitive'),
        FieldMeta('local_addr', 'localAddr', True, 'primitive'),
        FieldMeta('local_port', 'localPort', True, 'primitive'),
    )


@register_event("Network.directTCPSocketAborted")
@dataclass
class DirectTCPSocketAborted(Event):
    """Fired when direct_socket.TCPSocket is aborted."""
    identifier: RequestId
    error_message: str
    timestamp: MonotonicTime
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('identifier', 'identifier', False, 'primitive'),
        FieldMeta('error_message', 'errorMessage', False, 'primitive'),
        FieldMeta('timestamp', 'timestamp', False, 'primitive'),
    )


@register_event("Network.directTCPSocketClosed")
@dataclass
class DirectTCPSocketClosed(Event):
    """Fired when direct_socket.TCPSocket is closed."""
    identifier: RequestId
    timestamp: MonotonicTime
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('identifier', 'identifier', False, 'primitive'),
        FieldMeta('timestamp', 'timestamp', False, 'primitive'),
    )


@register_event("Network.directTCPSocketChunkSent")
@dataclass
class DirectTCPSocketChunkSent(Event):
    """Fired when data is sent to tcp direct socket stream."""
    identifier: RequestId
    data: str
    timestamp: MonotonicTime
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('identifier', 'identifier', False, 'primitive'),
        FieldMeta('data', 'data', False, 'primitive'),
        FieldMeta('timestamp', 'timestamp', False, 'primitive'),
    )


@register_event("Network.directTCPSocketChunkReceived")
@dataclass
class DirectTCPSocketChunkReceived(Event):
    """Fired when data is received from tcp direct socket stream."""
    identifier: RequestId
    data: str
    timestamp: MonotonicTime
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('identifier', 'identifier', False, 'primitive'),
        FieldMeta('data', 'data', False, 'primitive'),
        FieldMeta('timestamp', 'timestamp', False, 'primitive'),
    )


@register_event("Network.directUDPSocketJoinedMulticastGroup")
@dataclass
class DirectUDPSocketJoinedMulticastGroup(Event):
    identifier: RequestId
    ip_address: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('identifier', 'identifier', False, 'primitive'),
        FieldMeta('ip_address', 'IPAddress', False, 'primitive'),
    )


@register_event("Network.directUDPSocketLeftMulticastGroup")
@dataclass
class DirectUDPSocketLeftMulticastGroup(Event):
    identifier: RequestId
    ip_address: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('identifier', 'identifier', False, 'primitive'),
        FieldMeta('ip_address', 'IPAddress', False, 'primitive'),
    )


@register_event("Network.directUDPSocketCreated")
@dataclass
class DirectUDPSocketCreated(Event):
    """Fired upon direct_socket.UDPSocket creation."""
    identifier: RequestId
    options: DirectUDPSocketOptions
    timestamp: MonotonicTime
    initiator: Optional[Initiator] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('identifier', 'identifier', False, 'primitive'),
        FieldMeta('options', 'options', False, 'object', ref='Network.DirectUDPSocketOptions'),
        FieldMeta('timestamp', 'timestamp', False, 'primitive'),
        FieldMeta('initiator', 'initiator', True, 'object', ref='Network.Initiator'),
    )


@register_event("Network.directUDPSocketOpened")
@dataclass
class DirectUDPSocketOpened(Event):
    """Fired when direct_socket.UDPSocket connection is opened."""
    identifier: RequestId
    local_addr: str
    local_port: int
    timestamp: MonotonicTime
    remote_addr: Optional[str] = None
    remote_port: Optional[int] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('identifier', 'identifier', False, 'primitive'),
        FieldMeta('local_addr', 'localAddr', False, 'primitive'),
        FieldMeta('local_port', 'localPort', False, 'primitive'),
        FieldMeta('timestamp', 'timestamp', False, 'primitive'),
        FieldMeta('remote_addr', 'remoteAddr', True, 'primitive'),
        FieldMeta('remote_port', 'remotePort', True, 'primitive'),
    )


@register_event("Network.directUDPSocketAborted")
@dataclass
class DirectUDPSocketAborted(Event):
    """Fired when direct_socket.UDPSocket is aborted."""
    identifier: RequestId
    error_message: str
    timestamp: MonotonicTime
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('identifier', 'identifier', False, 'primitive'),
        FieldMeta('error_message', 'errorMessage', False, 'primitive'),
        FieldMeta('timestamp', 'timestamp', False, 'primitive'),
    )


@register_event("Network.directUDPSocketClosed")
@dataclass
class DirectUDPSocketClosed(Event):
    """Fired when direct_socket.UDPSocket is closed."""
    identifier: RequestId
    timestamp: MonotonicTime
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('identifier', 'identifier', False, 'primitive'),
        FieldMeta('timestamp', 'timestamp', False, 'primitive'),
    )


@register_event("Network.directUDPSocketChunkSent")
@dataclass
class DirectUDPSocketChunkSent(Event):
    """Fired when message is sent to udp direct socket stream."""
    identifier: RequestId
    message: DirectUDPMessage
    timestamp: MonotonicTime
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('identifier', 'identifier', False, 'primitive'),
        FieldMeta('message', 'message', False, 'object', ref='Network.DirectUDPMessage'),
        FieldMeta('timestamp', 'timestamp', False, 'primitive'),
    )


@register_event("Network.directUDPSocketChunkReceived")
@dataclass
class DirectUDPSocketChunkReceived(Event):
    """Fired when message is received from udp direct socket stream."""
    identifier: RequestId
    message: DirectUDPMessage
    timestamp: MonotonicTime
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('identifier', 'identifier', False, 'primitive'),
        FieldMeta('message', 'message', False, 'object', ref='Network.DirectUDPMessage'),
        FieldMeta('timestamp', 'timestamp', False, 'primitive'),
    )


@register_event("Network.requestWillBeSentExtraInfo")
@dataclass
class RequestWillBeSentExtraInfo(Event):
    """
    Fired when additional information about a requestWillBeSent event is available from the
    network stack. Not every requestWillBeSent event will have an additional
    requestWillBeSentExtraInfo fired for it, and there is no guarantee whether requestWillBeSent
    or requestWillBeSentExtraInfo will be fired first for the same request.
    """
    request_id: RequestId
    associated_cookies: List[AssociatedCookie]
    headers: Headers
    connect_timing: ConnectTiming
    client_security_state: Optional[ClientSecurityState] = None
    site_has_cookie_in_other_partition: Optional[bool] = None
    applied_network_conditions_id: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('request_id', 'requestId', False, 'primitive'),
        FieldMeta('associated_cookies', 'associatedCookies', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Network.AssociatedCookie')),
        FieldMeta('headers', 'headers', False, 'primitive'),
        FieldMeta('connect_timing', 'connectTiming', False, 'object', ref='Network.ConnectTiming'),
        FieldMeta('client_security_state', 'clientSecurityState', True, 'object', ref='Network.ClientSecurityState'),
        FieldMeta('site_has_cookie_in_other_partition', 'siteHasCookieInOtherPartition', True, 'primitive'),
        FieldMeta('applied_network_conditions_id', 'appliedNetworkConditionsId', True, 'primitive'),
    )


@register_event("Network.responseReceivedExtraInfo")
@dataclass
class ResponseReceivedExtraInfo(Event):
    """
    Fired when additional information about a responseReceived event is available from the network
    stack. Not every responseReceived event will have an additional responseReceivedExtraInfo for
    it, and responseReceivedExtraInfo may be fired before or after responseReceived.
    """
    request_id: RequestId
    blocked_cookies: List[BlockedSetCookieWithReason]
    headers: Headers
    resource_ip_address_space: IPAddressSpace
    status_code: int
    headers_text: Optional[str] = None
    cookie_partition_key: Optional[CookiePartitionKey] = None
    cookie_partition_key_opaque: Optional[bool] = None
    exempted_cookies: Optional[List[ExemptedSetCookieWithReason]] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('request_id', 'requestId', False, 'primitive'),
        FieldMeta('blocked_cookies', 'blockedCookies', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Network.BlockedSetCookieWithReason')),
        FieldMeta('headers', 'headers', False, 'primitive'),
        FieldMeta('resource_ip_address_space', 'resourceIPAddressSpace', False, 'enum', ref='Network.IPAddressSpace'),
        FieldMeta('status_code', 'statusCode', False, 'primitive'),
        FieldMeta('headers_text', 'headersText', True, 'primitive'),
        FieldMeta('cookie_partition_key', 'cookiePartitionKey', True, 'object', ref='Network.CookiePartitionKey'),
        FieldMeta('cookie_partition_key_opaque', 'cookiePartitionKeyOpaque', True, 'primitive'),
        FieldMeta('exempted_cookies', 'exemptedCookies', True, 'array', inner=FieldMeta('', '', False, 'object', ref='Network.ExemptedSetCookieWithReason')),
    )


@register_event("Network.responseReceivedEarlyHints")
@dataclass
class ResponseReceivedEarlyHints(Event):
    """
    Fired when 103 Early Hints headers is received in addition to the common response.
    Not every responseReceived event will have an responseReceivedEarlyHints fired.
    Only one responseReceivedEarlyHints may be fired for eached responseReceived event.
    """
    request_id: RequestId
    headers: Headers
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('request_id', 'requestId', False, 'primitive'),
        FieldMeta('headers', 'headers', False, 'primitive'),
    )


@register_event("Network.trustTokenOperationDone")
@dataclass
class TrustTokenOperationDone(Event):
    """
    Fired exactly once for each Trust Token operation. Depending on
    the type of the operation and whether the operation succeeded or
    failed, the event is fired before the corresponding request was sent
    or after the response was received.
    """
    status: Literal['Ok', 'InvalidArgument', 'MissingIssuerKeys', 'FailedPrecondition', 'ResourceExhausted', 'AlreadyExists', 'ResourceLimited', 'Unauthorized', 'BadResponse', 'InternalError', 'UnknownError', 'FulfilledLocally', 'SiteIssuerLimit']
    type_: TrustTokenOperationType
    request_id: RequestId
    top_level_origin: Optional[str] = None
    issuer_origin: Optional[str] = None
    issued_token_count: Optional[int] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('status', 'status', False, 'primitive'),
        FieldMeta('type_', 'type', False, 'enum', ref='Network.TrustTokenOperationType'),
        FieldMeta('request_id', 'requestId', False, 'primitive'),
        FieldMeta('top_level_origin', 'topLevelOrigin', True, 'primitive'),
        FieldMeta('issuer_origin', 'issuerOrigin', True, 'primitive'),
        FieldMeta('issued_token_count', 'issuedTokenCount', True, 'primitive'),
    )


@register_event("Network.policyUpdated")
@dataclass
class PolicyUpdated(Event):
    """Fired once security policy has been updated."""
    __FIELDS__: ClassVar[tuple] = ()


@register_event("Network.reportingApiReportAdded")
@dataclass
class ReportingApiReportAdded(Event):
    """
    Is sent whenever a new report is added.
    And after 'enableReportingApi' for all existing reports.
    """
    report: ReportingApiReport
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('report', 'report', False, 'object', ref='Network.ReportingApiReport'),
    )


@register_event("Network.reportingApiReportUpdated")
@dataclass
class ReportingApiReportUpdated(Event):
    report: ReportingApiReport
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('report', 'report', False, 'object', ref='Network.ReportingApiReport'),
    )


@register_event("Network.reportingApiEndpointsChangedForOrigin")
@dataclass
class ReportingApiEndpointsChangedForOrigin(Event):
    origin: str
    endpoints: List[ReportingApiEndpoint]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('origin', 'origin', False, 'primitive'),
        FieldMeta('endpoints', 'endpoints', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Network.ReportingApiEndpoint')),
    )

__all__ = ["DataReceived", "DirectTCPSocketAborted", "DirectTCPSocketChunkReceived", "DirectTCPSocketChunkSent", "DirectTCPSocketClosed", "DirectTCPSocketCreated", "DirectTCPSocketOpened", "DirectUDPSocketAborted", "DirectUDPSocketChunkReceived", "DirectUDPSocketChunkSent", "DirectUDPSocketClosed", "DirectUDPSocketCreated", "DirectUDPSocketJoinedMulticastGroup", "DirectUDPSocketLeftMulticastGroup", "DirectUDPSocketOpened", "EventSourceMessageReceived", "LoadingFailed", "LoadingFinished", "PolicyUpdated", "ReportingApiEndpointsChangedForOrigin", "ReportingApiReportAdded", "ReportingApiReportUpdated", "RequestIntercepted", "RequestServedFromCache", "RequestWillBeSent", "RequestWillBeSentExtraInfo", "ResourceChangedPriority", "ResponseReceived", "ResponseReceivedEarlyHints", "ResponseReceivedExtraInfo", "SignedExchangeReceived", "TrustTokenOperationDone", "WebSocketClosed", "WebSocketCreated", "WebSocketFrameError", "WebSocketFrameReceived", "WebSocketFrameSent", "WebSocketHandshakeResponseReceived", "WebSocketWillSendHandshakeRequest", "WebTransportClosed", "WebTransportConnectionEstablished", "WebTransportCreated"]
