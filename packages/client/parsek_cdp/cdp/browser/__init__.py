"""The Browser CDP domain (generated).

Importing ``Browser`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``Browser.SomeEvent`` /
``Browser.SomeType``); commands run on a target via ``page.cdp.Browser``.
"""
from . import events, functions, types
from .functions import Browser
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(Browser,)``).
DOMAIN = "Browser"

__all__ = ["events", "functions", "types", "Browser", "DOMAIN"]
