"""Events for the Page domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import FieldMeta
from ..mixins.event import Event, register_event

if TYPE_CHECKING:
    from .types import (
        BackForwardCacheNotRestoredExplanation,
        BackForwardCacheNotRestoredExplanationTree,
        ClientNavigationDisposition,
        ClientNavigationReason,
        DialogType,
        Frame,
        FrameId,
        NavigationType,
        ScreencastFrameMetadata,
    )
    from ..dom.types import BackendNodeId as DOM_BackendNodeId
    from ..network.types import LoaderId as Network_LoaderId
    from ..network.types import MonotonicTime as Network_MonotonicTime
    from ..runtime.types import StackTrace as Runtime_StackTrace

@register_event("Page.domContentEventFired")
@dataclass
class DomContentEventFired(Event):
    timestamp: Network_MonotonicTime
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('timestamp', 'timestamp', False, 'primitive'),
    )


@register_event("Page.fileChooserOpened")
@dataclass
class FileChooserOpened(Event):
    """Emitted only when `page.interceptFileChooser` is enabled."""
    frame_id: FrameId
    mode: Literal['selectSingle', 'selectMultiple']
    backend_node_id: Optional[DOM_BackendNodeId] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('frame_id', 'frameId', False, 'primitive'),
        FieldMeta('mode', 'mode', False, 'primitive'),
        FieldMeta('backend_node_id', 'backendNodeId', True, 'primitive'),
    )


@register_event("Page.frameAttached")
@dataclass
class FrameAttached(Event):
    """Fired when frame has been attached to its parent."""
    frame_id: FrameId
    parent_frame_id: FrameId
    stack: Optional[Runtime_StackTrace] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('frame_id', 'frameId', False, 'primitive'),
        FieldMeta('parent_frame_id', 'parentFrameId', False, 'primitive'),
        FieldMeta('stack', 'stack', True, 'object', ref='Runtime.StackTrace'),
    )


@register_event("Page.frameClearedScheduledNavigation")
@dataclass
class FrameClearedScheduledNavigation(Event):
    """Fired when frame no longer has a scheduled navigation."""
    frame_id: FrameId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('frame_id', 'frameId', False, 'primitive'),
    )


@register_event("Page.frameDetached")
@dataclass
class FrameDetached(Event):
    """Fired when frame has been detached from its parent."""
    frame_id: FrameId
    reason: Literal['remove', 'swap']
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('frame_id', 'frameId', False, 'primitive'),
        FieldMeta('reason', 'reason', False, 'primitive'),
    )


@register_event("Page.frameSubtreeWillBeDetached")
@dataclass
class FrameSubtreeWillBeDetached(Event):
    """
    Fired before frame subtree is detached. Emitted before any frame of the
    subtree is actually detached.
    """
    frame_id: FrameId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('frame_id', 'frameId', False, 'primitive'),
    )


@register_event("Page.frameNavigated")
@dataclass
class FrameNavigated(Event):
    """Fired once navigation of the frame has completed. Frame is now associated with the new loader."""
    frame: Frame
    type_: NavigationType
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('frame', 'frame', False, 'object', ref='Page.Frame'),
        FieldMeta('type_', 'type', False, 'enum', ref='Page.NavigationType'),
    )


@register_event("Page.documentOpened")
@dataclass
class DocumentOpened(Event):
    """Fired when opening document to write to."""
    frame: Frame
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('frame', 'frame', False, 'object', ref='Page.Frame'),
    )


@register_event("Page.frameResized")
@dataclass
class FrameResized(Event):
    pass
    __FIELDS__: ClassVar[tuple] = ()


@register_event("Page.frameStartedNavigating")
@dataclass
class FrameStartedNavigating(Event):
    """
    Fired when a navigation starts. This event is fired for both
    renderer-initiated and browser-initiated navigations. For renderer-initiated
    navigations, the event is fired after `frameRequestedNavigation`.
    Navigation may still be cancelled after the event is issued. Multiple events
    can be fired for a single navigation, for example, when a same-document
    navigation becomes a cross-document navigation (such as in the case of a
    frameset).
    """
    frame_id: FrameId
    url: str
    loader_id: Network_LoaderId
    navigation_type: Literal['reload', 'reloadBypassingCache', 'restore', 'restoreWithPost', 'historySameDocument', 'historyDifferentDocument', 'sameDocument', 'differentDocument']
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('frame_id', 'frameId', False, 'primitive'),
        FieldMeta('url', 'url', False, 'primitive'),
        FieldMeta('loader_id', 'loaderId', False, 'primitive'),
        FieldMeta('navigation_type', 'navigationType', False, 'primitive'),
    )


@register_event("Page.frameRequestedNavigation")
@dataclass
class FrameRequestedNavigation(Event):
    """
    Fired when a renderer-initiated navigation is requested.
    Navigation may still be cancelled after the event is issued.
    """
    frame_id: FrameId
    reason: ClientNavigationReason
    url: str
    disposition: ClientNavigationDisposition
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('frame_id', 'frameId', False, 'primitive'),
        FieldMeta('reason', 'reason', False, 'enum', ref='Page.ClientNavigationReason'),
        FieldMeta('url', 'url', False, 'primitive'),
        FieldMeta('disposition', 'disposition', False, 'enum', ref='Page.ClientNavigationDisposition'),
    )


@register_event("Page.frameScheduledNavigation")
@dataclass
class FrameScheduledNavigation(Event):
    """Fired when frame schedules a potential navigation."""
    frame_id: FrameId
    delay: float
    reason: ClientNavigationReason
    url: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('frame_id', 'frameId', False, 'primitive'),
        FieldMeta('delay', 'delay', False, 'primitive'),
        FieldMeta('reason', 'reason', False, 'enum', ref='Page.ClientNavigationReason'),
        FieldMeta('url', 'url', False, 'primitive'),
    )


@register_event("Page.frameStartedLoading")
@dataclass
class FrameStartedLoading(Event):
    """Fired when frame has started loading."""
    frame_id: FrameId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('frame_id', 'frameId', False, 'primitive'),
    )


@register_event("Page.frameStoppedLoading")
@dataclass
class FrameStoppedLoading(Event):
    """Fired when frame has stopped loading."""
    frame_id: FrameId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('frame_id', 'frameId', False, 'primitive'),
    )


@register_event("Page.downloadWillBegin")
@dataclass
class DownloadWillBegin(Event):
    """
    Fired when page is about to start a download.
    Deprecated. Use Browser.downloadWillBegin instead.
    """
    frame_id: FrameId
    guid: str
    url: str
    suggested_filename: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('frame_id', 'frameId', False, 'primitive'),
        FieldMeta('guid', 'guid', False, 'primitive'),
        FieldMeta('url', 'url', False, 'primitive'),
        FieldMeta('suggested_filename', 'suggestedFilename', False, 'primitive'),
    )


@register_event("Page.downloadProgress")
@dataclass
class DownloadProgress(Event):
    """
    Fired when download makes progress. Last call has |done| == true.
    Deprecated. Use Browser.downloadProgress instead.
    """
    guid: str
    total_bytes: float
    received_bytes: float
    state: Literal['inProgress', 'completed', 'canceled']
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('guid', 'guid', False, 'primitive'),
        FieldMeta('total_bytes', 'totalBytes', False, 'primitive'),
        FieldMeta('received_bytes', 'receivedBytes', False, 'primitive'),
        FieldMeta('state', 'state', False, 'primitive'),
    )


@register_event("Page.interstitialHidden")
@dataclass
class InterstitialHidden(Event):
    """Fired when interstitial page was hidden"""
    __FIELDS__: ClassVar[tuple] = ()


@register_event("Page.interstitialShown")
@dataclass
class InterstitialShown(Event):
    """Fired when interstitial page was shown"""
    __FIELDS__: ClassVar[tuple] = ()


@register_event("Page.javascriptDialogClosed")
@dataclass
class JavascriptDialogClosed(Event):
    """
    Fired when a JavaScript initiated dialog (alert, confirm, prompt, or onbeforeunload) has been
    closed.
    """
    frame_id: FrameId
    result: bool
    user_input: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('frame_id', 'frameId', False, 'primitive'),
        FieldMeta('result', 'result', False, 'primitive'),
        FieldMeta('user_input', 'userInput', False, 'primitive'),
    )


@register_event("Page.javascriptDialogOpening")
@dataclass
class JavascriptDialogOpening(Event):
    """
    Fired when a JavaScript initiated dialog (alert, confirm, prompt, or onbeforeunload) is about to
    open.
    """
    url: str
    frame_id: FrameId
    message: str
    type_: DialogType
    has_browser_handler: bool
    default_prompt: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('url', 'url', False, 'primitive'),
        FieldMeta('frame_id', 'frameId', False, 'primitive'),
        FieldMeta('message', 'message', False, 'primitive'),
        FieldMeta('type_', 'type', False, 'enum', ref='Page.DialogType'),
        FieldMeta('has_browser_handler', 'hasBrowserHandler', False, 'primitive'),
        FieldMeta('default_prompt', 'defaultPrompt', True, 'primitive'),
    )


@register_event("Page.lifecycleEvent")
@dataclass
class LifecycleEvent(Event):
    """
    Fired for lifecycle events (navigation, load, paint, etc) in the current
    target (including local frames).
    """
    frame_id: FrameId
    loader_id: Network_LoaderId
    name: str
    timestamp: Network_MonotonicTime
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('frame_id', 'frameId', False, 'primitive'),
        FieldMeta('loader_id', 'loaderId', False, 'primitive'),
        FieldMeta('name', 'name', False, 'primitive'),
        FieldMeta('timestamp', 'timestamp', False, 'primitive'),
    )


@register_event("Page.backForwardCacheNotUsed")
@dataclass
class BackForwardCacheNotUsed(Event):
    """
    Fired for failed bfcache history navigations if BackForwardCache feature is enabled. Do
    not assume any ordering with the Page.frameNavigated event. This event is fired only for
    main-frame history navigation where the document changes (non-same-document navigations),
    when bfcache navigation fails.
    """
    loader_id: Network_LoaderId
    frame_id: FrameId
    not_restored_explanations: List[BackForwardCacheNotRestoredExplanation]
    not_restored_explanations_tree: Optional[BackForwardCacheNotRestoredExplanationTree] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('loader_id', 'loaderId', False, 'primitive'),
        FieldMeta('frame_id', 'frameId', False, 'primitive'),
        FieldMeta('not_restored_explanations', 'notRestoredExplanations', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Page.BackForwardCacheNotRestoredExplanation')),
        FieldMeta('not_restored_explanations_tree', 'notRestoredExplanationsTree', True, 'object', ref='Page.BackForwardCacheNotRestoredExplanationTree'),
    )


@register_event("Page.loadEventFired")
@dataclass
class LoadEventFired(Event):
    timestamp: Network_MonotonicTime
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('timestamp', 'timestamp', False, 'primitive'),
    )


@register_event("Page.navigatedWithinDocument")
@dataclass
class NavigatedWithinDocument(Event):
    """Fired when same-document navigation happens, e.g. due to history API usage or anchor navigation."""
    frame_id: FrameId
    url: str
    navigation_type: Literal['fragment', 'historyApi', 'other']
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('frame_id', 'frameId', False, 'primitive'),
        FieldMeta('url', 'url', False, 'primitive'),
        FieldMeta('navigation_type', 'navigationType', False, 'primitive'),
    )


@register_event("Page.screencastFrame")
@dataclass
class ScreencastFrame(Event):
    """Compressed image data requested by the `startScreencast`."""
    data: str
    metadata: ScreencastFrameMetadata
    session_id: int
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('data', 'data', False, 'primitive'),
        FieldMeta('metadata', 'metadata', False, 'object', ref='Page.ScreencastFrameMetadata'),
        FieldMeta('session_id', 'sessionId', False, 'primitive'),
    )


@register_event("Page.screencastVisibilityChanged")
@dataclass
class ScreencastVisibilityChanged(Event):
    """Fired when the page with currently enabled screencast was shown or hidden `."""
    visible: bool
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('visible', 'visible', False, 'primitive'),
    )


@register_event("Page.windowOpen")
@dataclass
class WindowOpen(Event):
    """
    Fired when a new window is going to be opened, via window.open(), link click, form submission,
    etc.
    """
    url: str
    window_name: str
    window_features: List[str]
    user_gesture: bool
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('url', 'url', False, 'primitive'),
        FieldMeta('window_name', 'windowName', False, 'primitive'),
        FieldMeta('window_features', 'windowFeatures', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('user_gesture', 'userGesture', False, 'primitive'),
    )


@register_event("Page.compilationCacheProduced")
@dataclass
class CompilationCacheProduced(Event):
    """Issued for every compilation cache generated."""
    url: str
    data: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('url', 'url', False, 'primitive'),
        FieldMeta('data', 'data', False, 'primitive'),
    )

__all__ = ["BackForwardCacheNotUsed", "CompilationCacheProduced", "DocumentOpened", "DomContentEventFired", "DownloadProgress", "DownloadWillBegin", "FileChooserOpened", "FrameAttached", "FrameClearedScheduledNavigation", "FrameDetached", "FrameNavigated", "FrameRequestedNavigation", "FrameResized", "FrameScheduledNavigation", "FrameStartedLoading", "FrameStartedNavigating", "FrameStoppedLoading", "FrameSubtreeWillBeDetached", "InterstitialHidden", "InterstitialShown", "JavascriptDialogClosed", "JavascriptDialogOpening", "LifecycleEvent", "LoadEventFired", "NavigatedWithinDocument", "ScreencastFrame", "ScreencastVisibilityChanged", "WindowOpen"]
