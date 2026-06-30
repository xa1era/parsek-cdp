"""The EventBreakpoints CDP domain (generated).

Importing ``EventBreakpoints`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``EventBreakpoints.SomeEvent`` /
``EventBreakpoints.SomeType``); commands run on a target via ``page.cdp.EventBreakpoints``.
"""
from . import events, functions, types
from .functions import EventBreakpoints
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(EventBreakpoints,)``).
DOMAIN = "EventBreakpoints"

__all__ = ["events", "functions", "types", "EventBreakpoints", "DOMAIN"]
