"""Custom types and enums for the Tracing domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, register


type MemoryDumpConfig = Dict[str, Any]  # Configuration for memory dump. Used only when "memory-infra" category is enabled.


@register("Tracing.TraceConfig")
@dataclass
class TraceConfig(DataType):
    record_mode: Optional[Literal['recordUntilFull', 'recordContinuously', 'recordAsMuchAsPossible', 'echoToConsole']] = None
    trace_buffer_size_in_kb: Optional[float] = None
    enable_sampling: Optional[bool] = None
    enable_systrace: Optional[bool] = None
    enable_argument_filter: Optional[bool] = None
    included_categories: Optional[List[str]] = None
    excluded_categories: Optional[List[str]] = None
    synthetic_delays: Optional[List[str]] = None
    memory_dump_config: Optional[MemoryDumpConfig] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('record_mode', 'recordMode', True, 'primitive'),
        FieldMeta('trace_buffer_size_in_kb', 'traceBufferSizeInKb', True, 'primitive'),
        FieldMeta('enable_sampling', 'enableSampling', True, 'primitive'),
        FieldMeta('enable_systrace', 'enableSystrace', True, 'primitive'),
        FieldMeta('enable_argument_filter', 'enableArgumentFilter', True, 'primitive'),
        FieldMeta('included_categories', 'includedCategories', True, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('excluded_categories', 'excludedCategories', True, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('synthetic_delays', 'syntheticDelays', True, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('memory_dump_config', 'memoryDumpConfig', True, 'primitive'),
    )


@register("Tracing.StreamFormat")
class StreamFormat(str, Enum):
    """
    Data format of a trace. Can be either the legacy JSON format or the
    protocol buffer format. Note that the JSON format will be deprecated soon.
    """
    JSON = 'json'
    PROTO = 'proto'


@register("Tracing.StreamCompression")
class StreamCompression(str, Enum):
    """Compression type to use for traces returned via streams."""
    NONE = 'none'
    GZIP = 'gzip'


@register("Tracing.MemoryDumpLevelOfDetail")
class MemoryDumpLevelOfDetail(str, Enum):
    """
    Details exposed when memory request explicitly declared.
    Keep consistent with memory_dump_request_args.h and
    memory_instrumentation.mojom
    """
    BACKGROUND = 'background'
    LIGHT = 'light'
    DETAILED = 'detailed'


@register("Tracing.TracingBackend")
class TracingBackend(str, Enum):
    """
    Backend type to use for tracing. `chrome` uses the Chrome-integrated
    tracing service and is supported on all platforms. `system` is only
    supported on Chrome OS and uses the Perfetto system tracing service.
    `auto` chooses `system` when the perfettoConfig provided to Tracing.start
    specifies at least one non-Chrome data source; otherwise uses `chrome`.
    """
    AUTO = 'auto'
    CHROME = 'chrome'
    SYSTEM = 'system'

__all__ = ["MemoryDumpConfig", "MemoryDumpLevelOfDetail", "StreamCompression", "StreamFormat", "TraceConfig", "TracingBackend"]
