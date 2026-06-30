"""The Autofill CDP domain (generated).

Importing ``Autofill`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``Autofill.SomeEvent`` /
``Autofill.SomeType``); commands run on a target via ``page.cdp.Autofill``.
"""
from . import events, functions, types
from .functions import Autofill
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(Autofill,)``).
DOMAIN = "Autofill"

__all__ = ["events", "functions", "types", "Autofill", "DOMAIN"]
