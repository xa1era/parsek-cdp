"""Commands for the Schema domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode

if TYPE_CHECKING:
    from .types import Domain

@dataclass
class GetDomainsReturn(DataType):
    """Return value of :meth:`Schema.get_domains`."""
    domains: List[Domain]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('domains', 'domains', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Schema.Domain')),
    )


class Schema:
    """Commands of the Schema domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def get_domains(self) -> GetDomainsReturn:
        """Returns supported domains."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Schema.getDomains', _params)
        return GetDomainsReturn.from_json(_result)
