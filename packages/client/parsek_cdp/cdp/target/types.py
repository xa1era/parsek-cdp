"""Custom types and enums for the Target domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, register

if TYPE_CHECKING:
    from ..browser.types import BrowserContextID as Browser_BrowserContextID
    from ..page.types import FrameId as Page_FrameId

type TargetID = str


type SessionID = str  # Unique identifier of attached debugging session.


@register("Target.TargetInfo")
@dataclass
class TargetInfo(DataType):
    target_id: TargetID
    type_: str
    title: str
    url: str
    attached: bool
    can_access_opener: bool
    opener_id: Optional[TargetID] = None
    opener_frame_id: Optional[Page_FrameId] = None
    parent_frame_id: Optional[Page_FrameId] = None
    browser_context_id: Optional[Browser_BrowserContextID] = None
    subtype: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('target_id', 'targetId', False, 'primitive'),
        FieldMeta('type_', 'type', False, 'primitive'),
        FieldMeta('title', 'title', False, 'primitive'),
        FieldMeta('url', 'url', False, 'primitive'),
        FieldMeta('attached', 'attached', False, 'primitive'),
        FieldMeta('can_access_opener', 'canAccessOpener', False, 'primitive'),
        FieldMeta('opener_id', 'openerId', True, 'primitive'),
        FieldMeta('opener_frame_id', 'openerFrameId', True, 'primitive'),
        FieldMeta('parent_frame_id', 'parentFrameId', True, 'primitive'),
        FieldMeta('browser_context_id', 'browserContextId', True, 'primitive'),
        FieldMeta('subtype', 'subtype', True, 'primitive'),
    )


@register("Target.FilterEntry")
@dataclass
class FilterEntry(DataType):
    """A filter used by target query/discovery/auto-attach operations."""
    exclude: Optional[bool] = None
    type_: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('exclude', 'exclude', True, 'primitive'),
        FieldMeta('type_', 'type', True, 'primitive'),
    )


type TargetFilter = List[FilterEntry]  # The entries in TargetFilter are matched sequentially against targets and


@register("Target.RemoteLocation")
@dataclass
class RemoteLocation(DataType):
    host: str
    port: int
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('host', 'host', False, 'primitive'),
        FieldMeta('port', 'port', False, 'primitive'),
    )


@register("Target.WindowState")
class WindowState(str, Enum):
    """The state of the target window."""
    NORMAL = 'normal'
    MINIMIZED = 'minimized'
    MAXIMIZED = 'maximized'
    FULLSCREEN = 'fullscreen'

__all__ = ["FilterEntry", "RemoteLocation", "SessionID", "TargetFilter", "TargetID", "TargetInfo", "WindowState"]
