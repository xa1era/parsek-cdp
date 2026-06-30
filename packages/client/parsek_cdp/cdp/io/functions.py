"""Commands for the IO domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode

if TYPE_CHECKING:
    from .types import StreamHandle
    from ..runtime.types import RemoteObjectId as Runtime_RemoteObjectId

@dataclass
class ReadReturn(DataType):
    """Return value of :meth:`IO.read`."""
    data: str
    eof: bool
    base64_encoded: Optional[bool] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('data', 'data', False, 'primitive'),
        FieldMeta('eof', 'eof', False, 'primitive'),
        FieldMeta('base64_encoded', 'base64Encoded', True, 'primitive'),
    )


@dataclass
class ResolveBlobReturn(DataType):
    """Return value of :meth:`IO.resolve_blob`."""
    uuid: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('uuid', 'uuid', False, 'primitive'),
    )


class IO:
    """Commands of the IO domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def close(self, *, handle: StreamHandle) -> None:
        """
        Close the stream, discard any temporary backing storage.
        :param handle: Handle of the stream to close.
        """
        _params: Dict[str, Any] = {}
        _params['handle'] = encode(FieldMeta('', '', False, 'primitive'), handle)
        _result = await self._target.send('IO.close', _params)
        return None

    async def read(self, *, handle: StreamHandle, offset: Optional[int] = None, size: Optional[int] = None) -> ReadReturn:
        """
        Read a chunk of the stream
        :param handle: Handle of the stream to read.
        :param offset: Seek to the specified offset before reading (if not specified, proceed with offset
        following the last read). Some types of streams may only support sequential reads.
        :param size: Maximum number of bytes to read (left upon the agent discretion if not specified).
        """
        _params: Dict[str, Any] = {}
        _params['handle'] = encode(FieldMeta('', '', False, 'primitive'), handle)
        if offset is not None:
            _params['offset'] = encode(FieldMeta('', '', False, 'primitive'), offset)
        if size is not None:
            _params['size'] = encode(FieldMeta('', '', False, 'primitive'), size)
        _result = await self._target.send('IO.read', _params)
        return ReadReturn.from_json(_result)

    async def resolve_blob(self, *, object_id: Runtime_RemoteObjectId) -> ResolveBlobReturn:
        """
        Return UUID of Blob object specified by a remote object id.
        :param object_id: Object id of a Blob object wrapper.
        """
        _params: Dict[str, Any] = {}
        _params['objectId'] = encode(FieldMeta('', '', False, 'primitive'), object_id)
        _result = await self._target.send('IO.resolveBlob', _params)
        return ResolveBlobReturn.from_json(_result)
