"""Custom types and enums for the DOMDebugger domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, register

if TYPE_CHECKING:
    from ..dom.types import BackendNodeId as DOM_BackendNodeId
    from ..runtime.types import RemoteObject as Runtime_RemoteObject
    from ..runtime.types import ScriptId as Runtime_ScriptId

@register("DOMDebugger.DOMBreakpointType")
class DOMBreakpointType(str, Enum):
    """DOM breakpoint type."""
    SUBTREE_MODIFIED = 'subtree-modified'
    ATTRIBUTE_MODIFIED = 'attribute-modified'
    NODE_REMOVED = 'node-removed'


@register("DOMDebugger.CSPViolationType")
class CSPViolationType(str, Enum):
    """CSP Violation type."""
    TRUSTEDTYPE_SINK_VIOLATION = 'trustedtype-sink-violation'
    TRUSTEDTYPE_POLICY_VIOLATION = 'trustedtype-policy-violation'


@register("DOMDebugger.EventListener")
@dataclass
class EventListener(DataType):
    """Object event listener."""
    type_: str
    use_capture: bool
    passive: bool
    once: bool
    script_id: Runtime_ScriptId
    line_number: int
    column_number: int
    handler: Optional[Runtime_RemoteObject] = None
    original_handler: Optional[Runtime_RemoteObject] = None
    backend_node_id: Optional[DOM_BackendNodeId] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('type_', 'type', False, 'primitive'),
        FieldMeta('use_capture', 'useCapture', False, 'primitive'),
        FieldMeta('passive', 'passive', False, 'primitive'),
        FieldMeta('once', 'once', False, 'primitive'),
        FieldMeta('script_id', 'scriptId', False, 'primitive'),
        FieldMeta('line_number', 'lineNumber', False, 'primitive'),
        FieldMeta('column_number', 'columnNumber', False, 'primitive'),
        FieldMeta('handler', 'handler', True, 'object', ref='Runtime.RemoteObject'),
        FieldMeta('original_handler', 'originalHandler', True, 'object', ref='Runtime.RemoteObject'),
        FieldMeta('backend_node_id', 'backendNodeId', True, 'primitive'),
    )

__all__ = ["CSPViolationType", "DOMBreakpointType", "EventListener"]
