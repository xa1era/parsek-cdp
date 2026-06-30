"""Commands for the EventBreakpoints domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode


class EventBreakpoints:
    """Commands of the EventBreakpoints domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def set_instrumentation_breakpoint(self, *, event_name: str) -> None:
        """
        Sets breakpoint on particular native event.
        :param event_name: Instrumentation name to stop on.
        """
        _params: Dict[str, Any] = {}
        _params['eventName'] = encode(FieldMeta('', '', False, 'primitive'), event_name)
        _result = await self._target.send('EventBreakpoints.setInstrumentationBreakpoint', _params)
        return None

    async def remove_instrumentation_breakpoint(self, *, event_name: str) -> None:
        """
        Removes breakpoint on particular native event.
        :param event_name: Instrumentation name to stop on.
        """
        _params: Dict[str, Any] = {}
        _params['eventName'] = encode(FieldMeta('', '', False, 'primitive'), event_name)
        _result = await self._target.send('EventBreakpoints.removeInstrumentationBreakpoint', _params)
        return None

    async def disable(self) -> None:
        """Removes all breakpoints"""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('EventBreakpoints.disable', _params)
        return None
