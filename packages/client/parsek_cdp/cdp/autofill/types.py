"""Custom types and enums for the Autofill domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, register

if TYPE_CHECKING:
    from ..dom.types import BackendNodeId as DOM_BackendNodeId
    from ..page.types import FrameId as Page_FrameId

@register("Autofill.CreditCard")
@dataclass
class CreditCard(DataType):
    number: str
    name: str
    expiry_month: str
    expiry_year: str
    cvc: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('number', 'number', False, 'primitive'),
        FieldMeta('name', 'name', False, 'primitive'),
        FieldMeta('expiry_month', 'expiryMonth', False, 'primitive'),
        FieldMeta('expiry_year', 'expiryYear', False, 'primitive'),
        FieldMeta('cvc', 'cvc', False, 'primitive'),
    )


@register("Autofill.AddressField")
@dataclass
class AddressField(DataType):
    name: str
    value: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('name', 'name', False, 'primitive'),
        FieldMeta('value', 'value', False, 'primitive'),
    )


@register("Autofill.AddressFields")
@dataclass
class AddressFields(DataType):
    """A list of address fields."""
    fields: List[AddressField]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('fields', 'fields', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Autofill.AddressField')),
    )


@register("Autofill.Address")
@dataclass
class Address(DataType):
    fields: List[AddressField]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('fields', 'fields', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Autofill.AddressField')),
    )


@register("Autofill.AddressUI")
@dataclass
class AddressUI(DataType):
    """
    Defines how an address can be displayed like in chrome://settings/addresses.
    Address UI is a two dimensional array, each inner array is an "address information line", and when rendered in a UI surface should be displayed as such.
    The following address UI for instance:
    [[{name: "GIVE_NAME", value: "Jon"}, {name: "FAMILY_NAME", value: "Doe"}], [{name: "CITY", value: "Munich"}, {name: "ZIP", value: "81456"}]]
    should allow the receiver to render:
    Jon Doe
    Munich 81456
    """
    address_fields: List[AddressFields]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('address_fields', 'addressFields', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Autofill.AddressFields')),
    )


@register("Autofill.FillingStrategy")
class FillingStrategy(str, Enum):
    """Specified whether a filled field was done so by using the html autocomplete attribute or autofill heuristics."""
    AUTOCOMPLETEATTRIBUTE = 'autocompleteAttribute'
    AUTOFILLINFERRED = 'autofillInferred'


@register("Autofill.FilledField")
@dataclass
class FilledField(DataType):
    html_type: str
    id: str
    name: str
    value: str
    autofill_type: str
    filling_strategy: FillingStrategy
    frame_id: Page_FrameId
    field_id: DOM_BackendNodeId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('html_type', 'htmlType', False, 'primitive'),
        FieldMeta('id', 'id', False, 'primitive'),
        FieldMeta('name', 'name', False, 'primitive'),
        FieldMeta('value', 'value', False, 'primitive'),
        FieldMeta('autofill_type', 'autofillType', False, 'primitive'),
        FieldMeta('filling_strategy', 'fillingStrategy', False, 'enum', ref='Autofill.FillingStrategy'),
        FieldMeta('frame_id', 'frameId', False, 'primitive'),
        FieldMeta('field_id', 'fieldId', False, 'primitive'),
    )

__all__ = ["Address", "AddressField", "AddressFields", "AddressUI", "CreditCard", "FilledField", "FillingStrategy"]
