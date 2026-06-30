"""Commands for the HeapProfiler domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode

if TYPE_CHECKING:
    from .types import (
        HeapSnapshotObjectId,
        SamplingHeapProfile,
    )
    from ..runtime.types import RemoteObject as Runtime_RemoteObject
    from ..runtime.types import RemoteObjectId as Runtime_RemoteObjectId

@dataclass
class GetHeapObjectIdReturn(DataType):
    """Return value of :meth:`HeapProfiler.get_heap_object_id`."""
    heap_snapshot_object_id: HeapSnapshotObjectId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('heap_snapshot_object_id', 'heapSnapshotObjectId', False, 'primitive'),
    )


@dataclass
class GetObjectByHeapObjectIdReturn(DataType):
    """Return value of :meth:`HeapProfiler.get_object_by_heap_object_id`."""
    result: Runtime_RemoteObject
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('result', 'result', False, 'object', ref='Runtime.RemoteObject'),
    )


@dataclass
class GetSamplingProfileReturn(DataType):
    """Return value of :meth:`HeapProfiler.get_sampling_profile`."""
    profile: SamplingHeapProfile
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('profile', 'profile', False, 'object', ref='HeapProfiler.SamplingHeapProfile'),
    )


@dataclass
class StopSamplingReturn(DataType):
    """Return value of :meth:`HeapProfiler.stop_sampling`."""
    profile: SamplingHeapProfile
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('profile', 'profile', False, 'object', ref='HeapProfiler.SamplingHeapProfile'),
    )


class HeapProfiler:
    """Commands of the HeapProfiler domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def add_inspected_heap_object(self, *, heap_object_id: HeapSnapshotObjectId) -> None:
        """
        Enables console to refer to the node with given id via $x (see Command Line API for more details
        $x functions).
        :param heap_object_id: Heap snapshot object id to be accessible by means of $x command line API.
        """
        _params: Dict[str, Any] = {}
        _params['heapObjectId'] = encode(FieldMeta('', '', False, 'primitive'), heap_object_id)
        _result = await self._target.send('HeapProfiler.addInspectedHeapObject', _params)
        return None

    async def collect_garbage(self) -> None:
        _params: Dict[str, Any] = {}
        _result = await self._target.send('HeapProfiler.collectGarbage', _params)
        return None

    async def disable(self) -> None:
        _params: Dict[str, Any] = {}
        _result = await self._target.send('HeapProfiler.disable', _params)
        return None

    async def enable(self) -> None:
        _params: Dict[str, Any] = {}
        _result = await self._target.send('HeapProfiler.enable', _params)
        return None

    async def get_heap_object_id(self, *, object_id: Runtime_RemoteObjectId) -> GetHeapObjectIdReturn:
        """:param object_id: Identifier of the object to get heap object id for."""
        _params: Dict[str, Any] = {}
        _params['objectId'] = encode(FieldMeta('', '', False, 'primitive'), object_id)
        _result = await self._target.send('HeapProfiler.getHeapObjectId', _params)
        return GetHeapObjectIdReturn.from_json(_result)

    async def get_object_by_heap_object_id(self, *, object_id: HeapSnapshotObjectId, object_group: Optional[str] = None) -> GetObjectByHeapObjectIdReturn:
        """
        :param object_id:
        :param object_group: Symbolic group name that can be used to release multiple objects.
        """
        _params: Dict[str, Any] = {}
        _params['objectId'] = encode(FieldMeta('', '', False, 'primitive'), object_id)
        if object_group is not None:
            _params['objectGroup'] = encode(FieldMeta('', '', False, 'primitive'), object_group)
        _result = await self._target.send('HeapProfiler.getObjectByHeapObjectId', _params)
        return GetObjectByHeapObjectIdReturn.from_json(_result)

    async def get_sampling_profile(self) -> GetSamplingProfileReturn:
        _params: Dict[str, Any] = {}
        _result = await self._target.send('HeapProfiler.getSamplingProfile', _params)
        return GetSamplingProfileReturn.from_json(_result)

    async def start_sampling(self, *, sampling_interval: Optional[float] = None, stack_depth: Optional[float] = None, include_objects_collected_by_major_gc: Optional[bool] = None, include_objects_collected_by_minor_gc: Optional[bool] = None) -> None:
        """
        :param sampling_interval: Average sample interval in bytes. Poisson distribution is used for the intervals. The
        default value is 32768 bytes.
        :param stack_depth: Maximum stack depth. The default value is 128.
        :param include_objects_collected_by_major_gc: By default, the sampling heap profiler reports only objects which are
        still alive when the profile is returned via getSamplingProfile or
        stopSampling, which is useful for determining what functions contribute
        the most to steady-state memory usage. This flag instructs the sampling
        heap profiler to also include information about objects discarded by
        major GC, which will show which functions cause large temporary memory
        usage or long GC pauses.
        :param include_objects_collected_by_minor_gc: By default, the sampling heap profiler reports only objects which are
        still alive when the profile is returned via getSamplingProfile or
        stopSampling, which is useful for determining what functions contribute
        the most to steady-state memory usage. This flag instructs the sampling
        heap profiler to also include information about objects discarded by
        minor GC, which is useful when tuning a latency-sensitive application
        for minimal GC activity.
        """
        _params: Dict[str, Any] = {}
        if sampling_interval is not None:
            _params['samplingInterval'] = encode(FieldMeta('', '', False, 'primitive'), sampling_interval)
        if stack_depth is not None:
            _params['stackDepth'] = encode(FieldMeta('', '', False, 'primitive'), stack_depth)
        if include_objects_collected_by_major_gc is not None:
            _params['includeObjectsCollectedByMajorGC'] = encode(FieldMeta('', '', False, 'primitive'), include_objects_collected_by_major_gc)
        if include_objects_collected_by_minor_gc is not None:
            _params['includeObjectsCollectedByMinorGC'] = encode(FieldMeta('', '', False, 'primitive'), include_objects_collected_by_minor_gc)
        _result = await self._target.send('HeapProfiler.startSampling', _params)
        return None

    async def start_tracking_heap_objects(self, *, track_allocations: Optional[bool] = None) -> None:
        """:param track_allocations:"""
        _params: Dict[str, Any] = {}
        if track_allocations is not None:
            _params['trackAllocations'] = encode(FieldMeta('', '', False, 'primitive'), track_allocations)
        _result = await self._target.send('HeapProfiler.startTrackingHeapObjects', _params)
        return None

    async def stop_sampling(self) -> StopSamplingReturn:
        _params: Dict[str, Any] = {}
        _result = await self._target.send('HeapProfiler.stopSampling', _params)
        return StopSamplingReturn.from_json(_result)

    async def stop_tracking_heap_objects(self, *, report_progress: Optional[bool] = None, treat_global_objects_as_roots: Optional[bool] = None, capture_numeric_value: Optional[bool] = None, expose_internals: Optional[bool] = None) -> None:
        """
        :param report_progress: If true 'reportHeapSnapshotProgress' events will be generated while snapshot is being taken
        when the tracking is stopped.
        :param treat_global_objects_as_roots: Deprecated in favor of `exposeInternals`.
        :param capture_numeric_value: If true, numerical values are included in the snapshot
        :param expose_internals: If true, exposes internals of the snapshot.
        """
        _params: Dict[str, Any] = {}
        if report_progress is not None:
            _params['reportProgress'] = encode(FieldMeta('', '', False, 'primitive'), report_progress)
        if treat_global_objects_as_roots is not None:
            _params['treatGlobalObjectsAsRoots'] = encode(FieldMeta('', '', False, 'primitive'), treat_global_objects_as_roots)
        if capture_numeric_value is not None:
            _params['captureNumericValue'] = encode(FieldMeta('', '', False, 'primitive'), capture_numeric_value)
        if expose_internals is not None:
            _params['exposeInternals'] = encode(FieldMeta('', '', False, 'primitive'), expose_internals)
        _result = await self._target.send('HeapProfiler.stopTrackingHeapObjects', _params)
        return None

    async def take_heap_snapshot(self, *, report_progress: Optional[bool] = None, treat_global_objects_as_roots: Optional[bool] = None, capture_numeric_value: Optional[bool] = None, expose_internals: Optional[bool] = None) -> None:
        """
        :param report_progress: If true 'reportHeapSnapshotProgress' events will be generated while snapshot is being taken.
        :param treat_global_objects_as_roots: If true, a raw snapshot without artificial roots will be generated.
        Deprecated in favor of `exposeInternals`.
        :param capture_numeric_value: If true, numerical values are included in the snapshot
        :param expose_internals: If true, exposes internals of the snapshot.
        """
        _params: Dict[str, Any] = {}
        if report_progress is not None:
            _params['reportProgress'] = encode(FieldMeta('', '', False, 'primitive'), report_progress)
        if treat_global_objects_as_roots is not None:
            _params['treatGlobalObjectsAsRoots'] = encode(FieldMeta('', '', False, 'primitive'), treat_global_objects_as_roots)
        if capture_numeric_value is not None:
            _params['captureNumericValue'] = encode(FieldMeta('', '', False, 'primitive'), capture_numeric_value)
        if expose_internals is not None:
            _params['exposeInternals'] = encode(FieldMeta('', '', False, 'primitive'), expose_internals)
        _result = await self._target.send('HeapProfiler.takeHeapSnapshot', _params)
        return None
