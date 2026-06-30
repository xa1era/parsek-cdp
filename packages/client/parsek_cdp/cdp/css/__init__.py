"""The CSS CDP domain (generated).

Importing ``CSS`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``CSS.SomeEvent`` /
``CSS.SomeType``); commands run on a target via ``page.cdp.CSS``.
"""
from . import events, functions, types
from .functions import CSS
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(CSS,)``).
DOMAIN = "CSS"

__all__ = ["events", "functions", "types", "CSS", "DOMAIN"]
