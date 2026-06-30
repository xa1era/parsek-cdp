"""Commands for the Performance domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode

if TYPE_CHECKING:
    from .types import Metric

@dataclass
class GetMetricsReturn(DataType):
    """Return value of :meth:`Performance.get_metrics`."""
    metrics: List[Metric]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('metrics', 'metrics', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Performance.Metric')),
    )


class Performance:
    """Commands of the Performance domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def disable(self) -> None:
        """Disable collecting and reporting metrics."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Performance.disable', _params)
        return None

    async def enable(self, *, time_domain: Optional[Literal['timeTicks', 'threadTicks']] = None) -> None:
        """
        Enable collecting and reporting metrics.
        :param time_domain: Time domain to use for collecting and reporting duration metrics.
        """
        _params: Dict[str, Any] = {}
        if time_domain is not None:
            _params['timeDomain'] = encode(FieldMeta('', '', False, 'primitive'), time_domain)
        _result = await self._target.send('Performance.enable', _params)
        return None

    async def set_time_domain(self, *, time_domain: Literal['timeTicks', 'threadTicks']) -> None:
        """
        Sets time domain to use for collecting and reporting duration metrics.
        Note that this must be called before enabling metrics collection. Calling
        this method while metrics collection is enabled returns an error.
        
        .. deprecated::
        :param time_domain: Time domain
        """
        _params: Dict[str, Any] = {}
        _params['timeDomain'] = encode(FieldMeta('', '', False, 'primitive'), time_domain)
        _result = await self._target.send('Performance.setTimeDomain', _params)
        return None

    async def get_metrics(self) -> GetMetricsReturn:
        """Retrieve current values of run-time metrics."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Performance.getMetrics', _params)
        return GetMetricsReturn.from_json(_result)
