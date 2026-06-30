"""The Tethering CDP domain (generated).

Importing ``Tethering`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``Tethering.SomeEvent`` /
``Tethering.SomeType``); commands run on a target via ``page.cdp.Tethering``.
"""
from . import events, functions, types
from .functions import Tethering
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(Tethering,)``).
DOMAIN = "Tethering"

__all__ = ["events", "functions", "types", "Tethering", "DOMAIN"]
