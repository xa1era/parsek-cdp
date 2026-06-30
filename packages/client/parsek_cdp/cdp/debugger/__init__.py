"""The Debugger CDP domain (generated).

Importing ``Debugger`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``Debugger.SomeEvent`` /
``Debugger.SomeType``); commands run on a target via ``page.cdp.Debugger``.
"""
from . import events, functions, types
from .functions import Debugger
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(Debugger,)``).
DOMAIN = "Debugger"

__all__ = ["events", "functions", "types", "Debugger", "DOMAIN"]
