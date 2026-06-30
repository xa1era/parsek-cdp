"""The Inspector CDP domain (generated).

Importing ``Inspector`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``Inspector.SomeEvent`` /
``Inspector.SomeType``); commands run on a target via ``page.cdp.Inspector``.
"""
from . import events, functions, types
from .functions import Inspector
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(Inspector,)``).
DOMAIN = "Inspector"

__all__ = ["events", "functions", "types", "Inspector", "DOMAIN"]
