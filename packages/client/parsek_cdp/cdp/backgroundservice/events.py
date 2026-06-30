"""Events for the BackgroundService domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import FieldMeta
from ..mixins.event import Event, register_event

if TYPE_CHECKING:
    from .types import (
        BackgroundServiceEvent,
        ServiceName,
    )

@register_event("BackgroundService.recordingStateChanged")
@dataclass
class RecordingStateChanged(Event):
    """Called when the recording state for the service has been updated."""
    is_recording: bool
    service: ServiceName
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('is_recording', 'isRecording', False, 'primitive'),
        FieldMeta('service', 'service', False, 'enum', ref='BackgroundService.ServiceName'),
    )


@register_event("BackgroundService.backgroundServiceEventReceived")
@dataclass
class BackgroundServiceEventReceived(Event):
    """
    Called with all existing backgroundServiceEvents when enabled, and all new
    events afterwards if enabled and recording.
    """
    background_service_event: BackgroundServiceEvent
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('background_service_event', 'backgroundServiceEvent', False, 'object', ref='BackgroundService.BackgroundServiceEvent'),
    )

__all__ = ["BackgroundServiceEventReceived", "RecordingStateChanged"]
