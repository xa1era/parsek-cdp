"""Custom types and enums for the IO domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, register


type StreamHandle = str  # This is either obtained from another method or specified as `blob:<uuid>` where

__all__ = ["StreamHandle"]
