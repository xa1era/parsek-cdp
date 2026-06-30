"""Custom types and enums for the Media domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, register

if TYPE_CHECKING:
    from ..dom.types import BackendNodeId as DOM_BackendNodeId

type PlayerId = str  # Players will get an ID that is unique within the agent context.


type Timestamp = float


@register("Media.PlayerMessage")
@dataclass
class PlayerMessage(DataType):
    """
    Have one type per entry in MediaLogRecord::Type
    Corresponds to kMessage
    """
    level: Literal['error', 'warning', 'info', 'debug']
    message: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('level', 'level', False, 'primitive'),
        FieldMeta('message', 'message', False, 'primitive'),
    )


@register("Media.PlayerProperty")
@dataclass
class PlayerProperty(DataType):
    """Corresponds to kMediaPropertyChange"""
    name: str
    value: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('name', 'name', False, 'primitive'),
        FieldMeta('value', 'value', False, 'primitive'),
    )


@register("Media.PlayerEvent")
@dataclass
class PlayerEvent(DataType):
    """Corresponds to kMediaEventTriggered"""
    timestamp: Timestamp
    value: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('timestamp', 'timestamp', False, 'primitive'),
        FieldMeta('value', 'value', False, 'primitive'),
    )


@register("Media.PlayerErrorSourceLocation")
@dataclass
class PlayerErrorSourceLocation(DataType):
    """
    Represents logged source line numbers reported in an error.
    NOTE: file and line are from chromium c++ implementation code, not js.
    """
    file: str
    line: int
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('file', 'file', False, 'primitive'),
        FieldMeta('line', 'line', False, 'primitive'),
    )


@register("Media.PlayerError")
@dataclass
class PlayerError(DataType):
    """Corresponds to kMediaError"""
    error_type: str
    code: int
    stack: List[PlayerErrorSourceLocation]
    cause: List[PlayerError]
    data: Dict[str, Any]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('error_type', 'errorType', False, 'primitive'),
        FieldMeta('code', 'code', False, 'primitive'),
        FieldMeta('stack', 'stack', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Media.PlayerErrorSourceLocation')),
        FieldMeta('cause', 'cause', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Media.PlayerError')),
        FieldMeta('data', 'data', False, 'primitive'),
    )


@register("Media.Player")
@dataclass
class Player(DataType):
    player_id: PlayerId
    dom_node_id: Optional[DOM_BackendNodeId] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('player_id', 'playerId', False, 'primitive'),
        FieldMeta('dom_node_id', 'domNodeId', True, 'primitive'),
    )

__all__ = ["Player", "PlayerError", "PlayerErrorSourceLocation", "PlayerEvent", "PlayerId", "PlayerMessage", "PlayerProperty", "Timestamp"]
