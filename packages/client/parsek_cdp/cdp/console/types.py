"""Custom types and enums for the Console domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, register


@register("Console.ConsoleMessage")
@dataclass
class ConsoleMessage(DataType):
    """Console message."""
    source: Literal['xml', 'javascript', 'network', 'console-api', 'storage', 'appcache', 'rendering', 'security', 'other', 'deprecation', 'worker']
    level: Literal['log', 'warning', 'error', 'debug', 'info']
    text: str
    url: Optional[str] = None
    line: Optional[int] = None
    column: Optional[int] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('source', 'source', False, 'primitive'),
        FieldMeta('level', 'level', False, 'primitive'),
        FieldMeta('text', 'text', False, 'primitive'),
        FieldMeta('url', 'url', True, 'primitive'),
        FieldMeta('line', 'line', True, 'primitive'),
        FieldMeta('column', 'column', True, 'primitive'),
    )

__all__ = ["ConsoleMessage"]
