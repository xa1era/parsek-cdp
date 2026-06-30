"""Commands for the Target domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode

if TYPE_CHECKING:
    from .types import (
        RemoteLocation,
        SessionID,
        TargetFilter,
        TargetID,
        TargetInfo,
        WindowState,
    )
    from ..browser.types import BrowserContextID as Browser_BrowserContextID

@dataclass
class AttachToTargetReturn(DataType):
    """Return value of :meth:`Target.attach_to_target`."""
    session_id: SessionID
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('session_id', 'sessionId', False, 'primitive'),
    )


@dataclass
class AttachToBrowserTargetReturn(DataType):
    """Return value of :meth:`Target.attach_to_browser_target`."""
    session_id: SessionID
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('session_id', 'sessionId', False, 'primitive'),
    )


@dataclass
class CloseTargetReturn(DataType):
    """Return value of :meth:`Target.close_target`."""
    success: bool
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('success', 'success', False, 'primitive'),
    )


@dataclass
class CreateBrowserContextReturn(DataType):
    """Return value of :meth:`Target.create_browser_context`."""
    browser_context_id: Browser_BrowserContextID
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('browser_context_id', 'browserContextId', False, 'primitive'),
    )


@dataclass
class GetBrowserContextsReturn(DataType):
    """Return value of :meth:`Target.get_browser_contexts`."""
    browser_context_ids: List[Browser_BrowserContextID]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('browser_context_ids', 'browserContextIds', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


@dataclass
class CreateTargetReturn(DataType):
    """Return value of :meth:`Target.create_target`."""
    target_id: TargetID
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('target_id', 'targetId', False, 'primitive'),
    )


@dataclass
class GetTargetInfoReturn(DataType):
    """Return value of :meth:`Target.get_target_info`."""
    target_info: TargetInfo
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('target_info', 'targetInfo', False, 'object', ref='Target.TargetInfo'),
    )


@dataclass
class GetTargetsReturn(DataType):
    """Return value of :meth:`Target.get_targets`."""
    target_infos: List[TargetInfo]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('target_infos', 'targetInfos', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Target.TargetInfo')),
    )


@dataclass
class GetDevToolsTargetReturn(DataType):
    """Return value of :meth:`Target.get_dev_tools_target`."""
    target_id: Optional[TargetID] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('target_id', 'targetId', True, 'primitive'),
    )


@dataclass
class OpenDevToolsReturn(DataType):
    """Return value of :meth:`Target.open_dev_tools`."""
    target_id: TargetID
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('target_id', 'targetId', False, 'primitive'),
    )


class Target:
    """Commands of the Target domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def activate_target(self, *, target_id: TargetID) -> None:
        """
        Activates (focuses) the target.
        :param target_id:
        """
        _params: Dict[str, Any] = {}
        _params['targetId'] = encode(FieldMeta('', '', False, 'primitive'), target_id)
        _result = await self._target.send('Target.activateTarget', _params)
        return None

    async def attach_to_target(self, *, target_id: TargetID, flatten: Optional[bool] = None) -> AttachToTargetReturn:
        """
        Attaches to the target with given id.
        :param target_id:
        :param flatten: Enables "flat" access to the session via specifying sessionId attribute in the commands.
        We plan to make this the default, deprecate non-flattened mode,
        and eventually retire it. See crbug.com/991325.
        """
        _params: Dict[str, Any] = {}
        _params['targetId'] = encode(FieldMeta('', '', False, 'primitive'), target_id)
        if flatten is not None:
            _params['flatten'] = encode(FieldMeta('', '', False, 'primitive'), flatten)
        _result = await self._target.send('Target.attachToTarget', _params)
        return AttachToTargetReturn.from_json(_result)

    async def attach_to_browser_target(self) -> AttachToBrowserTargetReturn:
        """Attaches to the browser target, only uses flat sessionId mode."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Target.attachToBrowserTarget', _params)
        return AttachToBrowserTargetReturn.from_json(_result)

    async def close_target(self, *, target_id: TargetID) -> CloseTargetReturn:
        """
        Closes the target. If the target is a page that gets closed too.
        :param target_id:
        """
        _params: Dict[str, Any] = {}
        _params['targetId'] = encode(FieldMeta('', '', False, 'primitive'), target_id)
        _result = await self._target.send('Target.closeTarget', _params)
        return CloseTargetReturn.from_json(_result)

    async def expose_dev_tools_protocol(self, *, target_id: TargetID, binding_name: Optional[str] = None, inherit_permissions: Optional[bool] = None) -> None:
        """
        Inject object to the target's main frame that provides a communication
        channel with browser target.
        
        Injected object will be available as `window[bindingName]`.
        
        The object has the following API:
        - `binding.send(json)` - a method to send messages over the remote debugging protocol
        - `binding.onmessage = json => handleMessage(json)` - a callback that will be called for the protocol notifications and command responses.
        :param target_id:
        :param binding_name: Binding name, 'cdp' if not specified.
        :param inherit_permissions: If true, inherits the current root session's permissions (default: false).
        """
        _params: Dict[str, Any] = {}
        _params['targetId'] = encode(FieldMeta('', '', False, 'primitive'), target_id)
        if binding_name is not None:
            _params['bindingName'] = encode(FieldMeta('', '', False, 'primitive'), binding_name)
        if inherit_permissions is not None:
            _params['inheritPermissions'] = encode(FieldMeta('', '', False, 'primitive'), inherit_permissions)
        _result = await self._target.send('Target.exposeDevToolsProtocol', _params)
        return None

    async def create_browser_context(self, *, dispose_on_detach: Optional[bool] = None, proxy_server: Optional[str] = None, proxy_bypass_list: Optional[str] = None, origins_with_universal_network_access: Optional[List[str]] = None) -> CreateBrowserContextReturn:
        """
        Creates a new empty BrowserContext. Similar to an incognito profile but you can have more than
        one.
        :param dispose_on_detach: If specified, disposes this context when debugging session disconnects.
        :param proxy_server: Proxy server, similar to the one passed to --proxy-server
        :param proxy_bypass_list: Proxy bypass list, similar to the one passed to --proxy-bypass-list
        :param origins_with_universal_network_access: An optional list of origins to grant unlimited cross-origin access to.
        Parts of the URL other than those constituting origin are ignored.
        """
        _params: Dict[str, Any] = {}
        if dispose_on_detach is not None:
            _params['disposeOnDetach'] = encode(FieldMeta('', '', False, 'primitive'), dispose_on_detach)
        if proxy_server is not None:
            _params['proxyServer'] = encode(FieldMeta('', '', False, 'primitive'), proxy_server)
        if proxy_bypass_list is not None:
            _params['proxyBypassList'] = encode(FieldMeta('', '', False, 'primitive'), proxy_bypass_list)
        if origins_with_universal_network_access is not None:
            _params['originsWithUniversalNetworkAccess'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'primitive')), origins_with_universal_network_access)
        _result = await self._target.send('Target.createBrowserContext', _params)
        return CreateBrowserContextReturn.from_json(_result)

    async def get_browser_contexts(self) -> GetBrowserContextsReturn:
        """Returns all browser contexts created with `Target.createBrowserContext` method."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Target.getBrowserContexts', _params)
        return GetBrowserContextsReturn.from_json(_result)

    async def create_target(self, *, url: str, left: Optional[int] = None, top: Optional[int] = None, width: Optional[int] = None, height: Optional[int] = None, window_state: Optional[WindowState] = None, browser_context_id: Optional[Browser_BrowserContextID] = None, enable_begin_frame_control: Optional[bool] = None, new_window: Optional[bool] = None, background: Optional[bool] = None, for_tab: Optional[bool] = None, hidden: Optional[bool] = None) -> CreateTargetReturn:
        """
        Creates a new page.
        :param url: The initial URL the page will be navigated to. An empty string indicates about:blank.
        :param left: Frame left origin in DIP (requires newWindow to be true or headless shell).
        :param top: Frame top origin in DIP (requires newWindow to be true or headless shell).
        :param width: Frame width in DIP (requires newWindow to be true or headless shell).
        :param height: Frame height in DIP (requires newWindow to be true or headless shell).
        :param window_state: Frame window state (requires newWindow to be true or headless shell).
        Default is normal.
        :param browser_context_id: The browser context to create the page in.
        :param enable_begin_frame_control: Whether BeginFrames for this target will be controlled via DevTools (headless shell only,
        not supported on MacOS yet, false by default).
        :param new_window: Whether to create a new Window or Tab (false by default, not supported by headless shell).
        :param background: Whether to create the target in background or foreground (false by default, not supported
        by headless shell).
        :param for_tab: Whether to create the target of type "tab".
        :param hidden: Whether to create a hidden target. The hidden target is observable via protocol, but not
        present in the tab UI strip. Cannot be created with `forTab: true`, `newWindow: true` or
        `background: false`. The life-time of the tab is limited to the life-time of the session.
        """
        _params: Dict[str, Any] = {}
        _params['url'] = encode(FieldMeta('', '', False, 'primitive'), url)
        if left is not None:
            _params['left'] = encode(FieldMeta('', '', False, 'primitive'), left)
        if top is not None:
            _params['top'] = encode(FieldMeta('', '', False, 'primitive'), top)
        if width is not None:
            _params['width'] = encode(FieldMeta('', '', False, 'primitive'), width)
        if height is not None:
            _params['height'] = encode(FieldMeta('', '', False, 'primitive'), height)
        if window_state is not None:
            _params['windowState'] = encode(FieldMeta('', '', False, 'enum', ref='Target.WindowState'), window_state)
        if browser_context_id is not None:
            _params['browserContextId'] = encode(FieldMeta('', '', False, 'primitive'), browser_context_id)
        if enable_begin_frame_control is not None:
            _params['enableBeginFrameControl'] = encode(FieldMeta('', '', False, 'primitive'), enable_begin_frame_control)
        if new_window is not None:
            _params['newWindow'] = encode(FieldMeta('', '', False, 'primitive'), new_window)
        if background is not None:
            _params['background'] = encode(FieldMeta('', '', False, 'primitive'), background)
        if for_tab is not None:
            _params['forTab'] = encode(FieldMeta('', '', False, 'primitive'), for_tab)
        if hidden is not None:
            _params['hidden'] = encode(FieldMeta('', '', False, 'primitive'), hidden)
        _result = await self._target.send('Target.createTarget', _params)
        return CreateTargetReturn.from_json(_result)

    async def detach_from_target(self, *, session_id: Optional[SessionID] = None, target_id: Optional[TargetID] = None) -> None:
        """
        Detaches session with given id.
        :param session_id: Session to detach.
        :param target_id: Deprecated.
        """
        _params: Dict[str, Any] = {}
        if session_id is not None:
            _params['sessionId'] = encode(FieldMeta('', '', False, 'primitive'), session_id)
        if target_id is not None:
            _params['targetId'] = encode(FieldMeta('', '', False, 'primitive'), target_id)
        _result = await self._target.send('Target.detachFromTarget', _params)
        return None

    async def dispose_browser_context(self, *, browser_context_id: Browser_BrowserContextID) -> None:
        """
        Deletes a BrowserContext. All the belonging pages will be closed without calling their
        beforeunload hooks.
        :param browser_context_id:
        """
        _params: Dict[str, Any] = {}
        _params['browserContextId'] = encode(FieldMeta('', '', False, 'primitive'), browser_context_id)
        _result = await self._target.send('Target.disposeBrowserContext', _params)
        return None

    async def get_target_info(self, *, target_id: Optional[TargetID] = None) -> GetTargetInfoReturn:
        """
        Returns information about a target.
        :param target_id:
        """
        _params: Dict[str, Any] = {}
        if target_id is not None:
            _params['targetId'] = encode(FieldMeta('', '', False, 'primitive'), target_id)
        _result = await self._target.send('Target.getTargetInfo', _params)
        return GetTargetInfoReturn.from_json(_result)

    async def get_targets(self, *, filter: Optional[TargetFilter] = None) -> GetTargetsReturn:
        """
        Retrieves a list of available targets.
        :param filter: Only targets matching filter will be reported. If filter is not specified
        and target discovery is currently enabled, a filter used for target discovery
        is used for consistency.
        """
        _params: Dict[str, Any] = {}
        if filter is not None:
            _params['filter'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Target.FilterEntry')), filter)
        _result = await self._target.send('Target.getTargets', _params)
        return GetTargetsReturn.from_json(_result)

    async def send_message_to_target(self, *, message: str, session_id: Optional[SessionID] = None, target_id: Optional[TargetID] = None) -> None:
        """
        Sends protocol message over session with given id.
        Consider using flat mode instead; see commands attachToTarget, setAutoAttach,
        and crbug.com/991325.
        
        .. deprecated::
        :param message:
        :param session_id: Identifier of the session.
        :param target_id: Deprecated.
        """
        _params: Dict[str, Any] = {}
        _params['message'] = encode(FieldMeta('', '', False, 'primitive'), message)
        if session_id is not None:
            _params['sessionId'] = encode(FieldMeta('', '', False, 'primitive'), session_id)
        if target_id is not None:
            _params['targetId'] = encode(FieldMeta('', '', False, 'primitive'), target_id)
        _result = await self._target.send('Target.sendMessageToTarget', _params)
        return None

    async def set_auto_attach(self, *, auto_attach: bool, wait_for_debugger_on_start: bool, flatten: Optional[bool] = None, filter: Optional[TargetFilter] = None) -> None:
        """
        Controls whether to automatically attach to new targets which are considered
        to be directly related to this one (for example, iframes or workers).
        When turned on, attaches to all existing related targets as well. When turned off,
        automatically detaches from all currently attached targets.
        This also clears all targets added by `autoAttachRelated` from the list of targets to watch
        for creation of related targets.
        You might want to call this recursively for auto-attached targets to attach
        to all available targets.
        :param auto_attach: Whether to auto-attach to related targets.
        :param wait_for_debugger_on_start: Whether to pause new targets when attaching to them. Use `Runtime.runIfWaitingForDebugger`
        to run paused targets.
        :param flatten: Enables "flat" access to the session via specifying sessionId attribute in the commands.
        We plan to make this the default, deprecate non-flattened mode,
        and eventually retire it. See crbug.com/991325.
        :param filter: Only targets matching filter will be attached.
        """
        _params: Dict[str, Any] = {}
        _params['autoAttach'] = encode(FieldMeta('', '', False, 'primitive'), auto_attach)
        _params['waitForDebuggerOnStart'] = encode(FieldMeta('', '', False, 'primitive'), wait_for_debugger_on_start)
        if flatten is not None:
            _params['flatten'] = encode(FieldMeta('', '', False, 'primitive'), flatten)
        if filter is not None:
            _params['filter'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Target.FilterEntry')), filter)
        _result = await self._target.send('Target.setAutoAttach', _params)
        return None

    async def auto_attach_related(self, *, target_id: TargetID, wait_for_debugger_on_start: bool, filter: Optional[TargetFilter] = None) -> None:
        """
        Adds the specified target to the list of targets that will be monitored for any related target
        creation (such as child frames, child workers and new versions of service worker) and reported
        through `attachedToTarget`. The specified target is also auto-attached.
        This cancels the effect of any previous `setAutoAttach` and is also cancelled by subsequent
        `setAutoAttach`. Only available at the Browser target.
        :param target_id:
        :param wait_for_debugger_on_start: Whether to pause new targets when attaching to them. Use `Runtime.runIfWaitingForDebugger`
        to run paused targets.
        :param filter: Only targets matching filter will be attached.
        """
        _params: Dict[str, Any] = {}
        _params['targetId'] = encode(FieldMeta('', '', False, 'primitive'), target_id)
        _params['waitForDebuggerOnStart'] = encode(FieldMeta('', '', False, 'primitive'), wait_for_debugger_on_start)
        if filter is not None:
            _params['filter'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Target.FilterEntry')), filter)
        _result = await self._target.send('Target.autoAttachRelated', _params)
        return None

    async def set_discover_targets(self, *, discover: bool, filter: Optional[TargetFilter] = None) -> None:
        """
        Controls whether to discover available targets and notify via
        `targetCreated/targetInfoChanged/targetDestroyed` events.
        :param discover: Whether to discover available targets.
        :param filter: Only targets matching filter will be attached. If `discover` is false,
        `filter` must be omitted or empty.
        """
        _params: Dict[str, Any] = {}
        _params['discover'] = encode(FieldMeta('', '', False, 'primitive'), discover)
        if filter is not None:
            _params['filter'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Target.FilterEntry')), filter)
        _result = await self._target.send('Target.setDiscoverTargets', _params)
        return None

    async def set_remote_locations(self, *, locations: List[RemoteLocation]) -> None:
        """
        Enables target discovery for the specified locations, when `setDiscoverTargets` was set to
        `true`.
        :param locations: List of remote locations.
        """
        _params: Dict[str, Any] = {}
        _params['locations'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Target.RemoteLocation')), locations)
        _result = await self._target.send('Target.setRemoteLocations', _params)
        return None

    async def get_dev_tools_target(self, *, target_id: TargetID) -> GetDevToolsTargetReturn:
        """
        Gets the targetId of the DevTools page target opened for the given target
        (if any).
        :param target_id: Page or tab target ID.
        """
        _params: Dict[str, Any] = {}
        _params['targetId'] = encode(FieldMeta('', '', False, 'primitive'), target_id)
        _result = await self._target.send('Target.getDevToolsTarget', _params)
        return GetDevToolsTargetReturn.from_json(_result)

    async def open_dev_tools(self, *, target_id: TargetID, panel_id: Optional[str] = None) -> OpenDevToolsReturn:
        """
        Opens a DevTools window for the target.
        :param target_id: This can be the page or tab target ID.
        :param panel_id: The id of the panel we want DevTools to open initially. Currently
        supported panels are elements, console, network, sources, resources
        and performance.
        """
        _params: Dict[str, Any] = {}
        _params['targetId'] = encode(FieldMeta('', '', False, 'primitive'), target_id)
        if panel_id is not None:
            _params['panelId'] = encode(FieldMeta('', '', False, 'primitive'), panel_id)
        _result = await self._target.send('Target.openDevTools', _params)
        return OpenDevToolsReturn.from_json(_result)
