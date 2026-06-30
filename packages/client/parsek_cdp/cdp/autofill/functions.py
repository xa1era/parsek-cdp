"""Commands for the Autofill domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode

if TYPE_CHECKING:
    from .types import (
        Address,
        CreditCard,
    )
    from ..dom.types import BackendNodeId as DOM_BackendNodeId
    from ..page.types import FrameId as Page_FrameId

class Autofill:
    """Commands of the Autofill domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def trigger(self, *, field_id: DOM_BackendNodeId, frame_id: Optional[Page_FrameId] = None, card: Optional[CreditCard] = None, address: Optional[Address] = None) -> None:
        """
        Trigger autofill on a form identified by the fieldId.
        If the field and related form cannot be autofilled, returns an error.
        :param field_id: Identifies a field that serves as an anchor for autofill.
        :param frame_id: Identifies the frame that field belongs to.
        :param card: Credit card information to fill out the form. Credit card data is not saved.  Mutually exclusive with `address`.
        :param address: Address to fill out the form. Address data is not saved. Mutually exclusive with `card`.
        """
        _params: Dict[str, Any] = {}
        _params['fieldId'] = encode(FieldMeta('', '', False, 'primitive'), field_id)
        if frame_id is not None:
            _params['frameId'] = encode(FieldMeta('', '', False, 'primitive'), frame_id)
        if card is not None:
            _params['card'] = encode(FieldMeta('', '', False, 'object', ref='Autofill.CreditCard'), card)
        if address is not None:
            _params['address'] = encode(FieldMeta('', '', False, 'object', ref='Autofill.Address'), address)
        _result = await self._target.send('Autofill.trigger', _params)
        return None

    async def set_addresses(self, *, addresses: List[Address]) -> None:
        """
        Set addresses so that developers can verify their forms implementation.
        :param addresses:
        """
        _params: Dict[str, Any] = {}
        _params['addresses'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Autofill.Address')), addresses)
        _result = await self._target.send('Autofill.setAddresses', _params)
        return None

    async def disable(self) -> None:
        """Disables autofill domain notifications."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Autofill.disable', _params)
        return None

    async def enable(self) -> None:
        """Enables autofill domain notifications."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Autofill.enable', _params)
        return None
