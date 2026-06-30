"""Commands for the SystemInfo domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode

if TYPE_CHECKING:
    from .types import (
        GPUInfo,
        ProcessInfo,
    )

@dataclass
class GetInfoReturn(DataType):
    """Return value of :meth:`SystemInfo.get_info`."""
    gpu: GPUInfo
    model_name: str
    model_version: str
    command_line: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('gpu', 'gpu', False, 'object', ref='SystemInfo.GPUInfo'),
        FieldMeta('model_name', 'modelName', False, 'primitive'),
        FieldMeta('model_version', 'modelVersion', False, 'primitive'),
        FieldMeta('command_line', 'commandLine', False, 'primitive'),
    )


@dataclass
class GetFeatureStateReturn(DataType):
    """Return value of :meth:`SystemInfo.get_feature_state`."""
    feature_enabled: bool
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('feature_enabled', 'featureEnabled', False, 'primitive'),
    )


@dataclass
class GetProcessInfoReturn(DataType):
    """Return value of :meth:`SystemInfo.get_process_info`."""
    process_info: List[ProcessInfo]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('process_info', 'processInfo', False, 'array', inner=FieldMeta('', '', False, 'object', ref='SystemInfo.ProcessInfo')),
    )


class SystemInfo:
    """Commands of the SystemInfo domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def get_info(self) -> GetInfoReturn:
        """Returns information about the system."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('SystemInfo.getInfo', _params)
        return GetInfoReturn.from_json(_result)

    async def get_feature_state(self, *, feature_state: str) -> GetFeatureStateReturn:
        """
        Returns information about the feature state.
        :param feature_state:
        """
        _params: Dict[str, Any] = {}
        _params['featureState'] = encode(FieldMeta('', '', False, 'primitive'), feature_state)
        _result = await self._target.send('SystemInfo.getFeatureState', _params)
        return GetFeatureStateReturn.from_json(_result)

    async def get_process_info(self) -> GetProcessInfoReturn:
        """Returns information about all running processes."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('SystemInfo.getProcessInfo', _params)
        return GetProcessInfoReturn.from_json(_result)
