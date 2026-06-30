"""The HeadlessExperimental CDP domain (generated).

Importing ``HeadlessExperimental`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``HeadlessExperimental.SomeEvent`` /
``HeadlessExperimental.SomeType``); commands run on a target via ``page.cdp.HeadlessExperimental``.
"""
from . import events, functions, types
from .functions import HeadlessExperimental
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(HeadlessExperimental,)``).
DOMAIN = "HeadlessExperimental"

__all__ = ["events", "functions", "types", "HeadlessExperimental", "DOMAIN"]
