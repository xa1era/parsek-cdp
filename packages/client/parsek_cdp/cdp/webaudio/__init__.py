"""The WebAudio CDP domain (generated).

Importing ``WebAudio`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``WebAudio.SomeEvent`` /
``WebAudio.SomeType``); commands run on a target via ``page.cdp.WebAudio``.
"""
from . import events, functions, types
from .functions import WebAudio
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(WebAudio,)``).
DOMAIN = "WebAudio"

__all__ = ["events", "functions", "types", "WebAudio", "DOMAIN"]
