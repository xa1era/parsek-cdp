"""The Animation CDP domain (generated).

Importing ``Animation`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``Animation.SomeEvent`` /
``Animation.SomeType``); commands run on a target via ``page.cdp.Animation``.
"""
from . import events, functions, types
from .functions import Animation
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(Animation,)``).
DOMAIN = "Animation"

__all__ = ["events", "functions", "types", "Animation", "DOMAIN"]
