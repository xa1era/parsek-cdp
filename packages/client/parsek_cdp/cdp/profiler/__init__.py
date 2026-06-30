"""The Profiler CDP domain (generated).

Importing ``Profiler`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``Profiler.SomeEvent`` /
``Profiler.SomeType``); commands run on a target via ``page.cdp.Profiler``.
"""
from . import events, functions, types
from .functions import Profiler
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(Profiler,)``).
DOMAIN = "Profiler"

__all__ = ["events", "functions", "types", "Profiler", "DOMAIN"]
