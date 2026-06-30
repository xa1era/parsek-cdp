"""Custom types and enums for the WebAuthn domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, register


type AuthenticatorId = str


@register("WebAuthn.AuthenticatorProtocol")
class AuthenticatorProtocol(str, Enum):
    U2F = 'u2f'
    CTAP2 = 'ctap2'


@register("WebAuthn.Ctap2Version")
class Ctap2Version(str, Enum):
    CTAP2_0 = 'ctap2_0'
    CTAP2_1 = 'ctap2_1'


@register("WebAuthn.AuthenticatorTransport")
class AuthenticatorTransport(str, Enum):
    USB = 'usb'
    NFC = 'nfc'
    BLE = 'ble'
    CABLE = 'cable'
    INTERNAL = 'internal'


@register("WebAuthn.VirtualAuthenticatorOptions")
@dataclass
class VirtualAuthenticatorOptions(DataType):
    protocol: AuthenticatorProtocol
    transport: AuthenticatorTransport
    ctap2_version: Optional[Ctap2Version] = None
    has_resident_key: Optional[bool] = None
    has_user_verification: Optional[bool] = None
    has_large_blob: Optional[bool] = None
    has_cred_blob: Optional[bool] = None
    has_min_pin_length: Optional[bool] = None
    has_prf: Optional[bool] = None
    automatic_presence_simulation: Optional[bool] = None
    is_user_verified: Optional[bool] = None
    default_backup_eligibility: Optional[bool] = None
    default_backup_state: Optional[bool] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('protocol', 'protocol', False, 'enum', ref='WebAuthn.AuthenticatorProtocol'),
        FieldMeta('transport', 'transport', False, 'enum', ref='WebAuthn.AuthenticatorTransport'),
        FieldMeta('ctap2_version', 'ctap2Version', True, 'enum', ref='WebAuthn.Ctap2Version'),
        FieldMeta('has_resident_key', 'hasResidentKey', True, 'primitive'),
        FieldMeta('has_user_verification', 'hasUserVerification', True, 'primitive'),
        FieldMeta('has_large_blob', 'hasLargeBlob', True, 'primitive'),
        FieldMeta('has_cred_blob', 'hasCredBlob', True, 'primitive'),
        FieldMeta('has_min_pin_length', 'hasMinPinLength', True, 'primitive'),
        FieldMeta('has_prf', 'hasPrf', True, 'primitive'),
        FieldMeta('automatic_presence_simulation', 'automaticPresenceSimulation', True, 'primitive'),
        FieldMeta('is_user_verified', 'isUserVerified', True, 'primitive'),
        FieldMeta('default_backup_eligibility', 'defaultBackupEligibility', True, 'primitive'),
        FieldMeta('default_backup_state', 'defaultBackupState', True, 'primitive'),
    )


@register("WebAuthn.Credential")
@dataclass
class Credential(DataType):
    credential_id: str
    is_resident_credential: bool
    private_key: str
    sign_count: int
    rp_id: Optional[str] = None
    user_handle: Optional[str] = None
    large_blob: Optional[str] = None
    backup_eligibility: Optional[bool] = None
    backup_state: Optional[bool] = None
    user_name: Optional[str] = None
    user_display_name: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('credential_id', 'credentialId', False, 'primitive'),
        FieldMeta('is_resident_credential', 'isResidentCredential', False, 'primitive'),
        FieldMeta('private_key', 'privateKey', False, 'primitive'),
        FieldMeta('sign_count', 'signCount', False, 'primitive'),
        FieldMeta('rp_id', 'rpId', True, 'primitive'),
        FieldMeta('user_handle', 'userHandle', True, 'primitive'),
        FieldMeta('large_blob', 'largeBlob', True, 'primitive'),
        FieldMeta('backup_eligibility', 'backupEligibility', True, 'primitive'),
        FieldMeta('backup_state', 'backupState', True, 'primitive'),
        FieldMeta('user_name', 'userName', True, 'primitive'),
        FieldMeta('user_display_name', 'userDisplayName', True, 'primitive'),
    )

__all__ = ["AuthenticatorId", "AuthenticatorProtocol", "AuthenticatorTransport", "Credential", "Ctap2Version", "VirtualAuthenticatorOptions"]
