"""Commands for the Network domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode

if TYPE_CHECKING:
    from .types import (
        AuthChallengeResponse,
        BlockPattern,
        ConnectionType,
        ContentEncoding,
        Cookie,
        CookieParam,
        CookiePartitionKey,
        CookiePriority,
        CookieSameSite,
        CookieSourceScheme,
        ErrorReason,
        Headers,
        InterceptionId,
        LoadNetworkResourceOptions,
        LoadNetworkResourcePageResult,
        NetworkConditions,
        RequestId,
        RequestPattern,
        SecurityIsolationStatus,
        TimeSinceEpoch,
    )
    from ..debugger.types import SearchMatch as Debugger_SearchMatch
    from ..emulation.types import UserAgentMetadata as Emulation_UserAgentMetadata
    from ..io.types import StreamHandle as IO_StreamHandle
    from ..page.types import FrameId as Page_FrameId

@dataclass
class CanClearBrowserCacheReturn(DataType):
    """Return value of :meth:`Network.can_clear_browser_cache`."""
    result: bool
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('result', 'result', False, 'primitive'),
    )


@dataclass
class CanClearBrowserCookiesReturn(DataType):
    """Return value of :meth:`Network.can_clear_browser_cookies`."""
    result: bool
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('result', 'result', False, 'primitive'),
    )


@dataclass
class CanEmulateNetworkConditionsReturn(DataType):
    """Return value of :meth:`Network.can_emulate_network_conditions`."""
    result: bool
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('result', 'result', False, 'primitive'),
    )


@dataclass
class EmulateNetworkConditionsByRuleReturn(DataType):
    """Return value of :meth:`Network.emulate_network_conditions_by_rule`."""
    rule_ids: List[str]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('rule_ids', 'ruleIds', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


@dataclass
class GetAllCookiesReturn(DataType):
    """Return value of :meth:`Network.get_all_cookies`."""
    cookies: List[Cookie]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('cookies', 'cookies', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Network.Cookie')),
    )


@dataclass
class GetCertificateReturn(DataType):
    """Return value of :meth:`Network.get_certificate`."""
    table_names: List[str]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('table_names', 'tableNames', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


@dataclass
class GetCookiesReturn(DataType):
    """Return value of :meth:`Network.get_cookies`."""
    cookies: List[Cookie]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('cookies', 'cookies', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Network.Cookie')),
    )


@dataclass
class GetResponseBodyReturn(DataType):
    """Return value of :meth:`Network.get_response_body`."""
    body: str
    base64_encoded: bool
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('body', 'body', False, 'primitive'),
        FieldMeta('base64_encoded', 'base64Encoded', False, 'primitive'),
    )


@dataclass
class GetRequestPostDataReturn(DataType):
    """Return value of :meth:`Network.get_request_post_data`."""
    post_data: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('post_data', 'postData', False, 'primitive'),
    )


@dataclass
class GetResponseBodyForInterceptionReturn(DataType):
    """Return value of :meth:`Network.get_response_body_for_interception`."""
    body: str
    base64_encoded: bool
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('body', 'body', False, 'primitive'),
        FieldMeta('base64_encoded', 'base64Encoded', False, 'primitive'),
    )


@dataclass
class TakeResponseBodyForInterceptionAsStreamReturn(DataType):
    """Return value of :meth:`Network.take_response_body_for_interception_as_stream`."""
    stream: IO_StreamHandle
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('stream', 'stream', False, 'primitive'),
    )


@dataclass
class SearchInResponseBodyReturn(DataType):
    """Return value of :meth:`Network.search_in_response_body`."""
    result: List[Debugger_SearchMatch]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('result', 'result', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Debugger.SearchMatch')),
    )


@dataclass
class SetCookieReturn(DataType):
    """Return value of :meth:`Network.set_cookie`."""
    success: bool
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('success', 'success', False, 'primitive'),
    )


@dataclass
class StreamResourceContentReturn(DataType):
    """Return value of :meth:`Network.stream_resource_content`."""
    buffered_data: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('buffered_data', 'bufferedData', False, 'primitive'),
    )


@dataclass
class GetSecurityIsolationStatusReturn(DataType):
    """Return value of :meth:`Network.get_security_isolation_status`."""
    status: SecurityIsolationStatus
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('status', 'status', False, 'object', ref='Network.SecurityIsolationStatus'),
    )


@dataclass
class LoadNetworkResourceReturn(DataType):
    """Return value of :meth:`Network.load_network_resource`."""
    resource: LoadNetworkResourcePageResult
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('resource', 'resource', False, 'object', ref='Network.LoadNetworkResourcePageResult'),
    )


class Network:
    """Commands of the Network domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def set_accepted_encodings(self, *, encodings: List[ContentEncoding]) -> None:
        """
        Sets a list of content encodings that will be accepted. Empty list means no encoding is accepted.
        :param encodings: List of accepted content encodings.
        """
        _params: Dict[str, Any] = {}
        _params['encodings'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'enum', ref='Network.ContentEncoding')), encodings)
        _result = await self._target.send('Network.setAcceptedEncodings', _params)
        return None

    async def clear_accepted_encodings_override(self) -> None:
        """Clears accepted encodings set by setAcceptedEncodings"""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Network.clearAcceptedEncodingsOverride', _params)
        return None

    async def can_clear_browser_cache(self) -> CanClearBrowserCacheReturn:
        """
        Tells whether clearing browser cache is supported.
        
        .. deprecated::
        """
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Network.canClearBrowserCache', _params)
        return CanClearBrowserCacheReturn.from_json(_result)

    async def can_clear_browser_cookies(self) -> CanClearBrowserCookiesReturn:
        """
        Tells whether clearing browser cookies is supported.
        
        .. deprecated::
        """
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Network.canClearBrowserCookies', _params)
        return CanClearBrowserCookiesReturn.from_json(_result)

    async def can_emulate_network_conditions(self) -> CanEmulateNetworkConditionsReturn:
        """
        Tells whether emulation of network conditions is supported.
        
        .. deprecated::
        """
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Network.canEmulateNetworkConditions', _params)
        return CanEmulateNetworkConditionsReturn.from_json(_result)

    async def clear_browser_cache(self) -> None:
        """Clears browser cache."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Network.clearBrowserCache', _params)
        return None

    async def clear_browser_cookies(self) -> None:
        """Clears browser cookies."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Network.clearBrowserCookies', _params)
        return None

    async def continue_intercepted_request(self, *, interception_id: InterceptionId, error_reason: Optional[ErrorReason] = None, raw_response: Optional[str] = None, url: Optional[str] = None, method: Optional[str] = None, post_data: Optional[str] = None, headers: Optional[Headers] = None, auth_challenge_response: Optional[AuthChallengeResponse] = None) -> None:
        """
        Response to Network.requestIntercepted which either modifies the request to continue with any
        modifications, or blocks it, or completes it with the provided response bytes. If a network
        fetch occurs as a result which encounters a redirect an additional Network.requestIntercepted
        event will be sent with the same InterceptionId.
        Deprecated, use Fetch.continueRequest, Fetch.fulfillRequest and Fetch.failRequest instead.
        
        .. deprecated::
        :param interception_id:
        :param error_reason: If set this causes the request to fail with the given reason. Passing `Aborted` for requests
        marked with `isNavigationRequest` also cancels the navigation. Must not be set in response
        to an authChallenge.
        :param raw_response: If set the requests completes using with the provided base64 encoded raw response, including
        HTTP status line and headers etc... Must not be set in response to an authChallenge. (Encoded as a base64 string when passed over JSON)
        :param url: If set the request url will be modified in a way that's not observable by page. Must not be
        set in response to an authChallenge.
        :param method: If set this allows the request method to be overridden. Must not be set in response to an
        authChallenge.
        :param post_data: If set this allows postData to be set. Must not be set in response to an authChallenge.
        :param headers: If set this allows the request headers to be changed. Must not be set in response to an
        authChallenge.
        :param auth_challenge_response: Response to a requestIntercepted with an authChallenge. Must not be set otherwise.
        """
        _params: Dict[str, Any] = {}
        _params['interceptionId'] = encode(FieldMeta('', '', False, 'primitive'), interception_id)
        if error_reason is not None:
            _params['errorReason'] = encode(FieldMeta('', '', False, 'enum', ref='Network.ErrorReason'), error_reason)
        if raw_response is not None:
            _params['rawResponse'] = encode(FieldMeta('', '', False, 'primitive'), raw_response)
        if url is not None:
            _params['url'] = encode(FieldMeta('', '', False, 'primitive'), url)
        if method is not None:
            _params['method'] = encode(FieldMeta('', '', False, 'primitive'), method)
        if post_data is not None:
            _params['postData'] = encode(FieldMeta('', '', False, 'primitive'), post_data)
        if headers is not None:
            _params['headers'] = encode(FieldMeta('', '', False, 'primitive'), headers)
        if auth_challenge_response is not None:
            _params['authChallengeResponse'] = encode(FieldMeta('', '', False, 'object', ref='Network.AuthChallengeResponse'), auth_challenge_response)
        _result = await self._target.send('Network.continueInterceptedRequest', _params)
        return None

    async def delete_cookies(self, *, name: str, url: Optional[str] = None, domain: Optional[str] = None, path: Optional[str] = None, partition_key: Optional[CookiePartitionKey] = None) -> None:
        """
        Deletes browser cookies with matching name and url or domain/path/partitionKey pair.
        :param name: Name of the cookies to remove.
        :param url: If specified, deletes all the cookies with the given name where domain and path match
        provided URL.
        :param domain: If specified, deletes only cookies with the exact domain.
        :param path: If specified, deletes only cookies with the exact path.
        :param partition_key: If specified, deletes only cookies with the the given name and partitionKey where
        all partition key attributes match the cookie partition key attribute.
        """
        _params: Dict[str, Any] = {}
        _params['name'] = encode(FieldMeta('', '', False, 'primitive'), name)
        if url is not None:
            _params['url'] = encode(FieldMeta('', '', False, 'primitive'), url)
        if domain is not None:
            _params['domain'] = encode(FieldMeta('', '', False, 'primitive'), domain)
        if path is not None:
            _params['path'] = encode(FieldMeta('', '', False, 'primitive'), path)
        if partition_key is not None:
            _params['partitionKey'] = encode(FieldMeta('', '', False, 'object', ref='Network.CookiePartitionKey'), partition_key)
        _result = await self._target.send('Network.deleteCookies', _params)
        return None

    async def disable(self) -> None:
        """Disables network tracking, prevents network events from being sent to the client."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Network.disable', _params)
        return None

    async def emulate_network_conditions(self, *, offline: bool, latency: float, download_throughput: float, upload_throughput: float, connection_type: Optional[ConnectionType] = None, packet_loss: Optional[float] = None, packet_queue_length: Optional[int] = None, packet_reordering: Optional[bool] = None) -> None:
        """
        Activates emulation of network conditions. This command is deprecated in favor of the emulateNetworkConditionsByRule
        and overrideNetworkState commands, which can be used together to the same effect.
        
        .. deprecated::
        :param offline: True to emulate internet disconnection.
        :param latency: Minimum latency from request sent to response headers received (ms).
        :param download_throughput: Maximal aggregated download throughput (bytes/sec). -1 disables download throttling.
        :param upload_throughput: Maximal aggregated upload throughput (bytes/sec).  -1 disables upload throttling.
        :param connection_type: Connection type if known.
        :param packet_loss: WebRTC packet loss (percent, 0-100). 0 disables packet loss emulation, 100 drops all the packets.
        :param packet_queue_length: WebRTC packet queue length (packet). 0 removes any queue length limitations.
        :param packet_reordering: WebRTC packetReordering feature.
        """
        _params: Dict[str, Any] = {}
        _params['offline'] = encode(FieldMeta('', '', False, 'primitive'), offline)
        _params['latency'] = encode(FieldMeta('', '', False, 'primitive'), latency)
        _params['downloadThroughput'] = encode(FieldMeta('', '', False, 'primitive'), download_throughput)
        _params['uploadThroughput'] = encode(FieldMeta('', '', False, 'primitive'), upload_throughput)
        if connection_type is not None:
            _params['connectionType'] = encode(FieldMeta('', '', False, 'enum', ref='Network.ConnectionType'), connection_type)
        if packet_loss is not None:
            _params['packetLoss'] = encode(FieldMeta('', '', False, 'primitive'), packet_loss)
        if packet_queue_length is not None:
            _params['packetQueueLength'] = encode(FieldMeta('', '', False, 'primitive'), packet_queue_length)
        if packet_reordering is not None:
            _params['packetReordering'] = encode(FieldMeta('', '', False, 'primitive'), packet_reordering)
        _result = await self._target.send('Network.emulateNetworkConditions', _params)
        return None

    async def emulate_network_conditions_by_rule(self, *, offline: bool, matched_network_conditions: List[NetworkConditions]) -> EmulateNetworkConditionsByRuleReturn:
        """
        Activates emulation of network conditions for individual requests using URL match patterns. Unlike the deprecated
        Network.emulateNetworkConditions this method does not affect `navigator` state. Use Network.overrideNetworkState to
        explicitly modify `navigator` behavior.
        :param offline: True to emulate internet disconnection.
        :param matched_network_conditions: Configure conditions for matching requests. If multiple entries match a request, the first entry wins.  Global
        conditions can be configured by leaving the urlPattern for the conditions empty. These global conditions are
        also applied for throttling of p2p connections.
        """
        _params: Dict[str, Any] = {}
        _params['offline'] = encode(FieldMeta('', '', False, 'primitive'), offline)
        _params['matchedNetworkConditions'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Network.NetworkConditions')), matched_network_conditions)
        _result = await self._target.send('Network.emulateNetworkConditionsByRule', _params)
        return EmulateNetworkConditionsByRuleReturn.from_json(_result)

    async def override_network_state(self, *, offline: bool, latency: float, download_throughput: float, upload_throughput: float, connection_type: Optional[ConnectionType] = None) -> None:
        """
        Override the state of navigator.onLine and navigator.connection.
        :param offline: True to emulate internet disconnection.
        :param latency: Minimum latency from request sent to response headers received (ms).
        :param download_throughput: Maximal aggregated download throughput (bytes/sec). -1 disables download throttling.
        :param upload_throughput: Maximal aggregated upload throughput (bytes/sec).  -1 disables upload throttling.
        :param connection_type: Connection type if known.
        """
        _params: Dict[str, Any] = {}
        _params['offline'] = encode(FieldMeta('', '', False, 'primitive'), offline)
        _params['latency'] = encode(FieldMeta('', '', False, 'primitive'), latency)
        _params['downloadThroughput'] = encode(FieldMeta('', '', False, 'primitive'), download_throughput)
        _params['uploadThroughput'] = encode(FieldMeta('', '', False, 'primitive'), upload_throughput)
        if connection_type is not None:
            _params['connectionType'] = encode(FieldMeta('', '', False, 'enum', ref='Network.ConnectionType'), connection_type)
        _result = await self._target.send('Network.overrideNetworkState', _params)
        return None

    async def enable(self, *, max_total_buffer_size: Optional[int] = None, max_resource_buffer_size: Optional[int] = None, max_post_data_size: Optional[int] = None, report_direct_socket_traffic: Optional[bool] = None, enable_durable_messages: Optional[bool] = None) -> None:
        """
        Enables network tracking, network events will now be delivered to the client.
        :param max_total_buffer_size: Buffer size in bytes to use when preserving network payloads (XHRs, etc).
        :param max_resource_buffer_size: Per-resource buffer size in bytes to use when preserving network payloads (XHRs, etc).
        :param max_post_data_size: Longest post body size (in bytes) that would be included in requestWillBeSent notification
        :param report_direct_socket_traffic: Whether DirectSocket chunk send/receive events should be reported.
        :param enable_durable_messages: Enable storing response bodies outside of renderer, so that these survive
        a cross-process navigation. Requires maxTotalBufferSize to be set.
        Currently defaults to false.
        """
        _params: Dict[str, Any] = {}
        if max_total_buffer_size is not None:
            _params['maxTotalBufferSize'] = encode(FieldMeta('', '', False, 'primitive'), max_total_buffer_size)
        if max_resource_buffer_size is not None:
            _params['maxResourceBufferSize'] = encode(FieldMeta('', '', False, 'primitive'), max_resource_buffer_size)
        if max_post_data_size is not None:
            _params['maxPostDataSize'] = encode(FieldMeta('', '', False, 'primitive'), max_post_data_size)
        if report_direct_socket_traffic is not None:
            _params['reportDirectSocketTraffic'] = encode(FieldMeta('', '', False, 'primitive'), report_direct_socket_traffic)
        if enable_durable_messages is not None:
            _params['enableDurableMessages'] = encode(FieldMeta('', '', False, 'primitive'), enable_durable_messages)
        _result = await self._target.send('Network.enable', _params)
        return None

    async def get_all_cookies(self) -> GetAllCookiesReturn:
        """
        Returns all browser cookies. Depending on the backend support, will return detailed cookie
        information in the `cookies` field.
        Deprecated. Use Storage.getCookies instead.
        
        .. deprecated::
        """
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Network.getAllCookies', _params)
        return GetAllCookiesReturn.from_json(_result)

    async def get_certificate(self, *, origin: str) -> GetCertificateReturn:
        """
        Returns the DER-encoded certificate.
        :param origin: Origin to get certificate for.
        """
        _params: Dict[str, Any] = {}
        _params['origin'] = encode(FieldMeta('', '', False, 'primitive'), origin)
        _result = await self._target.send('Network.getCertificate', _params)
        return GetCertificateReturn.from_json(_result)

    async def get_cookies(self, *, urls: Optional[List[str]] = None) -> GetCookiesReturn:
        """
        Returns all browser cookies for the current URL. Depending on the backend support, will return
        detailed cookie information in the `cookies` field.
        :param urls: The list of URLs for which applicable cookies will be fetched.
        If not specified, it's assumed to be set to the list containing
        the URLs of the page and all of its subframes.
        """
        _params: Dict[str, Any] = {}
        if urls is not None:
            _params['urls'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'primitive')), urls)
        _result = await self._target.send('Network.getCookies', _params)
        return GetCookiesReturn.from_json(_result)

    async def get_response_body(self, *, request_id: RequestId) -> GetResponseBodyReturn:
        """
        Returns content served for the given request.
        :param request_id: Identifier of the network request to get content for.
        """
        _params: Dict[str, Any] = {}
        _params['requestId'] = encode(FieldMeta('', '', False, 'primitive'), request_id)
        _result = await self._target.send('Network.getResponseBody', _params)
        return GetResponseBodyReturn.from_json(_result)

    async def get_request_post_data(self, *, request_id: RequestId) -> GetRequestPostDataReturn:
        """
        Returns post data sent with the request. Returns an error when no data was sent with the request.
        :param request_id: Identifier of the network request to get content for.
        """
        _params: Dict[str, Any] = {}
        _params['requestId'] = encode(FieldMeta('', '', False, 'primitive'), request_id)
        _result = await self._target.send('Network.getRequestPostData', _params)
        return GetRequestPostDataReturn.from_json(_result)

    async def get_response_body_for_interception(self, *, interception_id: InterceptionId) -> GetResponseBodyForInterceptionReturn:
        """
        Returns content served for the given currently intercepted request.
        :param interception_id: Identifier for the intercepted request to get body for.
        """
        _params: Dict[str, Any] = {}
        _params['interceptionId'] = encode(FieldMeta('', '', False, 'primitive'), interception_id)
        _result = await self._target.send('Network.getResponseBodyForInterception', _params)
        return GetResponseBodyForInterceptionReturn.from_json(_result)

    async def take_response_body_for_interception_as_stream(self, *, interception_id: InterceptionId) -> TakeResponseBodyForInterceptionAsStreamReturn:
        """
        Returns a handle to the stream representing the response body. Note that after this command,
        the intercepted request can't be continued as is -- you either need to cancel it or to provide
        the response body. The stream only supports sequential read, IO.read will fail if the position
        is specified.
        :param interception_id:
        """
        _params: Dict[str, Any] = {}
        _params['interceptionId'] = encode(FieldMeta('', '', False, 'primitive'), interception_id)
        _result = await self._target.send('Network.takeResponseBodyForInterceptionAsStream', _params)
        return TakeResponseBodyForInterceptionAsStreamReturn.from_json(_result)

    async def replay_xhr(self, *, request_id: RequestId) -> None:
        """
        This method sends a new XMLHttpRequest which is identical to the original one. The following
        parameters should be identical: method, url, async, request body, extra headers, withCredentials
        attribute, user, password.
        :param request_id: Identifier of XHR to replay.
        """
        _params: Dict[str, Any] = {}
        _params['requestId'] = encode(FieldMeta('', '', False, 'primitive'), request_id)
        _result = await self._target.send('Network.replayXHR', _params)
        return None

    async def search_in_response_body(self, *, request_id: RequestId, query: str, case_sensitive: Optional[bool] = None, is_regex: Optional[bool] = None) -> SearchInResponseBodyReturn:
        """
        Searches for given string in response content.
        :param request_id: Identifier of the network response to search.
        :param query: String to search for.
        :param case_sensitive: If true, search is case sensitive.
        :param is_regex: If true, treats string parameter as regex.
        """
        _params: Dict[str, Any] = {}
        _params['requestId'] = encode(FieldMeta('', '', False, 'primitive'), request_id)
        _params['query'] = encode(FieldMeta('', '', False, 'primitive'), query)
        if case_sensitive is not None:
            _params['caseSensitive'] = encode(FieldMeta('', '', False, 'primitive'), case_sensitive)
        if is_regex is not None:
            _params['isRegex'] = encode(FieldMeta('', '', False, 'primitive'), is_regex)
        _result = await self._target.send('Network.searchInResponseBody', _params)
        return SearchInResponseBodyReturn.from_json(_result)

    async def set_blocked_ur_ls(self, *, url_patterns: Optional[List[BlockPattern]] = None, urls: Optional[List[str]] = None) -> None:
        """
        Blocks URLs from loading.
        :param url_patterns: Patterns to match in the order in which they are given. These patterns
        also take precedence over any wildcard patterns defined in `urls`.
        :param urls: URL patterns to block. Wildcards ('*') are allowed.
        """
        _params: Dict[str, Any] = {}
        if url_patterns is not None:
            _params['urlPatterns'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Network.BlockPattern')), url_patterns)
        if urls is not None:
            _params['urls'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'primitive')), urls)
        _result = await self._target.send('Network.setBlockedURLs', _params)
        return None

    async def set_bypass_service_worker(self, *, bypass: bool) -> None:
        """
        Toggles ignoring of service worker for each request.
        :param bypass: Bypass service worker and load from network.
        """
        _params: Dict[str, Any] = {}
        _params['bypass'] = encode(FieldMeta('', '', False, 'primitive'), bypass)
        _result = await self._target.send('Network.setBypassServiceWorker', _params)
        return None

    async def set_cache_disabled(self, *, cache_disabled: bool) -> None:
        """
        Toggles ignoring cache for each request. If `true`, cache will not be used.
        :param cache_disabled: Cache disabled state.
        """
        _params: Dict[str, Any] = {}
        _params['cacheDisabled'] = encode(FieldMeta('', '', False, 'primitive'), cache_disabled)
        _result = await self._target.send('Network.setCacheDisabled', _params)
        return None

    async def set_cookie(self, *, name: str, value: str, url: Optional[str] = None, domain: Optional[str] = None, path: Optional[str] = None, secure: Optional[bool] = None, http_only: Optional[bool] = None, same_site: Optional[CookieSameSite] = None, expires: Optional[TimeSinceEpoch] = None, priority: Optional[CookiePriority] = None, same_party: Optional[bool] = None, source_scheme: Optional[CookieSourceScheme] = None, source_port: Optional[int] = None, partition_key: Optional[CookiePartitionKey] = None) -> SetCookieReturn:
        """
        Sets a cookie with the given cookie data; may overwrite equivalent cookies if they exist.
        :param name: Cookie name.
        :param value: Cookie value.
        :param url: The request-URI to associate with the setting of the cookie. This value can affect the
        default domain, path, source port, and source scheme values of the created cookie.
        :param domain: Cookie domain.
        :param path: Cookie path.
        :param secure: True if cookie is secure.
        :param http_only: True if cookie is http-only.
        :param same_site: Cookie SameSite type.
        :param expires: Cookie expiration date, session cookie if not set
        :param priority: Cookie Priority type.
        :param same_party: True if cookie is SameParty.
        :param source_scheme: Cookie source scheme type.
        :param source_port: Cookie source port. Valid values are {-1, [1, 65535]}, -1 indicates an unspecified port.
        An unspecified port value allows protocol clients to emulate legacy cookie scope for the port.
        This is a temporary ability and it will be removed in the future.
        :param partition_key: Cookie partition key. If not set, the cookie will be set as not partitioned.
        """
        _params: Dict[str, Any] = {}
        _params['name'] = encode(FieldMeta('', '', False, 'primitive'), name)
        _params['value'] = encode(FieldMeta('', '', False, 'primitive'), value)
        if url is not None:
            _params['url'] = encode(FieldMeta('', '', False, 'primitive'), url)
        if domain is not None:
            _params['domain'] = encode(FieldMeta('', '', False, 'primitive'), domain)
        if path is not None:
            _params['path'] = encode(FieldMeta('', '', False, 'primitive'), path)
        if secure is not None:
            _params['secure'] = encode(FieldMeta('', '', False, 'primitive'), secure)
        if http_only is not None:
            _params['httpOnly'] = encode(FieldMeta('', '', False, 'primitive'), http_only)
        if same_site is not None:
            _params['sameSite'] = encode(FieldMeta('', '', False, 'enum', ref='Network.CookieSameSite'), same_site)
        if expires is not None:
            _params['expires'] = encode(FieldMeta('', '', False, 'primitive'), expires)
        if priority is not None:
            _params['priority'] = encode(FieldMeta('', '', False, 'enum', ref='Network.CookiePriority'), priority)
        if same_party is not None:
            _params['sameParty'] = encode(FieldMeta('', '', False, 'primitive'), same_party)
        if source_scheme is not None:
            _params['sourceScheme'] = encode(FieldMeta('', '', False, 'enum', ref='Network.CookieSourceScheme'), source_scheme)
        if source_port is not None:
            _params['sourcePort'] = encode(FieldMeta('', '', False, 'primitive'), source_port)
        if partition_key is not None:
            _params['partitionKey'] = encode(FieldMeta('', '', False, 'object', ref='Network.CookiePartitionKey'), partition_key)
        _result = await self._target.send('Network.setCookie', _params)
        return SetCookieReturn.from_json(_result)

    async def set_cookies(self, *, cookies: List[CookieParam]) -> None:
        """
        Sets given cookies.
        :param cookies: Cookies to be set.
        """
        _params: Dict[str, Any] = {}
        _params['cookies'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Network.CookieParam')), cookies)
        _result = await self._target.send('Network.setCookies', _params)
        return None

    async def set_extra_http_headers(self, *, headers: Headers) -> None:
        """
        Specifies whether to always send extra HTTP headers with the requests from this page.
        :param headers: Map with extra HTTP headers.
        """
        _params: Dict[str, Any] = {}
        _params['headers'] = encode(FieldMeta('', '', False, 'primitive'), headers)
        _result = await self._target.send('Network.setExtraHTTPHeaders', _params)
        return None

    async def set_attach_debug_stack(self, *, enabled: bool) -> None:
        """
        Specifies whether to attach a page script stack id in requests
        :param enabled: Whether to attach a page script stack for debugging purpose.
        """
        _params: Dict[str, Any] = {}
        _params['enabled'] = encode(FieldMeta('', '', False, 'primitive'), enabled)
        _result = await self._target.send('Network.setAttachDebugStack', _params)
        return None

    async def set_request_interception(self, *, patterns: List[RequestPattern]) -> None:
        """
        Sets the requests to intercept that match the provided patterns and optionally resource types.
        Deprecated, please use Fetch.enable instead.
        
        .. deprecated::
        :param patterns: Requests matching any of these patterns will be forwarded and wait for the corresponding
        continueInterceptedRequest call.
        """
        _params: Dict[str, Any] = {}
        _params['patterns'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Network.RequestPattern')), patterns)
        _result = await self._target.send('Network.setRequestInterception', _params)
        return None

    async def set_user_agent_override(self, *, user_agent: str, accept_language: Optional[str] = None, platform: Optional[str] = None, user_agent_metadata: Optional[Emulation_UserAgentMetadata] = None) -> None:
        """
        Allows overriding user agent with the given string.
        :param user_agent: User agent to use.
        :param accept_language: Browser language to emulate.
        :param platform: The platform navigator.platform should return.
        :param user_agent_metadata: To be sent in Sec-CH-UA-* headers and returned in navigator.userAgentData
        """
        _params: Dict[str, Any] = {}
        _params['userAgent'] = encode(FieldMeta('', '', False, 'primitive'), user_agent)
        if accept_language is not None:
            _params['acceptLanguage'] = encode(FieldMeta('', '', False, 'primitive'), accept_language)
        if platform is not None:
            _params['platform'] = encode(FieldMeta('', '', False, 'primitive'), platform)
        if user_agent_metadata is not None:
            _params['userAgentMetadata'] = encode(FieldMeta('', '', False, 'object', ref='Emulation.UserAgentMetadata'), user_agent_metadata)
        _result = await self._target.send('Network.setUserAgentOverride', _params)
        return None

    async def stream_resource_content(self, *, request_id: RequestId) -> StreamResourceContentReturn:
        """
        Enables streaming of the response for the given requestId.
        If enabled, the dataReceived event contains the data that was received during streaming.
        :param request_id: Identifier of the request to stream.
        """
        _params: Dict[str, Any] = {}
        _params['requestId'] = encode(FieldMeta('', '', False, 'primitive'), request_id)
        _result = await self._target.send('Network.streamResourceContent', _params)
        return StreamResourceContentReturn.from_json(_result)

    async def get_security_isolation_status(self, *, frame_id: Optional[Page_FrameId] = None) -> GetSecurityIsolationStatusReturn:
        """
        Returns information about the COEP/COOP isolation status.
        :param frame_id: If no frameId is provided, the status of the target is provided.
        """
        _params: Dict[str, Any] = {}
        if frame_id is not None:
            _params['frameId'] = encode(FieldMeta('', '', False, 'primitive'), frame_id)
        _result = await self._target.send('Network.getSecurityIsolationStatus', _params)
        return GetSecurityIsolationStatusReturn.from_json(_result)

    async def enable_reporting_api(self, *, enable: bool) -> None:
        """
        Enables tracking for the Reporting API, events generated by the Reporting API will now be delivered to the client.
        Enabling triggers 'reportingApiReportAdded' for all existing reports.
        :param enable: Whether to enable or disable events for the Reporting API
        """
        _params: Dict[str, Any] = {}
        _params['enable'] = encode(FieldMeta('', '', False, 'primitive'), enable)
        _result = await self._target.send('Network.enableReportingApi', _params)
        return None

    async def load_network_resource(self, *, url: str, options: LoadNetworkResourceOptions, frame_id: Optional[Page_FrameId] = None) -> LoadNetworkResourceReturn:
        """
        Fetches the resource and returns the content.
        :param frame_id: Frame id to get the resource for. Mandatory for frame targets, and
        should be omitted for worker targets.
        :param url: URL of the resource to get content for.
        :param options: Options for the request.
        """
        _params: Dict[str, Any] = {}
        _params['url'] = encode(FieldMeta('', '', False, 'primitive'), url)
        _params['options'] = encode(FieldMeta('', '', False, 'object', ref='Network.LoadNetworkResourceOptions'), options)
        if frame_id is not None:
            _params['frameId'] = encode(FieldMeta('', '', False, 'primitive'), frame_id)
        _result = await self._target.send('Network.loadNetworkResource', _params)
        return LoadNetworkResourceReturn.from_json(_result)

    async def set_cookie_controls(self, *, enable_third_party_cookie_restriction: bool, disable_third_party_cookie_metadata: bool, disable_third_party_cookie_heuristics: bool) -> None:
        """
        Sets Controls for third-party cookie access
        Page reload is required before the new cookie behavior will be observed
        :param enable_third_party_cookie_restriction: Whether 3pc restriction is enabled.
        :param disable_third_party_cookie_metadata: Whether 3pc grace period exception should be enabled; false by default.
        :param disable_third_party_cookie_heuristics: Whether 3pc heuristics exceptions should be enabled; false by default.
        """
        _params: Dict[str, Any] = {}
        _params['enableThirdPartyCookieRestriction'] = encode(FieldMeta('', '', False, 'primitive'), enable_third_party_cookie_restriction)
        _params['disableThirdPartyCookieMetadata'] = encode(FieldMeta('', '', False, 'primitive'), disable_third_party_cookie_metadata)
        _params['disableThirdPartyCookieHeuristics'] = encode(FieldMeta('', '', False, 'primitive'), disable_third_party_cookie_heuristics)
        _result = await self._target.send('Network.setCookieControls', _params)
        return None
