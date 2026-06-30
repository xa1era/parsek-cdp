"""The Security CDP domain (generated).

Importing ``Security`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``Security.SomeEvent`` /
``Security.SomeType``); commands run on a target via ``page.cdp.Security``.
"""
from . import events, functions, types
from .functions import Security
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(Security,)``).
DOMAIN = "Security"

__all__ = ["events", "functions", "types", "Security", "DOMAIN"]
