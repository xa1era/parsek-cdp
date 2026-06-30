"""Custom types and enums for the SystemInfo domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, register


@register("SystemInfo.GPUDevice")
@dataclass
class GPUDevice(DataType):
    """Describes a single graphics processor (GPU)."""
    vendor_id: float
    device_id: float
    vendor_string: str
    device_string: str
    driver_vendor: str
    driver_version: str
    sub_sys_id: Optional[float] = None
    revision: Optional[float] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('vendor_id', 'vendorId', False, 'primitive'),
        FieldMeta('device_id', 'deviceId', False, 'primitive'),
        FieldMeta('vendor_string', 'vendorString', False, 'primitive'),
        FieldMeta('device_string', 'deviceString', False, 'primitive'),
        FieldMeta('driver_vendor', 'driverVendor', False, 'primitive'),
        FieldMeta('driver_version', 'driverVersion', False, 'primitive'),
        FieldMeta('sub_sys_id', 'subSysId', True, 'primitive'),
        FieldMeta('revision', 'revision', True, 'primitive'),
    )


@register("SystemInfo.Size")
@dataclass
class Size(DataType):
    """Describes the width and height dimensions of an entity."""
    width: int
    height: int
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('width', 'width', False, 'primitive'),
        FieldMeta('height', 'height', False, 'primitive'),
    )


@register("SystemInfo.VideoDecodeAcceleratorCapability")
@dataclass
class VideoDecodeAcceleratorCapability(DataType):
    """
    Describes a supported video decoding profile with its associated minimum and
    maximum resolutions.
    """
    profile: str
    max_resolution: Size
    min_resolution: Size
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('profile', 'profile', False, 'primitive'),
        FieldMeta('max_resolution', 'maxResolution', False, 'object', ref='SystemInfo.Size'),
        FieldMeta('min_resolution', 'minResolution', False, 'object', ref='SystemInfo.Size'),
    )


@register("SystemInfo.VideoEncodeAcceleratorCapability")
@dataclass
class VideoEncodeAcceleratorCapability(DataType):
    """
    Describes a supported video encoding profile with its associated maximum
    resolution and maximum framerate.
    """
    profile: str
    max_resolution: Size
    max_framerate_numerator: int
    max_framerate_denominator: int
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('profile', 'profile', False, 'primitive'),
        FieldMeta('max_resolution', 'maxResolution', False, 'object', ref='SystemInfo.Size'),
        FieldMeta('max_framerate_numerator', 'maxFramerateNumerator', False, 'primitive'),
        FieldMeta('max_framerate_denominator', 'maxFramerateDenominator', False, 'primitive'),
    )


@register("SystemInfo.SubsamplingFormat")
class SubsamplingFormat(str, Enum):
    """YUV subsampling type of the pixels of a given image."""
    YUV420 = 'yuv420'
    YUV422 = 'yuv422'
    YUV444 = 'yuv444'


@register("SystemInfo.ImageType")
class ImageType(str, Enum):
    """Image format of a given image."""
    JPEG = 'jpeg'
    WEBP = 'webp'
    UNKNOWN = 'unknown'


@register("SystemInfo.GPUInfo")
@dataclass
class GPUInfo(DataType):
    """Provides information about the GPU(s) on the system."""
    devices: List[GPUDevice]
    driver_bug_workarounds: List[str]
    video_decoding: List[VideoDecodeAcceleratorCapability]
    video_encoding: List[VideoEncodeAcceleratorCapability]
    aux_attributes: Optional[Dict[str, Any]] = None
    feature_status: Optional[Dict[str, Any]] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('devices', 'devices', False, 'array', inner=FieldMeta('', '', False, 'object', ref='SystemInfo.GPUDevice')),
        FieldMeta('driver_bug_workarounds', 'driverBugWorkarounds', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('video_decoding', 'videoDecoding', False, 'array', inner=FieldMeta('', '', False, 'object', ref='SystemInfo.VideoDecodeAcceleratorCapability')),
        FieldMeta('video_encoding', 'videoEncoding', False, 'array', inner=FieldMeta('', '', False, 'object', ref='SystemInfo.VideoEncodeAcceleratorCapability')),
        FieldMeta('aux_attributes', 'auxAttributes', True, 'primitive'),
        FieldMeta('feature_status', 'featureStatus', True, 'primitive'),
    )


@register("SystemInfo.ProcessInfo")
@dataclass
class ProcessInfo(DataType):
    """Represents process info."""
    type_: str
    id: int
    cpu_time: float
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('type_', 'type', False, 'primitive'),
        FieldMeta('id', 'id', False, 'primitive'),
        FieldMeta('cpu_time', 'cpuTime', False, 'primitive'),
    )

__all__ = ["GPUDevice", "GPUInfo", "ImageType", "ProcessInfo", "Size", "SubsamplingFormat", "VideoDecodeAcceleratorCapability", "VideoEncodeAcceleratorCapability"]
