"""Commands for the Profiler domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode

if TYPE_CHECKING:
    from .types import (
        Profile,
        ScriptCoverage,
    )

@dataclass
class GetBestEffortCoverageReturn(DataType):
    """Return value of :meth:`Profiler.get_best_effort_coverage`."""
    result: List[ScriptCoverage]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('result', 'result', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Profiler.ScriptCoverage')),
    )


@dataclass
class StartPreciseCoverageReturn(DataType):
    """Return value of :meth:`Profiler.start_precise_coverage`."""
    timestamp: float
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('timestamp', 'timestamp', False, 'primitive'),
    )


@dataclass
class StopReturn(DataType):
    """Return value of :meth:`Profiler.stop`."""
    profile: Profile
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('profile', 'profile', False, 'object', ref='Profiler.Profile'),
    )


@dataclass
class TakePreciseCoverageReturn(DataType):
    """Return value of :meth:`Profiler.take_precise_coverage`."""
    result: List[ScriptCoverage]
    timestamp: float
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('result', 'result', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Profiler.ScriptCoverage')),
        FieldMeta('timestamp', 'timestamp', False, 'primitive'),
    )


class Profiler:
    """Commands of the Profiler domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def disable(self) -> None:
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Profiler.disable', _params)
        return None

    async def enable(self) -> None:
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Profiler.enable', _params)
        return None

    async def get_best_effort_coverage(self) -> GetBestEffortCoverageReturn:
        """
        Collect coverage data for the current isolate. The coverage data may be incomplete due to
        garbage collection.
        """
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Profiler.getBestEffortCoverage', _params)
        return GetBestEffortCoverageReturn.from_json(_result)

    async def set_sampling_interval(self, *, interval: int) -> None:
        """
        Changes CPU profiler sampling interval. Must be called before CPU profiles recording started.
        :param interval: New sampling interval in microseconds.
        """
        _params: Dict[str, Any] = {}
        _params['interval'] = encode(FieldMeta('', '', False, 'primitive'), interval)
        _result = await self._target.send('Profiler.setSamplingInterval', _params)
        return None

    async def start(self) -> None:
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Profiler.start', _params)
        return None

    async def start_precise_coverage(self, *, call_count: Optional[bool] = None, detailed: Optional[bool] = None, allow_triggered_updates: Optional[bool] = None) -> StartPreciseCoverageReturn:
        """
        Enable precise code coverage. Coverage data for JavaScript executed before enabling precise code
        coverage may be incomplete. Enabling prevents running optimized code and resets execution
        counters.
        :param call_count: Collect accurate call counts beyond simple 'covered' or 'not covered'.
        :param detailed: Collect block-based coverage.
        :param allow_triggered_updates: Allow the backend to send updates on its own initiative
        """
        _params: Dict[str, Any] = {}
        if call_count is not None:
            _params['callCount'] = encode(FieldMeta('', '', False, 'primitive'), call_count)
        if detailed is not None:
            _params['detailed'] = encode(FieldMeta('', '', False, 'primitive'), detailed)
        if allow_triggered_updates is not None:
            _params['allowTriggeredUpdates'] = encode(FieldMeta('', '', False, 'primitive'), allow_triggered_updates)
        _result = await self._target.send('Profiler.startPreciseCoverage', _params)
        return StartPreciseCoverageReturn.from_json(_result)

    async def stop(self) -> StopReturn:
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Profiler.stop', _params)
        return StopReturn.from_json(_result)

    async def stop_precise_coverage(self) -> None:
        """
        Disable precise code coverage. Disabling releases unnecessary execution count records and allows
        executing optimized code.
        """
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Profiler.stopPreciseCoverage', _params)
        return None

    async def take_precise_coverage(self) -> TakePreciseCoverageReturn:
        """
        Collect coverage data for the current isolate, and resets execution counters. Precise code
        coverage needs to have started.
        """
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Profiler.takePreciseCoverage', _params)
        return TakePreciseCoverageReturn.from_json(_result)
