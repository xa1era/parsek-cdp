"""Types for the request-listener feature -- both the wire shapes and the views.

* **wire dataclasses** (:class:`RequestData` / :class:`ResponseData` /
  :class:`RedirectEntry`) -- the aggregated shapes that cross the websocket;
  ``__FIELDS__`` are derived from annotations by
  :func:`~parsek_cdp.core.feature.parsek_type`.  Each folds several raw
  ``Network.*`` payloads into one record.
* **view types** (:class:`Request` / :class:`Response`) -- behavioural wrappers
  the reducers rebuild from the wire dataclasses; the body stays lazy.

Everything for this feature is self-contained in this package; nothing lives in
a separate protocol module.
"""

from __future__ import annotations

import asyncio
import base64
from dataclasses import field
from typing import TYPE_CHECKING, Dict, List, Optional, Union

from ...cdp.mixins.datatype import DataType
from ...core.feature import parsek_type

if TYPE_CHECKING:
    from . import RequestListener


# --------------------------------------------------------------------------- #
# wire dataclasses (aggregated)
# --------------------------------------------------------------------------- #


@parsek_type("Parsek.RequestListener.RedirectEntry")
class RedirectEntry(DataType):
    """One hop of a redirect chain, folded into the originating request."""

    url: str
    status_code: int


@parsek_type("Parsek.RequestListener.RequestData")
class RequestData(DataType):
    """The request side, aggregated.

    Folds ``requestWillBeSent`` + ``requestWillBeSentExtraInfo`` (merged headers)
    and the whole redirect chain into one record.
    """

    request_id: str
    url: str
    method: str
    headers: dict = field(default_factory=dict)
    post_data: Optional[str] = None
    resource_type: Optional[str] = None
    frame_id: Optional[str] = None
    loader_id: Optional[str] = None
    #: ``True`` for a main-frame document request (resets the current-doc log).
    is_navigation: bool = False
    redirects: List[RedirectEntry] = field(default_factory=list)


@parsek_type("Parsek.RequestListener.ResponseData")
class ResponseData(DataType):
    """The response side, aggregated and emitted once at completion.

    Folds ``responseReceived`` + ``responseReceivedExtraInfo`` (merged headers) +
    the terminal ``loadingFinished`` / ``loadingFailed`` (whose
    ``encodedDataLength`` is the byte total; per-chunk ``dataReceived`` is ignored).
    """

    request_id: str
    status_code: int
    status_text: str = ""
    mime_type: str = ""
    headers: dict = field(default_factory=dict)
    from_cache: bool = False
    remote_ip: Optional[str] = None
    #: Total bytes over the wire, taken from ``loadingFinished.encodedDataLength``
    #: (the browser's authoritative total -- per-chunk ``dataReceived`` is ignored).
    encoded_data_length: float = 0.0
    succeeded: bool = True
    error_text: Optional[str] = None


# --------------------------------------------------------------------------- #
# cookie helpers
# --------------------------------------------------------------------------- #


def parse_cookie_header(value: str) -> Dict[str, str]:
    """Parse a request ``Cookie`` header into ``name -> value``."""
    out: Dict[str, str] = {}
    for part in value.split(";"):
        if "=" in part:
            name, _, val = part.strip().partition("=")
            out[name] = val
    return out


def parse_set_cookie(value: str) -> Dict[str, str]:
    """Parse one or more ``Set-Cookie`` headers (CDP joins them with newlines)."""
    out: Dict[str, str] = {}
    for line in value.split("\n"):
        head = line.split(";", 1)[0].strip()
        if "=" in head:
            name, _, val = head.partition("=")
            out[name] = val
    return out


# --------------------------------------------------------------------------- #
# view types
# --------------------------------------------------------------------------- #


class Response:
    """A response rebuilt from :class:`ResponseData`; body fetched lazily."""

    def __init__(
        self, feature: "RequestListener", request: "Request", data: ResponseData
    ):
        self._feature = feature
        self.request = request
        self._data = data
        self._body: Optional[Union[str, bytes]] = None

    @property
    def url(self) -> str:
        return self.request.url

    @property
    def status_code(self) -> int:
        return self._data.status_code

    @property
    def headers(self) -> dict:
        return self._data.headers

    @property
    def mime_type(self) -> str:
        return self._data.mime_type

    @property
    def succeeded(self) -> bool:
        return self._data.succeeded

    @property
    def cookies(self) -> Dict[str, str]:
        for key, value in self.headers.items():
            if key.lower() == "set-cookie":
                return parse_set_cookie(value)
        return {}

    async def body(self) -> Union[str, bytes]:
        """Fetch the body once with plain CDP (``Network.getResponseBody``).

        Bodies are never pushed in the aggregated events; the client pulls them
        on demand and the server proxies the call straight to the browser.
        """
        if self._body is None:
            result = await self._feature.host.send(
                "Network.getResponseBody", {"requestId": self.request.id}
            )
            raw: Union[str, bytes] = result.get("body", "")
            if result.get("base64Encoded"):
                decoded = base64.b64decode(raw)
                try:
                    raw = decoded.decode("utf-8")
                except UnicodeDecodeError:
                    raw = decoded
            self._body = raw
        return self._body

    def __repr__(self) -> str:
        return f"<Response [{self.status_code}] {self.url}>"


class Request:
    """A request rebuilt from :class:`RequestData`, completed by a :class:`Response`."""

    def __init__(self, data: RequestData):
        self._data = data
        self.response: Optional[Response] = None
        self.finished = False
        self.succeeded: Optional[bool] = None
        self.error_text: Optional[str] = None
        self._completed = asyncio.Event()

    @property
    def id(self) -> str:
        return self._data.request_id

    @property
    def url(self) -> str:
        return self._data.url

    @property
    def method(self) -> str:
        return self._data.method

    @property
    def headers(self) -> dict:
        return self._data.headers

    @property
    def data(self) -> Optional[str]:
        return self._data.post_data

    @property
    def resource_type(self) -> Optional[str]:
        return self._data.resource_type

    @property
    def redirects(self) -> List[RedirectEntry]:
        return self._data.redirects

    @property
    def cookies(self) -> Dict[str, str]:
        for key, value in self.headers.items():
            if key.lower() == "cookie":
                return parse_cookie_header(value)
        return {}

    async def join(self, *, timeout: Optional[float] = None) -> "Request":
        await asyncio.wait_for(self._completed.wait(), timeout)
        return self

    wait = join

    def __repr__(self) -> str:
        state = (
            "pending" if not self.finished else ("ok" if self.succeeded else "failed")
        )
        return f"<Request {self.method} [{state}] {self.url:.50}>"
