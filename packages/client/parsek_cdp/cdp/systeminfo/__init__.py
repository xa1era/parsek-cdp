"""The SystemInfo CDP domain (generated).

Importing ``SystemInfo`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``SystemInfo.SomeEvent`` /
``SystemInfo.SomeType``); commands run on a target via ``page.cdp.SystemInfo``.
"""
from . import events, functions, types
from .functions import SystemInfo
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(SystemInfo,)``).
DOMAIN = "SystemInfo"

__all__ = ["events", "functions", "types", "SystemInfo", "DOMAIN"]
