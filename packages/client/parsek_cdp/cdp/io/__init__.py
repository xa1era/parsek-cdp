"""The IO CDP domain (generated).

Importing ``IO`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``IO.SomeEvent`` /
``IO.SomeType``); commands run on a target via ``page.cdp.IO``.
"""
from . import events, functions, types
from .functions import IO
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(IO,)``).
DOMAIN = "IO"

__all__ = ["events", "functions", "types", "IO", "DOMAIN"]
