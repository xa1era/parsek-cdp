"""The WebAuthn CDP domain (generated).

Importing ``WebAuthn`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``WebAuthn.SomeEvent`` /
``WebAuthn.SomeType``); commands run on a target via ``page.cdp.WebAuthn``.
"""
from . import events, functions, types
from .functions import WebAuthn
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(WebAuthn,)``).
DOMAIN = "WebAuthn"

__all__ = ["events", "functions", "types", "WebAuthn", "DOMAIN"]
