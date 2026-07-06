"""Request listener -- one self-contained feature, two roles.

Everything for this feature lives in this package: the wire types and view types
(:mod:`.types`), the aggregated events (:mod:`.events`) and the feature class
here.  There is no command surface -- the feature is a pure *observer* whose job
is aggregation; the one thing a client pulls on demand (a response body) is
fetched with plain CDP (``Network.getResponseBody``), proxied transparently.

* **server (producer)** -- owns ``Network``; the ``@on(Network.*)`` handlers
  accumulate the raw burst and emit exactly two aggregated events per request:
  ``RequestSent`` (once the request is final) and ``ResponseCompleted`` (at
  completion, with merged headers and total bytes).  Per-chunk ``dataReceived``
  never leaves the server.
* **client (view)** -- the ``@on(Parsek...)`` reducers rebuild ``.requests`` of
  :class:`~.types.Request` / :class:`~.types.Response` from those two events.

The reducers run in *both* roles, so the public API is identical client- and
server-side (and powers the server snapshot for late joiners).
"""

from __future__ import annotations

import asyncio
import re
from typing import Callable, Dict, List, Optional, Union

from ...cdp import Network
from ...cdp.mixins.namespace import attach_namespace
from ...core.feature import Feature, emit, on
from . import events as _events
from . import types as _types
from .events import RequestSent, ResponseCompleted
from .types import RedirectEntry, Request, RequestData, Response, ResponseData

Matcher = Union[str, "re.Pattern[str]"]


class RequestListener(Feature):
    """Aggregated network observation. Server produces, client views.

    Doubles as this feature's namespace: after ``from parsek_cdp.features import
    RequestListener`` you can reach its wire/view types and events as attributes
    (``RequestListener.RequestSent``, ``RequestListener.RequestData``,
    ``RequestListener.Request`` ...), so callers never import them individually.
    """

    domains = (Network,)

    def __init__(
        self, host, *, role: str = "client", preserve_log: bool = False
    ) -> None:
        self._requests: Dict[str, Request] = {}
        self.preserve_log = preserve_log
        self._waiters: List[tuple] = []
        self._pending: Dict[str, RequestData] = {}
        self._resp: Dict[str, ResponseData] = {}
        self._emitted: set[str] = set()
        #: request ids the browser reported as served from the memory cache
        #: (``requestServedFromCache`` fires before ``responseReceived``).
        self._served_from_cache: set[str] = set()
        super().__init__(host, role=role)

    @property
    def requests(self) -> List[Request]:
        return list(self._requests.values())

    def get(self, target: Matcher) -> Optional[Request]:
        pred = self._predicate(target)
        return next(
            (r for r in self._requests.values() if r.response and pred(r)), None
        )

    async def wait_for_response(
        self, target: Matcher, *, timeout: float = 60, load_body: bool = False
    ) -> Request:
        """Wait until a request matching ``target`` has a response.

        ``target`` is matched against the request URL: a ``str`` matches as a
        substring (so ``"/api/orders"`` finds ``https://site/api/orders?p=2``);
        a compiled regex is matched with :meth:`re.Pattern.search`.
        """
        pred = self._predicate(target)
        record = self.get(target)
        if record is None:
            future: asyncio.Future = asyncio.get_running_loop().create_future()
            self._waiters.append((pred, future))
            record = await asyncio.wait_for(future, timeout)
        if load_body and record.response is not None:
            await record.response.body()
        return record

    @staticmethod
    def _predicate(target: Matcher) -> Callable[[Request], bool]:
        """Build a URL predicate: regex -> ``search``, str -> substring match."""
        if isinstance(target, re.Pattern):
            return lambda r: target.search(r.url) is not None
        return lambda r: target in r.url

    def _notify(self) -> None:
        for pred, future in list(self._waiters):
            if future.done():
                self._waiters.remove((pred, future))
                continue
            rec = next(
                (r for r in self._requests.values() if r.response and pred(r)), None
            )
            if rec is not None:
                future.set_result(rec)
                self._waiters.remove((pred, future))

    async def snapshot(self) -> dict:
        """State for a late-joining client (the proxy may replay it on connect)."""
        return {"requests": [r._data.to_json() for r in self._requests.values()]}

    @on(RequestSent)
    def _reduce_request(self, e: RequestSent) -> None:
        data = e.request
        if data.is_navigation and not self.preserve_log:
            # A new document replaces the previous one.  Unblock any waiter on a
            # request we are about to drop (so ``join()`` returns instead of
            # hanging until its timeout -- ``finished`` stays False, the caller
            # can tell it was cut short), then reap producer-side state for the
            # old requests.  Keep the navigation request's own still-in-flight
            # state: its ``loadingFinished`` is yet to come.
            for old in self._requests.values():
                old._completed.set()
            self._requests.clear()
            keep = data.request_id
            self._pending = {keep: self._pending[keep]} if keep in self._pending else {}
            self._resp = {keep: self._resp[keep]} if keep in self._resp else {}
            self._emitted = {keep} if keep in self._emitted else set()
            self._served_from_cache = (
                {keep} if keep in self._served_from_cache else set()
            )
        self._requests[data.request_id] = Request(data)

    @on(ResponseCompleted)
    def _reduce_response(self, e: ResponseCompleted) -> None:
        req = self._requests.get(e.response.request_id)
        if req is None:
            return
        req.response = Response(self, req, e.response)
        req.finished = True
        req.succeeded = e.response.succeeded
        req.error_text = e.response.error_text
        req._completed.set()
        self._notify()

    @on(Network.RequestWillBeSent)
    def _on_request(self, e: "Network.RequestWillBeSent") -> None:
        rd = self._pending.get(e.request_id)
        if rd is None:
            rd = RequestData(request_id=e.request_id, url="", method="")
            self._pending[e.request_id] = rd
        if e.redirect_response is not None:  # redirect reuses the id
            rd.redirects.append(
                RedirectEntry(
                    url=rd.url or e.redirect_response.url,
                    status_code=e.redirect_response.status,
                )
            )
        rd.url = e.request.url
        rd.method = e.request.method
        rd.headers = dict(e.request.headers)
        rd.post_data = e.request.post_data
        rd.resource_type = e.type_.value if e.type_ else None
        rd.frame_id = e.frame_id
        rd.loader_id = e.loader_id
        rd.is_navigation = e.type_ == Network.ResourceType.DOCUMENT

    @on(Network.RequestServedFromCache)
    def _on_served_from_cache(self, e: "Network.RequestServedFromCache") -> None:
        self._served_from_cache.add(e.request_id)

    @on(Network.RequestWillBeSentExtraInfo)
    def _on_request_extra(self, e: "Network.RequestWillBeSentExtraInfo") -> None:
        rd = self._pending.get(e.request_id)
        if rd and e.headers:
            rd.headers = {**rd.headers, **e.headers}

    @on(Network.ResponseReceived)
    @emit(RequestSent)
    def _on_response(self, e: "Network.ResponseReceived") -> Optional[RequestSent]:
        rd = self._pending.get(e.request_id)
        if rd is None:
            return None
        self._resp[e.request_id] = ResponseData(
            request_id=e.request_id,
            status_code=e.response.status,
            status_text=e.response.status_text,
            mime_type=e.response.mime_type,
            headers=dict(e.response.headers),
            from_cache=(
                e.request_id in self._served_from_cache
                or bool(e.response.from_disk_cache)
                or bool(e.response.from_prefetch_cache)
            ),
            remote_ip=getattr(e.response, "remote_ip_address", None),
        )
        self._emitted.add(e.request_id)
        return RequestSent(request=rd)  # request is now final

    @on(Network.ResponseReceivedExtraInfo)
    def _on_response_extra(self, e: "Network.ResponseReceivedExtraInfo") -> None:
        resp = self._resp.get(e.request_id)
        if resp and e.headers:
            resp.headers = {**resp.headers, **e.headers}

    @on(Network.LoadingFinished)
    @emit(ResponseCompleted)
    def _on_finished(self, e: "Network.LoadingFinished"):
        return self._complete(
            e.request_id,
            encoded=float(e.encoded_data_length),
            succeeded=True,
            error=None,
        )

    @on(Network.LoadingFailed)
    @emit(ResponseCompleted)
    def _on_failed(self, e: "Network.LoadingFailed"):
        return self._complete(
            e.request_id, encoded=0.0, succeeded=False, error=e.error_text
        )

    def _complete(self, request_id, *, encoded, succeeded, error):
        rd = self._pending.get(request_id)
        if rd is None:
            return None
        resp = self._resp.get(request_id) or ResponseData(
            request_id=request_id, status_code=0
        )
        resp.encoded_data_length = encoded
        resp.succeeded = succeeded
        resp.error_text = error
        # emit RequestSent first if a bodyless failure skipped responseReceived
        out: list = [] if request_id in self._emitted else [RequestSent(request=rd)]
        out.append(ResponseCompleted(response=resp))
        # Terminal for this request: free the producer-side state so a
        # long-lived page can't accumulate it forever.  A duplicate terminal
        # (e.g. a stray second loadingFinished) now finds nothing and is
        # dropped, which is the right idempotent behaviour.
        self._pending.pop(request_id, None)
        self._resp.pop(request_id, None)
        self._emitted.discard(request_id)
        self._served_from_cache.discard(request_id)
        return out


# Expose this feature's events and types as attributes on the feature class,
# so it works as a namespace (RequestListener.RequestSent / .RequestData / ...).
attach_namespace(RequestListener, _types, _events)

__all__ = ["RequestListener"]
