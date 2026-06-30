"""Commands for the FedCm domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode

if TYPE_CHECKING:
    from .types import (
        AccountUrlType,
        DialogButton,
    )

class FedCm:
    """Commands of the FedCm domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def enable(self, *, disable_rejection_delay: Optional[bool] = None) -> None:
        """
        :param disable_rejection_delay: Allows callers to disable the promise rejection delay that would
        normally happen, if this is unimportant to what's being tested.
        (step 4 of https://fedidcg.github.io/FedCM/#browser-api-rp-sign-in)
        """
        _params: Dict[str, Any] = {}
        if disable_rejection_delay is not None:
            _params['disableRejectionDelay'] = encode(FieldMeta('', '', False, 'primitive'), disable_rejection_delay)
        _result = await self._target.send('FedCm.enable', _params)
        return None

    async def disable(self) -> None:
        _params: Dict[str, Any] = {}
        _result = await self._target.send('FedCm.disable', _params)
        return None

    async def select_account(self, *, dialog_id: str, account_index: int) -> None:
        """
        :param dialog_id:
        :param account_index:
        """
        _params: Dict[str, Any] = {}
        _params['dialogId'] = encode(FieldMeta('', '', False, 'primitive'), dialog_id)
        _params['accountIndex'] = encode(FieldMeta('', '', False, 'primitive'), account_index)
        _result = await self._target.send('FedCm.selectAccount', _params)
        return None

    async def click_dialog_button(self, *, dialog_id: str, dialog_button: DialogButton) -> None:
        """
        :param dialog_id:
        :param dialog_button:
        """
        _params: Dict[str, Any] = {}
        _params['dialogId'] = encode(FieldMeta('', '', False, 'primitive'), dialog_id)
        _params['dialogButton'] = encode(FieldMeta('', '', False, 'enum', ref='FedCm.DialogButton'), dialog_button)
        _result = await self._target.send('FedCm.clickDialogButton', _params)
        return None

    async def open_url(self, *, dialog_id: str, account_index: int, account_url_type: AccountUrlType) -> None:
        """
        :param dialog_id:
        :param account_index:
        :param account_url_type:
        """
        _params: Dict[str, Any] = {}
        _params['dialogId'] = encode(FieldMeta('', '', False, 'primitive'), dialog_id)
        _params['accountIndex'] = encode(FieldMeta('', '', False, 'primitive'), account_index)
        _params['accountUrlType'] = encode(FieldMeta('', '', False, 'enum', ref='FedCm.AccountUrlType'), account_url_type)
        _result = await self._target.send('FedCm.openUrl', _params)
        return None

    async def dismiss_dialog(self, *, dialog_id: str, trigger_cooldown: Optional[bool] = None) -> None:
        """
        :param dialog_id:
        :param trigger_cooldown:
        """
        _params: Dict[str, Any] = {}
        _params['dialogId'] = encode(FieldMeta('', '', False, 'primitive'), dialog_id)
        if trigger_cooldown is not None:
            _params['triggerCooldown'] = encode(FieldMeta('', '', False, 'primitive'), trigger_cooldown)
        _result = await self._target.send('FedCm.dismissDialog', _params)
        return None

    async def reset_cooldown(self) -> None:
        """
        Resets the cooldown time, if any, to allow the next FedCM call to show
        a dialog even if one was recently dismissed by the user.
        """
        _params: Dict[str, Any] = {}
        _result = await self._target.send('FedCm.resetCooldown', _params)
        return None
