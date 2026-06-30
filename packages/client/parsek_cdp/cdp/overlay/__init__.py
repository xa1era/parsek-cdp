"""The Overlay CDP domain (generated).

Importing ``Overlay`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``Overlay.SomeEvent`` /
``Overlay.SomeType``); commands run on a target via ``page.cdp.Overlay``.
"""
from . import events, functions, types
from .functions import Overlay
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(Overlay,)``).
DOMAIN = "Overlay"

__all__ = ["events", "functions", "types", "Overlay", "DOMAIN"]
