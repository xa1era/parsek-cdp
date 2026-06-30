"""Events for the FedCm domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import FieldMeta
from ..mixins.event import Event, register_event

if TYPE_CHECKING:
    from .types import (
        Account,
        DialogType,
    )

@register_event("FedCm.dialogShown")
@dataclass
class DialogShown(Event):
    dialog_id: str
    dialog_type: DialogType
    accounts: List[Account]
    title: str
    subtitle: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('dialog_id', 'dialogId', False, 'primitive'),
        FieldMeta('dialog_type', 'dialogType', False, 'enum', ref='FedCm.DialogType'),
        FieldMeta('accounts', 'accounts', False, 'array', inner=FieldMeta('', '', False, 'object', ref='FedCm.Account')),
        FieldMeta('title', 'title', False, 'primitive'),
        FieldMeta('subtitle', 'subtitle', True, 'primitive'),
    )


@register_event("FedCm.dialogClosed")
@dataclass
class DialogClosed(Event):
    """
    Triggered when a dialog is closed, either by user action, JS abort,
    or a command below.
    """
    dialog_id: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('dialog_id', 'dialogId', False, 'primitive'),
    )

__all__ = ["DialogClosed", "DialogShown"]
