"""Commands for the Fetch domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode

if TYPE_CHECKING:
    from .types import (
        AuthChallengeResponse,
        HeaderEntry,
        RequestId,
        RequestPattern,
    )
    from ..io.types import StreamHandle as IO_StreamHandle
    from ..network.types import ErrorReason as Network_ErrorReason

@dataclass
class GetResponseBodyReturn(DataType):
    """Return value of :meth:`Fetch.get_response_body`."""
    body: str
    base64_encoded: bool
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('body', 'body', False, 'primitive'),
        FieldMeta('base64_encoded', 'base64Encoded', False, 'primitive'),
    )


@dataclass
class TakeResponseBodyAsStreamReturn(DataType):
    """Return value of :meth:`Fetch.take_response_body_as_stream`."""
    stream: IO_StreamHandle
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('stream', 'stream', False, 'primitive'),
    )


class Fetch:
    """Commands of the Fetch domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def disable(self) -> None:
        """Disables the fetch domain."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Fetch.disable', _params)
        return None

    async def enable(self, *, patterns: Optional[List[RequestPattern]] = None, handle_auth_requests: Optional[bool] = None) -> None:
        """
        Enables issuing of requestPaused events. A request will be paused until client
        calls one of failRequest, fulfillRequest or continueRequest/continueWithAuth.
        :param patterns: If specified, only requests matching any of these patterns will produce
        fetchRequested event and will be paused until clients response. If not set,
        all requests will be affected.
        :param handle_auth_requests: If true, authRequired events will be issued and requests will be paused
        expecting a call to continueWithAuth.
        """
        _params: Dict[str, Any] = {}
        if patterns is not None:
            _params['patterns'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Fetch.RequestPattern')), patterns)
        if handle_auth_requests is not None:
            _params['handleAuthRequests'] = encode(FieldMeta('', '', False, 'primitive'), handle_auth_requests)
        _result = await self._target.send('Fetch.enable', _params)
        return None

    async def fail_request(self, *, request_id: RequestId, error_reason: Network_ErrorReason) -> None:
        """
        Causes the request to fail with specified reason.
        :param request_id: An id the client received in requestPaused event.
        :param error_reason: Causes the request to fail with the given reason.
        """
        _params: Dict[str, Any] = {}
        _params['requestId'] = encode(FieldMeta('', '', False, 'primitive'), request_id)
        _params['errorReason'] = encode(FieldMeta('', '', False, 'enum', ref='Network.ErrorReason'), error_reason)
        _result = await self._target.send('Fetch.failRequest', _params)
        return None

    async def fulfill_request(self, *, request_id: RequestId, response_code: int, response_headers: Optional[List[HeaderEntry]] = None, binary_response_headers: Optional[str] = None, body: Optional[str] = None, response_phrase: Optional[str] = None) -> None:
        """
        Provides response to the request.
        :param request_id: An id the client received in requestPaused event.
        :param response_code: An HTTP response code.
        :param response_headers: Response headers.
        :param binary_response_headers: Alternative way of specifying response headers as a \\0-separated
        series of name: value pairs. Prefer the above method unless you
        need to represent some non-UTF8 values that can't be transmitted
        over the protocol as text. (Encoded as a base64 string when passed over JSON)
        :param body: A response body. If absent, original response body will be used if
        the request is intercepted at the response stage and empty body
        will be used if the request is intercepted at the request stage. (Encoded as a base64 string when passed over JSON)
        :param response_phrase: A textual representation of responseCode.
        If absent, a standard phrase matching responseCode is used.
        """
        _params: Dict[str, Any] = {}
        _params['requestId'] = encode(FieldMeta('', '', False, 'primitive'), request_id)
        _params['responseCode'] = encode(FieldMeta('', '', False, 'primitive'), response_code)
        if response_headers is not None:
            _params['responseHeaders'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Fetch.HeaderEntry')), response_headers)
        if binary_response_headers is not None:
            _params['binaryResponseHeaders'] = encode(FieldMeta('', '', False, 'primitive'), binary_response_headers)
        if body is not None:
            _params['body'] = encode(FieldMeta('', '', False, 'primitive'), body)
        if response_phrase is not None:
            _params['responsePhrase'] = encode(FieldMeta('', '', False, 'primitive'), response_phrase)
        _result = await self._target.send('Fetch.fulfillRequest', _params)
        return None

    async def continue_request(self, *, request_id: RequestId, url: Optional[str] = None, method: Optional[str] = None, post_data: Optional[str] = None, headers: Optional[List[HeaderEntry]] = None, intercept_response: Optional[bool] = None) -> None:
        """
        Continues the request, optionally modifying some of its parameters.
        :param request_id: An id the client received in requestPaused event.
        :param url: If set, the request url will be modified in a way that's not observable by page.
        :param method: If set, the request method is overridden.
        :param post_data: If set, overrides the post data in the request. (Encoded as a base64 string when passed over JSON)
        :param headers: If set, overrides the request headers. Note that the overrides do not
        extend to subsequent redirect hops, if a redirect happens. Another override
        may be applied to a different request produced by a redirect.
        :param intercept_response: If set, overrides response interception behavior for this request.
        """
        _params: Dict[str, Any] = {}
        _params['requestId'] = encode(FieldMeta('', '', False, 'primitive'), request_id)
        if url is not None:
            _params['url'] = encode(FieldMeta('', '', False, 'primitive'), url)
        if method is not None:
            _params['method'] = encode(FieldMeta('', '', False, 'primitive'), method)
        if post_data is not None:
            _params['postData'] = encode(FieldMeta('', '', False, 'primitive'), post_data)
        if headers is not None:
            _params['headers'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Fetch.HeaderEntry')), headers)
        if intercept_response is not None:
            _params['interceptResponse'] = encode(FieldMeta('', '', False, 'primitive'), intercept_response)
        _result = await self._target.send('Fetch.continueRequest', _params)
        return None

    async def continue_with_auth(self, *, request_id: RequestId, auth_challenge_response: AuthChallengeResponse) -> None:
        """
        Continues a request supplying authChallengeResponse following authRequired event.
        :param request_id: An id the client received in authRequired event.
        :param auth_challenge_response: Response to  with an authChallenge.
        """
        _params: Dict[str, Any] = {}
        _params['requestId'] = encode(FieldMeta('', '', False, 'primitive'), request_id)
        _params['authChallengeResponse'] = encode(FieldMeta('', '', False, 'object', ref='Fetch.AuthChallengeResponse'), auth_challenge_response)
        _result = await self._target.send('Fetch.continueWithAuth', _params)
        return None

    async def continue_response(self, *, request_id: RequestId, response_code: Optional[int] = None, response_phrase: Optional[str] = None, response_headers: Optional[List[HeaderEntry]] = None, binary_response_headers: Optional[str] = None) -> None:
        """
        Continues loading of the paused response, optionally modifying the
        response headers. If either responseCode or headers are modified, all of them
        must be present.
        :param request_id: An id the client received in requestPaused event.
        :param response_code: An HTTP response code. If absent, original response code will be used.
        :param response_phrase: A textual representation of responseCode.
        If absent, a standard phrase matching responseCode is used.
        :param response_headers: Response headers. If absent, original response headers will be used.
        :param binary_response_headers: Alternative way of specifying response headers as a \\0-separated
        series of name: value pairs. Prefer the above method unless you
        need to represent some non-UTF8 values that can't be transmitted
        over the protocol as text. (Encoded as a base64 string when passed over JSON)
        """
        _params: Dict[str, Any] = {}
        _params['requestId'] = encode(FieldMeta('', '', False, 'primitive'), request_id)
        if response_code is not None:
            _params['responseCode'] = encode(FieldMeta('', '', False, 'primitive'), response_code)
        if response_phrase is not None:
            _params['responsePhrase'] = encode(FieldMeta('', '', False, 'primitive'), response_phrase)
        if response_headers is not None:
            _params['responseHeaders'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Fetch.HeaderEntry')), response_headers)
        if binary_response_headers is not None:
            _params['binaryResponseHeaders'] = encode(FieldMeta('', '', False, 'primitive'), binary_response_headers)
        _result = await self._target.send('Fetch.continueResponse', _params)
        return None

    async def get_response_body(self, *, request_id: RequestId) -> GetResponseBodyReturn:
        """
        Causes the body of the response to be received from the server and
        returned as a single string. May only be issued for a request that
        is paused in the Response stage and is mutually exclusive with
        takeResponseBodyForInterceptionAsStream. Calling other methods that
        affect the request or disabling fetch domain before body is received
        results in an undefined behavior.
        Note that the response body is not available for redirects. Requests
        paused in the _redirect received_ state may be differentiated by
        `responseCode` and presence of `location` response header, see
        comments to `requestPaused` for details.
        :param request_id: Identifier for the intercepted request to get body for.
        """
        _params: Dict[str, Any] = {}
        _params['requestId'] = encode(FieldMeta('', '', False, 'primitive'), request_id)
        _result = await self._target.send('Fetch.getResponseBody', _params)
        return GetResponseBodyReturn.from_json(_result)

    async def take_response_body_as_stream(self, *, request_id: RequestId) -> TakeResponseBodyAsStreamReturn:
        """
        Returns a handle to the stream representing the response body.
        The request must be paused in the HeadersReceived stage.
        Note that after this command the request can't be continued
        as is -- client either needs to cancel it or to provide the
        response body.
        The stream only supports sequential read, IO.read will fail if the position
        is specified.
        This method is mutually exclusive with getResponseBody.
        Calling other methods that affect the request or disabling fetch
        domain before body is received results in an undefined behavior.
        :param request_id:
        """
        _params: Dict[str, Any] = {}
        _params['requestId'] = encode(FieldMeta('', '', False, 'primitive'), request_id)
        _result = await self._target.send('Fetch.takeResponseBodyAsStream', _params)
        return TakeResponseBodyAsStreamReturn.from_json(_result)
