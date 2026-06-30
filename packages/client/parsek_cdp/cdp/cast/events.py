"""Events for the Cast domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import FieldMeta
from ..mixins.event import Event, register_event

if TYPE_CHECKING:
    from .types import Sink

@register_event("Cast.sinksUpdated")
@dataclass
class SinksUpdated(Event):
    """
    This is fired whenever the list of available sinks changes. A sink is a
    device or a software surface that you can cast to.
    """
    sinks: List[Sink]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('sinks', 'sinks', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Cast.Sink')),
    )


@register_event("Cast.issueUpdated")
@dataclass
class IssueUpdated(Event):
    """
    This is fired whenever the outstanding issue/error message changes.
    |issueMessage| is empty if there is no issue.
    """
    issue_message: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('issue_message', 'issueMessage', False, 'primitive'),
    )

__all__ = ["IssueUpdated", "SinksUpdated"]
