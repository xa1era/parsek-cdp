"""Commands for the PWA domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode

if TYPE_CHECKING:
    from .types import (
        DisplayMode,
        FileHandler,
    )
    from ..target.types import TargetID as Target_TargetID

@dataclass
class GetOsAppStateReturn(DataType):
    """Return value of :meth:`PWA.get_os_app_state`."""
    badge_count: int
    file_handlers: List[FileHandler]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('badge_count', 'badgeCount', False, 'primitive'),
        FieldMeta('file_handlers', 'fileHandlers', False, 'array', inner=FieldMeta('', '', False, 'object', ref='PWA.FileHandler')),
    )


@dataclass
class LaunchReturn(DataType):
    """Return value of :meth:`PWA.launch`."""
    target_id: Target_TargetID
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('target_id', 'targetId', False, 'primitive'),
    )


@dataclass
class LaunchFilesInAppReturn(DataType):
    """Return value of :meth:`PWA.launch_files_in_app`."""
    target_ids: List[Target_TargetID]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('target_ids', 'targetIds', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


class PWA:
    """Commands of the PWA domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def get_os_app_state(self, *, manifest_id: str) -> GetOsAppStateReturn:
        """
        Returns the following OS state for the given manifest id.
        :param manifest_id: The id from the webapp's manifest file, commonly it's the url of the
        site installing the webapp. See
        https://web.dev/learn/pwa/web-app-manifest.
        """
        _params: Dict[str, Any] = {}
        _params['manifestId'] = encode(FieldMeta('', '', False, 'primitive'), manifest_id)
        _result = await self._target.send('PWA.getOsAppState', _params)
        return GetOsAppStateReturn.from_json(_result)

    async def install(self, *, manifest_id: str, install_url_or_bundle_url: Optional[str] = None) -> None:
        """
        Installs the given manifest identity, optionally using the given installUrlOrBundleUrl
        
        IWA-specific install description:
        manifestId corresponds to isolated-app:// + web_package::SignedWebBundleId
        
        File installation mode:
        The installUrlOrBundleUrl can be either file:// or http(s):// pointing
        to a signed web bundle (.swbn). In this case SignedWebBundleId must correspond to
        The .swbn file's signing key.
        
        Dev proxy installation mode:
        installUrlOrBundleUrl must be http(s):// that serves dev mode IWA.
        web_package::SignedWebBundleId must be of type dev proxy.
        
        The advantage of dev proxy mode is that all changes to IWA
        automatically will be reflected in the running app without
        reinstallation.
        
        To generate bundle id for proxy mode:
        1. Generate 32 random bytes.
        2. Add a specific suffix at the end following the documentation
           https://github.com/WICG/isolated-web-apps/blob/main/Scheme.md#suffix
        3. Encode the entire sequence using Base32 without padding.
        
        If Chrome is not in IWA dev
        mode, the installation will fail, regardless of the state of the allowlist.
        :param manifest_id:
        :param install_url_or_bundle_url: The location of the app or bundle overriding the one derived from the
        manifestId.
        """
        _params: Dict[str, Any] = {}
        _params['manifestId'] = encode(FieldMeta('', '', False, 'primitive'), manifest_id)
        if install_url_or_bundle_url is not None:
            _params['installUrlOrBundleUrl'] = encode(FieldMeta('', '', False, 'primitive'), install_url_or_bundle_url)
        _result = await self._target.send('PWA.install', _params)
        return None

    async def uninstall(self, *, manifest_id: str) -> None:
        """
        Uninstalls the given manifest_id and closes any opened app windows.
        :param manifest_id:
        """
        _params: Dict[str, Any] = {}
        _params['manifestId'] = encode(FieldMeta('', '', False, 'primitive'), manifest_id)
        _result = await self._target.send('PWA.uninstall', _params)
        return None

    async def launch(self, *, manifest_id: str, url: Optional[str] = None) -> LaunchReturn:
        """
        Launches the installed web app, or an url in the same web app instead of the
        default start url if it is provided. Returns a page Target.TargetID which
        can be used to attach to via Target.attachToTarget or similar APIs.
        :param manifest_id:
        :param url:
        """
        _params: Dict[str, Any] = {}
        _params['manifestId'] = encode(FieldMeta('', '', False, 'primitive'), manifest_id)
        if url is not None:
            _params['url'] = encode(FieldMeta('', '', False, 'primitive'), url)
        _result = await self._target.send('PWA.launch', _params)
        return LaunchReturn.from_json(_result)

    async def launch_files_in_app(self, *, manifest_id: str, files: List[str]) -> LaunchFilesInAppReturn:
        """
        Opens one or more local files from an installed web app identified by its
        manifestId. The web app needs to have file handlers registered to process
        the files. The API returns one or more page Target.TargetIDs which can be
        used to attach to via Target.attachToTarget or similar APIs.
        If some files in the parameters cannot be handled by the web app, they will
        be ignored. If none of the files can be handled, this API returns an error.
        If no files are provided as the parameter, this API also returns an error.
        
        According to the definition of the file handlers in the manifest file, one
        Target.TargetID may represent a page handling one or more files. The order
        of the returned Target.TargetIDs is not guaranteed.
        
        TODO(crbug.com/339454034): Check the existences of the input files.
        :param manifest_id:
        :param files:
        """
        _params: Dict[str, Any] = {}
        _params['manifestId'] = encode(FieldMeta('', '', False, 'primitive'), manifest_id)
        _params['files'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'primitive')), files)
        _result = await self._target.send('PWA.launchFilesInApp', _params)
        return LaunchFilesInAppReturn.from_json(_result)

    async def open_current_page_in_app(self, *, manifest_id: str) -> None:
        """
        Opens the current page in its web app identified by the manifest id, needs
        to be called on a page target. This function returns immediately without
        waiting for the app to finish loading.
        :param manifest_id:
        """
        _params: Dict[str, Any] = {}
        _params['manifestId'] = encode(FieldMeta('', '', False, 'primitive'), manifest_id)
        _result = await self._target.send('PWA.openCurrentPageInApp', _params)
        return None

    async def change_app_user_settings(self, *, manifest_id: str, link_capturing: Optional[bool] = None, display_mode: Optional[DisplayMode] = None) -> None:
        """
        Changes user settings of the web app identified by its manifestId. If the
        app was not installed, this command returns an error. Unset parameters will
        be ignored; unrecognized values will cause an error.
        
        Unlike the ones defined in the manifest files of the web apps, these
        settings are provided by the browser and controlled by the users, they
        impact the way the browser handling the web apps.
        
        See the comment of each parameter.
        :param manifest_id:
        :param link_capturing: If user allows the links clicked on by the user in the app's scope, or
        extended scope if the manifest has scope extensions and the flags
        `DesktopPWAsLinkCapturingWithScopeExtensions` and
        `WebAppEnableScopeExtensions` are enabled.
        
        Note, the API does not support resetting the linkCapturing to the
        initial value, uninstalling and installing the web app again will reset
        it.
        
        TODO(crbug.com/339453269): Setting this value on ChromeOS is not
        supported yet.
        :param display_mode:
        """
        _params: Dict[str, Any] = {}
        _params['manifestId'] = encode(FieldMeta('', '', False, 'primitive'), manifest_id)
        if link_capturing is not None:
            _params['linkCapturing'] = encode(FieldMeta('', '', False, 'primitive'), link_capturing)
        if display_mode is not None:
            _params['displayMode'] = encode(FieldMeta('', '', False, 'enum', ref='PWA.DisplayMode'), display_mode)
        _result = await self._target.send('PWA.changeAppUserSettings', _params)
        return None
