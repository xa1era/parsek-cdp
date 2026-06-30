"""Custom types and enums for the ServiceWorker domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, register

if TYPE_CHECKING:
    from ..target.types import TargetID as Target_TargetID

type RegistrationID = str


@register("ServiceWorker.ServiceWorkerRegistration")
@dataclass
class ServiceWorkerRegistration(DataType):
    """ServiceWorker registration."""
    registration_id: RegistrationID
    scope_url: str
    is_deleted: bool
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('registration_id', 'registrationId', False, 'primitive'),
        FieldMeta('scope_url', 'scopeURL', False, 'primitive'),
        FieldMeta('is_deleted', 'isDeleted', False, 'primitive'),
    )


@register("ServiceWorker.ServiceWorkerVersionRunningStatus")
class ServiceWorkerVersionRunningStatus(str, Enum):
    STOPPED = 'stopped'
    STARTING = 'starting'
    RUNNING = 'running'
    STOPPING = 'stopping'


@register("ServiceWorker.ServiceWorkerVersionStatus")
class ServiceWorkerVersionStatus(str, Enum):
    NEW = 'new'
    INSTALLING = 'installing'
    INSTALLED = 'installed'
    ACTIVATING = 'activating'
    ACTIVATED = 'activated'
    REDUNDANT = 'redundant'


@register("ServiceWorker.ServiceWorkerVersion")
@dataclass
class ServiceWorkerVersion(DataType):
    """ServiceWorker version."""
    version_id: str
    registration_id: RegistrationID
    script_url: str
    running_status: ServiceWorkerVersionRunningStatus
    status: ServiceWorkerVersionStatus
    script_last_modified: Optional[float] = None
    script_response_time: Optional[float] = None
    controlled_clients: Optional[List[Target_TargetID]] = None
    target_id: Optional[Target_TargetID] = None
    router_rules: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('version_id', 'versionId', False, 'primitive'),
        FieldMeta('registration_id', 'registrationId', False, 'primitive'),
        FieldMeta('script_url', 'scriptURL', False, 'primitive'),
        FieldMeta('running_status', 'runningStatus', False, 'enum', ref='ServiceWorker.ServiceWorkerVersionRunningStatus'),
        FieldMeta('status', 'status', False, 'enum', ref='ServiceWorker.ServiceWorkerVersionStatus'),
        FieldMeta('script_last_modified', 'scriptLastModified', True, 'primitive'),
        FieldMeta('script_response_time', 'scriptResponseTime', True, 'primitive'),
        FieldMeta('controlled_clients', 'controlledClients', True, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('target_id', 'targetId', True, 'primitive'),
        FieldMeta('router_rules', 'routerRules', True, 'primitive'),
    )


@register("ServiceWorker.ServiceWorkerErrorMessage")
@dataclass
class ServiceWorkerErrorMessage(DataType):
    """ServiceWorker error message."""
    error_message: str
    registration_id: RegistrationID
    version_id: str
    source_url: str
    line_number: int
    column_number: int
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('error_message', 'errorMessage', False, 'primitive'),
        FieldMeta('registration_id', 'registrationId', False, 'primitive'),
        FieldMeta('version_id', 'versionId', False, 'primitive'),
        FieldMeta('source_url', 'sourceURL', False, 'primitive'),
        FieldMeta('line_number', 'lineNumber', False, 'primitive'),
        FieldMeta('column_number', 'columnNumber', False, 'primitive'),
    )

__all__ = ["RegistrationID", "ServiceWorkerErrorMessage", "ServiceWorkerRegistration", "ServiceWorkerVersion", "ServiceWorkerVersionRunningStatus", "ServiceWorkerVersionStatus"]
