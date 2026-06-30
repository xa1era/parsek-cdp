"""Commands for the Tethering domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode


class Tethering:
    """Commands of the Tethering domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def bind(self, *, port: int) -> None:
        """
        Request browser port binding.
        :param port: Port number to bind.
        """
        _params: Dict[str, Any] = {}
        _params['port'] = encode(FieldMeta('', '', False, 'primitive'), port)
        _result = await self._target.send('Tethering.bind', _params)
        return None

    async def unbind(self, *, port: int) -> None:
        """
        Request browser port unbinding.
        :param port: Port number to unbind.
        """
        _params: Dict[str, Any] = {}
        _params['port'] = encode(FieldMeta('', '', False, 'primitive'), port)
        _result = await self._target.send('Tethering.unbind', _params)
        return None
