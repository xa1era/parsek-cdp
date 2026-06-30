"""The Memory CDP domain (generated).

Importing ``Memory`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``Memory.SomeEvent`` /
``Memory.SomeType``); commands run on a target via ``page.cdp.Memory``.
"""
from . import events, functions, types
from .functions import Memory
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(Memory,)``).
DOMAIN = "Memory"

__all__ = ["events", "functions", "types", "Memory", "DOMAIN"]
