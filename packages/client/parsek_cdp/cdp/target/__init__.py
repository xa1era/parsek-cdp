"""The Target CDP domain (generated).

Importing ``Target`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``Target.SomeEvent`` /
``Target.SomeType``); commands run on a target via ``page.cdp.Target``.
"""
from . import events, functions, types
from .functions import Target
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(Target,)``).
DOMAIN = "Target"

__all__ = ["events", "functions", "types", "Target", "DOMAIN"]
