"""Commands for the Media domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode


class Media:
    """Commands of the Media domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def enable(self) -> None:
        """Enables the Media domain"""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Media.enable', _params)
        return None

    async def disable(self) -> None:
        """Disables the Media domain."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Media.disable', _params)
        return None
