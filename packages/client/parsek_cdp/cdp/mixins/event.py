"""Base machinery for CDP events.

Every event is a :class:`DataType` (so it deserializes from the ``params`` of a
protocol notification) plus a class-level handler registry.  Handlers can be
registered directly on the event class -- without ever instantiating it::

    @Network.RequestWillBeSent.add_handler
    async def on_request(event: Network.RequestWillBeSent) -> None:
        print(event.request.url)

The :data:`EVENT_REGISTRY` maps the protocol method name
(``"Domain.eventName"``) to its event class so a connection can locate and
deserialize an incoming notification.
"""

from __future__ import annotations

from typing import Any, Callable, ClassVar, List, TypeVar

from .datatype import DataType

# "Domain.eventName" -> Event subclass
EVENT_REGISTRY: dict[str, type["Event"]] = {}

EventHandler = Callable[["Event"], Any]

E = TypeVar("E", bound="Event")


def register_event(method: str) -> Callable[[type[E]], type[E]]:
    """Class decorator binding ``cls`` to its protocol method name.

    Returns the class unchanged (and with its concrete type preserved, so type
    checkers still see the event's own fields).
    """

    def deco(cls: type[E]) -> type[E]:
        cls.EVENT_METHOD = method
        EVENT_REGISTRY[method] = cls
        return cls

    return deco


class Event(DataType):
    """Base class for all protocol events.

    ``EVENT_METHOD`` is intentionally upper-case: some protocol events carry a
    parameter literally named ``method``, and a lower-case class attribute would
    be picked up by ``@dataclass`` as that field's default value.
    """

    #: Protocol method name, e.g. ``"Network.requestWillBeSent"``.
    EVENT_METHOD: ClassVar[str] = ""
    #: Handlers registered directly on the class (global, connection-agnostic).
    _global_handlers: ClassVar[List[EventHandler]]

    def __init_subclass__(cls, **kwargs: Any) -> None:
        super().__init_subclass__(**kwargs)
        cls._global_handlers = []

    @classmethod
    def add_handler(cls, handler: EventHandler) -> EventHandler:
        """Register ``handler`` for every occurrence of this event.

        Usable as a decorator.  Works without instantiating the class.
        """
        cls._global_handlers.append(handler)
        return handler

    @classmethod
    def remove_handler(cls, handler: EventHandler) -> None:
        cls._global_handlers.remove(handler)

    @classmethod
    def parse(cls, params: dict[str, Any]) -> "Event":
        """Deserialize the ``params`` payload of a notification."""
        return cls.from_json(params or {})