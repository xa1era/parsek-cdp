"""The ServiceWorker CDP domain (generated).

Importing ``ServiceWorker`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``ServiceWorker.SomeEvent`` /
``ServiceWorker.SomeType``); commands run on a target via ``page.cdp.ServiceWorker``.
"""
from . import events, functions, types
from .functions import ServiceWorker
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(ServiceWorker,)``).
DOMAIN = "ServiceWorker"

__all__ = ["events", "functions", "types", "ServiceWorker", "DOMAIN"]
