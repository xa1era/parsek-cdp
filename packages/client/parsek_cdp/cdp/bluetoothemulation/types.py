"""Custom types and enums for the BluetoothEmulation domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, register


@register("BluetoothEmulation.CentralState")
class CentralState(str, Enum):
    """Indicates the various states of Central."""
    ABSENT = 'absent'
    POWERED_OFF = 'powered-off'
    POWERED_ON = 'powered-on'


@register("BluetoothEmulation.GATTOperationType")
class GATTOperationType(str, Enum):
    """Indicates the various types of GATT event."""
    CONNECTION = 'connection'
    DISCOVERY = 'discovery'


@register("BluetoothEmulation.CharacteristicWriteType")
class CharacteristicWriteType(str, Enum):
    """Indicates the various types of characteristic write."""
    WRITE_DEFAULT_DEPRECATED = 'write-default-deprecated'
    WRITE_WITH_RESPONSE = 'write-with-response'
    WRITE_WITHOUT_RESPONSE = 'write-without-response'


@register("BluetoothEmulation.CharacteristicOperationType")
class CharacteristicOperationType(str, Enum):
    """Indicates the various types of characteristic operation."""
    READ = 'read'
    WRITE = 'write'
    SUBSCRIBE_TO_NOTIFICATIONS = 'subscribe-to-notifications'
    UNSUBSCRIBE_FROM_NOTIFICATIONS = 'unsubscribe-from-notifications'


@register("BluetoothEmulation.DescriptorOperationType")
class DescriptorOperationType(str, Enum):
    """Indicates the various types of descriptor operation."""
    READ = 'read'
    WRITE = 'write'


@register("BluetoothEmulation.ManufacturerData")
@dataclass
class ManufacturerData(DataType):
    """Stores the manufacturer data"""
    key: int
    data: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('key', 'key', False, 'primitive'),
        FieldMeta('data', 'data', False, 'primitive'),
    )


@register("BluetoothEmulation.ScanRecord")
@dataclass
class ScanRecord(DataType):
    """Stores the byte data of the advertisement packet sent by a Bluetooth device."""
    name: Optional[str] = None
    uuids: Optional[List[str]] = None
    appearance: Optional[int] = None
    tx_power: Optional[int] = None
    manufacturer_data: Optional[List[ManufacturerData]] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('name', 'name', True, 'primitive'),
        FieldMeta('uuids', 'uuids', True, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('appearance', 'appearance', True, 'primitive'),
        FieldMeta('tx_power', 'txPower', True, 'primitive'),
        FieldMeta('manufacturer_data', 'manufacturerData', True, 'array', inner=FieldMeta('', '', False, 'object', ref='BluetoothEmulation.ManufacturerData')),
    )


@register("BluetoothEmulation.ScanEntry")
@dataclass
class ScanEntry(DataType):
    """Stores the advertisement packet information that is sent by a Bluetooth device."""
    device_address: str
    rssi: int
    scan_record: ScanRecord
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('device_address', 'deviceAddress', False, 'primitive'),
        FieldMeta('rssi', 'rssi', False, 'primitive'),
        FieldMeta('scan_record', 'scanRecord', False, 'object', ref='BluetoothEmulation.ScanRecord'),
    )


@register("BluetoothEmulation.CharacteristicProperties")
@dataclass
class CharacteristicProperties(DataType):
    """
    Describes the properties of a characteristic. This follows Bluetooth Core
    Specification BT 4.2 Vol 3 Part G 3.3.1. Characteristic Properties.
    """
    broadcast: Optional[bool] = None
    read: Optional[bool] = None
    write_without_response: Optional[bool] = None
    write: Optional[bool] = None
    notify: Optional[bool] = None
    indicate: Optional[bool] = None
    authenticated_signed_writes: Optional[bool] = None
    extended_properties: Optional[bool] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('broadcast', 'broadcast', True, 'primitive'),
        FieldMeta('read', 'read', True, 'primitive'),
        FieldMeta('write_without_response', 'writeWithoutResponse', True, 'primitive'),
        FieldMeta('write', 'write', True, 'primitive'),
        FieldMeta('notify', 'notify', True, 'primitive'),
        FieldMeta('indicate', 'indicate', True, 'primitive'),
        FieldMeta('authenticated_signed_writes', 'authenticatedSignedWrites', True, 'primitive'),
        FieldMeta('extended_properties', 'extendedProperties', True, 'primitive'),
    )

__all__ = ["CentralState", "CharacteristicOperationType", "CharacteristicProperties", "CharacteristicWriteType", "DescriptorOperationType", "GATTOperationType", "ManufacturerData", "ScanEntry", "ScanRecord"]
