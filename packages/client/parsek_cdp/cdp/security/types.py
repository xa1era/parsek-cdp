"""Custom types and enums for the Security domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, register

if TYPE_CHECKING:
    from ..network.types import TimeSinceEpoch as Network_TimeSinceEpoch

type CertificateId = int  # An internal certificate ID value.


@register("Security.MixedContentType")
class MixedContentType(str, Enum):
    """
    A description of mixed content (HTTP resources on HTTPS pages), as defined by
    https://www.w3.org/TR/mixed-content/#categories
    """
    BLOCKABLE = 'blockable'
    OPTIONALLY_BLOCKABLE = 'optionally-blockable'
    NONE = 'none'


@register("Security.SecurityState")
class SecurityState(str, Enum):
    """The security level of a page or resource."""
    UNKNOWN = 'unknown'
    NEUTRAL = 'neutral'
    INSECURE = 'insecure'
    SECURE = 'secure'
    INFO = 'info'
    INSECURE_BROKEN = 'insecure-broken'


@register("Security.CertificateSecurityState")
@dataclass
class CertificateSecurityState(DataType):
    """Details about the security state of the page certificate."""
    protocol: str
    key_exchange: str
    cipher: str
    certificate: List[str]
    subject_name: str
    issuer: str
    valid_from: Network_TimeSinceEpoch
    valid_to: Network_TimeSinceEpoch
    certificate_has_weak_signature: bool
    certificate_has_sha1_signature: bool
    modern_ssl: bool
    obsolete_ssl_protocol: bool
    obsolete_ssl_key_exchange: bool
    obsolete_ssl_cipher: bool
    obsolete_ssl_signature: bool
    key_exchange_group: Optional[str] = None
    mac: Optional[str] = None
    certificate_network_error: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('protocol', 'protocol', False, 'primitive'),
        FieldMeta('key_exchange', 'keyExchange', False, 'primitive'),
        FieldMeta('cipher', 'cipher', False, 'primitive'),
        FieldMeta('certificate', 'certificate', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('subject_name', 'subjectName', False, 'primitive'),
        FieldMeta('issuer', 'issuer', False, 'primitive'),
        FieldMeta('valid_from', 'validFrom', False, 'primitive'),
        FieldMeta('valid_to', 'validTo', False, 'primitive'),
        FieldMeta('certificate_has_weak_signature', 'certificateHasWeakSignature', False, 'primitive'),
        FieldMeta('certificate_has_sha1_signature', 'certificateHasSha1Signature', False, 'primitive'),
        FieldMeta('modern_ssl', 'modernSSL', False, 'primitive'),
        FieldMeta('obsolete_ssl_protocol', 'obsoleteSslProtocol', False, 'primitive'),
        FieldMeta('obsolete_ssl_key_exchange', 'obsoleteSslKeyExchange', False, 'primitive'),
        FieldMeta('obsolete_ssl_cipher', 'obsoleteSslCipher', False, 'primitive'),
        FieldMeta('obsolete_ssl_signature', 'obsoleteSslSignature', False, 'primitive'),
        FieldMeta('key_exchange_group', 'keyExchangeGroup', True, 'primitive'),
        FieldMeta('mac', 'mac', True, 'primitive'),
        FieldMeta('certificate_network_error', 'certificateNetworkError', True, 'primitive'),
    )


@register("Security.SafetyTipStatus")
class SafetyTipStatus(str, Enum):
    BADREPUTATION = 'badReputation'
    LOOKALIKE = 'lookalike'


@register("Security.SafetyTipInfo")
@dataclass
class SafetyTipInfo(DataType):
    safety_tip_status: SafetyTipStatus
    safe_url: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('safety_tip_status', 'safetyTipStatus', False, 'enum', ref='Security.SafetyTipStatus'),
        FieldMeta('safe_url', 'safeUrl', True, 'primitive'),
    )


@register("Security.VisibleSecurityState")
@dataclass
class VisibleSecurityState(DataType):
    """Security state information about the page."""
    security_state: SecurityState
    security_state_issue_ids: List[str]
    certificate_security_state: Optional[CertificateSecurityState] = None
    safety_tip_info: Optional[SafetyTipInfo] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('security_state', 'securityState', False, 'enum', ref='Security.SecurityState'),
        FieldMeta('security_state_issue_ids', 'securityStateIssueIds', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('certificate_security_state', 'certificateSecurityState', True, 'object', ref='Security.CertificateSecurityState'),
        FieldMeta('safety_tip_info', 'safetyTipInfo', True, 'object', ref='Security.SafetyTipInfo'),
    )


@register("Security.SecurityStateExplanation")
@dataclass
class SecurityStateExplanation(DataType):
    """An explanation of an factor contributing to the security state."""
    security_state: SecurityState
    title: str
    summary: str
    description: str
    mixed_content_type: MixedContentType
    certificate: List[str]
    recommendations: Optional[List[str]] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('security_state', 'securityState', False, 'enum', ref='Security.SecurityState'),
        FieldMeta('title', 'title', False, 'primitive'),
        FieldMeta('summary', 'summary', False, 'primitive'),
        FieldMeta('description', 'description', False, 'primitive'),
        FieldMeta('mixed_content_type', 'mixedContentType', False, 'enum', ref='Security.MixedContentType'),
        FieldMeta('certificate', 'certificate', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('recommendations', 'recommendations', True, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


@register("Security.InsecureContentStatus")
@dataclass
class InsecureContentStatus(DataType):
    """Information about insecure content on the page."""
    ran_mixed_content: bool
    displayed_mixed_content: bool
    contained_mixed_form: bool
    ran_content_with_cert_errors: bool
    displayed_content_with_cert_errors: bool
    ran_insecure_content_style: SecurityState
    displayed_insecure_content_style: SecurityState
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('ran_mixed_content', 'ranMixedContent', False, 'primitive'),
        FieldMeta('displayed_mixed_content', 'displayedMixedContent', False, 'primitive'),
        FieldMeta('contained_mixed_form', 'containedMixedForm', False, 'primitive'),
        FieldMeta('ran_content_with_cert_errors', 'ranContentWithCertErrors', False, 'primitive'),
        FieldMeta('displayed_content_with_cert_errors', 'displayedContentWithCertErrors', False, 'primitive'),
        FieldMeta('ran_insecure_content_style', 'ranInsecureContentStyle', False, 'enum', ref='Security.SecurityState'),
        FieldMeta('displayed_insecure_content_style', 'displayedInsecureContentStyle', False, 'enum', ref='Security.SecurityState'),
    )


@register("Security.CertificateErrorAction")
class CertificateErrorAction(str, Enum):
    """
    The action to take when a certificate error occurs. continue will continue processing the
    request and cancel will cancel the request.
    """
    CONTINUE = 'continue'
    CANCEL = 'cancel'

__all__ = ["CertificateErrorAction", "CertificateId", "CertificateSecurityState", "InsecureContentStatus", "MixedContentType", "SafetyTipInfo", "SafetyTipStatus", "SecurityState", "SecurityStateExplanation", "VisibleSecurityState"]
