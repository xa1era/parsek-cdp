"""The Storage CDP domain (generated).

Importing ``Storage`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``Storage.SomeEvent`` /
``Storage.SomeType``); commands run on a target via ``page.cdp.Storage``.
"""
from . import events, functions, types
from .functions import Storage
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(Storage,)``).
DOMAIN = "Storage"

__all__ = ["events", "functions", "types", "Storage", "DOMAIN"]
