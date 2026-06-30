"""The Cast CDP domain (generated).

Importing ``Cast`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``Cast.SomeEvent`` /
``Cast.SomeType``); commands run on a target via ``page.cdp.Cast``.
"""
from . import events, functions, types
from .functions import Cast
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(Cast,)``).
DOMAIN = "Cast"

__all__ = ["events", "functions", "types", "Cast", "DOMAIN"]
