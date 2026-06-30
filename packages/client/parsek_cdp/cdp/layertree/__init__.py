"""The LayerTree CDP domain (generated).

Importing ``LayerTree`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``LayerTree.SomeEvent`` /
``LayerTree.SomeType``); commands run on a target via ``page.cdp.LayerTree``.
"""
from . import events, functions, types
from .functions import LayerTree
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(LayerTree,)``).
DOMAIN = "LayerTree"

__all__ = ["events", "functions", "types", "LayerTree", "DOMAIN"]
