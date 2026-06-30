"""Commands for the Log domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode

if TYPE_CHECKING:
    from .types import ViolationSetting

class Log:
    """Commands of the Log domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def clear(self) -> None:
        """Clears the log."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Log.clear', _params)
        return None

    async def disable(self) -> None:
        """Disables log domain, prevents further log entries from being reported to the client."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Log.disable', _params)
        return None

    async def enable(self) -> None:
        """
        Enables log domain, sends the entries collected so far to the client by means of the
        `entryAdded` notification.
        """
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Log.enable', _params)
        return None

    async def start_violations_report(self, *, config: List[ViolationSetting]) -> None:
        """
        start violation reporting.
        :param config: Configuration for violations.
        """
        _params: Dict[str, Any] = {}
        _params['config'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Log.ViolationSetting')), config)
        _result = await self._target.send('Log.startViolationsReport', _params)
        return None

    async def stop_violations_report(self) -> None:
        """Stop violation reporting."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Log.stopViolationsReport', _params)
        return None
