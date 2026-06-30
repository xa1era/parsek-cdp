"""The PerformanceTimeline CDP domain (generated).

Importing ``PerformanceTimeline`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``PerformanceTimeline.SomeEvent`` /
``PerformanceTimeline.SomeType``); commands run on a target via ``page.cdp.PerformanceTimeline``.
"""
from . import events, functions, types
from .functions import PerformanceTimeline
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(PerformanceTimeline,)``).
DOMAIN = "PerformanceTimeline"

__all__ = ["events", "functions", "types", "PerformanceTimeline", "DOMAIN"]
