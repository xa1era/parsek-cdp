"""The CacheStorage CDP domain (generated).

Importing ``CacheStorage`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``CacheStorage.SomeEvent`` /
``CacheStorage.SomeType``); commands run on a target via ``page.cdp.CacheStorage``.
"""
from . import events, functions, types
from .functions import CacheStorage
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(CacheStorage,)``).
DOMAIN = "CacheStorage"

__all__ = ["events", "functions", "types", "CacheStorage", "DOMAIN"]
