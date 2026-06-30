"""The BluetoothEmulation CDP domain (generated).

Importing ``BluetoothEmulation`` from ``parsek_cdp.cdp`` gives a namespace with this
domain's events and types as attributes (``BluetoothEmulation.SomeEvent`` /
``BluetoothEmulation.SomeType``); commands run on a target via ``page.cdp.BluetoothEmulation``.
"""
from . import events, functions, types
from .functions import BluetoothEmulation
from .events import *  # noqa: F401,F403 -- expose events on the namespace
from .types import *  # noqa: F401,F403 -- expose types on the namespace

#: Protocol domain name (used by features that declare ``domains=(BluetoothEmulation,)``).
DOMAIN = "BluetoothEmulation"

__all__ = ["events", "functions", "types", "BluetoothEmulation", "DOMAIN"]
