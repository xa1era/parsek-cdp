"""Events for the Target domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import FieldMeta
from ..mixins.event import Event, register_event

if TYPE_CHECKING:
    from .types import (
        SessionID,
        TargetID,
        TargetInfo,
    )

@register_event("Target.attachedToTarget")
@dataclass
class AttachedToTarget(Event):
    """Issued when attached to target because of auto-attach or `attachToTarget` command."""
    session_id: SessionID
    target_info: TargetInfo
    waiting_for_debugger: bool
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('session_id', 'sessionId', False, 'primitive'),
        FieldMeta('target_info', 'targetInfo', False, 'object', ref='Target.TargetInfo'),
        FieldMeta('waiting_for_debugger', 'waitingForDebugger', False, 'primitive'),
    )


@register_event("Target.detachedFromTarget")
@dataclass
class DetachedFromTarget(Event):
    """
    Issued when detached from target for any reason (including `detachFromTarget` command). Can be
    issued multiple times per target if multiple sessions have been attached to it.
    """
    session_id: SessionID
    target_id: Optional[TargetID] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('session_id', 'sessionId', False, 'primitive'),
        FieldMeta('target_id', 'targetId', True, 'primitive'),
    )


@register_event("Target.receivedMessageFromTarget")
@dataclass
class ReceivedMessageFromTarget(Event):
    """
    Notifies about a new protocol message received from the session (as reported in
    `attachedToTarget` event).
    """
    session_id: SessionID
    message: str
    target_id: Optional[TargetID] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('session_id', 'sessionId', False, 'primitive'),
        FieldMeta('message', 'message', False, 'primitive'),
        FieldMeta('target_id', 'targetId', True, 'primitive'),
    )


@register_event("Target.targetCreated")
@dataclass
class TargetCreated(Event):
    """Issued when a possible inspection target is created."""
    target_info: TargetInfo
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('target_info', 'targetInfo', False, 'object', ref='Target.TargetInfo'),
    )


@register_event("Target.targetDestroyed")
@dataclass
class TargetDestroyed(Event):
    """Issued when a target is destroyed."""
    target_id: TargetID
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('target_id', 'targetId', False, 'primitive'),
    )


@register_event("Target.targetCrashed")
@dataclass
class TargetCrashed(Event):
    """Issued when a target has crashed."""
    target_id: TargetID
    status: str
    error_code: int
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('target_id', 'targetId', False, 'primitive'),
        FieldMeta('status', 'status', False, 'primitive'),
        FieldMeta('error_code', 'errorCode', False, 'primitive'),
    )


@register_event("Target.targetInfoChanged")
@dataclass
class TargetInfoChanged(Event):
    """
    Issued when some information about a target has changed. This only happens between
    `targetCreated` and `targetDestroyed`.
    """
    target_info: TargetInfo
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('target_info', 'targetInfo', False, 'object', ref='Target.TargetInfo'),
    )

__all__ = ["AttachedToTarget", "DetachedFromTarget", "ReceivedMessageFromTarget", "TargetCrashed", "TargetCreated", "TargetDestroyed", "TargetInfoChanged"]
