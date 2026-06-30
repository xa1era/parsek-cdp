"""Events for the Emulation domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import FieldMeta
from ..mixins.event import Event, register_event


@register_event("Emulation.virtualTimeBudgetExpired")
@dataclass
class VirtualTimeBudgetExpired(Event):
    """Notification sent after the virtual time budget for the current VirtualTimePolicy has run out."""
    __FIELDS__: ClassVar[tuple] = ()

__all__ = ["VirtualTimeBudgetExpired"]
