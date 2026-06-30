"""Custom types and enums for the BackgroundService domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, register

if TYPE_CHECKING:
    from ..network.types import TimeSinceEpoch as Network_TimeSinceEpoch
    from ..serviceworker.types import RegistrationID as ServiceWorker_RegistrationID

@register("BackgroundService.ServiceName")
class ServiceName(str, Enum):
    """
    The Background Service that will be associated with the commands/events.
    Every Background Service operates independently, but they share the same
    API.
    """
    BACKGROUNDFETCH = 'backgroundFetch'
    BACKGROUNDSYNC = 'backgroundSync'
    PUSHMESSAGING = 'pushMessaging'
    NOTIFICATIONS = 'notifications'
    PAYMENTHANDLER = 'paymentHandler'
    PERIODICBACKGROUNDSYNC = 'periodicBackgroundSync'


@register("BackgroundService.EventMetadata")
@dataclass
class EventMetadata(DataType):
    """A key-value pair for additional event information to pass along."""
    key: str
    value: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('key', 'key', False, 'primitive'),
        FieldMeta('value', 'value', False, 'primitive'),
    )


@register("BackgroundService.BackgroundServiceEvent")
@dataclass
class BackgroundServiceEvent(DataType):
    timestamp: Network_TimeSinceEpoch
    origin: str
    service_worker_registration_id: ServiceWorker_RegistrationID
    service: ServiceName
    event_name: str
    instance_id: str
    event_metadata: List[EventMetadata]
    storage_key: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('timestamp', 'timestamp', False, 'primitive'),
        FieldMeta('origin', 'origin', False, 'primitive'),
        FieldMeta('service_worker_registration_id', 'serviceWorkerRegistrationId', False, 'primitive'),
        FieldMeta('service', 'service', False, 'enum', ref='BackgroundService.ServiceName'),
        FieldMeta('event_name', 'eventName', False, 'primitive'),
        FieldMeta('instance_id', 'instanceId', False, 'primitive'),
        FieldMeta('event_metadata', 'eventMetadata', False, 'array', inner=FieldMeta('', '', False, 'object', ref='BackgroundService.EventMetadata')),
        FieldMeta('storage_key', 'storageKey', False, 'primitive'),
    )

__all__ = ["BackgroundServiceEvent", "EventMetadata", "ServiceName"]
