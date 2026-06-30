"""The Performance CDP domain (generated).

Importing ``Performance`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``Performance.SomeEvent`` /
``Performance.SomeType``); commands run on a target via ``page.cdp.Performance``.
"""
from . import events, functions, types
from .functions import Performance
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(Performance,)``).
DOMAIN = "Performance"

__all__ = ["events", "functions", "types", "Performance", "DOMAIN"]
