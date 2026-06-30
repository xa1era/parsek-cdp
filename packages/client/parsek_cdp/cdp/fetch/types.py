"""Custom types and enums for the Fetch domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, register

if TYPE_CHECKING:
    from ..network.types import ResourceType as Network_ResourceType

type RequestId = str  # Unique request identifier.


@register("Fetch.RequestStage")
class RequestStage(str, Enum):
    """
    Stages of the request to handle. Request will intercept before the request is
    sent. Response will intercept after the response is received (but before response
    body is received).
    """
    REQUEST = 'Request'
    RESPONSE = 'Response'


@register("Fetch.RequestPattern")
@dataclass
class RequestPattern(DataType):
    url_pattern: Optional[str] = None
    resource_type: Optional[Network_ResourceType] = None
    request_stage: Optional[RequestStage] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('url_pattern', 'urlPattern', True, 'primitive'),
        FieldMeta('resource_type', 'resourceType', True, 'enum', ref='Network.ResourceType'),
        FieldMeta('request_stage', 'requestStage', True, 'enum', ref='Fetch.RequestStage'),
    )


@register("Fetch.HeaderEntry")
@dataclass
class HeaderEntry(DataType):
    """Response HTTP header entry"""
    name: str
    value: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('name', 'name', False, 'primitive'),
        FieldMeta('value', 'value', False, 'primitive'),
    )


@register("Fetch.AuthChallenge")
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


@register("Fetch.AuthChallengeResponse")
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

__all__ = ["AuthChallenge", "AuthChallengeResponse", "HeaderEntry", "RequestId", "RequestPattern", "RequestStage"]
