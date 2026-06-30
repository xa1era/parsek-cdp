"""Aggregated wire events for the request-listener feature.

Raw CDP emits, per request::

    requestWillBeSent → requestWillBeSentExtraInfo → responseReceived
      → responseReceivedExtraInfo → dataReceived × N → loadingFinished

collapsed by the producer into exactly two events: :class:`RequestSent` (once the
request is final) and :class:`ResponseCompleted` (at completion, with merged
headers and the total byte count).  Both carry the page ``sessionId`` so they
route to the owning page's target on the client.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar

from ...cdp.mixins.datatype import FieldMeta
from ...cdp.mixins.event import Event, register_event
from .types import RequestData, ResponseData


@register_event("Parsek.RequestListener.request")
@dataclass
class RequestSent(Event):
    """A request went out (folds requestWillBeSent + extraInfo + redirect chain)."""

    request: RequestData

    __FIELDS__: ClassVar[tuple] = (
        FieldMeta("request", "request", False, "object",
                  ref="Parsek.RequestListener.RequestData"),
    )


@register_event("Parsek.RequestListener.response")
@dataclass
class ResponseCompleted(Event):
    """A response fully arrived (folds responseReceived + extraInfo + dataReceived
    + loadingFinished/Failed into one message at completion)."""

    response: ResponseData

    __FIELDS__: ClassVar[tuple] = (
        FieldMeta("response", "response", False, "object",
                  ref="Parsek.RequestListener.ResponseData"),
    )
