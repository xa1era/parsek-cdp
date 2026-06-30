"""The Emulation CDP domain (generated).

Importing ``Emulation`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``Emulation.SomeEvent`` /
``Emulation.SomeType``); commands run on a target via ``page.cdp.Emulation``.
"""
from . import events, functions, types
from .functions import Emulation
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(Emulation,)``).
DOMAIN = "Emulation"

__all__ = ["events", "functions", "types", "Emulation", "DOMAIN"]
