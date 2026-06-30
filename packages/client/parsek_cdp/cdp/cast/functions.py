"""Commands for the Cast domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode


class Cast:
    """Commands of the Cast domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def enable(self, *, presentation_url: Optional[str] = None) -> None:
        """
        Starts observing for sinks that can be used for tab mirroring, and if set,
        sinks compatible with |presentationUrl| as well. When sinks are found, a
        |sinksUpdated| event is fired.
        Also starts observing for issue messages. When an issue is added or removed,
        an |issueUpdated| event is fired.
        :param presentation_url:
        """
        _params: Dict[str, Any] = {}
        if presentation_url is not None:
            _params['presentationUrl'] = encode(FieldMeta('', '', False, 'primitive'), presentation_url)
        _result = await self._target.send('Cast.enable', _params)
        return None

    async def disable(self) -> None:
        """Stops observing for sinks and issues."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Cast.disable', _params)
        return None

    async def set_sink_to_use(self, *, sink_name: str) -> None:
        """
        Sets a sink to be used when the web page requests the browser to choose a
        sink via Presentation API, Remote Playback API, or Cast SDK.
        :param sink_name:
        """
        _params: Dict[str, Any] = {}
        _params['sinkName'] = encode(FieldMeta('', '', False, 'primitive'), sink_name)
        _result = await self._target.send('Cast.setSinkToUse', _params)
        return None

    async def start_desktop_mirroring(self, *, sink_name: str) -> None:
        """
        Starts mirroring the desktop to the sink.
        :param sink_name:
        """
        _params: Dict[str, Any] = {}
        _params['sinkName'] = encode(FieldMeta('', '', False, 'primitive'), sink_name)
        _result = await self._target.send('Cast.startDesktopMirroring', _params)
        return None

    async def start_tab_mirroring(self, *, sink_name: str) -> None:
        """
        Starts mirroring the tab to the sink.
        :param sink_name:
        """
        _params: Dict[str, Any] = {}
        _params['sinkName'] = encode(FieldMeta('', '', False, 'primitive'), sink_name)
        _result = await self._target.send('Cast.startTabMirroring', _params)
        return None

    async def stop_casting(self, *, sink_name: str) -> None:
        """
        Stops the active Cast session on the sink.
        :param sink_name:
        """
        _params: Dict[str, Any] = {}
        _params['sinkName'] = encode(FieldMeta('', '', False, 'primitive'), sink_name)
        _result = await self._target.send('Cast.stopCasting', _params)
        return None
