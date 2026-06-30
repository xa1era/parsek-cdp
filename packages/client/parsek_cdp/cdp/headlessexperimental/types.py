"""Custom types and enums for the HeadlessExperimental domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, register


@register("HeadlessExperimental.ScreenshotParams")
@dataclass
class ScreenshotParams(DataType):
    """Encoding options for a screenshot."""
    format: Optional[Literal['jpeg', 'png', 'webp']] = None
    quality: Optional[int] = None
    optimize_for_speed: Optional[bool] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('format', 'format', True, 'primitive'),
        FieldMeta('quality', 'quality', True, 'primitive'),
        FieldMeta('optimize_for_speed', 'optimizeForSpeed', True, 'primitive'),
    )

__all__ = ["ScreenshotParams"]
