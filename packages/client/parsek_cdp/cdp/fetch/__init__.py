"""The Fetch CDP domain (generated).

Importing ``Fetch`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``Fetch.SomeEvent`` /
``Fetch.SomeType``); commands run on a target via ``page.cdp.Fetch``.
"""
from . import events, functions, types
from .functions import Fetch
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(Fetch,)``).
DOMAIN = "Fetch"

__all__ = ["events", "functions", "types", "Fetch", "DOMAIN"]
