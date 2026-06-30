"""Events for the Security domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import FieldMeta
from ..mixins.event import Event, register_event

if TYPE_CHECKING:
    from .types import (
        InsecureContentStatus,
        SecurityState,
        SecurityStateExplanation,
        VisibleSecurityState,
    )

@register_event("Security.certificateError")
@dataclass
class CertificateError(Event):
    """
    There is a certificate error. If overriding certificate errors is enabled, then it should be
    handled with the `handleCertificateError` command. Note: this event does not fire if the
    certificate error has been allowed internally. Only one client per target should override
    certificate errors at the same time.
    """
    event_id: int
    error_type: str
    request_url: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('event_id', 'eventId', False, 'primitive'),
        FieldMeta('error_type', 'errorType', False, 'primitive'),
        FieldMeta('request_url', 'requestURL', False, 'primitive'),
    )


@register_event("Security.visibleSecurityStateChanged")
@dataclass
class VisibleSecurityStateChanged(Event):
    """The security state of the page changed."""
    visible_security_state: VisibleSecurityState
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('visible_security_state', 'visibleSecurityState', False, 'object', ref='Security.VisibleSecurityState'),
    )


@register_event("Security.securityStateChanged")
@dataclass
class SecurityStateChanged(Event):
    """The security state of the page changed. No longer being sent."""
    security_state: SecurityState
    scheme_is_cryptographic: bool
    explanations: List[SecurityStateExplanation]
    insecure_content_status: InsecureContentStatus
    summary: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('security_state', 'securityState', False, 'enum', ref='Security.SecurityState'),
        FieldMeta('scheme_is_cryptographic', 'schemeIsCryptographic', False, 'primitive'),
        FieldMeta('explanations', 'explanations', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Security.SecurityStateExplanation')),
        FieldMeta('insecure_content_status', 'insecureContentStatus', False, 'object', ref='Security.InsecureContentStatus'),
        FieldMeta('summary', 'summary', True, 'primitive'),
    )

__all__ = ["CertificateError", "SecurityStateChanged", "VisibleSecurityStateChanged"]
