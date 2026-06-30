"""The BackgroundService CDP domain (generated).

Importing ``BackgroundService`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``BackgroundService.SomeEvent`` /
``BackgroundService.SomeType``); commands run on a target via ``page.cdp.BackgroundService``.
"""
from . import events, functions, types
from .functions import BackgroundService
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(BackgroundService,)``).
DOMAIN = "BackgroundService"

__all__ = ["events", "functions", "types", "BackgroundService", "DOMAIN"]
