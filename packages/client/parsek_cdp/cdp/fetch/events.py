"""Events for the Fetch domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import FieldMeta
from ..mixins.event import Event, register_event

if TYPE_CHECKING:
    from .types import (
        AuthChallenge,
        HeaderEntry,
        RequestId,
    )
    from ..network.types import ErrorReason as Network_ErrorReason
    from ..network.types import Request as Network_Request
    from ..network.types import RequestId as Network_RequestId
    from ..network.types import ResourceType as Network_ResourceType
    from ..page.types import FrameId as Page_FrameId

@register_event("Fetch.requestPaused")
@dataclass
class RequestPaused(Event):
    """
    Issued when the domain is enabled and the request URL matches the
    specified filter. The request is paused until the client responds
    with one of continueRequest, failRequest or fulfillRequest.
    The stage of the request can be determined by presence of responseErrorReason
    and responseStatusCode -- the request is at the response stage if either
    of these fields is present and in the request stage otherwise.
    Redirect responses and subsequent requests are reported similarly to regular
    responses and requests. Redirect responses may be distinguished by the value
    of `responseStatusCode` (which is one of 301, 302, 303, 307, 308) along with
    presence of the `location` header. Requests resulting from a redirect will
    have `redirectedRequestId` field set.
    """
    request_id: RequestId
    request: Network_Request
    frame_id: Page_FrameId
    resource_type: Network_ResourceType
    response_error_reason: Optional[Network_ErrorReason] = None
    response_status_code: Optional[int] = None
    response_status_text: Optional[str] = None
    response_headers: Optional[List[HeaderEntry]] = None
    network_id: Optional[Network_RequestId] = None
    redirected_request_id: Optional[RequestId] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('request_id', 'requestId', False, 'primitive'),
        FieldMeta('request', 'request', False, 'object', ref='Network.Request'),
        FieldMeta('frame_id', 'frameId', False, 'primitive'),
        FieldMeta('resource_type', 'resourceType', False, 'enum', ref='Network.ResourceType'),
        FieldMeta('response_error_reason', 'responseErrorReason', True, 'enum', ref='Network.ErrorReason'),
        FieldMeta('response_status_code', 'responseStatusCode', True, 'primitive'),
        FieldMeta('response_status_text', 'responseStatusText', True, 'primitive'),
        FieldMeta('response_headers', 'responseHeaders', True, 'array', inner=FieldMeta('', '', False, 'object', ref='Fetch.HeaderEntry')),
        FieldMeta('network_id', 'networkId', True, 'primitive'),
        FieldMeta('redirected_request_id', 'redirectedRequestId', True, 'primitive'),
    )


@register_event("Fetch.authRequired")
@dataclass
class AuthRequired(Event):
    """
    Issued when the domain is enabled with handleAuthRequests set to true.
    The request is paused until client responds with continueWithAuth.
    """
    request_id: RequestId
    request: Network_Request
    frame_id: Page_FrameId
    resource_type: Network_ResourceType
    auth_challenge: AuthChallenge
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('request_id', 'requestId', False, 'primitive'),
        FieldMeta('request', 'request', False, 'object', ref='Network.Request'),
        FieldMeta('frame_id', 'frameId', False, 'primitive'),
        FieldMeta('resource_type', 'resourceType', False, 'enum', ref='Network.ResourceType'),
        FieldMeta('auth_challenge', 'authChallenge', False, 'object', ref='Fetch.AuthChallenge'),
    )

__all__ = ["AuthRequired", "RequestPaused"]
