"""The Media CDP domain (generated).

Importing ``Media`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``Media.SomeEvent`` /
``Media.SomeType``); commands run on a target via ``page.cdp.Media``.
"""
from . import events, functions, types
from .functions import Media
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(Media,)``).
DOMAIN = "Media"

__all__ = ["events", "functions", "types", "Media", "DOMAIN"]
