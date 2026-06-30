"""Events for the Debugger domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import FieldMeta
from ..mixins.event import Event, register_event

if TYPE_CHECKING:
    from .types import (
        BreakpointId,
        CallFrame,
        DebugSymbols,
        Location,
        ResolvedBreakpoint,
        ScriptLanguage,
    )
    from ..runtime.types import ExecutionContextId as Runtime_ExecutionContextId
    from ..runtime.types import ScriptId as Runtime_ScriptId
    from ..runtime.types import StackTrace as Runtime_StackTrace
    from ..runtime.types import StackTraceId as Runtime_StackTraceId

@register_event("Debugger.breakpointResolved")
@dataclass
class BreakpointResolved(Event):
    """
    Fired when breakpoint is resolved to an actual script and location.
    Deprecated in favor of `resolvedBreakpoints` in the `scriptParsed` event.
    """
    breakpoint_id: BreakpointId
    location: Location
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('breakpoint_id', 'breakpointId', False, 'primitive'),
        FieldMeta('location', 'location', False, 'object', ref='Debugger.Location'),
    )


@register_event("Debugger.paused")
@dataclass
class Paused(Event):
    """Fired when the virtual machine stopped on breakpoint or exception or any other stop criteria."""
    call_frames: List[CallFrame]
    reason: Literal['ambiguous', 'assert', 'CSPViolation', 'debugCommand', 'DOM', 'EventListener', 'exception', 'instrumentation', 'OOM', 'other', 'promiseRejection', 'XHR', 'step']
    data: Optional[Dict[str, Any]] = None
    hit_breakpoints: Optional[List[str]] = None
    async_stack_trace: Optional[Runtime_StackTrace] = None
    async_stack_trace_id: Optional[Runtime_StackTraceId] = None
    async_call_stack_trace_id: Optional[Runtime_StackTraceId] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('call_frames', 'callFrames', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Debugger.CallFrame')),
        FieldMeta('reason', 'reason', False, 'primitive'),
        FieldMeta('data', 'data', True, 'primitive'),
        FieldMeta('hit_breakpoints', 'hitBreakpoints', True, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('async_stack_trace', 'asyncStackTrace', True, 'object', ref='Runtime.StackTrace'),
        FieldMeta('async_stack_trace_id', 'asyncStackTraceId', True, 'object', ref='Runtime.StackTraceId'),
        FieldMeta('async_call_stack_trace_id', 'asyncCallStackTraceId', True, 'object', ref='Runtime.StackTraceId'),
    )


@register_event("Debugger.resumed")
@dataclass
class Resumed(Event):
    """Fired when the virtual machine resumed execution."""
    __FIELDS__: ClassVar[tuple] = ()


@register_event("Debugger.scriptFailedToParse")
@dataclass
class ScriptFailedToParse(Event):
    """Fired when virtual machine fails to parse the script."""
    script_id: Runtime_ScriptId
    url: str
    start_line: int
    start_column: int
    end_line: int
    end_column: int
    execution_context_id: Runtime_ExecutionContextId
    hash: str
    build_id: str
    execution_context_aux_data: Optional[Dict[str, Any]] = None
    source_map_url: Optional[str] = None
    has_source_url: Optional[bool] = None
    is_module: Optional[bool] = None
    length: Optional[int] = None
    stack_trace: Optional[Runtime_StackTrace] = None
    code_offset: Optional[int] = None
    script_language: Optional[ScriptLanguage] = None
    embedder_name: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('script_id', 'scriptId', False, 'primitive'),
        FieldMeta('url', 'url', False, 'primitive'),
        FieldMeta('start_line', 'startLine', False, 'primitive'),
        FieldMeta('start_column', 'startColumn', False, 'primitive'),
        FieldMeta('end_line', 'endLine', False, 'primitive'),
        FieldMeta('end_column', 'endColumn', False, 'primitive'),
        FieldMeta('execution_context_id', 'executionContextId', False, 'primitive'),
        FieldMeta('hash', 'hash', False, 'primitive'),
        FieldMeta('build_id', 'buildId', False, 'primitive'),
        FieldMeta('execution_context_aux_data', 'executionContextAuxData', True, 'primitive'),
        FieldMeta('source_map_url', 'sourceMapURL', True, 'primitive'),
        FieldMeta('has_source_url', 'hasSourceURL', True, 'primitive'),
        FieldMeta('is_module', 'isModule', True, 'primitive'),
        FieldMeta('length', 'length', True, 'primitive'),
        FieldMeta('stack_trace', 'stackTrace', True, 'object', ref='Runtime.StackTrace'),
        FieldMeta('code_offset', 'codeOffset', True, 'primitive'),
        FieldMeta('script_language', 'scriptLanguage', True, 'enum', ref='Debugger.ScriptLanguage'),
        FieldMeta('embedder_name', 'embedderName', True, 'primitive'),
    )


@register_event("Debugger.scriptParsed")
@dataclass
class ScriptParsed(Event):
    """
    Fired when virtual machine parses script. This event is also fired for all known and uncollected
    scripts upon enabling debugger.
    """
    script_id: Runtime_ScriptId
    url: str
    start_line: int
    start_column: int
    end_line: int
    end_column: int
    execution_context_id: Runtime_ExecutionContextId
    hash: str
    build_id: str
    execution_context_aux_data: Optional[Dict[str, Any]] = None
    is_live_edit: Optional[bool] = None
    source_map_url: Optional[str] = None
    has_source_url: Optional[bool] = None
    is_module: Optional[bool] = None
    length: Optional[int] = None
    stack_trace: Optional[Runtime_StackTrace] = None
    code_offset: Optional[int] = None
    script_language: Optional[ScriptLanguage] = None
    debug_symbols: Optional[List[DebugSymbols]] = None
    embedder_name: Optional[str] = None
    resolved_breakpoints: Optional[List[ResolvedBreakpoint]] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('script_id', 'scriptId', False, 'primitive'),
        FieldMeta('url', 'url', False, 'primitive'),
        FieldMeta('start_line', 'startLine', False, 'primitive'),
        FieldMeta('start_column', 'startColumn', False, 'primitive'),
        FieldMeta('end_line', 'endLine', False, 'primitive'),
        FieldMeta('end_column', 'endColumn', False, 'primitive'),
        FieldMeta('execution_context_id', 'executionContextId', False, 'primitive'),
        FieldMeta('hash', 'hash', False, 'primitive'),
        FieldMeta('build_id', 'buildId', False, 'primitive'),
        FieldMeta('execution_context_aux_data', 'executionContextAuxData', True, 'primitive'),
        FieldMeta('is_live_edit', 'isLiveEdit', True, 'primitive'),
        FieldMeta('source_map_url', 'sourceMapURL', True, 'primitive'),
        FieldMeta('has_source_url', 'hasSourceURL', True, 'primitive'),
        FieldMeta('is_module', 'isModule', True, 'primitive'),
        FieldMeta('length', 'length', True, 'primitive'),
        FieldMeta('stack_trace', 'stackTrace', True, 'object', ref='Runtime.StackTrace'),
        FieldMeta('code_offset', 'codeOffset', True, 'primitive'),
        FieldMeta('script_language', 'scriptLanguage', True, 'enum', ref='Debugger.ScriptLanguage'),
        FieldMeta('debug_symbols', 'debugSymbols', True, 'array', inner=FieldMeta('', '', False, 'object', ref='Debugger.DebugSymbols')),
        FieldMeta('embedder_name', 'embedderName', True, 'primitive'),
        FieldMeta('resolved_breakpoints', 'resolvedBreakpoints', True, 'array', inner=FieldMeta('', '', False, 'object', ref='Debugger.ResolvedBreakpoint')),
    )

__all__ = ["BreakpointResolved", "Paused", "Resumed", "ScriptFailedToParse", "ScriptParsed"]
