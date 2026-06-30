"""Custom types and enums for the Debugger domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, register

if TYPE_CHECKING:
    from ..runtime.types import RemoteObject as Runtime_RemoteObject
    from ..runtime.types import ScriptId as Runtime_ScriptId

type BreakpointId = str  # Breakpoint identifier.


type CallFrameId = str  # Call frame identifier.


@register("Debugger.Location")
@dataclass
class Location(DataType):
    """Location in the source code."""
    script_id: Runtime_ScriptId
    line_number: int
    column_number: Optional[int] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('script_id', 'scriptId', False, 'primitive'),
        FieldMeta('line_number', 'lineNumber', False, 'primitive'),
        FieldMeta('column_number', 'columnNumber', True, 'primitive'),
    )


@register("Debugger.ScriptPosition")
@dataclass
class ScriptPosition(DataType):
    """Location in the source code."""
    line_number: int
    column_number: int
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('line_number', 'lineNumber', False, 'primitive'),
        FieldMeta('column_number', 'columnNumber', False, 'primitive'),
    )


@register("Debugger.LocationRange")
@dataclass
class LocationRange(DataType):
    """Location range within one script."""
    script_id: Runtime_ScriptId
    start: ScriptPosition
    end: ScriptPosition
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('script_id', 'scriptId', False, 'primitive'),
        FieldMeta('start', 'start', False, 'object', ref='Debugger.ScriptPosition'),
        FieldMeta('end', 'end', False, 'object', ref='Debugger.ScriptPosition'),
    )


@register("Debugger.CallFrame")
@dataclass
class CallFrame(DataType):
    """JavaScript call frame. Array of call frames form the call stack."""
    call_frame_id: CallFrameId
    function_name: str
    location: Location
    url: str
    scope_chain: List[Scope]
    this: Runtime_RemoteObject
    function_location: Optional[Location] = None
    return_value: Optional[Runtime_RemoteObject] = None
    can_be_restarted: Optional[bool] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('call_frame_id', 'callFrameId', False, 'primitive'),
        FieldMeta('function_name', 'functionName', False, 'primitive'),
        FieldMeta('location', 'location', False, 'object', ref='Debugger.Location'),
        FieldMeta('url', 'url', False, 'primitive'),
        FieldMeta('scope_chain', 'scopeChain', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Debugger.Scope')),
        FieldMeta('this', 'this', False, 'object', ref='Runtime.RemoteObject'),
        FieldMeta('function_location', 'functionLocation', True, 'object', ref='Debugger.Location'),
        FieldMeta('return_value', 'returnValue', True, 'object', ref='Runtime.RemoteObject'),
        FieldMeta('can_be_restarted', 'canBeRestarted', True, 'primitive'),
    )


@register("Debugger.Scope")
@dataclass
class Scope(DataType):
    """Scope description."""
    type_: Literal['global', 'local', 'with', 'closure', 'catch', 'block', 'script', 'eval', 'module', 'wasm-expression-stack']
    object: Runtime_RemoteObject
    name: Optional[str] = None
    start_location: Optional[Location] = None
    end_location: Optional[Location] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('type_', 'type', False, 'primitive'),
        FieldMeta('object', 'object', False, 'object', ref='Runtime.RemoteObject'),
        FieldMeta('name', 'name', True, 'primitive'),
        FieldMeta('start_location', 'startLocation', True, 'object', ref='Debugger.Location'),
        FieldMeta('end_location', 'endLocation', True, 'object', ref='Debugger.Location'),
    )


@register("Debugger.SearchMatch")
@dataclass
class SearchMatch(DataType):
    """Search match for resource."""
    line_number: float
    line_content: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('line_number', 'lineNumber', False, 'primitive'),
        FieldMeta('line_content', 'lineContent', False, 'primitive'),
    )


@register("Debugger.BreakLocation")
@dataclass
class BreakLocation(DataType):
    script_id: Runtime_ScriptId
    line_number: int
    column_number: Optional[int] = None
    type_: Optional[Literal['debuggerStatement', 'call', 'return']] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('script_id', 'scriptId', False, 'primitive'),
        FieldMeta('line_number', 'lineNumber', False, 'primitive'),
        FieldMeta('column_number', 'columnNumber', True, 'primitive'),
        FieldMeta('type_', 'type', True, 'primitive'),
    )


@register("Debugger.WasmDisassemblyChunk")
@dataclass
class WasmDisassemblyChunk(DataType):
    lines: List[str]
    bytecode_offsets: List[int]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('lines', 'lines', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('bytecode_offsets', 'bytecodeOffsets', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


@register("Debugger.ScriptLanguage")
class ScriptLanguage(str, Enum):
    """Enum of possible script languages."""
    JAVASCRIPT = 'JavaScript'
    WEBASSEMBLY = 'WebAssembly'


@register("Debugger.DebugSymbols")
@dataclass
class DebugSymbols(DataType):
    """Debug symbols available for a wasm script."""
    type_: Literal['SourceMap', 'EmbeddedDWARF', 'ExternalDWARF']
    external_url: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('type_', 'type', False, 'primitive'),
        FieldMeta('external_url', 'externalURL', True, 'primitive'),
    )


@register("Debugger.ResolvedBreakpoint")
@dataclass
class ResolvedBreakpoint(DataType):
    breakpoint_id: BreakpointId
    location: Location
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('breakpoint_id', 'breakpointId', False, 'primitive'),
        FieldMeta('location', 'location', False, 'object', ref='Debugger.Location'),
    )

__all__ = ["BreakLocation", "BreakpointId", "CallFrame", "CallFrameId", "DebugSymbols", "Location", "LocationRange", "ResolvedBreakpoint", "Scope", "ScriptLanguage", "ScriptPosition", "SearchMatch", "WasmDisassemblyChunk"]
