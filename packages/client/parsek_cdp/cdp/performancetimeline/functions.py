"""Commands for the PerformanceTimeline domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode


class PerformanceTimeline:
    """Commands of the PerformanceTimeline domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def enable(self, *, event_types: List[str]) -> None:
        """
        Previously buffered events would be reported before method returns.
        See also: timelineEventAdded
        :param event_types: The types of event to report, as specified in
        https://w3c.github.io/performance-timeline/#dom-performanceentry-entrytype
        The specified filter overrides any previous filters, passing empty
        filter disables recording.
        Note that not all types exposed to the web platform are currently supported.
        """
        _params: Dict[str, Any] = {}
        _params['eventTypes'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'primitive')), event_types)
        _result = await self._target.send('PerformanceTimeline.enable', _params)
        return None
