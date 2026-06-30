"""Events for the Media domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import FieldMeta
from ..mixins.event import Event, register_event

if TYPE_CHECKING:
    from .types import (
        Player,
        PlayerError,
        PlayerEvent,
        PlayerId,
        PlayerMessage,
        PlayerProperty,
    )

@register_event("Media.playerPropertiesChanged")
@dataclass
class PlayerPropertiesChanged(Event):
    """
    This can be called multiple times, and can be used to set / override /
    remove player properties. A null propValue indicates removal.
    """
    player_id: PlayerId
    properties: List[PlayerProperty]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('player_id', 'playerId', False, 'primitive'),
        FieldMeta('properties', 'properties', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Media.PlayerProperty')),
    )


@register_event("Media.playerEventsAdded")
@dataclass
class PlayerEventsAdded(Event):
    """
    Send events as a list, allowing them to be batched on the browser for less
    congestion. If batched, events must ALWAYS be in chronological order.
    """
    player_id: PlayerId
    events: List[PlayerEvent]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('player_id', 'playerId', False, 'primitive'),
        FieldMeta('events', 'events', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Media.PlayerEvent')),
    )


@register_event("Media.playerMessagesLogged")
@dataclass
class PlayerMessagesLogged(Event):
    """Send a list of any messages that need to be delivered."""
    player_id: PlayerId
    messages: List[PlayerMessage]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('player_id', 'playerId', False, 'primitive'),
        FieldMeta('messages', 'messages', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Media.PlayerMessage')),
    )


@register_event("Media.playerErrorsRaised")
@dataclass
class PlayerErrorsRaised(Event):
    """Send a list of any errors that need to be delivered."""
    player_id: PlayerId
    errors: List[PlayerError]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('player_id', 'playerId', False, 'primitive'),
        FieldMeta('errors', 'errors', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Media.PlayerError')),
    )


@register_event("Media.playerCreated")
@dataclass
class PlayerCreated(Event):
    """
    Called whenever a player is created, or when a new agent joins and receives
    a list of active players. If an agent is restored, it will receive one
    event for each active player.
    """
    player: Player
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('player', 'player', False, 'object', ref='Media.Player'),
    )

__all__ = ["PlayerCreated", "PlayerErrorsRaised", "PlayerEventsAdded", "PlayerMessagesLogged", "PlayerPropertiesChanged"]
