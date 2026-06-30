"""The DeviceAccess CDP domain (generated).

Importing ``DeviceAccess`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``DeviceAccess.SomeEvent`` /
``DeviceAccess.SomeType``); commands run on a target via ``page.cdp.DeviceAccess``.
"""
from . import events, functions, types
from .functions import DeviceAccess
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(DeviceAccess,)``).
DOMAIN = "DeviceAccess"

__all__ = ["events", "functions", "types", "DeviceAccess", "DOMAIN"]
