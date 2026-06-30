"""Commands for the Tracing domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode

if TYPE_CHECKING:
    from .types import (
        MemoryDumpLevelOfDetail,
        StreamCompression,
        StreamFormat,
        TraceConfig,
        TracingBackend,
    )

@dataclass
class GetCategoriesReturn(DataType):
    """Return value of :meth:`Tracing.get_categories`."""
    categories: List[str]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('categories', 'categories', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


@dataclass
class RequestMemoryDumpReturn(DataType):
    """Return value of :meth:`Tracing.request_memory_dump`."""
    dump_guid: str
    success: bool
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('dump_guid', 'dumpGuid', False, 'primitive'),
        FieldMeta('success', 'success', False, 'primitive'),
    )


class Tracing:
    """Commands of the Tracing domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def end(self) -> None:
        """Stop trace events collection."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Tracing.end', _params)
        return None

    async def get_categories(self) -> GetCategoriesReturn:
        """Gets supported tracing categories."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Tracing.getCategories', _params)
        return GetCategoriesReturn.from_json(_result)

    async def record_clock_sync_marker(self, *, sync_id: str) -> None:
        """
        Record a clock sync marker in the trace.
        :param sync_id: The ID of this clock sync marker
        """
        _params: Dict[str, Any] = {}
        _params['syncId'] = encode(FieldMeta('', '', False, 'primitive'), sync_id)
        _result = await self._target.send('Tracing.recordClockSyncMarker', _params)
        return None

    async def request_memory_dump(self, *, deterministic: Optional[bool] = None, level_of_detail: Optional[MemoryDumpLevelOfDetail] = None) -> RequestMemoryDumpReturn:
        """
        Request a global memory dump.
        :param deterministic: Enables more deterministic results by forcing garbage collection
        :param level_of_detail: Specifies level of details in memory dump. Defaults to "detailed".
        """
        _params: Dict[str, Any] = {}
        if deterministic is not None:
            _params['deterministic'] = encode(FieldMeta('', '', False, 'primitive'), deterministic)
        if level_of_detail is not None:
            _params['levelOfDetail'] = encode(FieldMeta('', '', False, 'enum', ref='Tracing.MemoryDumpLevelOfDetail'), level_of_detail)
        _result = await self._target.send('Tracing.requestMemoryDump', _params)
        return RequestMemoryDumpReturn.from_json(_result)

    async def start(self, *, categories: Optional[str] = None, options: Optional[str] = None, buffer_usage_reporting_interval: Optional[float] = None, transfer_mode: Optional[Literal['ReportEvents', 'ReturnAsStream']] = None, stream_format: Optional[StreamFormat] = None, stream_compression: Optional[StreamCompression] = None, trace_config: Optional[TraceConfig] = None, perfetto_config: Optional[str] = None, tracing_backend: Optional[TracingBackend] = None) -> None:
        """
        Start trace events collection.
        :param categories: Category/tag filter
        :param options: Tracing options
        :param buffer_usage_reporting_interval: If set, the agent will issue bufferUsage events at this interval, specified in milliseconds
        :param transfer_mode: Whether to report trace events as series of dataCollected events or to save trace to a
        stream (defaults to `ReportEvents`).
        :param stream_format: Trace data format to use. This only applies when using `ReturnAsStream`
        transfer mode (defaults to `json`).
        :param stream_compression: Compression format to use. This only applies when using `ReturnAsStream`
        transfer mode (defaults to `none`)
        :param trace_config:
        :param perfetto_config: Base64-encoded serialized perfetto.protos.TraceConfig protobuf message
        When specified, the parameters `categories`, `options`, `traceConfig`
        are ignored. (Encoded as a base64 string when passed over JSON)
        :param tracing_backend: Backend type (defaults to `auto`)
        """
        _params: Dict[str, Any] = {}
        if categories is not None:
            _params['categories'] = encode(FieldMeta('', '', False, 'primitive'), categories)
        if options is not None:
            _params['options'] = encode(FieldMeta('', '', False, 'primitive'), options)
        if buffer_usage_reporting_interval is not None:
            _params['bufferUsageReportingInterval'] = encode(FieldMeta('', '', False, 'primitive'), buffer_usage_reporting_interval)
        if transfer_mode is not None:
            _params['transferMode'] = encode(FieldMeta('', '', False, 'primitive'), transfer_mode)
        if stream_format is not None:
            _params['streamFormat'] = encode(FieldMeta('', '', False, 'enum', ref='Tracing.StreamFormat'), stream_format)
        if stream_compression is not None:
            _params['streamCompression'] = encode(FieldMeta('', '', False, 'enum', ref='Tracing.StreamCompression'), stream_compression)
        if trace_config is not None:
            _params['traceConfig'] = encode(FieldMeta('', '', False, 'object', ref='Tracing.TraceConfig'), trace_config)
        if perfetto_config is not None:
            _params['perfettoConfig'] = encode(FieldMeta('', '', False, 'primitive'), perfetto_config)
        if tracing_backend is not None:
            _params['tracingBackend'] = encode(FieldMeta('', '', False, 'enum', ref='Tracing.TracingBackend'), tracing_backend)
        _result = await self._target.send('Tracing.start', _params)
        return None
