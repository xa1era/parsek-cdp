"""Events for the Runtime domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import FieldMeta
from ..mixins.event import Event, register_event

if TYPE_CHECKING:
    from .types import (
        ExceptionDetails,
        ExecutionContextDescription,
        ExecutionContextId,
        RemoteObject,
        StackTrace,
        Timestamp,
    )

@register_event("Runtime.bindingCalled")
@dataclass
class BindingCalled(Event):
    """Notification is issued every time when binding is called."""
    name: str
    payload: str
    execution_context_id: ExecutionContextId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('name', 'name', False, 'primitive'),
        FieldMeta('payload', 'payload', False, 'primitive'),
        FieldMeta('execution_context_id', 'executionContextId', False, 'primitive'),
    )


@register_event("Runtime.consoleAPICalled")
@dataclass
class ConsoleAPICalled(Event):
    """Issued when console API was called."""
    type_: Literal['log', 'debug', 'info', 'error', 'warning', 'dir', 'dirxml', 'table', 'trace', 'clear', 'startGroup', 'startGroupCollapsed', 'endGroup', 'assert', 'profile', 'profileEnd', 'count', 'timeEnd']
    args: List[RemoteObject]
    execution_context_id: ExecutionContextId
    timestamp: Timestamp
    stack_trace: Optional[StackTrace] = None
    context: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('type_', 'type', False, 'primitive'),
        FieldMeta('args', 'args', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Runtime.RemoteObject')),
        FieldMeta('execution_context_id', 'executionContextId', False, 'primitive'),
        FieldMeta('timestamp', 'timestamp', False, 'primitive'),
        FieldMeta('stack_trace', 'stackTrace', True, 'object', ref='Runtime.StackTrace'),
        FieldMeta('context', 'context', True, 'primitive'),
    )


@register_event("Runtime.exceptionRevoked")
@dataclass
class ExceptionRevoked(Event):
    """Issued when unhandled exception was revoked."""
    reason: str
    exception_id: int
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('reason', 'reason', False, 'primitive'),
        FieldMeta('exception_id', 'exceptionId', False, 'primitive'),
    )


@register_event("Runtime.exceptionThrown")
@dataclass
class ExceptionThrown(Event):
    """Issued when exception was thrown and unhandled."""
    timestamp: Timestamp
    exception_details: ExceptionDetails
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('timestamp', 'timestamp', False, 'primitive'),
        FieldMeta('exception_details', 'exceptionDetails', False, 'object', ref='Runtime.ExceptionDetails'),
    )


@register_event("Runtime.executionContextCreated")
@dataclass
class ExecutionContextCreated(Event):
    """Issued when new execution context is created."""
    context: ExecutionContextDescription
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('context', 'context', False, 'object', ref='Runtime.ExecutionContextDescription'),
    )


@register_event("Runtime.executionContextDestroyed")
@dataclass
class ExecutionContextDestroyed(Event):
    """Issued when execution context is destroyed."""
    execution_context_id: ExecutionContextId
    execution_context_unique_id: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('execution_context_id', 'executionContextId', False, 'primitive'),
        FieldMeta('execution_context_unique_id', 'executionContextUniqueId', False, 'primitive'),
    )


@register_event("Runtime.executionContextsCleared")
@dataclass
class ExecutionContextsCleared(Event):
    """Issued when all executionContexts were cleared in browser"""
    __FIELDS__: ClassVar[tuple] = ()


@register_event("Runtime.inspectRequested")
@dataclass
class InspectRequested(Event):
    """
    Issued when object should be inspected (for example, as a result of inspect() command line API
    call).
    """
    object: RemoteObject
    hints: Dict[str, Any]
    execution_context_id: Optional[ExecutionContextId] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('object', 'object', False, 'object', ref='Runtime.RemoteObject'),
        FieldMeta('hints', 'hints', False, 'primitive'),
        FieldMeta('execution_context_id', 'executionContextId', True, 'primitive'),
    )

__all__ = ["BindingCalled", "ConsoleAPICalled", "ExceptionRevoked", "ExceptionThrown", "ExecutionContextCreated", "ExecutionContextDestroyed", "ExecutionContextsCleared", "InspectRequested"]
