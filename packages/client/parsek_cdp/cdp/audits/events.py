"""Events for the Audits domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import FieldMeta
from ..mixins.event import Event, register_event

if TYPE_CHECKING:
    from .types import InspectorIssue

@register_event("Audits.issueAdded")
@dataclass
class IssueAdded(Event):
    issue: InspectorIssue
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('issue', 'issue', False, 'object', ref='Audits.InspectorIssue'),
    )

__all__ = ["IssueAdded"]
