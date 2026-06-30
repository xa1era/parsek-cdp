"""The DOMStorage CDP domain (generated).

Importing ``DOMStorage`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``DOMStorage.SomeEvent`` /
``DOMStorage.SomeType``); commands run on a target via ``page.cdp.DOMStorage``.
"""
from . import events, functions, types
from .functions import DOMStorage
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(DOMStorage,)``).
DOMAIN = "DOMStorage"

__all__ = ["events", "functions", "types", "DOMStorage", "DOMAIN"]
