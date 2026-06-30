"""Commands for the BackgroundService domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode

if TYPE_CHECKING:
    from .types import ServiceName

class BackgroundService:
    """Commands of the BackgroundService domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def start_observing(self, *, service: ServiceName) -> None:
        """
        Enables event updates for the service.
        :param service:
        """
        _params: Dict[str, Any] = {}
        _params['service'] = encode(FieldMeta('', '', False, 'enum', ref='BackgroundService.ServiceName'), service)
        _result = await self._target.send('BackgroundService.startObserving', _params)
        return None

    async def stop_observing(self, *, service: ServiceName) -> None:
        """
        Disables event updates for the service.
        :param service:
        """
        _params: Dict[str, Any] = {}
        _params['service'] = encode(FieldMeta('', '', False, 'enum', ref='BackgroundService.ServiceName'), service)
        _result = await self._target.send('BackgroundService.stopObserving', _params)
        return None

    async def set_recording(self, *, should_record: bool, service: ServiceName) -> None:
        """
        Set the recording state for the service.
        :param should_record:
        :param service:
        """
        _params: Dict[str, Any] = {}
        _params['shouldRecord'] = encode(FieldMeta('', '', False, 'primitive'), should_record)
        _params['service'] = encode(FieldMeta('', '', False, 'enum', ref='BackgroundService.ServiceName'), service)
        _result = await self._target.send('BackgroundService.setRecording', _params)
        return None

    async def clear_events(self, *, service: ServiceName) -> None:
        """
        Clears all stored data for the service.
        :param service:
        """
        _params: Dict[str, Any] = {}
        _params['service'] = encode(FieldMeta('', '', False, 'enum', ref='BackgroundService.ServiceName'), service)
        _result = await self._target.send('BackgroundService.clearEvents', _params)
        return None
