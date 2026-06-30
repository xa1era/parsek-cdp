"""Commands for the WebAudio domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode

if TYPE_CHECKING:
    from .types import (
        ContextRealtimeData,
        GraphObjectId,
    )

@dataclass
class GetRealtimeDataReturn(DataType):
    """Return value of :meth:`WebAudio.get_realtime_data`."""
    realtime_data: ContextRealtimeData
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('realtime_data', 'realtimeData', False, 'object', ref='WebAudio.ContextRealtimeData'),
    )


class WebAudio:
    """Commands of the WebAudio domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def enable(self) -> None:
        """Enables the WebAudio domain and starts sending context lifetime events."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('WebAudio.enable', _params)
        return None

    async def disable(self) -> None:
        """Disables the WebAudio domain."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('WebAudio.disable', _params)
        return None

    async def get_realtime_data(self, *, context_id: GraphObjectId) -> GetRealtimeDataReturn:
        """
        Fetch the realtime data from the registered contexts.
        :param context_id:
        """
        _params: Dict[str, Any] = {}
        _params['contextId'] = encode(FieldMeta('', '', False, 'primitive'), context_id)
        _result = await self._target.send('WebAudio.getRealtimeData', _params)
        return GetRealtimeDataReturn.from_json(_result)
