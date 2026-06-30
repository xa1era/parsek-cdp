"""Commands for the DOMDebugger domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode

if TYPE_CHECKING:
    from .types import (
        CSPViolationType,
        DOMBreakpointType,
        EventListener,
    )
    from ..dom.types import NodeId as DOM_NodeId
    from ..runtime.types import RemoteObjectId as Runtime_RemoteObjectId

@dataclass
class GetEventListenersReturn(DataType):
    """Return value of :meth:`DOMDebugger.get_event_listeners`."""
    listeners: List[EventListener]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('listeners', 'listeners', False, 'array', inner=FieldMeta('', '', False, 'object', ref='DOMDebugger.EventListener')),
    )


class DOMDebugger:
    """Commands of the DOMDebugger domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def get_event_listeners(self, *, object_id: Runtime_RemoteObjectId, depth: Optional[int] = None, pierce: Optional[bool] = None) -> GetEventListenersReturn:
        """
        Returns event listeners of the given object.
        :param object_id: Identifier of the object to return listeners for.
        :param depth: The maximum depth at which Node children should be retrieved, defaults to 1. Use -1 for the
        entire subtree or provide an integer larger than 0.
        :param pierce: Whether or not iframes and shadow roots should be traversed when returning the subtree
        (default is false). Reports listeners for all contexts if pierce is enabled.
        """
        _params: Dict[str, Any] = {}
        _params['objectId'] = encode(FieldMeta('', '', False, 'primitive'), object_id)
        if depth is not None:
            _params['depth'] = encode(FieldMeta('', '', False, 'primitive'), depth)
        if pierce is not None:
            _params['pierce'] = encode(FieldMeta('', '', False, 'primitive'), pierce)
        _result = await self._target.send('DOMDebugger.getEventListeners', _params)
        return GetEventListenersReturn.from_json(_result)

    async def remove_dom_breakpoint(self, *, node_id: DOM_NodeId, type_: DOMBreakpointType) -> None:
        """
        Removes DOM breakpoint that was set using `setDOMBreakpoint`.
        :param node_id: Identifier of the node to remove breakpoint from.
        :param type_: Type of the breakpoint to remove.
        """
        _params: Dict[str, Any] = {}
        _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        _params['type'] = encode(FieldMeta('', '', False, 'enum', ref='DOMDebugger.DOMBreakpointType'), type_)
        _result = await self._target.send('DOMDebugger.removeDOMBreakpoint', _params)
        return None

    async def remove_event_listener_breakpoint(self, *, event_name: str, target_name: Optional[str] = None) -> None:
        """
        Removes breakpoint on particular DOM event.
        :param event_name: Event name.
        :param target_name: EventTarget interface name.
        """
        _params: Dict[str, Any] = {}
        _params['eventName'] = encode(FieldMeta('', '', False, 'primitive'), event_name)
        if target_name is not None:
            _params['targetName'] = encode(FieldMeta('', '', False, 'primitive'), target_name)
        _result = await self._target.send('DOMDebugger.removeEventListenerBreakpoint', _params)
        return None

    async def remove_instrumentation_breakpoint(self, *, event_name: str) -> None:
        """
        Removes breakpoint on particular native event.
        
        .. deprecated::
        :param event_name: Instrumentation name to stop on.
        """
        _params: Dict[str, Any] = {}
        _params['eventName'] = encode(FieldMeta('', '', False, 'primitive'), event_name)
        _result = await self._target.send('DOMDebugger.removeInstrumentationBreakpoint', _params)
        return None

    async def remove_xhr_breakpoint(self, *, url: str) -> None:
        """
        Removes breakpoint from XMLHttpRequest.
        :param url: Resource URL substring.
        """
        _params: Dict[str, Any] = {}
        _params['url'] = encode(FieldMeta('', '', False, 'primitive'), url)
        _result = await self._target.send('DOMDebugger.removeXHRBreakpoint', _params)
        return None

    async def set_break_on_csp_violation(self, *, violation_types: List[CSPViolationType]) -> None:
        """
        Sets breakpoint on particular CSP violations.
        :param violation_types: CSP Violations to stop upon.
        """
        _params: Dict[str, Any] = {}
        _params['violationTypes'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'enum', ref='DOMDebugger.CSPViolationType')), violation_types)
        _result = await self._target.send('DOMDebugger.setBreakOnCSPViolation', _params)
        return None

    async def set_dom_breakpoint(self, *, node_id: DOM_NodeId, type_: DOMBreakpointType) -> None:
        """
        Sets breakpoint on particular operation with DOM.
        :param node_id: Identifier of the node to set breakpoint on.
        :param type_: Type of the operation to stop upon.
        """
        _params: Dict[str, Any] = {}
        _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        _params['type'] = encode(FieldMeta('', '', False, 'enum', ref='DOMDebugger.DOMBreakpointType'), type_)
        _result = await self._target.send('DOMDebugger.setDOMBreakpoint', _params)
        return None

    async def set_event_listener_breakpoint(self, *, event_name: str, target_name: Optional[str] = None) -> None:
        """
        Sets breakpoint on particular DOM event.
        :param event_name: DOM Event name to stop on (any DOM event will do).
        :param target_name: EventTarget interface name to stop on. If equal to `"*"` or not provided, will stop on any
        EventTarget.
        """
        _params: Dict[str, Any] = {}
        _params['eventName'] = encode(FieldMeta('', '', False, 'primitive'), event_name)
        if target_name is not None:
            _params['targetName'] = encode(FieldMeta('', '', False, 'primitive'), target_name)
        _result = await self._target.send('DOMDebugger.setEventListenerBreakpoint', _params)
        return None

    async def set_instrumentation_breakpoint(self, *, event_name: str) -> None:
        """
        Sets breakpoint on particular native event.
        
        .. deprecated::
        :param event_name: Instrumentation name to stop on.
        """
        _params: Dict[str, Any] = {}
        _params['eventName'] = encode(FieldMeta('', '', False, 'primitive'), event_name)
        _result = await self._target.send('DOMDebugger.setInstrumentationBreakpoint', _params)
        return None

    async def set_xhr_breakpoint(self, *, url: str) -> None:
        """
        Sets breakpoint on XMLHttpRequest.
        :param url: Resource URL substring. All XHRs having this substring in the URL will get stopped upon.
        """
        _params: Dict[str, Any] = {}
        _params['url'] = encode(FieldMeta('', '', False, 'primitive'), url)
        _result = await self._target.send('DOMDebugger.setXHRBreakpoint', _params)
        return None
