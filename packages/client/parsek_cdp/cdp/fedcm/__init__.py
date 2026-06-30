"""The FedCm CDP domain (generated).

Importing ``FedCm`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``FedCm.SomeEvent`` /
``FedCm.SomeType``); commands run on a target via ``page.cdp.FedCm``.
"""
from . import events, functions, types
from .functions import FedCm
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(FedCm,)``).
DOMAIN = "FedCm"

__all__ = ["events", "functions", "types", "FedCm", "DOMAIN"]
