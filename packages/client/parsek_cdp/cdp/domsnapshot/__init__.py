"""The DOMSnapshot CDP domain (generated).

Importing ``DOMSnapshot`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``DOMSnapshot.SomeEvent`` /
``DOMSnapshot.SomeType``); commands run on a target via ``page.cdp.DOMSnapshot``.
"""
from . import events, functions, types
from .functions import DOMSnapshot
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(DOMSnapshot,)``).
DOMAIN = "DOMSnapshot"

__all__ = ["events", "functions", "types", "DOMSnapshot", "DOMAIN"]
