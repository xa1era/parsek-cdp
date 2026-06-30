"""Commands for the Memory domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode

if TYPE_CHECKING:
    from .types import (
        DOMCounter,
        PressureLevel,
        SamplingProfile,
    )

@dataclass
class GetDOMCountersReturn(DataType):
    """Return value of :meth:`Memory.get_dom_counters`."""
    documents: int
    nodes: int
    js_event_listeners: int
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('documents', 'documents', False, 'primitive'),
        FieldMeta('nodes', 'nodes', False, 'primitive'),
        FieldMeta('js_event_listeners', 'jsEventListeners', False, 'primitive'),
    )


@dataclass
class GetDOMCountersForLeakDetectionReturn(DataType):
    """Return value of :meth:`Memory.get_dom_counters_for_leak_detection`."""
    counters: List[DOMCounter]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('counters', 'counters', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Memory.DOMCounter')),
    )


@dataclass
class GetAllTimeSamplingProfileReturn(DataType):
    """Return value of :meth:`Memory.get_all_time_sampling_profile`."""
    profile: SamplingProfile
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('profile', 'profile', False, 'object', ref='Memory.SamplingProfile'),
    )


@dataclass
class GetBrowserSamplingProfileReturn(DataType):
    """Return value of :meth:`Memory.get_browser_sampling_profile`."""
    profile: SamplingProfile
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('profile', 'profile', False, 'object', ref='Memory.SamplingProfile'),
    )


@dataclass
class GetSamplingProfileReturn(DataType):
    """Return value of :meth:`Memory.get_sampling_profile`."""
    profile: SamplingProfile
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('profile', 'profile', False, 'object', ref='Memory.SamplingProfile'),
    )


class Memory:
    """Commands of the Memory domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def get_dom_counters(self) -> GetDOMCountersReturn:
        """Retruns current DOM object counters."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Memory.getDOMCounters', _params)
        return GetDOMCountersReturn.from_json(_result)

    async def get_dom_counters_for_leak_detection(self) -> GetDOMCountersForLeakDetectionReturn:
        """Retruns DOM object counters after preparing renderer for leak detection."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Memory.getDOMCountersForLeakDetection', _params)
        return GetDOMCountersForLeakDetectionReturn.from_json(_result)

    async def prepare_for_leak_detection(self) -> None:
        """
        Prepares for leak detection by terminating workers, stopping spellcheckers,
        dropping non-essential internal caches, running garbage collections, etc.
        """
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Memory.prepareForLeakDetection', _params)
        return None

    async def forcibly_purge_java_script_memory(self) -> None:
        """Simulate OomIntervention by purging V8 memory."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Memory.forciblyPurgeJavaScriptMemory', _params)
        return None

    async def set_pressure_notifications_suppressed(self, *, suppressed: bool) -> None:
        """
        Enable/disable suppressing memory pressure notifications in all processes.
        :param suppressed: If true, memory pressure notifications will be suppressed.
        """
        _params: Dict[str, Any] = {}
        _params['suppressed'] = encode(FieldMeta('', '', False, 'primitive'), suppressed)
        _result = await self._target.send('Memory.setPressureNotificationsSuppressed', _params)
        return None

    async def simulate_pressure_notification(self, *, level: PressureLevel) -> None:
        """
        Simulate a memory pressure notification in all processes.
        :param level: Memory pressure level of the notification.
        """
        _params: Dict[str, Any] = {}
        _params['level'] = encode(FieldMeta('', '', False, 'enum', ref='Memory.PressureLevel'), level)
        _result = await self._target.send('Memory.simulatePressureNotification', _params)
        return None

    async def start_sampling(self, *, sampling_interval: Optional[int] = None, suppress_randomness: Optional[bool] = None) -> None:
        """
        Start collecting native memory profile.
        :param sampling_interval: Average number of bytes between samples.
        :param suppress_randomness: Do not randomize intervals between samples.
        """
        _params: Dict[str, Any] = {}
        if sampling_interval is not None:
            _params['samplingInterval'] = encode(FieldMeta('', '', False, 'primitive'), sampling_interval)
        if suppress_randomness is not None:
            _params['suppressRandomness'] = encode(FieldMeta('', '', False, 'primitive'), suppress_randomness)
        _result = await self._target.send('Memory.startSampling', _params)
        return None

    async def stop_sampling(self) -> None:
        """Stop collecting native memory profile."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Memory.stopSampling', _params)
        return None

    async def get_all_time_sampling_profile(self) -> GetAllTimeSamplingProfileReturn:
        """
        Retrieve native memory allocations profile
        collected since renderer process startup.
        """
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Memory.getAllTimeSamplingProfile', _params)
        return GetAllTimeSamplingProfileReturn.from_json(_result)

    async def get_browser_sampling_profile(self) -> GetBrowserSamplingProfileReturn:
        """
        Retrieve native memory allocations profile
        collected since browser process startup.
        """
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Memory.getBrowserSamplingProfile', _params)
        return GetBrowserSamplingProfileReturn.from_json(_result)

    async def get_sampling_profile(self) -> GetSamplingProfileReturn:
        """
        Retrieve native memory allocations profile collected since last
        `startSampling` call.
        """
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Memory.getSamplingProfile', _params)
        return GetSamplingProfileReturn.from_json(_result)
