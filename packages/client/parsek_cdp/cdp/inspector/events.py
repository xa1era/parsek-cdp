"""Events for the Inspector domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import FieldMeta
from ..mixins.event import Event, register_event


@register_event("Inspector.detached")
@dataclass
class Detached(Event):
    """Fired when remote debugging connection is about to be terminated. Contains detach reason."""
    reason: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('reason', 'reason', False, 'primitive'),
    )


@register_event("Inspector.targetCrashed")
@dataclass
class TargetCrashed(Event):
    """Fired when debugging target has crashed"""
    __FIELDS__: ClassVar[tuple] = ()


@register_event("Inspector.targetReloadedAfterCrash")
@dataclass
class TargetReloadedAfterCrash(Event):
    """Fired when debugging target has reloaded after crash"""
    __FIELDS__: ClassVar[tuple] = ()


@register_event("Inspector.workerScriptLoaded")
@dataclass
class WorkerScriptLoaded(Event):
    """Fired on worker targets when main worker script and any imported scripts have been evaluated."""
    __FIELDS__: ClassVar[tuple] = ()

__all__ = ["Detached", "TargetCrashed", "TargetReloadedAfterCrash", "WorkerScriptLoaded"]
