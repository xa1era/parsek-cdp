"""Custom types and enums for the Browser domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, register


type BrowserContextID = str


type WindowID = int


@register("Browser.WindowState")
class WindowState(str, Enum):
    """The state of the browser window."""
    NORMAL = 'normal'
    MINIMIZED = 'minimized'
    MAXIMIZED = 'maximized'
    FULLSCREEN = 'fullscreen'


@register("Browser.Bounds")
@dataclass
class Bounds(DataType):
    """Browser window bounds information"""
    left: Optional[int] = None
    top: Optional[int] = None
    width: Optional[int] = None
    height: Optional[int] = None
    window_state: Optional[WindowState] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('left', 'left', True, 'primitive'),
        FieldMeta('top', 'top', True, 'primitive'),
        FieldMeta('width', 'width', True, 'primitive'),
        FieldMeta('height', 'height', True, 'primitive'),
        FieldMeta('window_state', 'windowState', True, 'enum', ref='Browser.WindowState'),
    )


@register("Browser.PermissionType")
class PermissionType(str, Enum):
    AR = 'ar'
    AUDIOCAPTURE = 'audioCapture'
    AUTOMATICFULLSCREEN = 'automaticFullscreen'
    BACKGROUNDFETCH = 'backgroundFetch'
    BACKGROUNDSYNC = 'backgroundSync'
    CAMERAPANTILTZOOM = 'cameraPanTiltZoom'
    CAPTUREDSURFACECONTROL = 'capturedSurfaceControl'
    CLIPBOARDREADWRITE = 'clipboardReadWrite'
    CLIPBOARDSANITIZEDWRITE = 'clipboardSanitizedWrite'
    DISPLAYCAPTURE = 'displayCapture'
    DURABLESTORAGE = 'durableStorage'
    GEOLOCATION = 'geolocation'
    HANDTRACKING = 'handTracking'
    IDLEDETECTION = 'idleDetection'
    KEYBOARDLOCK = 'keyboardLock'
    LOCALFONTS = 'localFonts'
    LOCALNETWORKACCESS = 'localNetworkAccess'
    MIDI = 'midi'
    MIDISYSEX = 'midiSysex'
    NFC = 'nfc'
    NOTIFICATIONS = 'notifications'
    PAYMENTHANDLER = 'paymentHandler'
    PERIODICBACKGROUNDSYNC = 'periodicBackgroundSync'
    POINTERLOCK = 'pointerLock'
    PROTECTEDMEDIAIDENTIFIER = 'protectedMediaIdentifier'
    SENSORS = 'sensors'
    SMARTCARD = 'smartCard'
    SPEAKERSELECTION = 'speakerSelection'
    STORAGEACCESS = 'storageAccess'
    TOPLEVELSTORAGEACCESS = 'topLevelStorageAccess'
    VIDEOCAPTURE = 'videoCapture'
    VR = 'vr'
    WAKELOCKSCREEN = 'wakeLockScreen'
    WAKELOCKSYSTEM = 'wakeLockSystem'
    WEBAPPINSTALLATION = 'webAppInstallation'
    WEBPRINTING = 'webPrinting'
    WINDOWMANAGEMENT = 'windowManagement'


@register("Browser.PermissionSetting")
class PermissionSetting(str, Enum):
    GRANTED = 'granted'
    DENIED = 'denied'
    PROMPT = 'prompt'


@register("Browser.PermissionDescriptor")
@dataclass
class PermissionDescriptor(DataType):
    """
    Definition of PermissionDescriptor defined in the Permissions API:
    https://w3c.github.io/permissions/#dom-permissiondescriptor.
    """
    name: str
    sysex: Optional[bool] = None
    user_visible_only: Optional[bool] = None
    allow_without_sanitization: Optional[bool] = None
    allow_without_gesture: Optional[bool] = None
    pan_tilt_zoom: Optional[bool] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('name', 'name', False, 'primitive'),
        FieldMeta('sysex', 'sysex', True, 'primitive'),
        FieldMeta('user_visible_only', 'userVisibleOnly', True, 'primitive'),
        FieldMeta('allow_without_sanitization', 'allowWithoutSanitization', True, 'primitive'),
        FieldMeta('allow_without_gesture', 'allowWithoutGesture', True, 'primitive'),
        FieldMeta('pan_tilt_zoom', 'panTiltZoom', True, 'primitive'),
    )


@register("Browser.BrowserCommandId")
class BrowserCommandId(str, Enum):
    """Browser command ids used by executeBrowserCommand."""
    OPENTABSEARCH = 'openTabSearch'
    CLOSETABSEARCH = 'closeTabSearch'
    OPENGLIC = 'openGlic'


@register("Browser.Bucket")
@dataclass
class Bucket(DataType):
    """Chrome histogram bucket."""
    low: int
    high: int
    count: int
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('low', 'low', False, 'primitive'),
        FieldMeta('high', 'high', False, 'primitive'),
        FieldMeta('count', 'count', False, 'primitive'),
    )


@register("Browser.Histogram")
@dataclass
class Histogram(DataType):
    """Chrome histogram."""
    name: str
    sum: int
    count: int
    buckets: List[Bucket]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('name', 'name', False, 'primitive'),
        FieldMeta('sum', 'sum', False, 'primitive'),
        FieldMeta('count', 'count', False, 'primitive'),
        FieldMeta('buckets', 'buckets', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Browser.Bucket')),
    )


@register("Browser.PrivacySandboxAPI")
class PrivacySandboxAPI(str, Enum):
    BIDDINGANDAUCTIONSERVICES = 'BiddingAndAuctionServices'
    TRUSTEDKEYVALUE = 'TrustedKeyValue'

__all__ = ["Bounds", "BrowserCommandId", "BrowserContextID", "Bucket", "Histogram", "PermissionDescriptor", "PermissionSetting", "PermissionType", "PrivacySandboxAPI", "WindowID", "WindowState"]
