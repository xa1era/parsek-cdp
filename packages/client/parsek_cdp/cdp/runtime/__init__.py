"""The Runtime CDP domain (generated).

Importing ``Runtime`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``Runtime.SomeEvent`` /
``Runtime.SomeType``); commands run on a target via ``page.cdp.Runtime``.
"""
from . import events, functions, types
from .functions import Runtime
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(Runtime,)``).
DOMAIN = "Runtime"

__all__ = ["events", "functions", "types", "Runtime", "DOMAIN"]
