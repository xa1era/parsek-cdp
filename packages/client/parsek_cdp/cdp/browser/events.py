"""Events for the Browser domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import FieldMeta
from ..mixins.event import Event, register_event

if TYPE_CHECKING:
    from ..page.types import FrameId as Page_FrameId

@register_event("Browser.downloadWillBegin")
@dataclass
class DownloadWillBegin(Event):
    """Fired when page is about to start a download."""
    frame_id: Page_FrameId
    guid: str
    url: str
    suggested_filename: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('frame_id', 'frameId', False, 'primitive'),
        FieldMeta('guid', 'guid', False, 'primitive'),
        FieldMeta('url', 'url', False, 'primitive'),
        FieldMeta('suggested_filename', 'suggestedFilename', False, 'primitive'),
    )


@register_event("Browser.downloadProgress")
@dataclass
class DownloadProgress(Event):
    """Fired when download makes progress. Last call has |done| == true."""
    guid: str
    total_bytes: float
    received_bytes: float
    state: Literal['inProgress', 'completed', 'canceled']
    file_path: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('guid', 'guid', False, 'primitive'),
        FieldMeta('total_bytes', 'totalBytes', False, 'primitive'),
        FieldMeta('received_bytes', 'receivedBytes', False, 'primitive'),
        FieldMeta('state', 'state', False, 'primitive'),
        FieldMeta('file_path', 'filePath', True, 'primitive'),
    )

__all__ = ["DownloadProgress", "DownloadWillBegin"]
