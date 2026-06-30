"""Commands for the DeviceOrientation domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode


class DeviceOrientation:
    """Commands of the DeviceOrientation domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def clear_device_orientation_override(self) -> None:
        """Clears the overridden Device Orientation."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('DeviceOrientation.clearDeviceOrientationOverride', _params)
        return None

    async def set_device_orientation_override(self, *, alpha: float, beta: float, gamma: float) -> None:
        """
        Overrides the Device Orientation.
        :param alpha: Mock alpha
        :param beta: Mock beta
        :param gamma: Mock gamma
        """
        _params: Dict[str, Any] = {}
        _params['alpha'] = encode(FieldMeta('', '', False, 'primitive'), alpha)
        _params['beta'] = encode(FieldMeta('', '', False, 'primitive'), beta)
        _params['gamma'] = encode(FieldMeta('', '', False, 'primitive'), gamma)
        _result = await self._target.send('DeviceOrientation.setDeviceOrientationOverride', _params)
        return None
