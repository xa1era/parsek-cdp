"""Commands for the ServiceWorker domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode

if TYPE_CHECKING:
    from .types import RegistrationID

class ServiceWorker:
    """Commands of the ServiceWorker domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def deliver_push_message(self, *, origin: str, registration_id: RegistrationID, data: str) -> None:
        """
        :param origin:
        :param registration_id:
        :param data:
        """
        _params: Dict[str, Any] = {}
        _params['origin'] = encode(FieldMeta('', '', False, 'primitive'), origin)
        _params['registrationId'] = encode(FieldMeta('', '', False, 'primitive'), registration_id)
        _params['data'] = encode(FieldMeta('', '', False, 'primitive'), data)
        _result = await self._target.send('ServiceWorker.deliverPushMessage', _params)
        return None

    async def disable(self) -> None:
        _params: Dict[str, Any] = {}
        _result = await self._target.send('ServiceWorker.disable', _params)
        return None

    async def dispatch_sync_event(self, *, origin: str, registration_id: RegistrationID, tag: str, last_chance: bool) -> None:
        """
        :param origin:
        :param registration_id:
        :param tag:
        :param last_chance:
        """
        _params: Dict[str, Any] = {}
        _params['origin'] = encode(FieldMeta('', '', False, 'primitive'), origin)
        _params['registrationId'] = encode(FieldMeta('', '', False, 'primitive'), registration_id)
        _params['tag'] = encode(FieldMeta('', '', False, 'primitive'), tag)
        _params['lastChance'] = encode(FieldMeta('', '', False, 'primitive'), last_chance)
        _result = await self._target.send('ServiceWorker.dispatchSyncEvent', _params)
        return None

    async def dispatch_periodic_sync_event(self, *, origin: str, registration_id: RegistrationID, tag: str) -> None:
        """
        :param origin:
        :param registration_id:
        :param tag:
        """
        _params: Dict[str, Any] = {}
        _params['origin'] = encode(FieldMeta('', '', False, 'primitive'), origin)
        _params['registrationId'] = encode(FieldMeta('', '', False, 'primitive'), registration_id)
        _params['tag'] = encode(FieldMeta('', '', False, 'primitive'), tag)
        _result = await self._target.send('ServiceWorker.dispatchPeriodicSyncEvent', _params)
        return None

    async def enable(self) -> None:
        _params: Dict[str, Any] = {}
        _result = await self._target.send('ServiceWorker.enable', _params)
        return None

    async def set_force_update_on_page_load(self, *, force_update_on_page_load: bool) -> None:
        """:param force_update_on_page_load:"""
        _params: Dict[str, Any] = {}
        _params['forceUpdateOnPageLoad'] = encode(FieldMeta('', '', False, 'primitive'), force_update_on_page_load)
        _result = await self._target.send('ServiceWorker.setForceUpdateOnPageLoad', _params)
        return None

    async def skip_waiting(self, *, scope_url: str) -> None:
        """:param scope_url:"""
        _params: Dict[str, Any] = {}
        _params['scopeURL'] = encode(FieldMeta('', '', False, 'primitive'), scope_url)
        _result = await self._target.send('ServiceWorker.skipWaiting', _params)
        return None

    async def start_worker(self, *, scope_url: str) -> None:
        """:param scope_url:"""
        _params: Dict[str, Any] = {}
        _params['scopeURL'] = encode(FieldMeta('', '', False, 'primitive'), scope_url)
        _result = await self._target.send('ServiceWorker.startWorker', _params)
        return None

    async def stop_all_workers(self) -> None:
        _params: Dict[str, Any] = {}
        _result = await self._target.send('ServiceWorker.stopAllWorkers', _params)
        return None

    async def stop_worker(self, *, version_id: str) -> None:
        """:param version_id:"""
        _params: Dict[str, Any] = {}
        _params['versionId'] = encode(FieldMeta('', '', False, 'primitive'), version_id)
        _result = await self._target.send('ServiceWorker.stopWorker', _params)
        return None

    async def unregister(self, *, scope_url: str) -> None:
        """:param scope_url:"""
        _params: Dict[str, Any] = {}
        _params['scopeURL'] = encode(FieldMeta('', '', False, 'primitive'), scope_url)
        _result = await self._target.send('ServiceWorker.unregister', _params)
        return None

    async def update_registration(self, *, scope_url: str) -> None:
        """:param scope_url:"""
        _params: Dict[str, Any] = {}
        _params['scopeURL'] = encode(FieldMeta('', '', False, 'primitive'), scope_url)
        _result = await self._target.send('ServiceWorker.updateRegistration', _params)
        return None
