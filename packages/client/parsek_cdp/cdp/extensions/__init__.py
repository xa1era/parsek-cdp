"""The Extensions CDP domain (generated).

Importing ``Extensions`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``Extensions.SomeEvent`` /
``Extensions.SomeType``); commands run on a target via ``page.cdp.Extensions``.
"""
from . import events, functions, types
from .functions import Extensions
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(Extensions,)``).
DOMAIN = "Extensions"

__all__ = ["events", "functions", "types", "Extensions", "DOMAIN"]
