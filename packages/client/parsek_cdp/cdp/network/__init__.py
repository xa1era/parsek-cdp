"""The Network CDP domain (generated).

Importing ``Network`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``Network.SomeEvent`` /
``Network.SomeType``); commands run on a target via ``page.cdp.Network``.
"""
from . import events, functions, types
from .functions import Network
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(Network,)``).
DOMAIN = "Network"

__all__ = ["events", "functions", "types", "Network", "DOMAIN"]
