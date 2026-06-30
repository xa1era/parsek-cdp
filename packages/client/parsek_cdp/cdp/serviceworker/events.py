"""Events for the ServiceWorker domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import FieldMeta
from ..mixins.event import Event, register_event

if TYPE_CHECKING:
    from .types import (
        ServiceWorkerErrorMessage,
        ServiceWorkerRegistration,
        ServiceWorkerVersion,
    )

@register_event("ServiceWorker.workerErrorReported")
@dataclass
class WorkerErrorReported(Event):
    error_message: ServiceWorkerErrorMessage
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('error_message', 'errorMessage', False, 'object', ref='ServiceWorker.ServiceWorkerErrorMessage'),
    )


@register_event("ServiceWorker.workerRegistrationUpdated")
@dataclass
class WorkerRegistrationUpdated(Event):
    registrations: List[ServiceWorkerRegistration]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('registrations', 'registrations', False, 'array', inner=FieldMeta('', '', False, 'object', ref='ServiceWorker.ServiceWorkerRegistration')),
    )


@register_event("ServiceWorker.workerVersionUpdated")
@dataclass
class WorkerVersionUpdated(Event):
    versions: List[ServiceWorkerVersion]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('versions', 'versions', False, 'array', inner=FieldMeta('', '', False, 'object', ref='ServiceWorker.ServiceWorkerVersion')),
    )

__all__ = ["WorkerErrorReported", "WorkerRegistrationUpdated", "WorkerVersionUpdated"]
