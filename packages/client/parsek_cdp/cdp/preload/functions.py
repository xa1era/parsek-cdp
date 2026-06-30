"""Commands for the Preload domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode


class Preload:
    """Commands of the Preload domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def enable(self) -> None:
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Preload.enable', _params)
        return None

    async def disable(self) -> None:
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Preload.disable', _params)
        return None
