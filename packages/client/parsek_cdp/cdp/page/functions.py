"""Commands for the Page domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode

if TYPE_CHECKING:
    from .types import (
        AdScriptAncestry,
        AppManifestError,
        AppManifestParsedProperties,
        CompilationCacheParams,
        FontFamilies,
        FontSizes,
        FrameId,
        FrameResourceTree,
        FrameTree,
        InstallabilityError,
        LayoutViewport,
        NavigationEntry,
        OriginTrial,
        PermissionsPolicyFeatureState,
        ReferrerPolicy,
        ScriptFontFamilies,
        ScriptIdentifier,
        TransitionType,
        Viewport,
        VisualViewport,
        WebAppManifest,
    )
    from ..dom.types import Rect as DOM_Rect
    from ..debugger.types import SearchMatch as Debugger_SearchMatch
    from ..emulation.types import ScreenOrientation as Emulation_ScreenOrientation
    from ..io.types import StreamHandle as IO_StreamHandle
    from ..network.types import LoaderId as Network_LoaderId
    from ..runtime.types import ExecutionContextId as Runtime_ExecutionContextId

@dataclass
class AddScriptToEvaluateOnLoadReturn(DataType):
    """Return value of :meth:`Page.add_script_to_evaluate_on_load`."""
    identifier: ScriptIdentifier
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('identifier', 'identifier', False, 'primitive'),
    )


@dataclass
class AddScriptToEvaluateOnNewDocumentReturn(DataType):
    """Return value of :meth:`Page.add_script_to_evaluate_on_new_document`."""
    identifier: ScriptIdentifier
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('identifier', 'identifier', False, 'primitive'),
    )


@dataclass
class CaptureScreenshotReturn(DataType):
    """Return value of :meth:`Page.capture_screenshot`."""
    data: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('data', 'data', False, 'primitive'),
    )


@dataclass
class CaptureSnapshotReturn(DataType):
    """Return value of :meth:`Page.capture_snapshot`."""
    data: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('data', 'data', False, 'primitive'),
    )


@dataclass
class CreateIsolatedWorldReturn(DataType):
    """Return value of :meth:`Page.create_isolated_world`."""
    execution_context_id: Runtime_ExecutionContextId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('execution_context_id', 'executionContextId', False, 'primitive'),
    )


@dataclass
class GetAppManifestReturn(DataType):
    """Return value of :meth:`Page.get_app_manifest`."""
    url: str
    errors: List[AppManifestError]
    manifest: WebAppManifest
    data: Optional[str] = None
    parsed: Optional[AppManifestParsedProperties] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('url', 'url', False, 'primitive'),
        FieldMeta('errors', 'errors', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Page.AppManifestError')),
        FieldMeta('manifest', 'manifest', False, 'object', ref='Page.WebAppManifest'),
        FieldMeta('data', 'data', True, 'primitive'),
        FieldMeta('parsed', 'parsed', True, 'object', ref='Page.AppManifestParsedProperties'),
    )


@dataclass
class GetInstallabilityErrorsReturn(DataType):
    """Return value of :meth:`Page.get_installability_errors`."""
    installability_errors: List[InstallabilityError]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('installability_errors', 'installabilityErrors', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Page.InstallabilityError')),
    )


@dataclass
class GetManifestIconsReturn(DataType):
    """Return value of :meth:`Page.get_manifest_icons`."""
    primary_icon: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('primary_icon', 'primaryIcon', True, 'primitive'),
    )


@dataclass
class GetAppIdReturn(DataType):
    """Return value of :meth:`Page.get_app_id`."""
    app_id: Optional[str] = None
    recommended_id: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('app_id', 'appId', True, 'primitive'),
        FieldMeta('recommended_id', 'recommendedId', True, 'primitive'),
    )


@dataclass
class GetAdScriptAncestryReturn(DataType):
    """Return value of :meth:`Page.get_ad_script_ancestry`."""
    ad_script_ancestry: Optional[AdScriptAncestry] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('ad_script_ancestry', 'adScriptAncestry', True, 'object', ref='Page.AdScriptAncestry'),
    )


@dataclass
class GetFrameTreeReturn(DataType):
    """Return value of :meth:`Page.get_frame_tree`."""
    frame_tree: FrameTree
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('frame_tree', 'frameTree', False, 'object', ref='Page.FrameTree'),
    )


@dataclass
class GetLayoutMetricsReturn(DataType):
    """Return value of :meth:`Page.get_layout_metrics`."""
    layout_viewport: LayoutViewport
    visual_viewport: VisualViewport
    content_size: DOM_Rect
    css_layout_viewport: LayoutViewport
    css_visual_viewport: VisualViewport
    css_content_size: DOM_Rect
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('layout_viewport', 'layoutViewport', False, 'object', ref='Page.LayoutViewport'),
        FieldMeta('visual_viewport', 'visualViewport', False, 'object', ref='Page.VisualViewport'),
        FieldMeta('content_size', 'contentSize', False, 'object', ref='DOM.Rect'),
        FieldMeta('css_layout_viewport', 'cssLayoutViewport', False, 'object', ref='Page.LayoutViewport'),
        FieldMeta('css_visual_viewport', 'cssVisualViewport', False, 'object', ref='Page.VisualViewport'),
        FieldMeta('css_content_size', 'cssContentSize', False, 'object', ref='DOM.Rect'),
    )


@dataclass
class GetNavigationHistoryReturn(DataType):
    """Return value of :meth:`Page.get_navigation_history`."""
    current_index: int
    entries: List[NavigationEntry]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('current_index', 'currentIndex', False, 'primitive'),
        FieldMeta('entries', 'entries', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Page.NavigationEntry')),
    )


@dataclass
class GetResourceContentReturn(DataType):
    """Return value of :meth:`Page.get_resource_content`."""
    content: str
    base64_encoded: bool
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('content', 'content', False, 'primitive'),
        FieldMeta('base64_encoded', 'base64Encoded', False, 'primitive'),
    )


@dataclass
class GetResourceTreeReturn(DataType):
    """Return value of :meth:`Page.get_resource_tree`."""
    frame_tree: FrameResourceTree
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('frame_tree', 'frameTree', False, 'object', ref='Page.FrameResourceTree'),
    )


@dataclass
class NavigateReturn(DataType):
    """Return value of :meth:`Page.navigate`."""
    frame_id: FrameId
    loader_id: Optional[Network_LoaderId] = None
    error_text: Optional[str] = None
    is_download: Optional[bool] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('frame_id', 'frameId', False, 'primitive'),
        FieldMeta('loader_id', 'loaderId', True, 'primitive'),
        FieldMeta('error_text', 'errorText', True, 'primitive'),
        FieldMeta('is_download', 'isDownload', True, 'primitive'),
    )


@dataclass
class PrintToPDFReturn(DataType):
    """Return value of :meth:`Page.print_to_pdf`."""
    data: str
    stream: Optional[IO_StreamHandle] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('data', 'data', False, 'primitive'),
        FieldMeta('stream', 'stream', True, 'primitive'),
    )


@dataclass
class SearchInResourceReturn(DataType):
    """Return value of :meth:`Page.search_in_resource`."""
    result: List[Debugger_SearchMatch]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('result', 'result', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Debugger.SearchMatch')),
    )


@dataclass
class GetPermissionsPolicyStateReturn(DataType):
    """Return value of :meth:`Page.get_permissions_policy_state`."""
    states: List[PermissionsPolicyFeatureState]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('states', 'states', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Page.PermissionsPolicyFeatureState')),
    )


@dataclass
class GetOriginTrialsReturn(DataType):
    """Return value of :meth:`Page.get_origin_trials`."""
    origin_trials: List[OriginTrial]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('origin_trials', 'originTrials', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Page.OriginTrial')),
    )


@dataclass
class GetAnnotatedPageContentReturn(DataType):
    """Return value of :meth:`Page.get_annotated_page_content`."""
    content: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('content', 'content', False, 'primitive'),
    )


class Page:
    """Commands of the Page domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def add_script_to_evaluate_on_load(self, *, script_source: str) -> AddScriptToEvaluateOnLoadReturn:
        """
        Deprecated, please use addScriptToEvaluateOnNewDocument instead.
        
        .. deprecated::
        :param script_source:
        """
        _params: Dict[str, Any] = {}
        _params['scriptSource'] = encode(FieldMeta('', '', False, 'primitive'), script_source)
        _result = await self._target.send('Page.addScriptToEvaluateOnLoad', _params)
        return AddScriptToEvaluateOnLoadReturn.from_json(_result)

    async def add_script_to_evaluate_on_new_document(self, *, source: str, world_name: Optional[str] = None, include_command_line_api: Optional[bool] = None, run_immediately: Optional[bool] = None) -> AddScriptToEvaluateOnNewDocumentReturn:
        """
        Evaluates given script in every frame upon creation (before loading frame's scripts).
        :param source:
        :param world_name: If specified, creates an isolated world with the given name and evaluates given script in it.
        This world name will be used as the ExecutionContextDescription::name when the corresponding
        event is emitted.
        :param include_command_line_api: Specifies whether command line API should be available to the script, defaults
        to false.
        :param run_immediately: If true, runs the script immediately on existing execution contexts or worlds.
        Default: false.
        """
        _params: Dict[str, Any] = {}
        _params['source'] = encode(FieldMeta('', '', False, 'primitive'), source)
        if world_name is not None:
            _params['worldName'] = encode(FieldMeta('', '', False, 'primitive'), world_name)
        if include_command_line_api is not None:
            _params['includeCommandLineAPI'] = encode(FieldMeta('', '', False, 'primitive'), include_command_line_api)
        if run_immediately is not None:
            _params['runImmediately'] = encode(FieldMeta('', '', False, 'primitive'), run_immediately)
        _result = await self._target.send('Page.addScriptToEvaluateOnNewDocument', _params)
        return AddScriptToEvaluateOnNewDocumentReturn.from_json(_result)

    async def bring_to_front(self) -> None:
        """Brings page to front (activates tab)."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Page.bringToFront', _params)
        return None

    async def capture_screenshot(self, *, format: Optional[Literal['jpeg', 'png', 'webp']] = None, quality: Optional[int] = None, clip: Optional[Viewport] = None, from_surface: Optional[bool] = None, capture_beyond_viewport: Optional[bool] = None, optimize_for_speed: Optional[bool] = None) -> CaptureScreenshotReturn:
        """
        Capture page screenshot.
        :param format: Image compression format (defaults to png).
        :param quality: Compression quality from range [0..100] (jpeg only).
        :param clip: Capture the screenshot of a given region only.
        :param from_surface: Capture the screenshot from the surface, rather than the view. Defaults to true.
        :param capture_beyond_viewport: Capture the screenshot beyond the viewport. Defaults to false.
        :param optimize_for_speed: Optimize image encoding for speed, not for resulting size (defaults to false)
        """
        _params: Dict[str, Any] = {}
        if format is not None:
            _params['format'] = encode(FieldMeta('', '', False, 'primitive'), format)
        if quality is not None:
            _params['quality'] = encode(FieldMeta('', '', False, 'primitive'), quality)
        if clip is not None:
            _params['clip'] = encode(FieldMeta('', '', False, 'object', ref='Page.Viewport'), clip)
        if from_surface is not None:
            _params['fromSurface'] = encode(FieldMeta('', '', False, 'primitive'), from_surface)
        if capture_beyond_viewport is not None:
            _params['captureBeyondViewport'] = encode(FieldMeta('', '', False, 'primitive'), capture_beyond_viewport)
        if optimize_for_speed is not None:
            _params['optimizeForSpeed'] = encode(FieldMeta('', '', False, 'primitive'), optimize_for_speed)
        _result = await self._target.send('Page.captureScreenshot', _params)
        return CaptureScreenshotReturn.from_json(_result)

    async def capture_snapshot(self, *, format: Optional[Literal['mhtml']] = None) -> CaptureSnapshotReturn:
        """
        Returns a snapshot of the page as a string. For MHTML format, the serialization includes
        iframes, shadow DOM, external resources, and element-inline styles.
        :param format: Format (defaults to mhtml).
        """
        _params: Dict[str, Any] = {}
        if format is not None:
            _params['format'] = encode(FieldMeta('', '', False, 'primitive'), format)
        _result = await self._target.send('Page.captureSnapshot', _params)
        return CaptureSnapshotReturn.from_json(_result)

    async def clear_device_metrics_override(self) -> None:
        """
        Clears the overridden device metrics.
        
        .. deprecated::
        """
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Page.clearDeviceMetricsOverride', _params)
        return None

    async def clear_device_orientation_override(self) -> None:
        """
        Clears the overridden Device Orientation.
        
        .. deprecated::
        """
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Page.clearDeviceOrientationOverride', _params)
        return None

    async def clear_geolocation_override(self) -> None:
        """
        Clears the overridden Geolocation Position and Error.
        
        .. deprecated::
        """
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Page.clearGeolocationOverride', _params)
        return None

    async def create_isolated_world(self, *, frame_id: FrameId, world_name: Optional[str] = None, grant_univeral_access: Optional[bool] = None) -> CreateIsolatedWorldReturn:
        """
        Creates an isolated world for the given frame.
        :param frame_id: Id of the frame in which the isolated world should be created.
        :param world_name: An optional name which is reported in the Execution Context.
        :param grant_univeral_access: Whether or not universal access should be granted to the isolated world. This is a powerful
        option, use with caution.
        """
        _params: Dict[str, Any] = {}
        _params['frameId'] = encode(FieldMeta('', '', False, 'primitive'), frame_id)
        if world_name is not None:
            _params['worldName'] = encode(FieldMeta('', '', False, 'primitive'), world_name)
        if grant_univeral_access is not None:
            _params['grantUniveralAccess'] = encode(FieldMeta('', '', False, 'primitive'), grant_univeral_access)
        _result = await self._target.send('Page.createIsolatedWorld', _params)
        return CreateIsolatedWorldReturn.from_json(_result)

    async def delete_cookie(self, *, cookie_name: str, url: str) -> None:
        """
        Deletes browser cookie with given name, domain and path.
        
        .. deprecated::
        :param cookie_name: Name of the cookie to remove.
        :param url: URL to match cooke domain and path.
        """
        _params: Dict[str, Any] = {}
        _params['cookieName'] = encode(FieldMeta('', '', False, 'primitive'), cookie_name)
        _params['url'] = encode(FieldMeta('', '', False, 'primitive'), url)
        _result = await self._target.send('Page.deleteCookie', _params)
        return None

    async def disable(self) -> None:
        """Disables page domain notifications."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Page.disable', _params)
        return None

    async def enable(self, *, enable_file_chooser_opened_event: Optional[bool] = None) -> None:
        """
        Enables page domain notifications.
        :param enable_file_chooser_opened_event: If true, the `Page.fileChooserOpened` event will be emitted regardless of the state set by
        `Page.setInterceptFileChooserDialog` command (default: false).
        """
        _params: Dict[str, Any] = {}
        if enable_file_chooser_opened_event is not None:
            _params['enableFileChooserOpenedEvent'] = encode(FieldMeta('', '', False, 'primitive'), enable_file_chooser_opened_event)
        _result = await self._target.send('Page.enable', _params)
        return None

    async def get_app_manifest(self, *, manifest_id: Optional[str] = None) -> GetAppManifestReturn:
        """
        Gets the processed manifest for this current document.
          This API always waits for the manifest to be loaded.
          If manifestId is provided, and it does not match the manifest of the
            current document, this API errors out.
          If there is not a loaded page, this API errors out immediately.
        :param manifest_id:
        """
        _params: Dict[str, Any] = {}
        if manifest_id is not None:
            _params['manifestId'] = encode(FieldMeta('', '', False, 'primitive'), manifest_id)
        _result = await self._target.send('Page.getAppManifest', _params)
        return GetAppManifestReturn.from_json(_result)

    async def get_installability_errors(self) -> GetInstallabilityErrorsReturn:
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Page.getInstallabilityErrors', _params)
        return GetInstallabilityErrorsReturn.from_json(_result)

    async def get_manifest_icons(self) -> GetManifestIconsReturn:
        """
        Deprecated because it's not guaranteed that the returned icon is in fact the one used for PWA installation.
        
        .. deprecated::
        """
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Page.getManifestIcons', _params)
        return GetManifestIconsReturn.from_json(_result)

    async def get_app_id(self) -> GetAppIdReturn:
        """
        Returns the unique (PWA) app id.
        Only returns values if the feature flag 'WebAppEnableManifestId' is enabled
        """
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Page.getAppId', _params)
        return GetAppIdReturn.from_json(_result)

    async def get_ad_script_ancestry(self, *, frame_id: FrameId) -> GetAdScriptAncestryReturn:
        """:param frame_id:"""
        _params: Dict[str, Any] = {}
        _params['frameId'] = encode(FieldMeta('', '', False, 'primitive'), frame_id)
        _result = await self._target.send('Page.getAdScriptAncestry', _params)
        return GetAdScriptAncestryReturn.from_json(_result)

    async def get_frame_tree(self) -> GetFrameTreeReturn:
        """Returns present frame tree structure."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Page.getFrameTree', _params)
        return GetFrameTreeReturn.from_json(_result)

    async def get_layout_metrics(self) -> GetLayoutMetricsReturn:
        """Returns metrics relating to the layouting of the page, such as viewport bounds/scale."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Page.getLayoutMetrics', _params)
        return GetLayoutMetricsReturn.from_json(_result)

    async def get_navigation_history(self) -> GetNavigationHistoryReturn:
        """Returns navigation history for the current page."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Page.getNavigationHistory', _params)
        return GetNavigationHistoryReturn.from_json(_result)

    async def reset_navigation_history(self) -> None:
        """Resets navigation history for the current page."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Page.resetNavigationHistory', _params)
        return None

    async def get_resource_content(self, *, frame_id: FrameId, url: str) -> GetResourceContentReturn:
        """
        Returns content of the given resource.
        :param frame_id: Frame id to get resource for.
        :param url: URL of the resource to get content for.
        """
        _params: Dict[str, Any] = {}
        _params['frameId'] = encode(FieldMeta('', '', False, 'primitive'), frame_id)
        _params['url'] = encode(FieldMeta('', '', False, 'primitive'), url)
        _result = await self._target.send('Page.getResourceContent', _params)
        return GetResourceContentReturn.from_json(_result)

    async def get_resource_tree(self) -> GetResourceTreeReturn:
        """Returns present frame / resource tree structure."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Page.getResourceTree', _params)
        return GetResourceTreeReturn.from_json(_result)

    async def handle_java_script_dialog(self, *, accept: bool, prompt_text: Optional[str] = None) -> None:
        """
        Accepts or dismisses a JavaScript initiated dialog (alert, confirm, prompt, or onbeforeunload).
        :param accept: Whether to accept or dismiss the dialog.
        :param prompt_text: The text to enter into the dialog prompt before accepting. Used only if this is a prompt
        dialog.
        """
        _params: Dict[str, Any] = {}
        _params['accept'] = encode(FieldMeta('', '', False, 'primitive'), accept)
        if prompt_text is not None:
            _params['promptText'] = encode(FieldMeta('', '', False, 'primitive'), prompt_text)
        _result = await self._target.send('Page.handleJavaScriptDialog', _params)
        return None

    async def navigate(self, *, url: str, referrer: Optional[str] = None, transition_type: Optional[TransitionType] = None, frame_id: Optional[FrameId] = None, referrer_policy: Optional[ReferrerPolicy] = None) -> NavigateReturn:
        """
        Navigates current page to the given URL.
        :param url: URL to navigate the page to.
        :param referrer: Referrer URL.
        :param transition_type: Intended transition type.
        :param frame_id: Frame id to navigate, if not specified navigates the top frame.
        :param referrer_policy: Referrer-policy used for the navigation.
        """
        _params: Dict[str, Any] = {}
        _params['url'] = encode(FieldMeta('', '', False, 'primitive'), url)
        if referrer is not None:
            _params['referrer'] = encode(FieldMeta('', '', False, 'primitive'), referrer)
        if transition_type is not None:
            _params['transitionType'] = encode(FieldMeta('', '', False, 'enum', ref='Page.TransitionType'), transition_type)
        if frame_id is not None:
            _params['frameId'] = encode(FieldMeta('', '', False, 'primitive'), frame_id)
        if referrer_policy is not None:
            _params['referrerPolicy'] = encode(FieldMeta('', '', False, 'enum', ref='Page.ReferrerPolicy'), referrer_policy)
        _result = await self._target.send('Page.navigate', _params)
        return NavigateReturn.from_json(_result)

    async def navigate_to_history_entry(self, *, entry_id: int) -> None:
        """
        Navigates current page to the given history entry.
        :param entry_id: Unique id of the entry to navigate to.
        """
        _params: Dict[str, Any] = {}
        _params['entryId'] = encode(FieldMeta('', '', False, 'primitive'), entry_id)
        _result = await self._target.send('Page.navigateToHistoryEntry', _params)
        return None

    async def print_to_pdf(self, *, landscape: Optional[bool] = None, display_header_footer: Optional[bool] = None, print_background: Optional[bool] = None, scale: Optional[float] = None, paper_width: Optional[float] = None, paper_height: Optional[float] = None, margin_top: Optional[float] = None, margin_bottom: Optional[float] = None, margin_left: Optional[float] = None, margin_right: Optional[float] = None, page_ranges: Optional[str] = None, header_template: Optional[str] = None, footer_template: Optional[str] = None, prefer_css_page_size: Optional[bool] = None, transfer_mode: Optional[Literal['ReturnAsBase64', 'ReturnAsStream']] = None, generate_tagged_pdf: Optional[bool] = None, generate_document_outline: Optional[bool] = None) -> PrintToPDFReturn:
        """
        Print page as PDF.
        :param landscape: Paper orientation. Defaults to false.
        :param display_header_footer: Display header and footer. Defaults to false.
        :param print_background: Print background graphics. Defaults to false.
        :param scale: Scale of the webpage rendering. Defaults to 1.
        :param paper_width: Paper width in inches. Defaults to 8.5 inches.
        :param paper_height: Paper height in inches. Defaults to 11 inches.
        :param margin_top: Top margin in inches. Defaults to 1cm (~0.4 inches).
        :param margin_bottom: Bottom margin in inches. Defaults to 1cm (~0.4 inches).
        :param margin_left: Left margin in inches. Defaults to 1cm (~0.4 inches).
        :param margin_right: Right margin in inches. Defaults to 1cm (~0.4 inches).
        :param page_ranges: Paper ranges to print, one based, e.g., '1-5, 8, 11-13'. Pages are
        printed in the document order, not in the order specified, and no
        more than once.
        Defaults to empty string, which implies the entire document is printed.
        The page numbers are quietly capped to actual page count of the
        document, and ranges beyond the end of the document are ignored.
        If this results in no pages to print, an error is reported.
        It is an error to specify a range with start greater than end.
        :param header_template: HTML template for the print header. Should be valid HTML markup with following
        classes used to inject printing values into them:
        - `date`: formatted print date
        - `title`: document title
        - `url`: document location
        - `pageNumber`: current page number
        - `totalPages`: total pages in the document
        
        For example, `<span class=title></span>` would generate span containing the title.
        :param footer_template: HTML template for the print footer. Should use the same format as the `headerTemplate`.
        :param prefer_css_page_size: Whether or not to prefer page size as defined by css. Defaults to false,
        in which case the content will be scaled to fit the paper size.
        :param transfer_mode: return as stream
        :param generate_tagged_pdf: Whether or not to generate tagged (accessible) PDF. Defaults to embedder choice.
        :param generate_document_outline: Whether or not to embed the document outline into the PDF.
        """
        _params: Dict[str, Any] = {}
        if landscape is not None:
            _params['landscape'] = encode(FieldMeta('', '', False, 'primitive'), landscape)
        if display_header_footer is not None:
            _params['displayHeaderFooter'] = encode(FieldMeta('', '', False, 'primitive'), display_header_footer)
        if print_background is not None:
            _params['printBackground'] = encode(FieldMeta('', '', False, 'primitive'), print_background)
        if scale is not None:
            _params['scale'] = encode(FieldMeta('', '', False, 'primitive'), scale)
        if paper_width is not None:
            _params['paperWidth'] = encode(FieldMeta('', '', False, 'primitive'), paper_width)
        if paper_height is not None:
            _params['paperHeight'] = encode(FieldMeta('', '', False, 'primitive'), paper_height)
        if margin_top is not None:
            _params['marginTop'] = encode(FieldMeta('', '', False, 'primitive'), margin_top)
        if margin_bottom is not None:
            _params['marginBottom'] = encode(FieldMeta('', '', False, 'primitive'), margin_bottom)
        if margin_left is not None:
            _params['marginLeft'] = encode(FieldMeta('', '', False, 'primitive'), margin_left)
        if margin_right is not None:
            _params['marginRight'] = encode(FieldMeta('', '', False, 'primitive'), margin_right)
        if page_ranges is not None:
            _params['pageRanges'] = encode(FieldMeta('', '', False, 'primitive'), page_ranges)
        if header_template is not None:
            _params['headerTemplate'] = encode(FieldMeta('', '', False, 'primitive'), header_template)
        if footer_template is not None:
            _params['footerTemplate'] = encode(FieldMeta('', '', False, 'primitive'), footer_template)
        if prefer_css_page_size is not None:
            _params['preferCSSPageSize'] = encode(FieldMeta('', '', False, 'primitive'), prefer_css_page_size)
        if transfer_mode is not None:
            _params['transferMode'] = encode(FieldMeta('', '', False, 'primitive'), transfer_mode)
        if generate_tagged_pdf is not None:
            _params['generateTaggedPDF'] = encode(FieldMeta('', '', False, 'primitive'), generate_tagged_pdf)
        if generate_document_outline is not None:
            _params['generateDocumentOutline'] = encode(FieldMeta('', '', False, 'primitive'), generate_document_outline)
        _result = await self._target.send('Page.printToPDF', _params)
        return PrintToPDFReturn.from_json(_result)

    async def reload(self, *, ignore_cache: Optional[bool] = None, script_to_evaluate_on_load: Optional[str] = None, loader_id: Optional[Network_LoaderId] = None) -> None:
        """
        Reloads given page optionally ignoring the cache.
        :param ignore_cache: If true, browser cache is ignored (as if the user pressed Shift+refresh).
        :param script_to_evaluate_on_load: If set, the script will be injected into all frames of the inspected page after reload.
        Argument will be ignored if reloading dataURL origin.
        :param loader_id: If set, an error will be thrown if the target page's main frame's
        loader id does not match the provided id. This prevents accidentally
        reloading an unintended target in case there's a racing navigation.
        """
        _params: Dict[str, Any] = {}
        if ignore_cache is not None:
            _params['ignoreCache'] = encode(FieldMeta('', '', False, 'primitive'), ignore_cache)
        if script_to_evaluate_on_load is not None:
            _params['scriptToEvaluateOnLoad'] = encode(FieldMeta('', '', False, 'primitive'), script_to_evaluate_on_load)
        if loader_id is not None:
            _params['loaderId'] = encode(FieldMeta('', '', False, 'primitive'), loader_id)
        _result = await self._target.send('Page.reload', _params)
        return None

    async def remove_script_to_evaluate_on_load(self, *, identifier: ScriptIdentifier) -> None:
        """
        Deprecated, please use removeScriptToEvaluateOnNewDocument instead.
        
        .. deprecated::
        :param identifier:
        """
        _params: Dict[str, Any] = {}
        _params['identifier'] = encode(FieldMeta('', '', False, 'primitive'), identifier)
        _result = await self._target.send('Page.removeScriptToEvaluateOnLoad', _params)
        return None

    async def remove_script_to_evaluate_on_new_document(self, *, identifier: ScriptIdentifier) -> None:
        """
        Removes given script from the list.
        :param identifier:
        """
        _params: Dict[str, Any] = {}
        _params['identifier'] = encode(FieldMeta('', '', False, 'primitive'), identifier)
        _result = await self._target.send('Page.removeScriptToEvaluateOnNewDocument', _params)
        return None

    async def screencast_frame_ack(self, *, session_id: int) -> None:
        """
        Acknowledges that a screencast frame has been received by the frontend.
        :param session_id: Frame number.
        """
        _params: Dict[str, Any] = {}
        _params['sessionId'] = encode(FieldMeta('', '', False, 'primitive'), session_id)
        _result = await self._target.send('Page.screencastFrameAck', _params)
        return None

    async def search_in_resource(self, *, frame_id: FrameId, url: str, query: str, case_sensitive: Optional[bool] = None, is_regex: Optional[bool] = None) -> SearchInResourceReturn:
        """
        Searches for given string in resource content.
        :param frame_id: Frame id for resource to search in.
        :param url: URL of the resource to search in.
        :param query: String to search for.
        :param case_sensitive: If true, search is case sensitive.
        :param is_regex: If true, treats string parameter as regex.
        """
        _params: Dict[str, Any] = {}
        _params['frameId'] = encode(FieldMeta('', '', False, 'primitive'), frame_id)
        _params['url'] = encode(FieldMeta('', '', False, 'primitive'), url)
        _params['query'] = encode(FieldMeta('', '', False, 'primitive'), query)
        if case_sensitive is not None:
            _params['caseSensitive'] = encode(FieldMeta('', '', False, 'primitive'), case_sensitive)
        if is_regex is not None:
            _params['isRegex'] = encode(FieldMeta('', '', False, 'primitive'), is_regex)
        _result = await self._target.send('Page.searchInResource', _params)
        return SearchInResourceReturn.from_json(_result)

    async def set_ad_blocking_enabled(self, *, enabled: bool) -> None:
        """
        Enable Chrome's experimental ad filter on all sites.
        :param enabled: Whether to block ads.
        """
        _params: Dict[str, Any] = {}
        _params['enabled'] = encode(FieldMeta('', '', False, 'primitive'), enabled)
        _result = await self._target.send('Page.setAdBlockingEnabled', _params)
        return None

    async def set_bypass_csp(self, *, enabled: bool) -> None:
        """
        Enable page Content Security Policy by-passing.
        :param enabled: Whether to bypass page CSP.
        """
        _params: Dict[str, Any] = {}
        _params['enabled'] = encode(FieldMeta('', '', False, 'primitive'), enabled)
        _result = await self._target.send('Page.setBypassCSP', _params)
        return None

    async def get_permissions_policy_state(self, *, frame_id: FrameId) -> GetPermissionsPolicyStateReturn:
        """
        Get Permissions Policy state on given frame.
        :param frame_id:
        """
        _params: Dict[str, Any] = {}
        _params['frameId'] = encode(FieldMeta('', '', False, 'primitive'), frame_id)
        _result = await self._target.send('Page.getPermissionsPolicyState', _params)
        return GetPermissionsPolicyStateReturn.from_json(_result)

    async def get_origin_trials(self, *, frame_id: FrameId) -> GetOriginTrialsReturn:
        """
        Get Origin Trials on given frame.
        :param frame_id:
        """
        _params: Dict[str, Any] = {}
        _params['frameId'] = encode(FieldMeta('', '', False, 'primitive'), frame_id)
        _result = await self._target.send('Page.getOriginTrials', _params)
        return GetOriginTrialsReturn.from_json(_result)

    async def set_device_metrics_override(self, *, width: int, height: int, device_scale_factor: float, mobile: bool, scale: Optional[float] = None, screen_width: Optional[int] = None, screen_height: Optional[int] = None, position_x: Optional[int] = None, position_y: Optional[int] = None, dont_set_visible_size: Optional[bool] = None, screen_orientation: Optional[Emulation_ScreenOrientation] = None, viewport: Optional[Viewport] = None) -> None:
        """
        Overrides the values of device screen dimensions (window.screen.width, window.screen.height,
        window.innerWidth, window.innerHeight, and "device-width"/"device-height"-related CSS media
        query results).
        
        .. deprecated::
        :param width: Overriding width value in pixels (minimum 0, maximum 10000000). 0 disables the override.
        :param height: Overriding height value in pixels (minimum 0, maximum 10000000). 0 disables the override.
        :param device_scale_factor: Overriding device scale factor value. 0 disables the override.
        :param mobile: Whether to emulate mobile device. This includes viewport meta tag, overlay scrollbars, text
        autosizing and more.
        :param scale: Scale to apply to resulting view image.
        :param screen_width: Overriding screen width value in pixels (minimum 0, maximum 10000000).
        :param screen_height: Overriding screen height value in pixels (minimum 0, maximum 10000000).
        :param position_x: Overriding view X position on screen in pixels (minimum 0, maximum 10000000).
        :param position_y: Overriding view Y position on screen in pixels (minimum 0, maximum 10000000).
        :param dont_set_visible_size: Do not set visible view size, rely upon explicit setVisibleSize call.
        :param screen_orientation: Screen orientation override.
        :param viewport: The viewport dimensions and scale. If not set, the override is cleared.
        """
        _params: Dict[str, Any] = {}
        _params['width'] = encode(FieldMeta('', '', False, 'primitive'), width)
        _params['height'] = encode(FieldMeta('', '', False, 'primitive'), height)
        _params['deviceScaleFactor'] = encode(FieldMeta('', '', False, 'primitive'), device_scale_factor)
        _params['mobile'] = encode(FieldMeta('', '', False, 'primitive'), mobile)
        if scale is not None:
            _params['scale'] = encode(FieldMeta('', '', False, 'primitive'), scale)
        if screen_width is not None:
            _params['screenWidth'] = encode(FieldMeta('', '', False, 'primitive'), screen_width)
        if screen_height is not None:
            _params['screenHeight'] = encode(FieldMeta('', '', False, 'primitive'), screen_height)
        if position_x is not None:
            _params['positionX'] = encode(FieldMeta('', '', False, 'primitive'), position_x)
        if position_y is not None:
            _params['positionY'] = encode(FieldMeta('', '', False, 'primitive'), position_y)
        if dont_set_visible_size is not None:
            _params['dontSetVisibleSize'] = encode(FieldMeta('', '', False, 'primitive'), dont_set_visible_size)
        if screen_orientation is not None:
            _params['screenOrientation'] = encode(FieldMeta('', '', False, 'object', ref='Emulation.ScreenOrientation'), screen_orientation)
        if viewport is not None:
            _params['viewport'] = encode(FieldMeta('', '', False, 'object', ref='Page.Viewport'), viewport)
        _result = await self._target.send('Page.setDeviceMetricsOverride', _params)
        return None

    async def set_device_orientation_override(self, *, alpha: float, beta: float, gamma: float) -> None:
        """
        Overrides the Device Orientation.
        
        .. deprecated::
        :param alpha: Mock alpha
        :param beta: Mock beta
        :param gamma: Mock gamma
        """
        _params: Dict[str, Any] = {}
        _params['alpha'] = encode(FieldMeta('', '', False, 'primitive'), alpha)
        _params['beta'] = encode(FieldMeta('', '', False, 'primitive'), beta)
        _params['gamma'] = encode(FieldMeta('', '', False, 'primitive'), gamma)
        _result = await self._target.send('Page.setDeviceOrientationOverride', _params)
        return None

    async def set_font_families(self, *, font_families: FontFamilies, for_scripts: Optional[List[ScriptFontFamilies]] = None) -> None:
        """
        Set generic font families.
        :param font_families: Specifies font families to set. If a font family is not specified, it won't be changed.
        :param for_scripts: Specifies font families to set for individual scripts.
        """
        _params: Dict[str, Any] = {}
        _params['fontFamilies'] = encode(FieldMeta('', '', False, 'object', ref='Page.FontFamilies'), font_families)
        if for_scripts is not None:
            _params['forScripts'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Page.ScriptFontFamilies')), for_scripts)
        _result = await self._target.send('Page.setFontFamilies', _params)
        return None

    async def set_font_sizes(self, *, font_sizes: FontSizes) -> None:
        """
        Set default font sizes.
        :param font_sizes: Specifies font sizes to set. If a font size is not specified, it won't be changed.
        """
        _params: Dict[str, Any] = {}
        _params['fontSizes'] = encode(FieldMeta('', '', False, 'object', ref='Page.FontSizes'), font_sizes)
        _result = await self._target.send('Page.setFontSizes', _params)
        return None

    async def set_document_content(self, *, frame_id: FrameId, html: str) -> None:
        """
        Sets given markup as the document's HTML.
        :param frame_id: Frame id to set HTML for.
        :param html: HTML content to set.
        """
        _params: Dict[str, Any] = {}
        _params['frameId'] = encode(FieldMeta('', '', False, 'primitive'), frame_id)
        _params['html'] = encode(FieldMeta('', '', False, 'primitive'), html)
        _result = await self._target.send('Page.setDocumentContent', _params)
        return None

    async def set_download_behavior(self, *, behavior: Literal['deny', 'allow', 'default'], download_path: Optional[str] = None) -> None:
        """
        Set the behavior when downloading a file.
        
        .. deprecated::
        :param behavior: Whether to allow all or deny all download requests, or use default Chrome behavior if
        available (otherwise deny).
        :param download_path: The default path to save downloaded files to. This is required if behavior is set to 'allow'
        """
        _params: Dict[str, Any] = {}
        _params['behavior'] = encode(FieldMeta('', '', False, 'primitive'), behavior)
        if download_path is not None:
            _params['downloadPath'] = encode(FieldMeta('', '', False, 'primitive'), download_path)
        _result = await self._target.send('Page.setDownloadBehavior', _params)
        return None

    async def set_geolocation_override(self, *, latitude: Optional[float] = None, longitude: Optional[float] = None, accuracy: Optional[float] = None) -> None:
        """
        Overrides the Geolocation Position or Error. Omitting any of the parameters emulates position
        unavailable.
        
        .. deprecated::
        :param latitude: Mock latitude
        :param longitude: Mock longitude
        :param accuracy: Mock accuracy
        """
        _params: Dict[str, Any] = {}
        if latitude is not None:
            _params['latitude'] = encode(FieldMeta('', '', False, 'primitive'), latitude)
        if longitude is not None:
            _params['longitude'] = encode(FieldMeta('', '', False, 'primitive'), longitude)
        if accuracy is not None:
            _params['accuracy'] = encode(FieldMeta('', '', False, 'primitive'), accuracy)
        _result = await self._target.send('Page.setGeolocationOverride', _params)
        return None

    async def set_lifecycle_events_enabled(self, *, enabled: bool) -> None:
        """
        Controls whether page will emit lifecycle events.
        :param enabled: If true, starts emitting lifecycle events.
        """
        _params: Dict[str, Any] = {}
        _params['enabled'] = encode(FieldMeta('', '', False, 'primitive'), enabled)
        _result = await self._target.send('Page.setLifecycleEventsEnabled', _params)
        return None

    async def set_touch_emulation_enabled(self, *, enabled: bool, configuration: Optional[Literal['mobile', 'desktop']] = None) -> None:
        """
        Toggles mouse event-based touch event emulation.
        
        .. deprecated::
        :param enabled: Whether the touch event emulation should be enabled.
        :param configuration: Touch/gesture events configuration. Default: current platform.
        """
        _params: Dict[str, Any] = {}
        _params['enabled'] = encode(FieldMeta('', '', False, 'primitive'), enabled)
        if configuration is not None:
            _params['configuration'] = encode(FieldMeta('', '', False, 'primitive'), configuration)
        _result = await self._target.send('Page.setTouchEmulationEnabled', _params)
        return None

    async def start_screencast(self, *, format: Optional[Literal['jpeg', 'png']] = None, quality: Optional[int] = None, max_width: Optional[int] = None, max_height: Optional[int] = None, every_nth_frame: Optional[int] = None) -> None:
        """
        Starts sending each frame using the `screencastFrame` event.
        :param format: Image compression format.
        :param quality: Compression quality from range [0..100].
        :param max_width: Maximum screenshot width.
        :param max_height: Maximum screenshot height.
        :param every_nth_frame: Send every n-th frame.
        """
        _params: Dict[str, Any] = {}
        if format is not None:
            _params['format'] = encode(FieldMeta('', '', False, 'primitive'), format)
        if quality is not None:
            _params['quality'] = encode(FieldMeta('', '', False, 'primitive'), quality)
        if max_width is not None:
            _params['maxWidth'] = encode(FieldMeta('', '', False, 'primitive'), max_width)
        if max_height is not None:
            _params['maxHeight'] = encode(FieldMeta('', '', False, 'primitive'), max_height)
        if every_nth_frame is not None:
            _params['everyNthFrame'] = encode(FieldMeta('', '', False, 'primitive'), every_nth_frame)
        _result = await self._target.send('Page.startScreencast', _params)
        return None

    async def stop_loading(self) -> None:
        """Force the page stop all navigations and pending resource fetches."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Page.stopLoading', _params)
        return None

    async def crash(self) -> None:
        """Crashes renderer on the IO thread, generates minidumps."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Page.crash', _params)
        return None

    async def close(self) -> None:
        """Tries to close page, running its beforeunload hooks, if any."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Page.close', _params)
        return None

    async def set_web_lifecycle_state(self, *, state: Literal['frozen', 'active']) -> None:
        """
        Tries to update the web lifecycle state of the page.
        It will transition the page to the given state according to:
        https://github.com/WICG/web-lifecycle/
        :param state: Target lifecycle state
        """
        _params: Dict[str, Any] = {}
        _params['state'] = encode(FieldMeta('', '', False, 'primitive'), state)
        _result = await self._target.send('Page.setWebLifecycleState', _params)
        return None

    async def stop_screencast(self) -> None:
        """Stops sending each frame in the `screencastFrame`."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Page.stopScreencast', _params)
        return None

    async def produce_compilation_cache(self, *, scripts: List[CompilationCacheParams]) -> None:
        """
        Requests backend to produce compilation cache for the specified scripts.
        `scripts` are appended to the list of scripts for which the cache
        would be produced. The list may be reset during page navigation.
        When script with a matching URL is encountered, the cache is optionally
        produced upon backend discretion, based on internal heuristics.
        See also: `Page.compilationCacheProduced`.
        :param scripts:
        """
        _params: Dict[str, Any] = {}
        _params['scripts'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Page.CompilationCacheParams')), scripts)
        _result = await self._target.send('Page.produceCompilationCache', _params)
        return None

    async def add_compilation_cache(self, *, url: str, data: str) -> None:
        """
        Seeds compilation cache for given url. Compilation cache does not survive
        cross-process navigation.
        :param url:
        :param data: Base64-encoded data (Encoded as a base64 string when passed over JSON)
        """
        _params: Dict[str, Any] = {}
        _params['url'] = encode(FieldMeta('', '', False, 'primitive'), url)
        _params['data'] = encode(FieldMeta('', '', False, 'primitive'), data)
        _result = await self._target.send('Page.addCompilationCache', _params)
        return None

    async def clear_compilation_cache(self) -> None:
        """Clears seeded compilation cache."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Page.clearCompilationCache', _params)
        return None

    async def set_spc_transaction_mode(self, *, mode: Literal['none', 'autoAccept', 'autoChooseToAuthAnotherWay', 'autoReject', 'autoOptOut']) -> None:
        """
        Sets the Secure Payment Confirmation transaction mode.
        https://w3c.github.io/secure-payment-confirmation/#sctn-automation-set-spc-transaction-mode
        :param mode:
        """
        _params: Dict[str, Any] = {}
        _params['mode'] = encode(FieldMeta('', '', False, 'primitive'), mode)
        _result = await self._target.send('Page.setSPCTransactionMode', _params)
        return None

    async def set_rph_registration_mode(self, *, mode: Literal['none', 'autoAccept', 'autoReject']) -> None:
        """
        Extensions for Custom Handlers API:
        https://html.spec.whatwg.org/multipage/system-state.html#rph-automation
        :param mode:
        """
        _params: Dict[str, Any] = {}
        _params['mode'] = encode(FieldMeta('', '', False, 'primitive'), mode)
        _result = await self._target.send('Page.setRPHRegistrationMode', _params)
        return None

    async def generate_test_report(self, *, message: str, group: Optional[str] = None) -> None:
        """
        Generates a report for testing.
        :param message: Message to be displayed in the report.
        :param group: Specifies the endpoint group to deliver the report to.
        """
        _params: Dict[str, Any] = {}
        _params['message'] = encode(FieldMeta('', '', False, 'primitive'), message)
        if group is not None:
            _params['group'] = encode(FieldMeta('', '', False, 'primitive'), group)
        _result = await self._target.send('Page.generateTestReport', _params)
        return None

    async def wait_for_debugger(self) -> None:
        """Pauses page execution. Can be resumed using generic Runtime.runIfWaitingForDebugger."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Page.waitForDebugger', _params)
        return None

    async def set_intercept_file_chooser_dialog(self, *, enabled: bool, cancel: Optional[bool] = None) -> None:
        """
        Intercept file chooser requests and transfer control to protocol clients.
        When file chooser interception is enabled, native file chooser dialog is not shown.
        Instead, a protocol event `Page.fileChooserOpened` is emitted.
        :param enabled:
        :param cancel: If true, cancels the dialog by emitting relevant events (if any)
        in addition to not showing it if the interception is enabled
        (default: false).
        """
        _params: Dict[str, Any] = {}
        _params['enabled'] = encode(FieldMeta('', '', False, 'primitive'), enabled)
        if cancel is not None:
            _params['cancel'] = encode(FieldMeta('', '', False, 'primitive'), cancel)
        _result = await self._target.send('Page.setInterceptFileChooserDialog', _params)
        return None

    async def set_prerendering_allowed(self, *, is_allowed: bool) -> None:
        """
        Enable/disable prerendering manually.
        
        This command is a short-term solution for https://crbug.com/1440085.
        See https://docs.google.com/document/d/12HVmFxYj5Jc-eJr5OmWsa2bqTJsbgGLKI6ZIyx0_wpA
        for more details.
        
        TODO(https://crbug.com/1440085): Remove this once Puppeteer supports tab targets.
        :param is_allowed:
        """
        _params: Dict[str, Any] = {}
        _params['isAllowed'] = encode(FieldMeta('', '', False, 'primitive'), is_allowed)
        _result = await self._target.send('Page.setPrerenderingAllowed', _params)
        return None

    async def get_annotated_page_content(self, *, include_actionable_information: Optional[bool] = None) -> GetAnnotatedPageContentReturn:
        """
        Get the annotated page content for the main frame.
        This is an experimental command that is subject to change.
        :param include_actionable_information: Whether to include actionable information. Defaults to true.
        """
        _params: Dict[str, Any] = {}
        if include_actionable_information is not None:
            _params['includeActionableInformation'] = encode(FieldMeta('', '', False, 'primitive'), include_actionable_information)
        _result = await self._target.send('Page.getAnnotatedPageContent', _params)
        return GetAnnotatedPageContentReturn.from_json(_result)
