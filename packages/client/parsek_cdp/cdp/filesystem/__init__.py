"""The FileSystem CDP domain (generated).

Importing ``FileSystem`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``FileSystem.SomeEvent`` /
``FileSystem.SomeType``); commands run on a target via ``page.cdp.FileSystem``.
"""
from . import events, functions, types
from .functions import FileSystem
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(FileSystem,)``).
DOMAIN = "FileSystem"

__all__ = ["events", "functions", "types", "FileSystem", "DOMAIN"]
