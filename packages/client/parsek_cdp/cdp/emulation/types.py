"""Custom types and enums for the Emulation domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, register


@register("Emulation.SafeAreaInsets")
@dataclass
class SafeAreaInsets(DataType):
    top: Optional[int] = None
    top_max: Optional[int] = None
    left: Optional[int] = None
    left_max: Optional[int] = None
    bottom: Optional[int] = None
    bottom_max: Optional[int] = None
    right: Optional[int] = None
    right_max: Optional[int] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('top', 'top', True, 'primitive'),
        FieldMeta('top_max', 'topMax', True, 'primitive'),
        FieldMeta('left', 'left', True, 'primitive'),
        FieldMeta('left_max', 'leftMax', True, 'primitive'),
        FieldMeta('bottom', 'bottom', True, 'primitive'),
        FieldMeta('bottom_max', 'bottomMax', True, 'primitive'),
        FieldMeta('right', 'right', True, 'primitive'),
        FieldMeta('right_max', 'rightMax', True, 'primitive'),
    )


@register("Emulation.ScreenOrientation")
@dataclass
class ScreenOrientation(DataType):
    """Screen orientation."""
    type_: Literal['portraitPrimary', 'portraitSecondary', 'landscapePrimary', 'landscapeSecondary']
    angle: int
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('type_', 'type', False, 'primitive'),
        FieldMeta('angle', 'angle', False, 'primitive'),
    )


@register("Emulation.DisplayFeature")
@dataclass
class DisplayFeature(DataType):
    orientation: Literal['vertical', 'horizontal']
    offset: int
    mask_length: int
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('orientation', 'orientation', False, 'primitive'),
        FieldMeta('offset', 'offset', False, 'primitive'),
        FieldMeta('mask_length', 'maskLength', False, 'primitive'),
    )


@register("Emulation.DevicePosture")
@dataclass
class DevicePosture(DataType):
    type_: Literal['continuous', 'folded']
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('type_', 'type', False, 'primitive'),
    )


@register("Emulation.MediaFeature")
@dataclass
class MediaFeature(DataType):
    name: str
    value: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('name', 'name', False, 'primitive'),
        FieldMeta('value', 'value', False, 'primitive'),
    )


@register("Emulation.VirtualTimePolicy")
class VirtualTimePolicy(str, Enum):
    """
    advance: If the scheduler runs out of immediate work, the virtual time base may fast forward to
    allow the next delayed task (if any) to run; pause: The virtual time base may not advance;
    pauseIfNetworkFetchesPending: The virtual time base may not advance if there are any pending
    resource fetches.
    """
    ADVANCE = 'advance'
    PAUSE = 'pause'
    PAUSEIFNETWORKFETCHESPENDING = 'pauseIfNetworkFetchesPending'


@register("Emulation.UserAgentBrandVersion")
@dataclass
class UserAgentBrandVersion(DataType):
    """Used to specify User Agent Client Hints to emulate. See https://wicg.github.io/ua-client-hints"""
    brand: str
    version: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('brand', 'brand', False, 'primitive'),
        FieldMeta('version', 'version', False, 'primitive'),
    )


@register("Emulation.UserAgentMetadata")
@dataclass
class UserAgentMetadata(DataType):
    """
    Used to specify User Agent Client Hints to emulate. See https://wicg.github.io/ua-client-hints
    Missing optional values will be filled in by the target with what it would normally use.
    """
    platform: str
    platform_version: str
    architecture: str
    model: str
    mobile: bool
    brands: Optional[List[UserAgentBrandVersion]] = None
    full_version_list: Optional[List[UserAgentBrandVersion]] = None
    full_version: Optional[str] = None
    bitness: Optional[str] = None
    wow64: Optional[bool] = None
    form_factors: Optional[List[str]] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('platform', 'platform', False, 'primitive'),
        FieldMeta('platform_version', 'platformVersion', False, 'primitive'),
        FieldMeta('architecture', 'architecture', False, 'primitive'),
        FieldMeta('model', 'model', False, 'primitive'),
        FieldMeta('mobile', 'mobile', False, 'primitive'),
        FieldMeta('brands', 'brands', True, 'array', inner=FieldMeta('', '', False, 'object', ref='Emulation.UserAgentBrandVersion')),
        FieldMeta('full_version_list', 'fullVersionList', True, 'array', inner=FieldMeta('', '', False, 'object', ref='Emulation.UserAgentBrandVersion')),
        FieldMeta('full_version', 'fullVersion', True, 'primitive'),
        FieldMeta('bitness', 'bitness', True, 'primitive'),
        FieldMeta('wow64', 'wow64', True, 'primitive'),
        FieldMeta('form_factors', 'formFactors', True, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


@register("Emulation.SensorType")
class SensorType(str, Enum):
    """
    Used to specify sensor types to emulate.
    See https://w3c.github.io/sensors/#automation for more information.
    """
    ABSOLUTE_ORIENTATION = 'absolute-orientation'
    ACCELEROMETER = 'accelerometer'
    AMBIENT_LIGHT = 'ambient-light'
    GRAVITY = 'gravity'
    GYROSCOPE = 'gyroscope'
    LINEAR_ACCELERATION = 'linear-acceleration'
    MAGNETOMETER = 'magnetometer'
    RELATIVE_ORIENTATION = 'relative-orientation'


@register("Emulation.SensorMetadata")
@dataclass
class SensorMetadata(DataType):
    available: Optional[bool] = None
    minimum_frequency: Optional[float] = None
    maximum_frequency: Optional[float] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('available', 'available', True, 'primitive'),
        FieldMeta('minimum_frequency', 'minimumFrequency', True, 'primitive'),
        FieldMeta('maximum_frequency', 'maximumFrequency', True, 'primitive'),
    )


@register("Emulation.SensorReadingSingle")
@dataclass
class SensorReadingSingle(DataType):
    value: float
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('value', 'value', False, 'primitive'),
    )


@register("Emulation.SensorReadingXYZ")
@dataclass
class SensorReadingXYZ(DataType):
    x: float
    y: float
    z: float
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('x', 'x', False, 'primitive'),
        FieldMeta('y', 'y', False, 'primitive'),
        FieldMeta('z', 'z', False, 'primitive'),
    )


@register("Emulation.SensorReadingQuaternion")
@dataclass
class SensorReadingQuaternion(DataType):
    x: float
    y: float
    z: float
    w: float
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('x', 'x', False, 'primitive'),
        FieldMeta('y', 'y', False, 'primitive'),
        FieldMeta('z', 'z', False, 'primitive'),
        FieldMeta('w', 'w', False, 'primitive'),
    )


@register("Emulation.SensorReading")
@dataclass
class SensorReading(DataType):
    single: Optional[SensorReadingSingle] = None
    xyz: Optional[SensorReadingXYZ] = None
    quaternion: Optional[SensorReadingQuaternion] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('single', 'single', True, 'object', ref='Emulation.SensorReadingSingle'),
        FieldMeta('xyz', 'xyz', True, 'object', ref='Emulation.SensorReadingXYZ'),
        FieldMeta('quaternion', 'quaternion', True, 'object', ref='Emulation.SensorReadingQuaternion'),
    )


@register("Emulation.PressureSource")
class PressureSource(str, Enum):
    CPU = 'cpu'


@register("Emulation.PressureState")
class PressureState(str, Enum):
    NOMINAL = 'nominal'
    FAIR = 'fair'
    SERIOUS = 'serious'
    CRITICAL = 'critical'


@register("Emulation.PressureMetadata")
@dataclass
class PressureMetadata(DataType):
    available: Optional[bool] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('available', 'available', True, 'primitive'),
    )


@register("Emulation.WorkAreaInsets")
@dataclass
class WorkAreaInsets(DataType):
    top: Optional[int] = None
    left: Optional[int] = None
    bottom: Optional[int] = None
    right: Optional[int] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('top', 'top', True, 'primitive'),
        FieldMeta('left', 'left', True, 'primitive'),
        FieldMeta('bottom', 'bottom', True, 'primitive'),
        FieldMeta('right', 'right', True, 'primitive'),
    )


type ScreenId = str


@register("Emulation.ScreenInfo")
@dataclass
class ScreenInfo(DataType):
    """
    Screen information similar to the one returned by window.getScreenDetails() method,
    see https://w3c.github.io/window-management/#screendetailed.
    """
    left: int
    top: int
    width: int
    height: int
    avail_left: int
    avail_top: int
    avail_width: int
    avail_height: int
    device_pixel_ratio: float
    orientation: ScreenOrientation
    color_depth: int
    is_extended: bool
    is_internal: bool
    is_primary: bool
    label: str
    id: ScreenId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('left', 'left', False, 'primitive'),
        FieldMeta('top', 'top', False, 'primitive'),
        FieldMeta('width', 'width', False, 'primitive'),
        FieldMeta('height', 'height', False, 'primitive'),
        FieldMeta('avail_left', 'availLeft', False, 'primitive'),
        FieldMeta('avail_top', 'availTop', False, 'primitive'),
        FieldMeta('avail_width', 'availWidth', False, 'primitive'),
        FieldMeta('avail_height', 'availHeight', False, 'primitive'),
        FieldMeta('device_pixel_ratio', 'devicePixelRatio', False, 'primitive'),
        FieldMeta('orientation', 'orientation', False, 'object', ref='Emulation.ScreenOrientation'),
        FieldMeta('color_depth', 'colorDepth', False, 'primitive'),
        FieldMeta('is_extended', 'isExtended', False, 'primitive'),
        FieldMeta('is_internal', 'isInternal', False, 'primitive'),
        FieldMeta('is_primary', 'isPrimary', False, 'primitive'),
        FieldMeta('label', 'label', False, 'primitive'),
        FieldMeta('id', 'id', False, 'primitive'),
    )


@register("Emulation.DisabledImageType")
class DisabledImageType(str, Enum):
    """Enum of image types that can be disabled."""
    AVIF = 'avif'
    WEBP = 'webp'

__all__ = ["DevicePosture", "DisabledImageType", "DisplayFeature", "MediaFeature", "PressureMetadata", "PressureSource", "PressureState", "SafeAreaInsets", "ScreenId", "ScreenInfo", "ScreenOrientation", "SensorMetadata", "SensorReading", "SensorReadingQuaternion", "SensorReadingSingle", "SensorReadingXYZ", "SensorType", "UserAgentBrandVersion", "UserAgentMetadata", "VirtualTimePolicy", "WorkAreaInsets"]
