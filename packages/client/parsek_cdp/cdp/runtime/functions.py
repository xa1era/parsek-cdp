"""Commands for the Runtime domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode

if TYPE_CHECKING:
    from .types import (
        CallArgument,
        ExceptionDetails,
        ExecutionContextId,
        InternalPropertyDescriptor,
        PrivatePropertyDescriptor,
        PropertyDescriptor,
        RemoteObject,
        RemoteObjectId,
        ScriptId,
        SerializationOptions,
        TimeDelta,
    )

@dataclass
class AwaitPromiseReturn(DataType):
    """Return value of :meth:`Runtime.await_promise`."""
    result: RemoteObject
    exception_details: Optional[ExceptionDetails] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('result', 'result', False, 'object', ref='Runtime.RemoteObject'),
        FieldMeta('exception_details', 'exceptionDetails', True, 'object', ref='Runtime.ExceptionDetails'),
    )


@dataclass
class CallFunctionOnReturn(DataType):
    """Return value of :meth:`Runtime.call_function_on`."""
    result: RemoteObject
    exception_details: Optional[ExceptionDetails] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('result', 'result', False, 'object', ref='Runtime.RemoteObject'),
        FieldMeta('exception_details', 'exceptionDetails', True, 'object', ref='Runtime.ExceptionDetails'),
    )


@dataclass
class CompileScriptReturn(DataType):
    """Return value of :meth:`Runtime.compile_script`."""
    script_id: Optional[ScriptId] = None
    exception_details: Optional[ExceptionDetails] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('script_id', 'scriptId', True, 'primitive'),
        FieldMeta('exception_details', 'exceptionDetails', True, 'object', ref='Runtime.ExceptionDetails'),
    )


@dataclass
class EvaluateReturn(DataType):
    """Return value of :meth:`Runtime.evaluate`."""
    result: RemoteObject
    exception_details: Optional[ExceptionDetails] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('result', 'result', False, 'object', ref='Runtime.RemoteObject'),
        FieldMeta('exception_details', 'exceptionDetails', True, 'object', ref='Runtime.ExceptionDetails'),
    )


@dataclass
class GetIsolateIdReturn(DataType):
    """Return value of :meth:`Runtime.get_isolate_id`."""
    id: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('id', 'id', False, 'primitive'),
    )


@dataclass
class GetHeapUsageReturn(DataType):
    """Return value of :meth:`Runtime.get_heap_usage`."""
    used_size: float
    total_size: float
    embedder_heap_used_size: float
    backing_storage_size: float
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('used_size', 'usedSize', False, 'primitive'),
        FieldMeta('total_size', 'totalSize', False, 'primitive'),
        FieldMeta('embedder_heap_used_size', 'embedderHeapUsedSize', False, 'primitive'),
        FieldMeta('backing_storage_size', 'backingStorageSize', False, 'primitive'),
    )


@dataclass
class GetPropertiesReturn(DataType):
    """Return value of :meth:`Runtime.get_properties`."""
    result: List[PropertyDescriptor]
    internal_properties: Optional[List[InternalPropertyDescriptor]] = None
    private_properties: Optional[List[PrivatePropertyDescriptor]] = None
    exception_details: Optional[ExceptionDetails] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('result', 'result', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Runtime.PropertyDescriptor')),
        FieldMeta('internal_properties', 'internalProperties', True, 'array', inner=FieldMeta('', '', False, 'object', ref='Runtime.InternalPropertyDescriptor')),
        FieldMeta('private_properties', 'privateProperties', True, 'array', inner=FieldMeta('', '', False, 'object', ref='Runtime.PrivatePropertyDescriptor')),
        FieldMeta('exception_details', 'exceptionDetails', True, 'object', ref='Runtime.ExceptionDetails'),
    )


@dataclass
class GlobalLexicalScopeNamesReturn(DataType):
    """Return value of :meth:`Runtime.global_lexical_scope_names`."""
    names: List[str]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('names', 'names', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


@dataclass
class QueryObjectsReturn(DataType):
    """Return value of :meth:`Runtime.query_objects`."""
    objects: RemoteObject
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('objects', 'objects', False, 'object', ref='Runtime.RemoteObject'),
    )


@dataclass
class RunScriptReturn(DataType):
    """Return value of :meth:`Runtime.run_script`."""
    result: RemoteObject
    exception_details: Optional[ExceptionDetails] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('result', 'result', False, 'object', ref='Runtime.RemoteObject'),
        FieldMeta('exception_details', 'exceptionDetails', True, 'object', ref='Runtime.ExceptionDetails'),
    )


@dataclass
class GetExceptionDetailsReturn(DataType):
    """Return value of :meth:`Runtime.get_exception_details`."""
    exception_details: Optional[ExceptionDetails] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('exception_details', 'exceptionDetails', True, 'object', ref='Runtime.ExceptionDetails'),
    )


class Runtime:
    """Commands of the Runtime domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def await_promise(self, *, promise_object_id: RemoteObjectId, return_by_value: Optional[bool] = None, generate_preview: Optional[bool] = None) -> AwaitPromiseReturn:
        """
        Add handler to promise with given promise object id.
        :param promise_object_id: Identifier of the promise.
        :param return_by_value: Whether the result is expected to be a JSON object that should be sent by value.
        :param generate_preview: Whether preview should be generated for the result.
        """
        _params: Dict[str, Any] = {}
        _params['promiseObjectId'] = encode(FieldMeta('', '', False, 'primitive'), promise_object_id)
        if return_by_value is not None:
            _params['returnByValue'] = encode(FieldMeta('', '', False, 'primitive'), return_by_value)
        if generate_preview is not None:
            _params['generatePreview'] = encode(FieldMeta('', '', False, 'primitive'), generate_preview)
        _result = await self._target.send('Runtime.awaitPromise', _params)
        return AwaitPromiseReturn.from_json(_result)

    async def call_function_on(self, *, function_declaration: str, object_id: Optional[RemoteObjectId] = None, arguments: Optional[List[CallArgument]] = None, silent: Optional[bool] = None, return_by_value: Optional[bool] = None, generate_preview: Optional[bool] = None, user_gesture: Optional[bool] = None, await_promise: Optional[bool] = None, execution_context_id: Optional[ExecutionContextId] = None, object_group: Optional[str] = None, throw_on_side_effect: Optional[bool] = None, unique_context_id: Optional[str] = None, serialization_options: Optional[SerializationOptions] = None) -> CallFunctionOnReturn:
        """
        Calls function with given declaration on the given object. Object group of the result is
        inherited from the target object.
        :param function_declaration: Declaration of the function to call.
        :param object_id: Identifier of the object to call function on. Either objectId or executionContextId should
        be specified.
        :param arguments: Call arguments. All call arguments must belong to the same JavaScript world as the target
        object.
        :param silent: In silent mode exceptions thrown during evaluation are not reported and do not pause
        execution. Overrides `setPauseOnException` state.
        :param return_by_value: Whether the result is expected to be a JSON object which should be sent by value.
        Can be overriden by `serializationOptions`.
        :param generate_preview: Whether preview should be generated for the result.
        :param user_gesture: Whether execution should be treated as initiated by user in the UI.
        :param await_promise: Whether execution should `await` for resulting value and return once awaited promise is
        resolved.
        :param execution_context_id: Specifies execution context which global object will be used to call function on. Either
        executionContextId or objectId should be specified.
        :param object_group: Symbolic group name that can be used to release multiple objects. If objectGroup is not
        specified and objectId is, objectGroup will be inherited from object.
        :param throw_on_side_effect: Whether to throw an exception if side effect cannot be ruled out during evaluation.
        :param unique_context_id: An alternative way to specify the execution context to call function on.
        Compared to contextId that may be reused across processes, this is guaranteed to be
        system-unique, so it can be used to prevent accidental function call
        in context different than intended (e.g. as a result of navigation across process
        boundaries).
        This is mutually exclusive with `executionContextId`.
        :param serialization_options: Specifies the result serialization. If provided, overrides
        `generatePreview` and `returnByValue`.
        """
        _params: Dict[str, Any] = {}
        _params['functionDeclaration'] = encode(FieldMeta('', '', False, 'primitive'), function_declaration)
        if object_id is not None:
            _params['objectId'] = encode(FieldMeta('', '', False, 'primitive'), object_id)
        if arguments is not None:
            _params['arguments'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Runtime.CallArgument')), arguments)
        if silent is not None:
            _params['silent'] = encode(FieldMeta('', '', False, 'primitive'), silent)
        if return_by_value is not None:
            _params['returnByValue'] = encode(FieldMeta('', '', False, 'primitive'), return_by_value)
        if generate_preview is not None:
            _params['generatePreview'] = encode(FieldMeta('', '', False, 'primitive'), generate_preview)
        if user_gesture is not None:
            _params['userGesture'] = encode(FieldMeta('', '', False, 'primitive'), user_gesture)
        if await_promise is not None:
            _params['awaitPromise'] = encode(FieldMeta('', '', False, 'primitive'), await_promise)
        if execution_context_id is not None:
            _params['executionContextId'] = encode(FieldMeta('', '', False, 'primitive'), execution_context_id)
        if object_group is not None:
            _params['objectGroup'] = encode(FieldMeta('', '', False, 'primitive'), object_group)
        if throw_on_side_effect is not None:
            _params['throwOnSideEffect'] = encode(FieldMeta('', '', False, 'primitive'), throw_on_side_effect)
        if unique_context_id is not None:
            _params['uniqueContextId'] = encode(FieldMeta('', '', False, 'primitive'), unique_context_id)
        if serialization_options is not None:
            _params['serializationOptions'] = encode(FieldMeta('', '', False, 'object', ref='Runtime.SerializationOptions'), serialization_options)
        _result = await self._target.send('Runtime.callFunctionOn', _params)
        return CallFunctionOnReturn.from_json(_result)

    async def compile_script(self, *, expression: str, source_url: str, persist_script: bool, execution_context_id: Optional[ExecutionContextId] = None) -> CompileScriptReturn:
        """
        Compiles expression.
        :param expression: Expression to compile.
        :param source_url: Source url to be set for the script.
        :param persist_script: Specifies whether the compiled script should be persisted.
        :param execution_context_id: Specifies in which execution context to perform script run. If the parameter is omitted the
        evaluation will be performed in the context of the inspected page.
        """
        _params: Dict[str, Any] = {}
        _params['expression'] = encode(FieldMeta('', '', False, 'primitive'), expression)
        _params['sourceURL'] = encode(FieldMeta('', '', False, 'primitive'), source_url)
        _params['persistScript'] = encode(FieldMeta('', '', False, 'primitive'), persist_script)
        if execution_context_id is not None:
            _params['executionContextId'] = encode(FieldMeta('', '', False, 'primitive'), execution_context_id)
        _result = await self._target.send('Runtime.compileScript', _params)
        return CompileScriptReturn.from_json(_result)

    async def disable(self) -> None:
        """Disables reporting of execution contexts creation."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Runtime.disable', _params)
        return None

    async def discard_console_entries(self) -> None:
        """Discards collected exceptions and console API calls."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Runtime.discardConsoleEntries', _params)
        return None

    async def enable(self) -> None:
        """
        Enables reporting of execution contexts creation by means of `executionContextCreated` event.
        When the reporting gets enabled the event will be sent immediately for each existing execution
        context.
        """
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Runtime.enable', _params)
        return None

    async def evaluate(self, *, expression: str, object_group: Optional[str] = None, include_command_line_api: Optional[bool] = None, silent: Optional[bool] = None, context_id: Optional[ExecutionContextId] = None, return_by_value: Optional[bool] = None, generate_preview: Optional[bool] = None, user_gesture: Optional[bool] = None, await_promise: Optional[bool] = None, throw_on_side_effect: Optional[bool] = None, timeout: Optional[TimeDelta] = None, disable_breaks: Optional[bool] = None, repl_mode: Optional[bool] = None, allow_unsafe_eval_blocked_by_csp: Optional[bool] = None, unique_context_id: Optional[str] = None, serialization_options: Optional[SerializationOptions] = None) -> EvaluateReturn:
        """
        Evaluates expression on global object.
        :param expression: Expression to evaluate.
        :param object_group: Symbolic group name that can be used to release multiple objects.
        :param include_command_line_api: Determines whether Command Line API should be available during the evaluation.
        :param silent: In silent mode exceptions thrown during evaluation are not reported and do not pause
        execution. Overrides `setPauseOnException` state.
        :param context_id: Specifies in which execution context to perform evaluation. If the parameter is omitted the
        evaluation will be performed in the context of the inspected page.
        This is mutually exclusive with `uniqueContextId`, which offers an
        alternative way to identify the execution context that is more reliable
        in a multi-process environment.
        :param return_by_value: Whether the result is expected to be a JSON object that should be sent by value.
        :param generate_preview: Whether preview should be generated for the result.
        :param user_gesture: Whether execution should be treated as initiated by user in the UI.
        :param await_promise: Whether execution should `await` for resulting value and return once awaited promise is
        resolved.
        :param throw_on_side_effect: Whether to throw an exception if side effect cannot be ruled out during evaluation.
        This implies `disableBreaks` below.
        :param timeout: Terminate execution after timing out (number of milliseconds).
        :param disable_breaks: Disable breakpoints during execution.
        :param repl_mode: Setting this flag to true enables `let` re-declaration and top-level `await`.
        Note that `let` variables can only be re-declared if they originate from
        `replMode` themselves.
        :param allow_unsafe_eval_blocked_by_csp: The Content Security Policy (CSP) for the target might block 'unsafe-eval'
        which includes eval(), Function(), setTimeout() and setInterval()
        when called with non-callable arguments. This flag bypasses CSP for this
        evaluation and allows unsafe-eval. Defaults to true.
        :param unique_context_id: An alternative way to specify the execution context to evaluate in.
        Compared to contextId that may be reused across processes, this is guaranteed to be
        system-unique, so it can be used to prevent accidental evaluation of the expression
        in context different than intended (e.g. as a result of navigation across process
        boundaries).
        This is mutually exclusive with `contextId`.
        :param serialization_options: Specifies the result serialization. If provided, overrides
        `generatePreview` and `returnByValue`.
        """
        _params: Dict[str, Any] = {}
        _params['expression'] = encode(FieldMeta('', '', False, 'primitive'), expression)
        if object_group is not None:
            _params['objectGroup'] = encode(FieldMeta('', '', False, 'primitive'), object_group)
        if include_command_line_api is not None:
            _params['includeCommandLineAPI'] = encode(FieldMeta('', '', False, 'primitive'), include_command_line_api)
        if silent is not None:
            _params['silent'] = encode(FieldMeta('', '', False, 'primitive'), silent)
        if context_id is not None:
            _params['contextId'] = encode(FieldMeta('', '', False, 'primitive'), context_id)
        if return_by_value is not None:
            _params['returnByValue'] = encode(FieldMeta('', '', False, 'primitive'), return_by_value)
        if generate_preview is not None:
            _params['generatePreview'] = encode(FieldMeta('', '', False, 'primitive'), generate_preview)
        if user_gesture is not None:
            _params['userGesture'] = encode(FieldMeta('', '', False, 'primitive'), user_gesture)
        if await_promise is not None:
            _params['awaitPromise'] = encode(FieldMeta('', '', False, 'primitive'), await_promise)
        if throw_on_side_effect is not None:
            _params['throwOnSideEffect'] = encode(FieldMeta('', '', False, 'primitive'), throw_on_side_effect)
        if timeout is not None:
            _params['timeout'] = encode(FieldMeta('', '', False, 'primitive'), timeout)
        if disable_breaks is not None:
            _params['disableBreaks'] = encode(FieldMeta('', '', False, 'primitive'), disable_breaks)
        if repl_mode is not None:
            _params['replMode'] = encode(FieldMeta('', '', False, 'primitive'), repl_mode)
        if allow_unsafe_eval_blocked_by_csp is not None:
            _params['allowUnsafeEvalBlockedByCSP'] = encode(FieldMeta('', '', False, 'primitive'), allow_unsafe_eval_blocked_by_csp)
        if unique_context_id is not None:
            _params['uniqueContextId'] = encode(FieldMeta('', '', False, 'primitive'), unique_context_id)
        if serialization_options is not None:
            _params['serializationOptions'] = encode(FieldMeta('', '', False, 'object', ref='Runtime.SerializationOptions'), serialization_options)
        _result = await self._target.send('Runtime.evaluate', _params)
        return EvaluateReturn.from_json(_result)

    async def get_isolate_id(self) -> GetIsolateIdReturn:
        """Returns the isolate id."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Runtime.getIsolateId', _params)
        return GetIsolateIdReturn.from_json(_result)

    async def get_heap_usage(self) -> GetHeapUsageReturn:
        """
        Returns the JavaScript heap usage.
        It is the total usage of the corresponding isolate not scoped to a particular Runtime.
        """
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Runtime.getHeapUsage', _params)
        return GetHeapUsageReturn.from_json(_result)

    async def get_properties(self, *, object_id: RemoteObjectId, own_properties: Optional[bool] = None, accessor_properties_only: Optional[bool] = None, generate_preview: Optional[bool] = None, non_indexed_properties_only: Optional[bool] = None) -> GetPropertiesReturn:
        """
        Returns properties of a given object. Object group of the result is inherited from the target
        object.
        :param object_id: Identifier of the object to return properties for.
        :param own_properties: If true, returns properties belonging only to the element itself, not to its prototype
        chain.
        :param accessor_properties_only: If true, returns accessor properties (with getter/setter) only; internal properties are not
        returned either.
        :param generate_preview: Whether preview should be generated for the results.
        :param non_indexed_properties_only: If true, returns non-indexed properties only.
        """
        _params: Dict[str, Any] = {}
        _params['objectId'] = encode(FieldMeta('', '', False, 'primitive'), object_id)
        if own_properties is not None:
            _params['ownProperties'] = encode(FieldMeta('', '', False, 'primitive'), own_properties)
        if accessor_properties_only is not None:
            _params['accessorPropertiesOnly'] = encode(FieldMeta('', '', False, 'primitive'), accessor_properties_only)
        if generate_preview is not None:
            _params['generatePreview'] = encode(FieldMeta('', '', False, 'primitive'), generate_preview)
        if non_indexed_properties_only is not None:
            _params['nonIndexedPropertiesOnly'] = encode(FieldMeta('', '', False, 'primitive'), non_indexed_properties_only)
        _result = await self._target.send('Runtime.getProperties', _params)
        return GetPropertiesReturn.from_json(_result)

    async def global_lexical_scope_names(self, *, execution_context_id: Optional[ExecutionContextId] = None) -> GlobalLexicalScopeNamesReturn:
        """
        Returns all let, const and class variables from global scope.
        :param execution_context_id: Specifies in which execution context to lookup global scope variables.
        """
        _params: Dict[str, Any] = {}
        if execution_context_id is not None:
            _params['executionContextId'] = encode(FieldMeta('', '', False, 'primitive'), execution_context_id)
        _result = await self._target.send('Runtime.globalLexicalScopeNames', _params)
        return GlobalLexicalScopeNamesReturn.from_json(_result)

    async def query_objects(self, *, prototype_object_id: RemoteObjectId, object_group: Optional[str] = None) -> QueryObjectsReturn:
        """
        :param prototype_object_id: Identifier of the prototype to return objects for.
        :param object_group: Symbolic group name that can be used to release the results.
        """
        _params: Dict[str, Any] = {}
        _params['prototypeObjectId'] = encode(FieldMeta('', '', False, 'primitive'), prototype_object_id)
        if object_group is not None:
            _params['objectGroup'] = encode(FieldMeta('', '', False, 'primitive'), object_group)
        _result = await self._target.send('Runtime.queryObjects', _params)
        return QueryObjectsReturn.from_json(_result)

    async def release_object(self, *, object_id: RemoteObjectId) -> None:
        """
        Releases remote object with given id.
        :param object_id: Identifier of the object to release.
        """
        _params: Dict[str, Any] = {}
        _params['objectId'] = encode(FieldMeta('', '', False, 'primitive'), object_id)
        _result = await self._target.send('Runtime.releaseObject', _params)
        return None

    async def release_object_group(self, *, object_group: str) -> None:
        """
        Releases all remote objects that belong to a given group.
        :param object_group: Symbolic object group name.
        """
        _params: Dict[str, Any] = {}
        _params['objectGroup'] = encode(FieldMeta('', '', False, 'primitive'), object_group)
        _result = await self._target.send('Runtime.releaseObjectGroup', _params)
        return None

    async def run_if_waiting_for_debugger(self) -> None:
        """Tells inspected instance to run if it was waiting for debugger to attach."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Runtime.runIfWaitingForDebugger', _params)
        return None

    async def run_script(self, *, script_id: ScriptId, execution_context_id: Optional[ExecutionContextId] = None, object_group: Optional[str] = None, silent: Optional[bool] = None, include_command_line_api: Optional[bool] = None, return_by_value: Optional[bool] = None, generate_preview: Optional[bool] = None, await_promise: Optional[bool] = None) -> RunScriptReturn:
        """
        Runs script with given id in a given context.
        :param script_id: Id of the script to run.
        :param execution_context_id: Specifies in which execution context to perform script run. If the parameter is omitted the
        evaluation will be performed in the context of the inspected page.
        :param object_group: Symbolic group name that can be used to release multiple objects.
        :param silent: In silent mode exceptions thrown during evaluation are not reported and do not pause
        execution. Overrides `setPauseOnException` state.
        :param include_command_line_api: Determines whether Command Line API should be available during the evaluation.
        :param return_by_value: Whether the result is expected to be a JSON object which should be sent by value.
        :param generate_preview: Whether preview should be generated for the result.
        :param await_promise: Whether execution should `await` for resulting value and return once awaited promise is
        resolved.
        """
        _params: Dict[str, Any] = {}
        _params['scriptId'] = encode(FieldMeta('', '', False, 'primitive'), script_id)
        if execution_context_id is not None:
            _params['executionContextId'] = encode(FieldMeta('', '', False, 'primitive'), execution_context_id)
        if object_group is not None:
            _params['objectGroup'] = encode(FieldMeta('', '', False, 'primitive'), object_group)
        if silent is not None:
            _params['silent'] = encode(FieldMeta('', '', False, 'primitive'), silent)
        if include_command_line_api is not None:
            _params['includeCommandLineAPI'] = encode(FieldMeta('', '', False, 'primitive'), include_command_line_api)
        if return_by_value is not None:
            _params['returnByValue'] = encode(FieldMeta('', '', False, 'primitive'), return_by_value)
        if generate_preview is not None:
            _params['generatePreview'] = encode(FieldMeta('', '', False, 'primitive'), generate_preview)
        if await_promise is not None:
            _params['awaitPromise'] = encode(FieldMeta('', '', False, 'primitive'), await_promise)
        _result = await self._target.send('Runtime.runScript', _params)
        return RunScriptReturn.from_json(_result)

    async def set_async_call_stack_depth(self, *, max_depth: int) -> None:
        """
        Enables or disables async call stacks tracking.
        :param max_depth: Maximum depth of async call stacks. Setting to `0` will effectively disable collecting async
        call stacks (default).
        """
        _params: Dict[str, Any] = {}
        _params['maxDepth'] = encode(FieldMeta('', '', False, 'primitive'), max_depth)
        _result = await self._target.send('Runtime.setAsyncCallStackDepth', _params)
        return None

    async def set_custom_object_formatter_enabled(self, *, enabled: bool) -> None:
        """:param enabled:"""
        _params: Dict[str, Any] = {}
        _params['enabled'] = encode(FieldMeta('', '', False, 'primitive'), enabled)
        _result = await self._target.send('Runtime.setCustomObjectFormatterEnabled', _params)
        return None

    async def set_max_call_stack_size_to_capture(self, *, size: int) -> None:
        """:param size:"""
        _params: Dict[str, Any] = {}
        _params['size'] = encode(FieldMeta('', '', False, 'primitive'), size)
        _result = await self._target.send('Runtime.setMaxCallStackSizeToCapture', _params)
        return None

    async def terminate_execution(self) -> None:
        """
        Terminate current or next JavaScript execution.
        Will cancel the termination when the outer-most script execution ends.
        """
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Runtime.terminateExecution', _params)
        return None

    async def add_binding(self, *, name: str, execution_context_id: Optional[ExecutionContextId] = None, execution_context_name: Optional[str] = None) -> None:
        """
        If executionContextId is empty, adds binding with the given name on the
        global objects of all inspected contexts, including those created later,
        bindings survive reloads.
        Binding function takes exactly one argument, this argument should be string,
        in case of any other input, function throws an exception.
        Each binding function call produces Runtime.bindingCalled notification.
        :param name:
        :param execution_context_id: If specified, the binding would only be exposed to the specified
        execution context. If omitted and `executionContextName` is not set,
        the binding is exposed to all execution contexts of the target.
        This parameter is mutually exclusive with `executionContextName`.
        Deprecated in favor of `executionContextName` due to an unclear use case
        and bugs in implementation (crbug.com/1169639). `executionContextId` will be
        removed in the future.
        :param execution_context_name: If specified, the binding is exposed to the executionContext with
        matching name, even for contexts created after the binding is added.
        See also `ExecutionContext.name` and `worldName` parameter to
        `Page.addScriptToEvaluateOnNewDocument`.
        This parameter is mutually exclusive with `executionContextId`.
        """
        _params: Dict[str, Any] = {}
        _params['name'] = encode(FieldMeta('', '', False, 'primitive'), name)
        if execution_context_id is not None:
            _params['executionContextId'] = encode(FieldMeta('', '', False, 'primitive'), execution_context_id)
        if execution_context_name is not None:
            _params['executionContextName'] = encode(FieldMeta('', '', False, 'primitive'), execution_context_name)
        _result = await self._target.send('Runtime.addBinding', _params)
        return None

    async def remove_binding(self, *, name: str) -> None:
        """
        This method does not remove binding function from global object but
        unsubscribes current runtime agent from Runtime.bindingCalled notifications.
        :param name:
        """
        _params: Dict[str, Any] = {}
        _params['name'] = encode(FieldMeta('', '', False, 'primitive'), name)
        _result = await self._target.send('Runtime.removeBinding', _params)
        return None

    async def get_exception_details(self, *, error_object_id: RemoteObjectId) -> GetExceptionDetailsReturn:
        """
        This method tries to lookup and populate exception details for a
        JavaScript Error object.
        Note that the stackTrace portion of the resulting exceptionDetails will
        only be populated if the Runtime domain was enabled at the time when the
        Error was thrown.
        :param error_object_id: The error object for which to resolve the exception details.
        """
        _params: Dict[str, Any] = {}
        _params['errorObjectId'] = encode(FieldMeta('', '', False, 'primitive'), error_object_id)
        _result = await self._target.send('Runtime.getExceptionDetails', _params)
        return GetExceptionDetailsReturn.from_json(_result)
