"""Events for the DeviceAccess domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import FieldMeta
from ..mixins.event import Event, register_event

if TYPE_CHECKING:
    from .types import (
        PromptDevice,
        RequestId,
    )

@register_event("DeviceAccess.deviceRequestPrompted")
@dataclass
class DeviceRequestPrompted(Event):
    """
    A device request opened a user prompt to select a device. Respond with the
    selectPrompt or cancelPrompt command.
    """
    id: RequestId
    devices: List[PromptDevice]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('id', 'id', False, 'primitive'),
        FieldMeta('devices', 'devices', False, 'array', inner=FieldMeta('', '', False, 'object', ref='DeviceAccess.PromptDevice')),
    )

__all__ = ["DeviceRequestPrompted"]
