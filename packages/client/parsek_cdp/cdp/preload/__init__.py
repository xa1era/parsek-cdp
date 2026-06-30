"""The Preload CDP domain (generated).

Importing ``Preload`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``Preload.SomeEvent`` /
``Preload.SomeType``); commands run on a target via ``page.cdp.Preload``.
"""
from . import events, functions, types
from .functions import Preload
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(Preload,)``).
DOMAIN = "Preload"

__all__ = ["events", "functions", "types", "Preload", "DOMAIN"]
