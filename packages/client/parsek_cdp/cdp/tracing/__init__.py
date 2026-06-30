"""The Tracing CDP domain (generated).

Importing ``Tracing`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``Tracing.SomeEvent`` /
``Tracing.SomeType``); commands run on a target via ``page.cdp.Tracing``.
"""
from . import events, functions, types
from .functions import Tracing
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(Tracing,)``).
DOMAIN = "Tracing"

__all__ = ["events", "functions", "types", "Tracing", "DOMAIN"]
