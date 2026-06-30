"""The DeviceOrientation CDP domain (generated).

Importing ``DeviceOrientation`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``DeviceOrientation.SomeEvent`` /
``DeviceOrientation.SomeType``); commands run on a target via ``page.cdp.DeviceOrientation``.
"""
from . import events, functions, types
from .functions import DeviceOrientation
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(DeviceOrientation,)``).
DOMAIN = "DeviceOrientation"

__all__ = ["events", "functions", "types", "DeviceOrientation", "DOMAIN"]
