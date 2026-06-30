"""Commands for the WebAuthn domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode

if TYPE_CHECKING:
    from .types import (
        AuthenticatorId,
        Credential,
        VirtualAuthenticatorOptions,
    )

@dataclass
class AddVirtualAuthenticatorReturn(DataType):
    """Return value of :meth:`WebAuthn.add_virtual_authenticator`."""
    authenticator_id: AuthenticatorId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('authenticator_id', 'authenticatorId', False, 'primitive'),
    )


@dataclass
class GetCredentialReturn(DataType):
    """Return value of :meth:`WebAuthn.get_credential`."""
    credential: Credential
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('credential', 'credential', False, 'object', ref='WebAuthn.Credential'),
    )


@dataclass
class GetCredentialsReturn(DataType):
    """Return value of :meth:`WebAuthn.get_credentials`."""
    credentials: List[Credential]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('credentials', 'credentials', False, 'array', inner=FieldMeta('', '', False, 'object', ref='WebAuthn.Credential')),
    )


class WebAuthn:
    """Commands of the WebAuthn domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def enable(self, *, enable_ui: Optional[bool] = None) -> None:
        """
        Enable the WebAuthn domain and start intercepting credential storage and
        retrieval with a virtual authenticator.
        :param enable_ui: Whether to enable the WebAuthn user interface. Enabling the UI is
        recommended for debugging and demo purposes, as it is closer to the real
        experience. Disabling the UI is recommended for automated testing.
        Supported at the embedder's discretion if UI is available.
        Defaults to false.
        """
        _params: Dict[str, Any] = {}
        if enable_ui is not None:
            _params['enableUI'] = encode(FieldMeta('', '', False, 'primitive'), enable_ui)
        _result = await self._target.send('WebAuthn.enable', _params)
        return None

    async def disable(self) -> None:
        """Disable the WebAuthn domain."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('WebAuthn.disable', _params)
        return None

    async def add_virtual_authenticator(self, *, options: VirtualAuthenticatorOptions) -> AddVirtualAuthenticatorReturn:
        """
        Creates and adds a virtual authenticator.
        :param options:
        """
        _params: Dict[str, Any] = {}
        _params['options'] = encode(FieldMeta('', '', False, 'object', ref='WebAuthn.VirtualAuthenticatorOptions'), options)
        _result = await self._target.send('WebAuthn.addVirtualAuthenticator', _params)
        return AddVirtualAuthenticatorReturn.from_json(_result)

    async def set_response_override_bits(self, *, authenticator_id: AuthenticatorId, is_bogus_signature: Optional[bool] = None, is_bad_uv: Optional[bool] = None, is_bad_up: Optional[bool] = None) -> None:
        """
        Resets parameters isBogusSignature, isBadUV, isBadUP to false if they are not present.
        :param authenticator_id:
        :param is_bogus_signature: If isBogusSignature is set, overrides the signature in the authenticator response to be zero.
        Defaults to false.
        :param is_bad_uv: If isBadUV is set, overrides the UV bit in the flags in the authenticator response to
        be zero. Defaults to false.
        :param is_bad_up: If isBadUP is set, overrides the UP bit in the flags in the authenticator response to
        be zero. Defaults to false.
        """
        _params: Dict[str, Any] = {}
        _params['authenticatorId'] = encode(FieldMeta('', '', False, 'primitive'), authenticator_id)
        if is_bogus_signature is not None:
            _params['isBogusSignature'] = encode(FieldMeta('', '', False, 'primitive'), is_bogus_signature)
        if is_bad_uv is not None:
            _params['isBadUV'] = encode(FieldMeta('', '', False, 'primitive'), is_bad_uv)
        if is_bad_up is not None:
            _params['isBadUP'] = encode(FieldMeta('', '', False, 'primitive'), is_bad_up)
        _result = await self._target.send('WebAuthn.setResponseOverrideBits', _params)
        return None

    async def remove_virtual_authenticator(self, *, authenticator_id: AuthenticatorId) -> None:
        """
        Removes the given authenticator.
        :param authenticator_id:
        """
        _params: Dict[str, Any] = {}
        _params['authenticatorId'] = encode(FieldMeta('', '', False, 'primitive'), authenticator_id)
        _result = await self._target.send('WebAuthn.removeVirtualAuthenticator', _params)
        return None

    async def add_credential(self, *, authenticator_id: AuthenticatorId, credential: Credential) -> None:
        """
        Adds the credential to the specified authenticator.
        :param authenticator_id:
        :param credential:
        """
        _params: Dict[str, Any] = {}
        _params['authenticatorId'] = encode(FieldMeta('', '', False, 'primitive'), authenticator_id)
        _params['credential'] = encode(FieldMeta('', '', False, 'object', ref='WebAuthn.Credential'), credential)
        _result = await self._target.send('WebAuthn.addCredential', _params)
        return None

    async def get_credential(self, *, authenticator_id: AuthenticatorId, credential_id: str) -> GetCredentialReturn:
        """
        Returns a single credential stored in the given virtual authenticator that
        matches the credential ID.
        :param authenticator_id:
        :param credential_id:
        """
        _params: Dict[str, Any] = {}
        _params['authenticatorId'] = encode(FieldMeta('', '', False, 'primitive'), authenticator_id)
        _params['credentialId'] = encode(FieldMeta('', '', False, 'primitive'), credential_id)
        _result = await self._target.send('WebAuthn.getCredential', _params)
        return GetCredentialReturn.from_json(_result)

    async def get_credentials(self, *, authenticator_id: AuthenticatorId) -> GetCredentialsReturn:
        """
        Returns all the credentials stored in the given virtual authenticator.
        :param authenticator_id:
        """
        _params: Dict[str, Any] = {}
        _params['authenticatorId'] = encode(FieldMeta('', '', False, 'primitive'), authenticator_id)
        _result = await self._target.send('WebAuthn.getCredentials', _params)
        return GetCredentialsReturn.from_json(_result)

    async def remove_credential(self, *, authenticator_id: AuthenticatorId, credential_id: str) -> None:
        """
        Removes a credential from the authenticator.
        :param authenticator_id:
        :param credential_id:
        """
        _params: Dict[str, Any] = {}
        _params['authenticatorId'] = encode(FieldMeta('', '', False, 'primitive'), authenticator_id)
        _params['credentialId'] = encode(FieldMeta('', '', False, 'primitive'), credential_id)
        _result = await self._target.send('WebAuthn.removeCredential', _params)
        return None

    async def clear_credentials(self, *, authenticator_id: AuthenticatorId) -> None:
        """
        Clears all the credentials from the specified device.
        :param authenticator_id:
        """
        _params: Dict[str, Any] = {}
        _params['authenticatorId'] = encode(FieldMeta('', '', False, 'primitive'), authenticator_id)
        _result = await self._target.send('WebAuthn.clearCredentials', _params)
        return None

    async def set_user_verified(self, *, authenticator_id: AuthenticatorId, is_user_verified: bool) -> None:
        """
        Sets whether User Verification succeeds or fails for an authenticator.
        The default is true.
        :param authenticator_id:
        :param is_user_verified:
        """
        _params: Dict[str, Any] = {}
        _params['authenticatorId'] = encode(FieldMeta('', '', False, 'primitive'), authenticator_id)
        _params['isUserVerified'] = encode(FieldMeta('', '', False, 'primitive'), is_user_verified)
        _result = await self._target.send('WebAuthn.setUserVerified', _params)
        return None

    async def set_automatic_presence_simulation(self, *, authenticator_id: AuthenticatorId, enabled: bool) -> None:
        """
        Sets whether tests of user presence will succeed immediately (if true) or fail to resolve (if false) for an authenticator.
        The default is true.
        :param authenticator_id:
        :param enabled:
        """
        _params: Dict[str, Any] = {}
        _params['authenticatorId'] = encode(FieldMeta('', '', False, 'primitive'), authenticator_id)
        _params['enabled'] = encode(FieldMeta('', '', False, 'primitive'), enabled)
        _result = await self._target.send('WebAuthn.setAutomaticPresenceSimulation', _params)
        return None

    async def set_credential_properties(self, *, authenticator_id: AuthenticatorId, credential_id: str, backup_eligibility: Optional[bool] = None, backup_state: Optional[bool] = None) -> None:
        """
        Allows setting credential properties.
        https://w3c.github.io/webauthn/#sctn-automation-set-credential-properties
        :param authenticator_id:
        :param credential_id:
        :param backup_eligibility:
        :param backup_state:
        """
        _params: Dict[str, Any] = {}
        _params['authenticatorId'] = encode(FieldMeta('', '', False, 'primitive'), authenticator_id)
        _params['credentialId'] = encode(FieldMeta('', '', False, 'primitive'), credential_id)
        if backup_eligibility is not None:
            _params['backupEligibility'] = encode(FieldMeta('', '', False, 'primitive'), backup_eligibility)
        if backup_state is not None:
            _params['backupState'] = encode(FieldMeta('', '', False, 'primitive'), backup_state)
        _result = await self._target.send('WebAuthn.setCredentialProperties', _params)
        return None
