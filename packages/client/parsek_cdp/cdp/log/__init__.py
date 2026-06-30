"""The Log CDP domain (generated).

Importing ``Log`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``Log.SomeEvent`` /
``Log.SomeType``); commands run on a target via ``page.cdp.Log``.
"""
from . import events, functions, types
from .functions import Log
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(Log,)``).
DOMAIN = "Log"

__all__ = ["events", "functions", "types", "Log", "DOMAIN"]
