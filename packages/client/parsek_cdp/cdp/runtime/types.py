"""Custom types and enums for the Runtime domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, register


type ScriptId = str  # Unique script identifier.


@register("Runtime.SerializationOptions")
@dataclass
class SerializationOptions(DataType):
    """Represents options for serialization. Overrides `generatePreview` and `returnByValue`."""
    serialization: Literal['deep', 'json', 'idOnly']
    max_depth: Optional[int] = None
    additional_parameters: Optional[Dict[str, Any]] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('serialization', 'serialization', False, 'primitive'),
        FieldMeta('max_depth', 'maxDepth', True, 'primitive'),
        FieldMeta('additional_parameters', 'additionalParameters', True, 'primitive'),
    )


@register("Runtime.DeepSerializedValue")
@dataclass
class DeepSerializedValue(DataType):
    """Represents deep serialized value."""
    type_: Literal['undefined', 'null', 'string', 'number', 'boolean', 'bigint', 'regexp', 'date', 'symbol', 'array', 'object', 'function', 'map', 'set', 'weakmap', 'weakset', 'error', 'proxy', 'promise', 'typedarray', 'arraybuffer', 'node', 'window', 'generator']
    value: Optional[Any] = None
    object_id: Optional[str] = None
    weak_local_object_reference: Optional[int] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('type_', 'type', False, 'primitive'),
        FieldMeta('value', 'value', True, 'primitive'),
        FieldMeta('object_id', 'objectId', True, 'primitive'),
        FieldMeta('weak_local_object_reference', 'weakLocalObjectReference', True, 'primitive'),
    )


type RemoteObjectId = str  # Unique object identifier.


type UnserializableValue = str  # Primitive value which cannot be JSON-stringified. Includes values `-0`, `NaN`, `Infinity`,


@register("Runtime.RemoteObject")
@dataclass
class RemoteObject(DataType):
    """Mirror object referencing original JavaScript object."""
    type_: Literal['object', 'function', 'undefined', 'string', 'number', 'boolean', 'symbol', 'bigint']
    subtype: Optional[Literal['array', 'null', 'node', 'regexp', 'date', 'map', 'set', 'weakmap', 'weakset', 'iterator', 'generator', 'error', 'proxy', 'promise', 'typedarray', 'arraybuffer', 'dataview', 'webassemblymemory', 'wasmvalue', 'trustedtype']] = None
    class_name: Optional[str] = None
    value: Optional[Any] = None
    unserializable_value: Optional[UnserializableValue] = None
    description: Optional[str] = None
    deep_serialized_value: Optional[DeepSerializedValue] = None
    object_id: Optional[RemoteObjectId] = None
    preview: Optional[ObjectPreview] = None
    custom_preview: Optional[CustomPreview] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('type_', 'type', False, 'primitive'),
        FieldMeta('subtype', 'subtype', True, 'primitive'),
        FieldMeta('class_name', 'className', True, 'primitive'),
        FieldMeta('value', 'value', True, 'primitive'),
        FieldMeta('unserializable_value', 'unserializableValue', True, 'primitive'),
        FieldMeta('description', 'description', True, 'primitive'),
        FieldMeta('deep_serialized_value', 'deepSerializedValue', True, 'object', ref='Runtime.DeepSerializedValue'),
        FieldMeta('object_id', 'objectId', True, 'primitive'),
        FieldMeta('preview', 'preview', True, 'object', ref='Runtime.ObjectPreview'),
        FieldMeta('custom_preview', 'customPreview', True, 'object', ref='Runtime.CustomPreview'),
    )


@register("Runtime.CustomPreview")
@dataclass
class CustomPreview(DataType):
    header: str
    body_getter_id: Optional[RemoteObjectId] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('header', 'header', False, 'primitive'),
        FieldMeta('body_getter_id', 'bodyGetterId', True, 'primitive'),
    )


@register("Runtime.ObjectPreview")
@dataclass
class ObjectPreview(DataType):
    """Object containing abbreviated remote object value."""
    type_: Literal['object', 'function', 'undefined', 'string', 'number', 'boolean', 'symbol', 'bigint']
    overflow: bool
    properties: List[PropertyPreview]
    subtype: Optional[Literal['array', 'null', 'node', 'regexp', 'date', 'map', 'set', 'weakmap', 'weakset', 'iterator', 'generator', 'error', 'proxy', 'promise', 'typedarray', 'arraybuffer', 'dataview', 'webassemblymemory', 'wasmvalue', 'trustedtype']] = None
    description: Optional[str] = None
    entries: Optional[List[EntryPreview]] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('type_', 'type', False, 'primitive'),
        FieldMeta('overflow', 'overflow', False, 'primitive'),
        FieldMeta('properties', 'properties', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Runtime.PropertyPreview')),
        FieldMeta('subtype', 'subtype', True, 'primitive'),
        FieldMeta('description', 'description', True, 'primitive'),
        FieldMeta('entries', 'entries', True, 'array', inner=FieldMeta('', '', False, 'object', ref='Runtime.EntryPreview')),
    )


@register("Runtime.PropertyPreview")
@dataclass
class PropertyPreview(DataType):
    name: str
    type_: Literal['object', 'function', 'undefined', 'string', 'number', 'boolean', 'symbol', 'accessor', 'bigint']
    value: Optional[str] = None
    value_preview: Optional[ObjectPreview] = None
    subtype: Optional[Literal['array', 'null', 'node', 'regexp', 'date', 'map', 'set', 'weakmap', 'weakset', 'iterator', 'generator', 'error', 'proxy', 'promise', 'typedarray', 'arraybuffer', 'dataview', 'webassemblymemory', 'wasmvalue', 'trustedtype']] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('name', 'name', False, 'primitive'),
        FieldMeta('type_', 'type', False, 'primitive'),
        FieldMeta('value', 'value', True, 'primitive'),
        FieldMeta('value_preview', 'valuePreview', True, 'object', ref='Runtime.ObjectPreview'),
        FieldMeta('subtype', 'subtype', True, 'primitive'),
    )


@register("Runtime.EntryPreview")
@dataclass
class EntryPreview(DataType):
    value: ObjectPreview
    key: Optional[ObjectPreview] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('value', 'value', False, 'object', ref='Runtime.ObjectPreview'),
        FieldMeta('key', 'key', True, 'object', ref='Runtime.ObjectPreview'),
    )


@register("Runtime.PropertyDescriptor")
@dataclass
class PropertyDescriptor(DataType):
    """Object property descriptor."""
    name: str
    configurable: bool
    enumerable: bool
    value: Optional[RemoteObject] = None
    writable: Optional[bool] = None
    get: Optional[RemoteObject] = None
    set: Optional[RemoteObject] = None
    was_thrown: Optional[bool] = None
    is_own: Optional[bool] = None
    symbol: Optional[RemoteObject] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('name', 'name', False, 'primitive'),
        FieldMeta('configurable', 'configurable', False, 'primitive'),
        FieldMeta('enumerable', 'enumerable', False, 'primitive'),
        FieldMeta('value', 'value', True, 'object', ref='Runtime.RemoteObject'),
        FieldMeta('writable', 'writable', True, 'primitive'),
        FieldMeta('get', 'get', True, 'object', ref='Runtime.RemoteObject'),
        FieldMeta('set', 'set', True, 'object', ref='Runtime.RemoteObject'),
        FieldMeta('was_thrown', 'wasThrown', True, 'primitive'),
        FieldMeta('is_own', 'isOwn', True, 'primitive'),
        FieldMeta('symbol', 'symbol', True, 'object', ref='Runtime.RemoteObject'),
    )


@register("Runtime.InternalPropertyDescriptor")
@dataclass
class InternalPropertyDescriptor(DataType):
    """Object internal property descriptor. This property isn't normally visible in JavaScript code."""
    name: str
    value: Optional[RemoteObject] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('name', 'name', False, 'primitive'),
        FieldMeta('value', 'value', True, 'object', ref='Runtime.RemoteObject'),
    )


@register("Runtime.PrivatePropertyDescriptor")
@dataclass
class PrivatePropertyDescriptor(DataType):
    """Object private field descriptor."""
    name: str
    value: Optional[RemoteObject] = None
    get: Optional[RemoteObject] = None
    set: Optional[RemoteObject] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('name', 'name', False, 'primitive'),
        FieldMeta('value', 'value', True, 'object', ref='Runtime.RemoteObject'),
        FieldMeta('get', 'get', True, 'object', ref='Runtime.RemoteObject'),
        FieldMeta('set', 'set', True, 'object', ref='Runtime.RemoteObject'),
    )


@register("Runtime.CallArgument")
@dataclass
class CallArgument(DataType):
    """
    Represents function call argument. Either remote object id `objectId`, primitive `value`,
    unserializable primitive value or neither of (for undefined) them should be specified.
    """
    value: Optional[Any] = None
    unserializable_value: Optional[UnserializableValue] = None
    object_id: Optional[RemoteObjectId] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('value', 'value', True, 'primitive'),
        FieldMeta('unserializable_value', 'unserializableValue', True, 'primitive'),
        FieldMeta('object_id', 'objectId', True, 'primitive'),
    )


type ExecutionContextId = int  # Id of an execution context.


@register("Runtime.ExecutionContextDescription")
@dataclass
class ExecutionContextDescription(DataType):
    """Description of an isolated world."""
    id: ExecutionContextId
    origin: str
    name: str
    unique_id: str
    aux_data: Optional[Dict[str, Any]] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('id', 'id', False, 'primitive'),
        FieldMeta('origin', 'origin', False, 'primitive'),
        FieldMeta('name', 'name', False, 'primitive'),
        FieldMeta('unique_id', 'uniqueId', False, 'primitive'),
        FieldMeta('aux_data', 'auxData', True, 'primitive'),
    )


@register("Runtime.ExceptionDetails")
@dataclass
class ExceptionDetails(DataType):
    """
    Detailed information about exception (or error) that was thrown during script compilation or
    execution.
    """
    exception_id: int
    text: str
    line_number: int
    column_number: int
    script_id: Optional[ScriptId] = None
    url: Optional[str] = None
    stack_trace: Optional[StackTrace] = None
    exception: Optional[RemoteObject] = None
    execution_context_id: Optional[ExecutionContextId] = None
    exception_meta_data: Optional[Dict[str, Any]] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('exception_id', 'exceptionId', False, 'primitive'),
        FieldMeta('text', 'text', False, 'primitive'),
        FieldMeta('line_number', 'lineNumber', False, 'primitive'),
        FieldMeta('column_number', 'columnNumber', False, 'primitive'),
        FieldMeta('script_id', 'scriptId', True, 'primitive'),
        FieldMeta('url', 'url', True, 'primitive'),
        FieldMeta('stack_trace', 'stackTrace', True, 'object', ref='Runtime.StackTrace'),
        FieldMeta('exception', 'exception', True, 'object', ref='Runtime.RemoteObject'),
        FieldMeta('execution_context_id', 'executionContextId', True, 'primitive'),
        FieldMeta('exception_meta_data', 'exceptionMetaData', True, 'primitive'),
    )


type Timestamp = float  # Number of milliseconds since epoch.


type TimeDelta = float  # Number of milliseconds.


@register("Runtime.CallFrame")
@dataclass
class CallFrame(DataType):
    """Stack entry for runtime errors and assertions."""
    function_name: str
    script_id: ScriptId
    url: str
    line_number: int
    column_number: int
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('function_name', 'functionName', False, 'primitive'),
        FieldMeta('script_id', 'scriptId', False, 'primitive'),
        FieldMeta('url', 'url', False, 'primitive'),
        FieldMeta('line_number', 'lineNumber', False, 'primitive'),
        FieldMeta('column_number', 'columnNumber', False, 'primitive'),
    )


@register("Runtime.StackTrace")
@dataclass
class StackTrace(DataType):
    """Call frames for assertions or error messages."""
    call_frames: List[CallFrame]
    description: Optional[str] = None
    parent: Optional[StackTrace] = None
    parent_id: Optional[StackTraceId] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('call_frames', 'callFrames', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Runtime.CallFrame')),
        FieldMeta('description', 'description', True, 'primitive'),
        FieldMeta('parent', 'parent', True, 'object', ref='Runtime.StackTrace'),
        FieldMeta('parent_id', 'parentId', True, 'object', ref='Runtime.StackTraceId'),
    )


type UniqueDebuggerId = str  # Unique identifier of current debugger.


@register("Runtime.StackTraceId")
@dataclass
class StackTraceId(DataType):
    """
    If `debuggerId` is set stack trace comes from another debugger and can be resolved there. This
    allows to track cross-debugger calls. See `Runtime.StackTrace` and `Debugger.paused` for usages.
    """
    id: str
    debugger_id: Optional[UniqueDebuggerId] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('id', 'id', False, 'primitive'),
        FieldMeta('debugger_id', 'debuggerId', True, 'primitive'),
    )

__all__ = ["CallArgument", "CallFrame", "CustomPreview", "DeepSerializedValue", "EntryPreview", "ExceptionDetails", "ExecutionContextDescription", "ExecutionContextId", "InternalPropertyDescriptor", "ObjectPreview", "PrivatePropertyDescriptor", "PropertyDescriptor", "PropertyPreview", "RemoteObject", "RemoteObjectId", "ScriptId", "SerializationOptions", "StackTrace", "StackTraceId", "TimeDelta", "Timestamp", "UniqueDebuggerId", "UnserializableValue"]
