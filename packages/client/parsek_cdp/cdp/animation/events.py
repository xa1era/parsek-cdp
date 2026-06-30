"""Events for the Animation domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import FieldMeta
from ..mixins.event import Event, register_event

if TYPE_CHECKING:
    from .types import Animation

@register_event("Animation.animationCanceled")
@dataclass
class AnimationCanceled(Event):
    """Event for when an animation has been cancelled."""
    id: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('id', 'id', False, 'primitive'),
    )


@register_event("Animation.animationCreated")
@dataclass
class AnimationCreated(Event):
    """Event for each animation that has been created."""
    id: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('id', 'id', False, 'primitive'),
    )


@register_event("Animation.animationStarted")
@dataclass
class AnimationStarted(Event):
    """Event for animation that has been started."""
    animation: Animation
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('animation', 'animation', False, 'object', ref='Animation.Animation'),
    )


@register_event("Animation.animationUpdated")
@dataclass
class AnimationUpdated(Event):
    """Event for animation that has been updated."""
    animation: Animation
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('animation', 'animation', False, 'object', ref='Animation.Animation'),
    )

__all__ = ["AnimationCanceled", "AnimationCreated", "AnimationStarted", "AnimationUpdated"]
