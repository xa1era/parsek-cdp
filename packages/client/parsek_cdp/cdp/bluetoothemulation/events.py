"""Events for the BluetoothEmulation domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import FieldMeta
from ..mixins.event import Event, register_event

if TYPE_CHECKING:
    from .types import (
        CharacteristicOperationType,
        CharacteristicWriteType,
        DescriptorOperationType,
        GATTOperationType,
    )

@register_event("BluetoothEmulation.gattOperationReceived")
@dataclass
class GattOperationReceived(Event):
    """
    Event for when a GATT operation of |type| to the peripheral with |address|
    happened.
    """
    address: str
    type_: GATTOperationType
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('address', 'address', False, 'primitive'),
        FieldMeta('type_', 'type', False, 'enum', ref='BluetoothEmulation.GATTOperationType'),
    )


@register_event("BluetoothEmulation.characteristicOperationReceived")
@dataclass
class CharacteristicOperationReceived(Event):
    """
    Event for when a characteristic operation of |type| to the characteristic
    respresented by |characteristicId| happened. |data| and |writeType| is
    expected to exist when |type| is write.
    """
    characteristic_id: str
    type_: CharacteristicOperationType
    data: Optional[str] = None
    write_type: Optional[CharacteristicWriteType] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('characteristic_id', 'characteristicId', False, 'primitive'),
        FieldMeta('type_', 'type', False, 'enum', ref='BluetoothEmulation.CharacteristicOperationType'),
        FieldMeta('data', 'data', True, 'primitive'),
        FieldMeta('write_type', 'writeType', True, 'enum', ref='BluetoothEmulation.CharacteristicWriteType'),
    )


@register_event("BluetoothEmulation.descriptorOperationReceived")
@dataclass
class DescriptorOperationReceived(Event):
    """
    Event for when a descriptor operation of |type| to the descriptor
    respresented by |descriptorId| happened. |data| is expected to exist when
    |type| is write.
    """
    descriptor_id: str
    type_: DescriptorOperationType
    data: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('descriptor_id', 'descriptorId', False, 'primitive'),
        FieldMeta('type_', 'type', False, 'enum', ref='BluetoothEmulation.DescriptorOperationType'),
        FieldMeta('data', 'data', True, 'primitive'),
    )

__all__ = ["CharacteristicOperationReceived", "DescriptorOperationReceived", "GattOperationReceived"]
