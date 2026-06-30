"""Events for the WebAuthn domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import FieldMeta
from ..mixins.event import Event, register_event

if TYPE_CHECKING:
    from .types import (
        AuthenticatorId,
        Credential,
    )

@register_event("WebAuthn.credentialAdded")
@dataclass
class CredentialAdded(Event):
    """Triggered when a credential is added to an authenticator."""
    authenticator_id: AuthenticatorId
    credential: Credential
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('authenticator_id', 'authenticatorId', False, 'primitive'),
        FieldMeta('credential', 'credential', False, 'object', ref='WebAuthn.Credential'),
    )


@register_event("WebAuthn.credentialDeleted")
@dataclass
class CredentialDeleted(Event):
    """
    Triggered when a credential is deleted, e.g. through
    PublicKeyCredential.signalUnknownCredential().
    """
    authenticator_id: AuthenticatorId
    credential_id: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('authenticator_id', 'authenticatorId', False, 'primitive'),
        FieldMeta('credential_id', 'credentialId', False, 'primitive'),
    )


@register_event("WebAuthn.credentialUpdated")
@dataclass
class CredentialUpdated(Event):
    """
    Triggered when a credential is updated, e.g. through
    PublicKeyCredential.signalCurrentUserDetails().
    """
    authenticator_id: AuthenticatorId
    credential: Credential
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('authenticator_id', 'authenticatorId', False, 'primitive'),
        FieldMeta('credential', 'credential', False, 'object', ref='WebAuthn.Credential'),
    )


@register_event("WebAuthn.credentialAsserted")
@dataclass
class CredentialAsserted(Event):
    """Triggered when a credential is used in a webauthn assertion."""
    authenticator_id: AuthenticatorId
    credential: Credential
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('authenticator_id', 'authenticatorId', False, 'primitive'),
        FieldMeta('credential', 'credential', False, 'object', ref='WebAuthn.Credential'),
    )

__all__ = ["CredentialAdded", "CredentialAsserted", "CredentialDeleted", "CredentialUpdated"]
