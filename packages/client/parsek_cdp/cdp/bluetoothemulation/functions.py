"""Commands for the BluetoothEmulation domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode

if TYPE_CHECKING:
    from .types import (
        CentralState,
        CharacteristicOperationType,
        CharacteristicProperties,
        DescriptorOperationType,
        GATTOperationType,
        ManufacturerData,
        ScanEntry,
    )

@dataclass
class AddServiceReturn(DataType):
    """Return value of :meth:`BluetoothEmulation.add_service`."""
    service_id: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('service_id', 'serviceId', False, 'primitive'),
    )


@dataclass
class AddCharacteristicReturn(DataType):
    """Return value of :meth:`BluetoothEmulation.add_characteristic`."""
    characteristic_id: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('characteristic_id', 'characteristicId', False, 'primitive'),
    )


@dataclass
class AddDescriptorReturn(DataType):
    """Return value of :meth:`BluetoothEmulation.add_descriptor`."""
    descriptor_id: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('descriptor_id', 'descriptorId', False, 'primitive'),
    )


class BluetoothEmulation:
    """Commands of the BluetoothEmulation domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def enable(self, *, state: CentralState, le_supported: bool) -> None:
        """
        Enable the BluetoothEmulation domain.
        :param state: State of the simulated central.
        :param le_supported: If the simulated central supports low-energy.
        """
        _params: Dict[str, Any] = {}
        _params['state'] = encode(FieldMeta('', '', False, 'enum', ref='BluetoothEmulation.CentralState'), state)
        _params['leSupported'] = encode(FieldMeta('', '', False, 'primitive'), le_supported)
        _result = await self._target.send('BluetoothEmulation.enable', _params)
        return None

    async def set_simulated_central_state(self, *, state: CentralState) -> None:
        """
        Set the state of the simulated central.
        :param state: State of the simulated central.
        """
        _params: Dict[str, Any] = {}
        _params['state'] = encode(FieldMeta('', '', False, 'enum', ref='BluetoothEmulation.CentralState'), state)
        _result = await self._target.send('BluetoothEmulation.setSimulatedCentralState', _params)
        return None

    async def disable(self) -> None:
        """Disable the BluetoothEmulation domain."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('BluetoothEmulation.disable', _params)
        return None

    async def simulate_preconnected_peripheral(self, *, address: str, name: str, manufacturer_data: List[ManufacturerData], known_service_uuids: List[str]) -> None:
        """
        Simulates a peripheral with |address|, |name| and |knownServiceUuids|
        that has already been connected to the system.
        :param address:
        :param name:
        :param manufacturer_data:
        :param known_service_uuids:
        """
        _params: Dict[str, Any] = {}
        _params['address'] = encode(FieldMeta('', '', False, 'primitive'), address)
        _params['name'] = encode(FieldMeta('', '', False, 'primitive'), name)
        _params['manufacturerData'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'object', ref='BluetoothEmulation.ManufacturerData')), manufacturer_data)
        _params['knownServiceUuids'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'primitive')), known_service_uuids)
        _result = await self._target.send('BluetoothEmulation.simulatePreconnectedPeripheral', _params)
        return None

    async def simulate_advertisement(self, *, entry: ScanEntry) -> None:
        """
        Simulates an advertisement packet described in |entry| being received by
        the central.
        :param entry:
        """
        _params: Dict[str, Any] = {}
        _params['entry'] = encode(FieldMeta('', '', False, 'object', ref='BluetoothEmulation.ScanEntry'), entry)
        _result = await self._target.send('BluetoothEmulation.simulateAdvertisement', _params)
        return None

    async def simulate_gatt_operation_response(self, *, address: str, type_: GATTOperationType, code: int) -> None:
        """
        Simulates the response code from the peripheral with |address| for a
        GATT operation of |type|. The |code| value follows the HCI Error Codes from
        Bluetooth Core Specification Vol 2 Part D 1.3 List Of Error Codes.
        :param address:
        :param type_:
        :param code:
        """
        _params: Dict[str, Any] = {}
        _params['address'] = encode(FieldMeta('', '', False, 'primitive'), address)
        _params['type'] = encode(FieldMeta('', '', False, 'enum', ref='BluetoothEmulation.GATTOperationType'), type_)
        _params['code'] = encode(FieldMeta('', '', False, 'primitive'), code)
        _result = await self._target.send('BluetoothEmulation.simulateGATTOperationResponse', _params)
        return None

    async def simulate_characteristic_operation_response(self, *, characteristic_id: str, type_: CharacteristicOperationType, code: int, data: Optional[str] = None) -> None:
        """
        Simulates the response from the characteristic with |characteristicId| for a
        characteristic operation of |type|. The |code| value follows the Error
        Codes from Bluetooth Core Specification Vol 3 Part F 3.4.1.1 Error Response.
        The |data| is expected to exist when simulating a successful read operation
        response.
        :param characteristic_id:
        :param type_:
        :param code:
        :param data:
        """
        _params: Dict[str, Any] = {}
        _params['characteristicId'] = encode(FieldMeta('', '', False, 'primitive'), characteristic_id)
        _params['type'] = encode(FieldMeta('', '', False, 'enum', ref='BluetoothEmulation.CharacteristicOperationType'), type_)
        _params['code'] = encode(FieldMeta('', '', False, 'primitive'), code)
        if data is not None:
            _params['data'] = encode(FieldMeta('', '', False, 'primitive'), data)
        _result = await self._target.send('BluetoothEmulation.simulateCharacteristicOperationResponse', _params)
        return None

    async def simulate_descriptor_operation_response(self, *, descriptor_id: str, type_: DescriptorOperationType, code: int, data: Optional[str] = None) -> None:
        """
        Simulates the response from the descriptor with |descriptorId| for a
        descriptor operation of |type|. The |code| value follows the Error
        Codes from Bluetooth Core Specification Vol 3 Part F 3.4.1.1 Error Response.
        The |data| is expected to exist when simulating a successful read operation
        response.
        :param descriptor_id:
        :param type_:
        :param code:
        :param data:
        """
        _params: Dict[str, Any] = {}
        _params['descriptorId'] = encode(FieldMeta('', '', False, 'primitive'), descriptor_id)
        _params['type'] = encode(FieldMeta('', '', False, 'enum', ref='BluetoothEmulation.DescriptorOperationType'), type_)
        _params['code'] = encode(FieldMeta('', '', False, 'primitive'), code)
        if data is not None:
            _params['data'] = encode(FieldMeta('', '', False, 'primitive'), data)
        _result = await self._target.send('BluetoothEmulation.simulateDescriptorOperationResponse', _params)
        return None

    async def add_service(self, *, address: str, service_uuid: str) -> AddServiceReturn:
        """
        Adds a service with |serviceUuid| to the peripheral with |address|.
        :param address:
        :param service_uuid:
        """
        _params: Dict[str, Any] = {}
        _params['address'] = encode(FieldMeta('', '', False, 'primitive'), address)
        _params['serviceUuid'] = encode(FieldMeta('', '', False, 'primitive'), service_uuid)
        _result = await self._target.send('BluetoothEmulation.addService', _params)
        return AddServiceReturn.from_json(_result)

    async def remove_service(self, *, service_id: str) -> None:
        """
        Removes the service respresented by |serviceId| from the simulated central.
        :param service_id:
        """
        _params: Dict[str, Any] = {}
        _params['serviceId'] = encode(FieldMeta('', '', False, 'primitive'), service_id)
        _result = await self._target.send('BluetoothEmulation.removeService', _params)
        return None

    async def add_characteristic(self, *, service_id: str, characteristic_uuid: str, properties: CharacteristicProperties) -> AddCharacteristicReturn:
        """
        Adds a characteristic with |characteristicUuid| and |properties| to the
        service represented by |serviceId|.
        :param service_id:
        :param characteristic_uuid:
        :param properties:
        """
        _params: Dict[str, Any] = {}
        _params['serviceId'] = encode(FieldMeta('', '', False, 'primitive'), service_id)
        _params['characteristicUuid'] = encode(FieldMeta('', '', False, 'primitive'), characteristic_uuid)
        _params['properties'] = encode(FieldMeta('', '', False, 'object', ref='BluetoothEmulation.CharacteristicProperties'), properties)
        _result = await self._target.send('BluetoothEmulation.addCharacteristic', _params)
        return AddCharacteristicReturn.from_json(_result)

    async def remove_characteristic(self, *, characteristic_id: str) -> None:
        """
        Removes the characteristic respresented by |characteristicId| from the
        simulated central.
        :param characteristic_id:
        """
        _params: Dict[str, Any] = {}
        _params['characteristicId'] = encode(FieldMeta('', '', False, 'primitive'), characteristic_id)
        _result = await self._target.send('BluetoothEmulation.removeCharacteristic', _params)
        return None

    async def add_descriptor(self, *, characteristic_id: str, descriptor_uuid: str) -> AddDescriptorReturn:
        """
        Adds a descriptor with |descriptorUuid| to the characteristic respresented
        by |characteristicId|.
        :param characteristic_id:
        :param descriptor_uuid:
        """
        _params: Dict[str, Any] = {}
        _params['characteristicId'] = encode(FieldMeta('', '', False, 'primitive'), characteristic_id)
        _params['descriptorUuid'] = encode(FieldMeta('', '', False, 'primitive'), descriptor_uuid)
        _result = await self._target.send('BluetoothEmulation.addDescriptor', _params)
        return AddDescriptorReturn.from_json(_result)

    async def remove_descriptor(self, *, descriptor_id: str) -> None:
        """
        Removes the descriptor with |descriptorId| from the simulated central.
        :param descriptor_id:
        """
        _params: Dict[str, Any] = {}
        _params['descriptorId'] = encode(FieldMeta('', '', False, 'primitive'), descriptor_id)
        _result = await self._target.send('BluetoothEmulation.removeDescriptor', _params)
        return None

    async def simulate_gatt_disconnection(self, *, address: str) -> None:
        """
        Simulates a GATT disconnection from the peripheral with |address|.
        :param address:
        """
        _params: Dict[str, Any] = {}
        _params['address'] = encode(FieldMeta('', '', False, 'primitive'), address)
        _result = await self._target.send('BluetoothEmulation.simulateGATTDisconnection', _params)
        return None
