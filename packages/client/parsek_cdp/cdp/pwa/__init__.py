"""The PWA CDP domain (generated).

Importing ``PWA`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``PWA.SomeEvent`` /
``PWA.SomeType``); commands run on a target via ``page.cdp.PWA``.
"""
from . import events, functions, types
from .functions import PWA
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(PWA,)``).
DOMAIN = "PWA"

__all__ = ["events", "functions", "types", "PWA", "DOMAIN"]
