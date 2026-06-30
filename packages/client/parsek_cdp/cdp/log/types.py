"""Custom types and enums for the Log domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, register

if TYPE_CHECKING:
    from ..network.types import RequestId as Network_RequestId
    from ..runtime.types import RemoteObject as Runtime_RemoteObject
    from ..runtime.types import StackTrace as Runtime_StackTrace
    from ..runtime.types import Timestamp as Runtime_Timestamp

@register("Log.LogEntry")
@dataclass
class LogEntry(DataType):
    """Log entry."""
    source: Literal['xml', 'javascript', 'network', 'storage', 'appcache', 'rendering', 'security', 'deprecation', 'worker', 'violation', 'intervention', 'recommendation', 'other']
    level: Literal['verbose', 'info', 'warning', 'error']
    text: str
    timestamp: Runtime_Timestamp
    category: Optional[Literal['cors']] = None
    url: Optional[str] = None
    line_number: Optional[int] = None
    stack_trace: Optional[Runtime_StackTrace] = None
    network_request_id: Optional[Network_RequestId] = None
    worker_id: Optional[str] = None
    args: Optional[List[Runtime_RemoteObject]] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('source', 'source', False, 'primitive'),
        FieldMeta('level', 'level', False, 'primitive'),
        FieldMeta('text', 'text', False, 'primitive'),
        FieldMeta('timestamp', 'timestamp', False, 'primitive'),
        FieldMeta('category', 'category', True, 'primitive'),
        FieldMeta('url', 'url', True, 'primitive'),
        FieldMeta('line_number', 'lineNumber', True, 'primitive'),
        FieldMeta('stack_trace', 'stackTrace', True, 'object', ref='Runtime.StackTrace'),
        FieldMeta('network_request_id', 'networkRequestId', True, 'primitive'),
        FieldMeta('worker_id', 'workerId', True, 'primitive'),
        FieldMeta('args', 'args', True, 'array', inner=FieldMeta('', '', False, 'object', ref='Runtime.RemoteObject')),
    )


@register("Log.ViolationSetting")
@dataclass
class ViolationSetting(DataType):
    """Violation configuration setting."""
    name: Literal['longTask', 'longLayout', 'blockedEvent', 'blockedParser', 'discouragedAPIUse', 'handler', 'recurringHandler']
    threshold: float
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('name', 'name', False, 'primitive'),
        FieldMeta('threshold', 'threshold', False, 'primitive'),
    )

__all__ = ["LogEntry", "ViolationSetting"]
