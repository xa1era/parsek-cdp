"""The Schema CDP domain (generated).

Importing ``Schema`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``Schema.SomeEvent`` /
``Schema.SomeType``); commands run on a target via ``page.cdp.Schema``.
"""
from . import events, functions, types
from .functions import Schema
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(Schema,)``).
DOMAIN = "Schema"

__all__ = ["events", "functions", "types", "Schema", "DOMAIN"]
