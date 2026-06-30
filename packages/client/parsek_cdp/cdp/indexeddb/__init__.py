"""The IndexedDB CDP domain (generated).

Importing ``IndexedDB`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``IndexedDB.SomeEvent`` /
``IndexedDB.SomeType``); commands run on a target via ``page.cdp.IndexedDB``.
"""
from . import events, functions, types
from .functions import IndexedDB
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(IndexedDB,)``).
DOMAIN = "IndexedDB"

__all__ = ["events", "functions", "types", "IndexedDB", "DOMAIN"]
