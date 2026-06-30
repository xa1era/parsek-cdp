"""Events for the Autofill domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import FieldMeta
from ..mixins.event import Event, register_event

if TYPE_CHECKING:
    from .types import (
        AddressUI,
        FilledField,
    )

@register_event("Autofill.addressFormFilled")
@dataclass
class AddressFormFilled(Event):
    """Emitted when an address form is filled."""
    filled_fields: List[FilledField]
    address_ui: AddressUI
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('filled_fields', 'filledFields', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Autofill.FilledField')),
        FieldMeta('address_ui', 'addressUi', False, 'object', ref='Autofill.AddressUI'),
    )

__all__ = ["AddressFormFilled"]
