"""Commands for the Console domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode


class Console:
    """Commands of the Console domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def clear_messages(self) -> None:
        """Does nothing."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Console.clearMessages', _params)
        return None

    async def disable(self) -> None:
        """Disables console domain, prevents further console messages from being reported to the client."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Console.disable', _params)
        return None

    async def enable(self) -> None:
        """
        Enables console domain, sends the messages collected so far to the client by means of the
        `messageAdded` notification.
        """
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Console.enable', _params)
        return None
