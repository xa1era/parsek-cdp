"""Commands for the Debugger domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode

if TYPE_CHECKING:
    from .types import (
        BreakLocation,
        BreakpointId,
        CallFrame,
        CallFrameId,
        Location,
        LocationRange,
        ScriptPosition,
        SearchMatch,
        WasmDisassemblyChunk,
    )
    from ..runtime.types import CallArgument as Runtime_CallArgument
    from ..runtime.types import ExceptionDetails as Runtime_ExceptionDetails
    from ..runtime.types import RemoteObject as Runtime_RemoteObject
    from ..runtime.types import RemoteObjectId as Runtime_RemoteObjectId
    from ..runtime.types import ScriptId as Runtime_ScriptId
    from ..runtime.types import StackTrace as Runtime_StackTrace
    from ..runtime.types import StackTraceId as Runtime_StackTraceId
    from ..runtime.types import TimeDelta as Runtime_TimeDelta
    from ..runtime.types import UniqueDebuggerId as Runtime_UniqueDebuggerId

@dataclass
class EnableReturn(DataType):
    """Return value of :meth:`Debugger.enable`."""
    debugger_id: Runtime_UniqueDebuggerId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('debugger_id', 'debuggerId', False, 'primitive'),
    )


@dataclass
class EvaluateOnCallFrameReturn(DataType):
    """Return value of :meth:`Debugger.evaluate_on_call_frame`."""
    result: Runtime_RemoteObject
    exception_details: Optional[Runtime_ExceptionDetails] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('result', 'result', False, 'object', ref='Runtime.RemoteObject'),
        FieldMeta('exception_details', 'exceptionDetails', True, 'object', ref='Runtime.ExceptionDetails'),
    )


@dataclass
class GetPossibleBreakpointsReturn(DataType):
    """Return value of :meth:`Debugger.get_possible_breakpoints`."""
    locations: List[BreakLocation]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('locations', 'locations', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Debugger.BreakLocation')),
    )


@dataclass
class GetScriptSourceReturn(DataType):
    """Return value of :meth:`Debugger.get_script_source`."""
    script_source: str
    bytecode: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('script_source', 'scriptSource', False, 'primitive'),
        FieldMeta('bytecode', 'bytecode', True, 'primitive'),
    )


@dataclass
class DisassembleWasmModuleReturn(DataType):
    """Return value of :meth:`Debugger.disassemble_wasm_module`."""
    total_number_of_lines: int
    function_body_offsets: List[int]
    chunk: WasmDisassemblyChunk
    stream_id: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('total_number_of_lines', 'totalNumberOfLines', False, 'primitive'),
        FieldMeta('function_body_offsets', 'functionBodyOffsets', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('chunk', 'chunk', False, 'object', ref='Debugger.WasmDisassemblyChunk'),
        FieldMeta('stream_id', 'streamId', True, 'primitive'),
    )


@dataclass
class NextWasmDisassemblyChunkReturn(DataType):
    """Return value of :meth:`Debugger.next_wasm_disassembly_chunk`."""
    chunk: WasmDisassemblyChunk
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('chunk', 'chunk', False, 'object', ref='Debugger.WasmDisassemblyChunk'),
    )


@dataclass
class GetWasmBytecodeReturn(DataType):
    """Return value of :meth:`Debugger.get_wasm_bytecode`."""
    bytecode: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('bytecode', 'bytecode', False, 'primitive'),
    )


@dataclass
class GetStackTraceReturn(DataType):
    """Return value of :meth:`Debugger.get_stack_trace`."""
    stack_trace: Runtime_StackTrace
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('stack_trace', 'stackTrace', False, 'object', ref='Runtime.StackTrace'),
    )


@dataclass
class RestartFrameReturn(DataType):
    """Return value of :meth:`Debugger.restart_frame`."""
    call_frames: List[CallFrame]
    async_stack_trace: Optional[Runtime_StackTrace] = None
    async_stack_trace_id: Optional[Runtime_StackTraceId] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('call_frames', 'callFrames', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Debugger.CallFrame')),
        FieldMeta('async_stack_trace', 'asyncStackTrace', True, 'object', ref='Runtime.StackTrace'),
        FieldMeta('async_stack_trace_id', 'asyncStackTraceId', True, 'object', ref='Runtime.StackTraceId'),
    )


@dataclass
class SearchInContentReturn(DataType):
    """Return value of :meth:`Debugger.search_in_content`."""
    result: List[SearchMatch]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('result', 'result', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Debugger.SearchMatch')),
    )


@dataclass
class SetBreakpointReturn(DataType):
    """Return value of :meth:`Debugger.set_breakpoint`."""
    breakpoint_id: BreakpointId
    actual_location: Location
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('breakpoint_id', 'breakpointId', False, 'primitive'),
        FieldMeta('actual_location', 'actualLocation', False, 'object', ref='Debugger.Location'),
    )


@dataclass
class SetInstrumentationBreakpointReturn(DataType):
    """Return value of :meth:`Debugger.set_instrumentation_breakpoint`."""
    breakpoint_id: BreakpointId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('breakpoint_id', 'breakpointId', False, 'primitive'),
    )


@dataclass
class SetBreakpointByUrlReturn(DataType):
    """Return value of :meth:`Debugger.set_breakpoint_by_url`."""
    breakpoint_id: BreakpointId
    locations: List[Location]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('breakpoint_id', 'breakpointId', False, 'primitive'),
        FieldMeta('locations', 'locations', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Debugger.Location')),
    )


@dataclass
class SetBreakpointOnFunctionCallReturn(DataType):
    """Return value of :meth:`Debugger.set_breakpoint_on_function_call`."""
    breakpoint_id: BreakpointId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('breakpoint_id', 'breakpointId', False, 'primitive'),
    )


@dataclass
class SetScriptSourceReturn(DataType):
    """Return value of :meth:`Debugger.set_script_source`."""
    status: Literal['Ok', 'CompileError', 'BlockedByActiveGenerator', 'BlockedByActiveFunction', 'BlockedByTopLevelEsModuleChange']
    call_frames: Optional[List[CallFrame]] = None
    stack_changed: Optional[bool] = None
    async_stack_trace: Optional[Runtime_StackTrace] = None
    async_stack_trace_id: Optional[Runtime_StackTraceId] = None
    exception_details: Optional[Runtime_ExceptionDetails] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('status', 'status', False, 'primitive'),
        FieldMeta('call_frames', 'callFrames', True, 'array', inner=FieldMeta('', '', False, 'object', ref='Debugger.CallFrame')),
        FieldMeta('stack_changed', 'stackChanged', True, 'primitive'),
        FieldMeta('async_stack_trace', 'asyncStackTrace', True, 'object', ref='Runtime.StackTrace'),
        FieldMeta('async_stack_trace_id', 'asyncStackTraceId', True, 'object', ref='Runtime.StackTraceId'),
        FieldMeta('exception_details', 'exceptionDetails', True, 'object', ref='Runtime.ExceptionDetails'),
    )


class Debugger:
    """Commands of the Debugger domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def continue_to_location(self, *, location: Location, target_call_frames: Optional[Literal['any', 'current']] = None) -> None:
        """
        Continues execution until specific location is reached.
        :param location: Location to continue to.
        :param target_call_frames:
        """
        _params: Dict[str, Any] = {}
        _params['location'] = encode(FieldMeta('', '', False, 'object', ref='Debugger.Location'), location)
        if target_call_frames is not None:
            _params['targetCallFrames'] = encode(FieldMeta('', '', False, 'primitive'), target_call_frames)
        _result = await self._target.send('Debugger.continueToLocation', _params)
        return None

    async def disable(self) -> None:
        """Disables debugger for given page."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Debugger.disable', _params)
        return None

    async def enable(self, *, max_scripts_cache_size: Optional[float] = None) -> EnableReturn:
        """
        Enables debugger for the given page. Clients should not assume that the debugging has been
        enabled until the result for this command is received.
        :param max_scripts_cache_size: The maximum size in bytes of collected scripts (not referenced by other heap objects)
        the debugger can hold. Puts no limit if parameter is omitted.
        """
        _params: Dict[str, Any] = {}
        if max_scripts_cache_size is not None:
            _params['maxScriptsCacheSize'] = encode(FieldMeta('', '', False, 'primitive'), max_scripts_cache_size)
        _result = await self._target.send('Debugger.enable', _params)
        return EnableReturn.from_json(_result)

    async def evaluate_on_call_frame(self, *, call_frame_id: CallFrameId, expression: str, object_group: Optional[str] = None, include_command_line_api: Optional[bool] = None, silent: Optional[bool] = None, return_by_value: Optional[bool] = None, generate_preview: Optional[bool] = None, throw_on_side_effect: Optional[bool] = None, timeout: Optional[Runtime_TimeDelta] = None) -> EvaluateOnCallFrameReturn:
        """
        Evaluates expression on a given call frame.
        :param call_frame_id: Call frame identifier to evaluate on.
        :param expression: Expression to evaluate.
        :param object_group: String object group name to put result into (allows rapid releasing resulting object handles
        using `releaseObjectGroup`).
        :param include_command_line_api: Specifies whether command line API should be available to the evaluated expression, defaults
        to false.
        :param silent: In silent mode exceptions thrown during evaluation are not reported and do not pause
        execution. Overrides `setPauseOnException` state.
        :param return_by_value: Whether the result is expected to be a JSON object that should be sent by value.
        :param generate_preview: Whether preview should be generated for the result.
        :param throw_on_side_effect: Whether to throw an exception if side effect cannot be ruled out during evaluation.
        :param timeout: Terminate execution after timing out (number of milliseconds).
        """
        _params: Dict[str, Any] = {}
        _params['callFrameId'] = encode(FieldMeta('', '', False, 'primitive'), call_frame_id)
        _params['expression'] = encode(FieldMeta('', '', False, 'primitive'), expression)
        if object_group is not None:
            _params['objectGroup'] = encode(FieldMeta('', '', False, 'primitive'), object_group)
        if include_command_line_api is not None:
            _params['includeCommandLineAPI'] = encode(FieldMeta('', '', False, 'primitive'), include_command_line_api)
        if silent is not None:
            _params['silent'] = encode(FieldMeta('', '', False, 'primitive'), silent)
        if return_by_value is not None:
            _params['returnByValue'] = encode(FieldMeta('', '', False, 'primitive'), return_by_value)
        if generate_preview is not None:
            _params['generatePreview'] = encode(FieldMeta('', '', False, 'primitive'), generate_preview)
        if throw_on_side_effect is not None:
            _params['throwOnSideEffect'] = encode(FieldMeta('', '', False, 'primitive'), throw_on_side_effect)
        if timeout is not None:
            _params['timeout'] = encode(FieldMeta('', '', False, 'primitive'), timeout)
        _result = await self._target.send('Debugger.evaluateOnCallFrame', _params)
        return EvaluateOnCallFrameReturn.from_json(_result)

    async def get_possible_breakpoints(self, *, start: Location, end: Optional[Location] = None, restrict_to_function: Optional[bool] = None) -> GetPossibleBreakpointsReturn:
        """
        Returns possible locations for breakpoint. scriptId in start and end range locations should be
        the same.
        :param start: Start of range to search possible breakpoint locations in.
        :param end: End of range to search possible breakpoint locations in (excluding). When not specified, end
        of scripts is used as end of range.
        :param restrict_to_function: Only consider locations which are in the same (non-nested) function as start.
        """
        _params: Dict[str, Any] = {}
        _params['start'] = encode(FieldMeta('', '', False, 'object', ref='Debugger.Location'), start)
        if end is not None:
            _params['end'] = encode(FieldMeta('', '', False, 'object', ref='Debugger.Location'), end)
        if restrict_to_function is not None:
            _params['restrictToFunction'] = encode(FieldMeta('', '', False, 'primitive'), restrict_to_function)
        _result = await self._target.send('Debugger.getPossibleBreakpoints', _params)
        return GetPossibleBreakpointsReturn.from_json(_result)

    async def get_script_source(self, *, script_id: Runtime_ScriptId) -> GetScriptSourceReturn:
        """
        Returns source for the script with given id.
        :param script_id: Id of the script to get source for.
        """
        _params: Dict[str, Any] = {}
        _params['scriptId'] = encode(FieldMeta('', '', False, 'primitive'), script_id)
        _result = await self._target.send('Debugger.getScriptSource', _params)
        return GetScriptSourceReturn.from_json(_result)

    async def disassemble_wasm_module(self, *, script_id: Runtime_ScriptId) -> DisassembleWasmModuleReturn:
        """:param script_id: Id of the script to disassemble"""
        _params: Dict[str, Any] = {}
        _params['scriptId'] = encode(FieldMeta('', '', False, 'primitive'), script_id)
        _result = await self._target.send('Debugger.disassembleWasmModule', _params)
        return DisassembleWasmModuleReturn.from_json(_result)

    async def next_wasm_disassembly_chunk(self, *, stream_id: str) -> NextWasmDisassemblyChunkReturn:
        """
        Disassemble the next chunk of lines for the module corresponding to the
        stream. If disassembly is complete, this API will invalidate the streamId
        and return an empty chunk. Any subsequent calls for the now invalid stream
        will return errors.
        :param stream_id:
        """
        _params: Dict[str, Any] = {}
        _params['streamId'] = encode(FieldMeta('', '', False, 'primitive'), stream_id)
        _result = await self._target.send('Debugger.nextWasmDisassemblyChunk', _params)
        return NextWasmDisassemblyChunkReturn.from_json(_result)

    async def get_wasm_bytecode(self, *, script_id: Runtime_ScriptId) -> GetWasmBytecodeReturn:
        """
        This command is deprecated. Use getScriptSource instead.
        
        .. deprecated::
        :param script_id: Id of the Wasm script to get source for.
        """
        _params: Dict[str, Any] = {}
        _params['scriptId'] = encode(FieldMeta('', '', False, 'primitive'), script_id)
        _result = await self._target.send('Debugger.getWasmBytecode', _params)
        return GetWasmBytecodeReturn.from_json(_result)

    async def get_stack_trace(self, *, stack_trace_id: Runtime_StackTraceId) -> GetStackTraceReturn:
        """
        Returns stack trace with given `stackTraceId`.
        :param stack_trace_id:
        """
        _params: Dict[str, Any] = {}
        _params['stackTraceId'] = encode(FieldMeta('', '', False, 'object', ref='Runtime.StackTraceId'), stack_trace_id)
        _result = await self._target.send('Debugger.getStackTrace', _params)
        return GetStackTraceReturn.from_json(_result)

    async def pause(self) -> None:
        """Stops on the next JavaScript statement."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Debugger.pause', _params)
        return None

    async def pause_on_async_call(self, *, parent_stack_trace_id: Runtime_StackTraceId) -> None:
        """
        
        .. deprecated::
        :param parent_stack_trace_id: Debugger will pause when async call with given stack trace is started.
        """
        _params: Dict[str, Any] = {}
        _params['parentStackTraceId'] = encode(FieldMeta('', '', False, 'object', ref='Runtime.StackTraceId'), parent_stack_trace_id)
        _result = await self._target.send('Debugger.pauseOnAsyncCall', _params)
        return None

    async def remove_breakpoint(self, *, breakpoint_id: BreakpointId) -> None:
        """
        Removes JavaScript breakpoint.
        :param breakpoint_id:
        """
        _params: Dict[str, Any] = {}
        _params['breakpointId'] = encode(FieldMeta('', '', False, 'primitive'), breakpoint_id)
        _result = await self._target.send('Debugger.removeBreakpoint', _params)
        return None

    async def restart_frame(self, *, call_frame_id: CallFrameId, mode: Optional[Literal['StepInto']] = None) -> RestartFrameReturn:
        """
        Restarts particular call frame from the beginning. The old, deprecated
        behavior of `restartFrame` is to stay paused and allow further CDP commands
        after a restart was scheduled. This can cause problems with restarting, so
        we now continue execution immediatly after it has been scheduled until we
        reach the beginning of the restarted frame.
        
        To stay back-wards compatible, `restartFrame` now expects a `mode`
        parameter to be present. If the `mode` parameter is missing, `restartFrame`
        errors out.
        
        The various return values are deprecated and `callFrames` is always empty.
        Use the call frames from the `Debugger#paused` events instead, that fires
        once V8 pauses at the beginning of the restarted function.
        :param call_frame_id: Call frame identifier to evaluate on.
        :param mode: The `mode` parameter must be present and set to 'StepInto', otherwise
        `restartFrame` will error out.
        """
        _params: Dict[str, Any] = {}
        _params['callFrameId'] = encode(FieldMeta('', '', False, 'primitive'), call_frame_id)
        if mode is not None:
            _params['mode'] = encode(FieldMeta('', '', False, 'primitive'), mode)
        _result = await self._target.send('Debugger.restartFrame', _params)
        return RestartFrameReturn.from_json(_result)

    async def resume(self, *, terminate_on_resume: Optional[bool] = None) -> None:
        """
        Resumes JavaScript execution.
        :param terminate_on_resume: Set to true to terminate execution upon resuming execution. In contrast
        to Runtime.terminateExecution, this will allows to execute further
        JavaScript (i.e. via evaluation) until execution of the paused code
        is actually resumed, at which point termination is triggered.
        If execution is currently not paused, this parameter has no effect.
        """
        _params: Dict[str, Any] = {}
        if terminate_on_resume is not None:
            _params['terminateOnResume'] = encode(FieldMeta('', '', False, 'primitive'), terminate_on_resume)
        _result = await self._target.send('Debugger.resume', _params)
        return None

    async def search_in_content(self, *, script_id: Runtime_ScriptId, query: str, case_sensitive: Optional[bool] = None, is_regex: Optional[bool] = None) -> SearchInContentReturn:
        """
        Searches for given string in script content.
        :param script_id: Id of the script to search in.
        :param query: String to search for.
        :param case_sensitive: If true, search is case sensitive.
        :param is_regex: If true, treats string parameter as regex.
        """
        _params: Dict[str, Any] = {}
        _params['scriptId'] = encode(FieldMeta('', '', False, 'primitive'), script_id)
        _params['query'] = encode(FieldMeta('', '', False, 'primitive'), query)
        if case_sensitive is not None:
            _params['caseSensitive'] = encode(FieldMeta('', '', False, 'primitive'), case_sensitive)
        if is_regex is not None:
            _params['isRegex'] = encode(FieldMeta('', '', False, 'primitive'), is_regex)
        _result = await self._target.send('Debugger.searchInContent', _params)
        return SearchInContentReturn.from_json(_result)

    async def set_async_call_stack_depth(self, *, max_depth: int) -> None:
        """
        Enables or disables async call stacks tracking.
        :param max_depth: Maximum depth of async call stacks. Setting to `0` will effectively disable collecting async
        call stacks (default).
        """
        _params: Dict[str, Any] = {}
        _params['maxDepth'] = encode(FieldMeta('', '', False, 'primitive'), max_depth)
        _result = await self._target.send('Debugger.setAsyncCallStackDepth', _params)
        return None

    async def set_blackbox_execution_contexts(self, *, unique_ids: List[str]) -> None:
        """
        Replace previous blackbox execution contexts with passed ones. Forces backend to skip
        stepping/pausing in scripts in these execution contexts. VM will try to leave blackboxed script by
        performing 'step in' several times, finally resorting to 'step out' if unsuccessful.
        :param unique_ids: Array of execution context unique ids for the debugger to ignore.
        """
        _params: Dict[str, Any] = {}
        _params['uniqueIds'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'primitive')), unique_ids)
        _result = await self._target.send('Debugger.setBlackboxExecutionContexts', _params)
        return None

    async def set_blackbox_patterns(self, *, patterns: List[str], skip_anonymous: Optional[bool] = None) -> None:
        """
        Replace previous blackbox patterns with passed ones. Forces backend to skip stepping/pausing in
        scripts with url matching one of the patterns. VM will try to leave blackboxed script by
        performing 'step in' several times, finally resorting to 'step out' if unsuccessful.
        :param patterns: Array of regexps that will be used to check script url for blackbox state.
        :param skip_anonymous: If true, also ignore scripts with no source url.
        """
        _params: Dict[str, Any] = {}
        _params['patterns'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'primitive')), patterns)
        if skip_anonymous is not None:
            _params['skipAnonymous'] = encode(FieldMeta('', '', False, 'primitive'), skip_anonymous)
        _result = await self._target.send('Debugger.setBlackboxPatterns', _params)
        return None

    async def set_blackboxed_ranges(self, *, script_id: Runtime_ScriptId, positions: List[ScriptPosition]) -> None:
        """
        Makes backend skip steps in the script in blackboxed ranges. VM will try leave blacklisted
        scripts by performing 'step in' several times, finally resorting to 'step out' if unsuccessful.
        Positions array contains positions where blackbox state is changed. First interval isn't
        blackboxed. Array should be sorted.
        :param script_id: Id of the script.
        :param positions:
        """
        _params: Dict[str, Any] = {}
        _params['scriptId'] = encode(FieldMeta('', '', False, 'primitive'), script_id)
        _params['positions'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Debugger.ScriptPosition')), positions)
        _result = await self._target.send('Debugger.setBlackboxedRanges', _params)
        return None

    async def set_breakpoint(self, *, location: Location, condition: Optional[str] = None) -> SetBreakpointReturn:
        """
        Sets JavaScript breakpoint at a given location.
        :param location: Location to set breakpoint in.
        :param condition: Expression to use as a breakpoint condition. When specified, debugger will only stop on the
        breakpoint if this expression evaluates to true.
        """
        _params: Dict[str, Any] = {}
        _params['location'] = encode(FieldMeta('', '', False, 'object', ref='Debugger.Location'), location)
        if condition is not None:
            _params['condition'] = encode(FieldMeta('', '', False, 'primitive'), condition)
        _result = await self._target.send('Debugger.setBreakpoint', _params)
        return SetBreakpointReturn.from_json(_result)

    async def set_instrumentation_breakpoint(self, *, instrumentation: Literal['beforeScriptExecution', 'beforeScriptWithSourceMapExecution']) -> SetInstrumentationBreakpointReturn:
        """
        Sets instrumentation breakpoint.
        :param instrumentation: Instrumentation name.
        """
        _params: Dict[str, Any] = {}
        _params['instrumentation'] = encode(FieldMeta('', '', False, 'primitive'), instrumentation)
        _result = await self._target.send('Debugger.setInstrumentationBreakpoint', _params)
        return SetInstrumentationBreakpointReturn.from_json(_result)

    async def set_breakpoint_by_url(self, *, line_number: int, url: Optional[str] = None, url_regex: Optional[str] = None, script_hash: Optional[str] = None, column_number: Optional[int] = None, condition: Optional[str] = None) -> SetBreakpointByUrlReturn:
        """
        Sets JavaScript breakpoint at given location specified either by URL or URL regex. Once this
        command is issued, all existing parsed scripts will have breakpoints resolved and returned in
        `locations` property. Further matching script parsing will result in subsequent
        `breakpointResolved` events issued. This logical breakpoint will survive page reloads.
        :param line_number: Line number to set breakpoint at.
        :param url: URL of the resources to set breakpoint on.
        :param url_regex: Regex pattern for the URLs of the resources to set breakpoints on. Either `url` or
        `urlRegex` must be specified.
        :param script_hash: Script hash of the resources to set breakpoint on.
        :param column_number: Offset in the line to set breakpoint at.
        :param condition: Expression to use as a breakpoint condition. When specified, debugger will only stop on the
        breakpoint if this expression evaluates to true.
        """
        _params: Dict[str, Any] = {}
        _params['lineNumber'] = encode(FieldMeta('', '', False, 'primitive'), line_number)
        if url is not None:
            _params['url'] = encode(FieldMeta('', '', False, 'primitive'), url)
        if url_regex is not None:
            _params['urlRegex'] = encode(FieldMeta('', '', False, 'primitive'), url_regex)
        if script_hash is not None:
            _params['scriptHash'] = encode(FieldMeta('', '', False, 'primitive'), script_hash)
        if column_number is not None:
            _params['columnNumber'] = encode(FieldMeta('', '', False, 'primitive'), column_number)
        if condition is not None:
            _params['condition'] = encode(FieldMeta('', '', False, 'primitive'), condition)
        _result = await self._target.send('Debugger.setBreakpointByUrl', _params)
        return SetBreakpointByUrlReturn.from_json(_result)

    async def set_breakpoint_on_function_call(self, *, object_id: Runtime_RemoteObjectId, condition: Optional[str] = None) -> SetBreakpointOnFunctionCallReturn:
        """
        Sets JavaScript breakpoint before each call to the given function.
        If another function was created from the same source as a given one,
        calling it will also trigger the breakpoint.
        :param object_id: Function object id.
        :param condition: Expression to use as a breakpoint condition. When specified, debugger will
        stop on the breakpoint if this expression evaluates to true.
        """
        _params: Dict[str, Any] = {}
        _params['objectId'] = encode(FieldMeta('', '', False, 'primitive'), object_id)
        if condition is not None:
            _params['condition'] = encode(FieldMeta('', '', False, 'primitive'), condition)
        _result = await self._target.send('Debugger.setBreakpointOnFunctionCall', _params)
        return SetBreakpointOnFunctionCallReturn.from_json(_result)

    async def set_breakpoints_active(self, *, active: bool) -> None:
        """
        Activates / deactivates all breakpoints on the page.
        :param active: New value for breakpoints active state.
        """
        _params: Dict[str, Any] = {}
        _params['active'] = encode(FieldMeta('', '', False, 'primitive'), active)
        _result = await self._target.send('Debugger.setBreakpointsActive', _params)
        return None

    async def set_pause_on_exceptions(self, *, state: Literal['none', 'caught', 'uncaught', 'all']) -> None:
        """
        Defines pause on exceptions state. Can be set to stop on all exceptions, uncaught exceptions,
        or caught exceptions, no exceptions. Initial pause on exceptions state is `none`.
        :param state: Pause on exceptions mode.
        """
        _params: Dict[str, Any] = {}
        _params['state'] = encode(FieldMeta('', '', False, 'primitive'), state)
        _result = await self._target.send('Debugger.setPauseOnExceptions', _params)
        return None

    async def set_return_value(self, *, new_value: Runtime_CallArgument) -> None:
        """
        Changes return value in top frame. Available only at return break position.
        :param new_value: New return value.
        """
        _params: Dict[str, Any] = {}
        _params['newValue'] = encode(FieldMeta('', '', False, 'object', ref='Runtime.CallArgument'), new_value)
        _result = await self._target.send('Debugger.setReturnValue', _params)
        return None

    async def set_script_source(self, *, script_id: Runtime_ScriptId, script_source: str, dry_run: Optional[bool] = None, allow_top_frame_editing: Optional[bool] = None) -> SetScriptSourceReturn:
        """
        Edits JavaScript source live.
        
        In general, functions that are currently on the stack can not be edited with
        a single exception: If the edited function is the top-most stack frame and
        that is the only activation of that function on the stack. In this case
        the live edit will be successful and a `Debugger.restartFrame` for the
        top-most function is automatically triggered.
        :param script_id: Id of the script to edit.
        :param script_source: New content of the script.
        :param dry_run: If true the change will not actually be applied. Dry run may be used to get result
        description without actually modifying the code.
        :param allow_top_frame_editing: If true, then `scriptSource` is allowed to change the function on top of the stack
        as long as the top-most stack frame is the only activation of that function.
        """
        _params: Dict[str, Any] = {}
        _params['scriptId'] = encode(FieldMeta('', '', False, 'primitive'), script_id)
        _params['scriptSource'] = encode(FieldMeta('', '', False, 'primitive'), script_source)
        if dry_run is not None:
            _params['dryRun'] = encode(FieldMeta('', '', False, 'primitive'), dry_run)
        if allow_top_frame_editing is not None:
            _params['allowTopFrameEditing'] = encode(FieldMeta('', '', False, 'primitive'), allow_top_frame_editing)
        _result = await self._target.send('Debugger.setScriptSource', _params)
        return SetScriptSourceReturn.from_json(_result)

    async def set_skip_all_pauses(self, *, skip: bool) -> None:
        """
        Makes page not interrupt on any pauses (breakpoint, exception, dom exception etc).
        :param skip: New value for skip pauses state.
        """
        _params: Dict[str, Any] = {}
        _params['skip'] = encode(FieldMeta('', '', False, 'primitive'), skip)
        _result = await self._target.send('Debugger.setSkipAllPauses', _params)
        return None

    async def set_variable_value(self, *, scope_number: int, variable_name: str, new_value: Runtime_CallArgument, call_frame_id: CallFrameId) -> None:
        """
        Changes value of variable in a callframe. Object-based scopes are not supported and must be
        mutated manually.
        :param scope_number: 0-based number of scope as was listed in scope chain. Only 'local', 'closure' and 'catch'
        scope types are allowed. Other scopes could be manipulated manually.
        :param variable_name: Variable name.
        :param new_value: New variable value.
        :param call_frame_id: Id of callframe that holds variable.
        """
        _params: Dict[str, Any] = {}
        _params['scopeNumber'] = encode(FieldMeta('', '', False, 'primitive'), scope_number)
        _params['variableName'] = encode(FieldMeta('', '', False, 'primitive'), variable_name)
        _params['newValue'] = encode(FieldMeta('', '', False, 'object', ref='Runtime.CallArgument'), new_value)
        _params['callFrameId'] = encode(FieldMeta('', '', False, 'primitive'), call_frame_id)
        _result = await self._target.send('Debugger.setVariableValue', _params)
        return None

    async def step_into(self, *, break_on_async_call: Optional[bool] = None, skip_list: Optional[List[LocationRange]] = None) -> None:
        """
        Steps into the function call.
        :param break_on_async_call: Debugger will pause on the execution of the first async task which was scheduled
        before next pause.
        :param skip_list: The skipList specifies location ranges that should be skipped on step into.
        """
        _params: Dict[str, Any] = {}
        if break_on_async_call is not None:
            _params['breakOnAsyncCall'] = encode(FieldMeta('', '', False, 'primitive'), break_on_async_call)
        if skip_list is not None:
            _params['skipList'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Debugger.LocationRange')), skip_list)
        _result = await self._target.send('Debugger.stepInto', _params)
        return None

    async def step_out(self) -> None:
        """Steps out of the function call."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Debugger.stepOut', _params)
        return None

    async def step_over(self, *, skip_list: Optional[List[LocationRange]] = None) -> None:
        """
        Steps over the statement.
        :param skip_list: The skipList specifies location ranges that should be skipped on step over.
        """
        _params: Dict[str, Any] = {}
        if skip_list is not None:
            _params['skipList'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Debugger.LocationRange')), skip_list)
        _result = await self._target.send('Debugger.stepOver', _params)
        return None
