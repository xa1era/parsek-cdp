"""Events for the Profiler domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import FieldMeta
from ..mixins.event import Event, register_event

if TYPE_CHECKING:
    from .types import (
        Profile,
        ScriptCoverage,
    )
    from ..debugger.types import Location as Debugger_Location

@register_event("Profiler.consoleProfileFinished")
@dataclass
class ConsoleProfileFinished(Event):
    id: str
    location: Debugger_Location
    profile: Profile
    title: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('id', 'id', False, 'primitive'),
        FieldMeta('location', 'location', False, 'object', ref='Debugger.Location'),
        FieldMeta('profile', 'profile', False, 'object', ref='Profiler.Profile'),
        FieldMeta('title', 'title', True, 'primitive'),
    )


@register_event("Profiler.consoleProfileStarted")
@dataclass
class ConsoleProfileStarted(Event):
    """Sent when new profile recording is started using console.profile() call."""
    id: str
    location: Debugger_Location
    title: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('id', 'id', False, 'primitive'),
        FieldMeta('location', 'location', False, 'object', ref='Debugger.Location'),
        FieldMeta('title', 'title', True, 'primitive'),
    )


@register_event("Profiler.preciseCoverageDeltaUpdate")
@dataclass
class PreciseCoverageDeltaUpdate(Event):
    """
    Reports coverage delta since the last poll (either from an event like this, or from
    `takePreciseCoverage` for the current isolate. May only be sent if precise code
    coverage has been started. This event can be trigged by the embedder to, for example,
    trigger collection of coverage data immediately at a certain point in time.
    """
    timestamp: float
    occasion: str
    result: List[ScriptCoverage]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('timestamp', 'timestamp', False, 'primitive'),
        FieldMeta('occasion', 'occasion', False, 'primitive'),
        FieldMeta('result', 'result', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Profiler.ScriptCoverage')),
    )

__all__ = ["ConsoleProfileFinished", "ConsoleProfileStarted", "PreciseCoverageDeltaUpdate"]
