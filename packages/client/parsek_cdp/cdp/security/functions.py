"""Commands for the Security domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode

if TYPE_CHECKING:
    from .types import CertificateErrorAction

class Security:
    """Commands of the Security domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def disable(self) -> None:
        """Disables tracking security state changes."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Security.disable', _params)
        return None

    async def enable(self) -> None:
        """Enables tracking security state changes."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Security.enable', _params)
        return None

    async def set_ignore_certificate_errors(self, *, ignore: bool) -> None:
        """
        Enable/disable whether all certificate errors should be ignored.
        :param ignore: If true, all certificate errors will be ignored.
        """
        _params: Dict[str, Any] = {}
        _params['ignore'] = encode(FieldMeta('', '', False, 'primitive'), ignore)
        _result = await self._target.send('Security.setIgnoreCertificateErrors', _params)
        return None

    async def handle_certificate_error(self, *, event_id: int, action: CertificateErrorAction) -> None:
        """
        Handles a certificate error that fired a certificateError event.
        
        .. deprecated::
        :param event_id: The ID of the event.
        :param action: The action to take on the certificate error.
        """
        _params: Dict[str, Any] = {}
        _params['eventId'] = encode(FieldMeta('', '', False, 'primitive'), event_id)
        _params['action'] = encode(FieldMeta('', '', False, 'enum', ref='Security.CertificateErrorAction'), action)
        _result = await self._target.send('Security.handleCertificateError', _params)
        return None

    async def set_override_certificate_errors(self, *, override: bool) -> None:
        """
        Enable/disable overriding certificate errors. If enabled, all certificate error events need to
        be handled by the DevTools client and should be answered with `handleCertificateError` commands.
        
        .. deprecated::
        :param override: If true, certificate errors will be overridden.
        """
        _params: Dict[str, Any] = {}
        _params['override'] = encode(FieldMeta('', '', False, 'primitive'), override)
        _result = await self._target.send('Security.setOverrideCertificateErrors', _params)
        return None
