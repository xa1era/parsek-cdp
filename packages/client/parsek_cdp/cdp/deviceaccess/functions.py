"""Commands for the DeviceAccess domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode

if TYPE_CHECKING:
    from .types import (
        DeviceId,
        RequestId,
    )

class DeviceAccess:
    """Commands of the DeviceAccess domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def enable(self) -> None:
        """Enable events in this domain."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('DeviceAccess.enable', _params)
        return None

    async def disable(self) -> None:
        """Disable events in this domain."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('DeviceAccess.disable', _params)
        return None

    async def select_prompt(self, *, id: RequestId, device_id: DeviceId) -> None:
        """
        Select a device in response to a DeviceAccess.deviceRequestPrompted event.
        :param id:
        :param device_id:
        """
        _params: Dict[str, Any] = {}
        _params['id'] = encode(FieldMeta('', '', False, 'primitive'), id)
        _params['deviceId'] = encode(FieldMeta('', '', False, 'primitive'), device_id)
        _result = await self._target.send('DeviceAccess.selectPrompt', _params)
        return None

    async def cancel_prompt(self, *, id: RequestId) -> None:
        """
        Cancel a prompt in response to a DeviceAccess.deviceRequestPrompted event.
        :param id:
        """
        _params: Dict[str, Any] = {}
        _params['id'] = encode(FieldMeta('', '', False, 'primitive'), id)
        _result = await self._target.send('DeviceAccess.cancelPrompt', _params)
        return None
