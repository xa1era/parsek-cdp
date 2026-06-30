"""Commands for the Browser domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode

if TYPE_CHECKING:
    from .types import (
        Bounds,
        BrowserCommandId,
        BrowserContextID,
        Histogram,
        PermissionDescriptor,
        PermissionSetting,
        PermissionType,
        PrivacySandboxAPI,
        WindowID,
    )
    from ..target.types import TargetID as Target_TargetID

@dataclass
class GetVersionReturn(DataType):
    """Return value of :meth:`Browser.get_version`."""
    protocol_version: str
    product: str
    revision: str
    user_agent: str
    js_version: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('protocol_version', 'protocolVersion', False, 'primitive'),
        FieldMeta('product', 'product', False, 'primitive'),
        FieldMeta('revision', 'revision', False, 'primitive'),
        FieldMeta('user_agent', 'userAgent', False, 'primitive'),
        FieldMeta('js_version', 'jsVersion', False, 'primitive'),
    )


@dataclass
class GetBrowserCommandLineReturn(DataType):
    """Return value of :meth:`Browser.get_browser_command_line`."""
    arguments: List[str]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('arguments', 'arguments', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


@dataclass
class GetHistogramsReturn(DataType):
    """Return value of :meth:`Browser.get_histograms`."""
    histograms: List[Histogram]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('histograms', 'histograms', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Browser.Histogram')),
    )


@dataclass
class GetHistogramReturn(DataType):
    """Return value of :meth:`Browser.get_histogram`."""
    histogram: Histogram
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('histogram', 'histogram', False, 'object', ref='Browser.Histogram'),
    )


@dataclass
class GetWindowBoundsReturn(DataType):
    """Return value of :meth:`Browser.get_window_bounds`."""
    bounds: Bounds
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('bounds', 'bounds', False, 'object', ref='Browser.Bounds'),
    )


@dataclass
class GetWindowForTargetReturn(DataType):
    """Return value of :meth:`Browser.get_window_for_target`."""
    window_id: WindowID
    bounds: Bounds
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('window_id', 'windowId', False, 'primitive'),
        FieldMeta('bounds', 'bounds', False, 'object', ref='Browser.Bounds'),
    )


class Browser:
    """Commands of the Browser domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def set_permission(self, *, permission: PermissionDescriptor, setting: PermissionSetting, origin: Optional[str] = None, embedded_origin: Optional[str] = None, browser_context_id: Optional[BrowserContextID] = None) -> None:
        """
        Set permission settings for given embedding and embedded origins.
        :param permission: Descriptor of permission to override.
        :param setting: Setting of the permission.
        :param origin: Embedding origin the permission applies to, all origins if not specified.
        :param embedded_origin: Embedded origin the permission applies to. It is ignored unless the embedding origin is
        present and valid. If the embedding origin is provided but the embedded origin isn't, the
        embedding origin is used as the embedded origin.
        :param browser_context_id: Context to override. When omitted, default browser context is used.
        """
        _params: Dict[str, Any] = {}
        _params['permission'] = encode(FieldMeta('', '', False, 'object', ref='Browser.PermissionDescriptor'), permission)
        _params['setting'] = encode(FieldMeta('', '', False, 'enum', ref='Browser.PermissionSetting'), setting)
        if origin is not None:
            _params['origin'] = encode(FieldMeta('', '', False, 'primitive'), origin)
        if embedded_origin is not None:
            _params['embeddedOrigin'] = encode(FieldMeta('', '', False, 'primitive'), embedded_origin)
        if browser_context_id is not None:
            _params['browserContextId'] = encode(FieldMeta('', '', False, 'primitive'), browser_context_id)
        _result = await self._target.send('Browser.setPermission', _params)
        return None

    async def grant_permissions(self, *, permissions: List[PermissionType], origin: Optional[str] = None, browser_context_id: Optional[BrowserContextID] = None) -> None:
        """
        Grant specific permissions to the given origin and reject all others. Deprecated. Use
        setPermission instead.
        
        .. deprecated::
        :param permissions:
        :param origin: Origin the permission applies to, all origins if not specified.
        :param browser_context_id: BrowserContext to override permissions. When omitted, default browser context is used.
        """
        _params: Dict[str, Any] = {}
        _params['permissions'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'enum', ref='Browser.PermissionType')), permissions)
        if origin is not None:
            _params['origin'] = encode(FieldMeta('', '', False, 'primitive'), origin)
        if browser_context_id is not None:
            _params['browserContextId'] = encode(FieldMeta('', '', False, 'primitive'), browser_context_id)
        _result = await self._target.send('Browser.grantPermissions', _params)
        return None

    async def reset_permissions(self, *, browser_context_id: Optional[BrowserContextID] = None) -> None:
        """
        Reset all permission management for all origins.
        :param browser_context_id: BrowserContext to reset permissions. When omitted, default browser context is used.
        """
        _params: Dict[str, Any] = {}
        if browser_context_id is not None:
            _params['browserContextId'] = encode(FieldMeta('', '', False, 'primitive'), browser_context_id)
        _result = await self._target.send('Browser.resetPermissions', _params)
        return None

    async def set_download_behavior(self, *, behavior: Literal['deny', 'allow', 'allowAndName', 'default'], browser_context_id: Optional[BrowserContextID] = None, download_path: Optional[str] = None, events_enabled: Optional[bool] = None) -> None:
        """
        Set the behavior when downloading a file.
        :param behavior: Whether to allow all or deny all download requests, or use default Chrome behavior if
        available (otherwise deny). |allowAndName| allows download and names files according to
        their download guids.
        :param browser_context_id: BrowserContext to set download behavior. When omitted, default browser context is used.
        :param download_path: The default path to save downloaded files to. This is required if behavior is set to 'allow'
        or 'allowAndName'.
        :param events_enabled: Whether to emit download events (defaults to false).
        """
        _params: Dict[str, Any] = {}
        _params['behavior'] = encode(FieldMeta('', '', False, 'primitive'), behavior)
        if browser_context_id is not None:
            _params['browserContextId'] = encode(FieldMeta('', '', False, 'primitive'), browser_context_id)
        if download_path is not None:
            _params['downloadPath'] = encode(FieldMeta('', '', False, 'primitive'), download_path)
        if events_enabled is not None:
            _params['eventsEnabled'] = encode(FieldMeta('', '', False, 'primitive'), events_enabled)
        _result = await self._target.send('Browser.setDownloadBehavior', _params)
        return None

    async def cancel_download(self, *, guid: str, browser_context_id: Optional[BrowserContextID] = None) -> None:
        """
        Cancel a download if in progress
        :param guid: Global unique identifier of the download.
        :param browser_context_id: BrowserContext to perform the action in. When omitted, default browser context is used.
        """
        _params: Dict[str, Any] = {}
        _params['guid'] = encode(FieldMeta('', '', False, 'primitive'), guid)
        if browser_context_id is not None:
            _params['browserContextId'] = encode(FieldMeta('', '', False, 'primitive'), browser_context_id)
        _result = await self._target.send('Browser.cancelDownload', _params)
        return None

    async def close(self) -> None:
        """Close browser gracefully."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Browser.close', _params)
        return None

    async def crash(self) -> None:
        """Crashes browser on the main thread."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Browser.crash', _params)
        return None

    async def crash_gpu_process(self) -> None:
        """Crashes GPU process."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Browser.crashGpuProcess', _params)
        return None

    async def get_version(self) -> GetVersionReturn:
        """Returns version information."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Browser.getVersion', _params)
        return GetVersionReturn.from_json(_result)

    async def get_browser_command_line(self) -> GetBrowserCommandLineReturn:
        """
        Returns the command line switches for the browser process if, and only if
        --enable-automation is on the commandline.
        """
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Browser.getBrowserCommandLine', _params)
        return GetBrowserCommandLineReturn.from_json(_result)

    async def get_histograms(self, *, query: Optional[str] = None, delta: Optional[bool] = None) -> GetHistogramsReturn:
        """
        Get Chrome histograms.
        :param query: Requested substring in name. Only histograms which have query as a
        substring in their name are extracted. An empty or absent query returns
        all histograms.
        :param delta: If true, retrieve delta since last delta call.
        """
        _params: Dict[str, Any] = {}
        if query is not None:
            _params['query'] = encode(FieldMeta('', '', False, 'primitive'), query)
        if delta is not None:
            _params['delta'] = encode(FieldMeta('', '', False, 'primitive'), delta)
        _result = await self._target.send('Browser.getHistograms', _params)
        return GetHistogramsReturn.from_json(_result)

    async def get_histogram(self, *, name: str, delta: Optional[bool] = None) -> GetHistogramReturn:
        """
        Get a Chrome histogram by name.
        :param name: Requested histogram name.
        :param delta: If true, retrieve delta since last delta call.
        """
        _params: Dict[str, Any] = {}
        _params['name'] = encode(FieldMeta('', '', False, 'primitive'), name)
        if delta is not None:
            _params['delta'] = encode(FieldMeta('', '', False, 'primitive'), delta)
        _result = await self._target.send('Browser.getHistogram', _params)
        return GetHistogramReturn.from_json(_result)

    async def get_window_bounds(self, *, window_id: WindowID) -> GetWindowBoundsReturn:
        """
        Get position and size of the browser window.
        :param window_id: Browser window id.
        """
        _params: Dict[str, Any] = {}
        _params['windowId'] = encode(FieldMeta('', '', False, 'primitive'), window_id)
        _result = await self._target.send('Browser.getWindowBounds', _params)
        return GetWindowBoundsReturn.from_json(_result)

    async def get_window_for_target(self, *, target_id: Optional[Target_TargetID] = None) -> GetWindowForTargetReturn:
        """
        Get the browser window that contains the devtools target.
        :param target_id: Devtools agent host id. If called as a part of the session, associated targetId is used.
        """
        _params: Dict[str, Any] = {}
        if target_id is not None:
            _params['targetId'] = encode(FieldMeta('', '', False, 'primitive'), target_id)
        _result = await self._target.send('Browser.getWindowForTarget', _params)
        return GetWindowForTargetReturn.from_json(_result)

    async def set_window_bounds(self, *, window_id: WindowID, bounds: Bounds) -> None:
        """
        Set position and/or size of the browser window.
        :param window_id: Browser window id.
        :param bounds: New window bounds. The 'minimized', 'maximized' and 'fullscreen' states cannot be combined
        with 'left', 'top', 'width' or 'height'. Leaves unspecified fields unchanged.
        """
        _params: Dict[str, Any] = {}
        _params['windowId'] = encode(FieldMeta('', '', False, 'primitive'), window_id)
        _params['bounds'] = encode(FieldMeta('', '', False, 'object', ref='Browser.Bounds'), bounds)
        _result = await self._target.send('Browser.setWindowBounds', _params)
        return None

    async def set_contents_size(self, *, window_id: WindowID, width: Optional[int] = None, height: Optional[int] = None) -> None:
        """
        Set size of the browser contents resizing browser window as necessary.
        :param window_id: Browser window id.
        :param width: The window contents width in DIP. Assumes current width if omitted.
        Must be specified if 'height' is omitted.
        :param height: The window contents height in DIP. Assumes current height if omitted.
        Must be specified if 'width' is omitted.
        """
        _params: Dict[str, Any] = {}
        _params['windowId'] = encode(FieldMeta('', '', False, 'primitive'), window_id)
        if width is not None:
            _params['width'] = encode(FieldMeta('', '', False, 'primitive'), width)
        if height is not None:
            _params['height'] = encode(FieldMeta('', '', False, 'primitive'), height)
        _result = await self._target.send('Browser.setContentsSize', _params)
        return None

    async def set_dock_tile(self, *, badge_label: Optional[str] = None, image: Optional[str] = None) -> None:
        """
        Set dock tile details, platform-specific.
        :param badge_label:
        :param image: Png encoded image. (Encoded as a base64 string when passed over JSON)
        """
        _params: Dict[str, Any] = {}
        if badge_label is not None:
            _params['badgeLabel'] = encode(FieldMeta('', '', False, 'primitive'), badge_label)
        if image is not None:
            _params['image'] = encode(FieldMeta('', '', False, 'primitive'), image)
        _result = await self._target.send('Browser.setDockTile', _params)
        return None

    async def execute_browser_command(self, *, command_id: BrowserCommandId) -> None:
        """
        Invoke custom browser commands used by telemetry.
        :param command_id:
        """
        _params: Dict[str, Any] = {}
        _params['commandId'] = encode(FieldMeta('', '', False, 'enum', ref='Browser.BrowserCommandId'), command_id)
        _result = await self._target.send('Browser.executeBrowserCommand', _params)
        return None

    async def add_privacy_sandbox_enrollment_override(self, *, url: str) -> None:
        """
        Allows a site to use privacy sandbox features that require enrollment
        without the site actually being enrolled. Only supported on page targets.
        :param url:
        """
        _params: Dict[str, Any] = {}
        _params['url'] = encode(FieldMeta('', '', False, 'primitive'), url)
        _result = await self._target.send('Browser.addPrivacySandboxEnrollmentOverride', _params)
        return None

    async def add_privacy_sandbox_coordinator_key_config(self, *, api: PrivacySandboxAPI, coordinator_origin: str, key_config: str, browser_context_id: Optional[BrowserContextID] = None) -> None:
        """
        Configures encryption keys used with a given privacy sandbox API to talk
        to a trusted coordinator.  Since this is intended for test automation only,
        coordinatorOrigin must be a .test domain. No existing coordinator
        configuration for the origin may exist.
        :param api:
        :param coordinator_origin:
        :param key_config:
        :param browser_context_id: BrowserContext to perform the action in. When omitted, default browser
        context is used.
        """
        _params: Dict[str, Any] = {}
        _params['api'] = encode(FieldMeta('', '', False, 'enum', ref='Browser.PrivacySandboxAPI'), api)
        _params['coordinatorOrigin'] = encode(FieldMeta('', '', False, 'primitive'), coordinator_origin)
        _params['keyConfig'] = encode(FieldMeta('', '', False, 'primitive'), key_config)
        if browser_context_id is not None:
            _params['browserContextId'] = encode(FieldMeta('', '', False, 'primitive'), browser_context_id)
        _result = await self._target.send('Browser.addPrivacySandboxCoordinatorKeyConfig', _params)
        return None
