"""The Page CDP domain (generated).

Importing ``Page`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``Page.SomeEvent`` /
``Page.SomeType``); commands run on a target via ``page.cdp.Page``.
"""
from . import events, functions, types
from .functions import Page
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(Page,)``).
DOMAIN = "Page"

__all__ = ["events", "functions", "types", "Page", "DOMAIN"]
