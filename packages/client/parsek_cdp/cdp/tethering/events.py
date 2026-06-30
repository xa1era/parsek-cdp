"""Events for the Tethering domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import FieldMeta
from ..mixins.event import Event, register_event


@register_event("Tethering.accepted")
@dataclass
class Accepted(Event):
    """Informs that port was successfully bound and got a specified connection id."""
    port: int
    connection_id: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('port', 'port', False, 'primitive'),
        FieldMeta('connection_id', 'connectionId', False, 'primitive'),
    )

__all__ = ["Accepted"]
