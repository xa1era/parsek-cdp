"""Commands for the Inspector domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode


class Inspector:
    """Commands of the Inspector domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def disable(self) -> None:
        """Disables inspector domain notifications."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Inspector.disable', _params)
        return None

    async def enable(self) -> None:
        """Enables inspector domain notifications."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Inspector.enable', _params)
        return None
