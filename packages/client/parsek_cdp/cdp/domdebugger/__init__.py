"""The DOMDebugger CDP domain (generated).

Importing ``DOMDebugger`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``DOMDebugger.SomeEvent`` /
``DOMDebugger.SomeType``); commands run on a target via ``page.cdp.DOMDebugger``.
"""
from . import events, functions, types
from .functions import DOMDebugger
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(DOMDebugger,)``).
DOMAIN = "DOMDebugger"

__all__ = ["events", "functions", "types", "DOMDebugger", "DOMAIN"]
