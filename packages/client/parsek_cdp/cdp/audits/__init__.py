"""The Audits CDP domain (generated).

Importing ``Audits`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``Audits.SomeEvent`` /
``Audits.SomeType``); commands run on a target via ``page.cdp.Audits``.
"""
from . import events, functions, types
from .functions import Audits
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(Audits,)``).
DOMAIN = "Audits"

__all__ = ["events", "functions", "types", "Audits", "DOMAIN"]
