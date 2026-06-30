"""Custom types and enums for the DeviceAccess domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, register


type RequestId = str  # Device request id.


type DeviceId = str  # A device id.


@register("DeviceAccess.PromptDevice")
@dataclass
class PromptDevice(DataType):
    """Device information displayed in a user prompt to select a device."""
    id: DeviceId
    name: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('id', 'id', False, 'primitive'),
        FieldMeta('name', 'name', False, 'primitive'),
    )

__all__ = ["DeviceId", "PromptDevice", "RequestId"]
