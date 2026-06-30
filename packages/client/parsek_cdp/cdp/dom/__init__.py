"""The DOM CDP domain (generated).

Importing ``DOM`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``DOM.SomeEvent`` /
``DOM.SomeType``); commands run on a target via ``page.cdp.DOM``.
"""
from . import events, functions, types
from .functions import DOM
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(DOM,)``).
DOMAIN = "DOM"

__all__ = ["events", "functions", "types", "DOM", "DOMAIN"]
