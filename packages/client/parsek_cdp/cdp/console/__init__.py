"""The Console CDP domain (generated).

Importing ``Console`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``Console.SomeEvent`` /
``Console.SomeType``); commands run on a target via ``page.cdp.Console``.
"""
from . import events, functions, types
from .functions import Console
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(Console,)``).
DOMAIN = "Console"

__all__ = ["events", "functions", "types", "Console", "DOMAIN"]
