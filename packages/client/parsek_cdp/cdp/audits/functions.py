"""Commands for the Audits domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode

if TYPE_CHECKING:
    from .types import GenericIssueDetails
    from ..network.types import RequestId as Network_RequestId

@dataclass
class GetEncodedResponseReturn(DataType):
    """Return value of :meth:`Audits.get_encoded_response`."""
    original_size: int
    encoded_size: int
    body: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('original_size', 'originalSize', False, 'primitive'),
        FieldMeta('encoded_size', 'encodedSize', False, 'primitive'),
        FieldMeta('body', 'body', True, 'primitive'),
    )


@dataclass
class CheckFormsIssuesReturn(DataType):
    """Return value of :meth:`Audits.check_forms_issues`."""
    form_issues: List[GenericIssueDetails]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('form_issues', 'formIssues', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Audits.GenericIssueDetails')),
    )


class Audits:
    """Commands of the Audits domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def get_encoded_response(self, *, request_id: Network_RequestId, encoding: Literal['webp', 'jpeg', 'png'], quality: Optional[float] = None, size_only: Optional[bool] = None) -> GetEncodedResponseReturn:
        """
        Returns the response body and size if it were re-encoded with the specified settings. Only
        applies to images.
        :param request_id: Identifier of the network request to get content for.
        :param encoding: The encoding to use.
        :param quality: The quality of the encoding (0-1). (defaults to 1)
        :param size_only: Whether to only return the size information (defaults to false).
        """
        _params: Dict[str, Any] = {}
        _params['requestId'] = encode(FieldMeta('', '', False, 'primitive'), request_id)
        _params['encoding'] = encode(FieldMeta('', '', False, 'primitive'), encoding)
        if quality is not None:
            _params['quality'] = encode(FieldMeta('', '', False, 'primitive'), quality)
        if size_only is not None:
            _params['sizeOnly'] = encode(FieldMeta('', '', False, 'primitive'), size_only)
        _result = await self._target.send('Audits.getEncodedResponse', _params)
        return GetEncodedResponseReturn.from_json(_result)

    async def disable(self) -> None:
        """Disables issues domain, prevents further issues from being reported to the client."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Audits.disable', _params)
        return None

    async def enable(self) -> None:
        """
        Enables issues domain, sends the issues collected so far to the client by means of the
        `issueAdded` event.
        """
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Audits.enable', _params)
        return None

    async def check_contrast(self, *, report_aaa: Optional[bool] = None) -> None:
        """
        Runs the contrast check for the target page. Found issues are reported
        using Audits.issueAdded event.
        :param report_aaa: Whether to report WCAG AAA level issues. Default is false.
        """
        _params: Dict[str, Any] = {}
        if report_aaa is not None:
            _params['reportAAA'] = encode(FieldMeta('', '', False, 'primitive'), report_aaa)
        _result = await self._target.send('Audits.checkContrast', _params)
        return None

    async def check_forms_issues(self) -> CheckFormsIssuesReturn:
        """
        Runs the form issues check for the target page. Found issues are reported
        using Audits.issueAdded event.
        """
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Audits.checkFormsIssues', _params)
        return CheckFormsIssuesReturn.from_json(_result)
