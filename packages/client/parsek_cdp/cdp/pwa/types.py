"""Custom types and enums for the PWA domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, register


@register("PWA.FileHandlerAccept")
@dataclass
class FileHandlerAccept(DataType):
    """
    The following types are the replica of
    https://crsrc.org/c/chrome/browser/web_applications/proto/web_app_os_integration_state.proto;drc=9910d3be894c8f142c977ba1023f30a656bc13fc;l=67
    """
    media_type: str
    file_extensions: List[str]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('media_type', 'mediaType', False, 'primitive'),
        FieldMeta('file_extensions', 'fileExtensions', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


@register("PWA.FileHandler")
@dataclass
class FileHandler(DataType):
    action: str
    accepts: List[FileHandlerAccept]
    display_name: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('action', 'action', False, 'primitive'),
        FieldMeta('accepts', 'accepts', False, 'array', inner=FieldMeta('', '', False, 'object', ref='PWA.FileHandlerAccept')),
        FieldMeta('display_name', 'displayName', False, 'primitive'),
    )


@register("PWA.DisplayMode")
class DisplayMode(str, Enum):
    """If user prefers opening the app in browser or an app window."""
    STANDALONE = 'standalone'
    BROWSER = 'browser'

__all__ = ["DisplayMode", "FileHandler", "FileHandlerAccept"]
