"""The Accessibility CDP domain (generated).

Importing ``Accessibility`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``Accessibility.SomeEvent`` /
``Accessibility.SomeType``); commands run on a target via ``page.cdp.Accessibility``.
"""
from . import events, functions, types
from .functions import Accessibility
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(Accessibility,)``).
DOMAIN = "Accessibility"

__all__ = ["events", "functions", "types", "Accessibility", "DOMAIN"]
