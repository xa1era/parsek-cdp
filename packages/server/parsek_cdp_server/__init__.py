"""parsek-cdp-server -- the server scope: launch, supervise and proxy a browser.

Separate distribution from ``parsek-cdp`` (the client); installed via
``pip install parsek-cdp[server]``.  It *depends on* ``parsek-cdp`` and reuses
its shared layers wholesale -- the generated ``cdp`` protocol, the ``core``
primitives (``CDPConnection``, ``Target``, ``DataType``) and the ``parsek``
contract -- adding only what must live next to the browser:

* :mod:`~parsek_cdp_server.launcher`   -- spawn Chrome, find its websocket;
* :mod:`~parsek_cdp_server.supervisor` -- own the browser lifecycle: health,
  crash detection, restart, idle shutdown, and ``Parsek.browserStateChanged``
  broadcast;
* :mod:`~parsek_cdp_server.proxy`      -- accept client websockets and bridge
  each one 1:1 to a Chrome target (no ``sessionId`` multiplexing, no id remap),
  hosting feature producers on page pipes and serving the ``Parsek.*`` surface;
* :mod:`~parsek_cdp_server.metrics`    -- Prometheus exposition at ``/metrics``
  (browsers, targets/types, nested targets, per-target CDP events, CPU/RAM);
* :mod:`~parsek_cdp_server.reaper`     -- a separate subprocess that kills leaked
  (zombie/orphaned) parsek-launched Chrome processes.

Feature *producers* (raw CDP -> ``Parsek.*``) are shared code shipped in the
client distribution (:mod:`parsek_cdp.features`); the server hosts them but does
not define them.  ``ParsekServer`` registers none by default -- it is a pure
passthrough until features are added via ``register_feature``.

Endpoints (see :mod:`~parsek_cdp_server.proxy`)::

    HTTP POST /browsers                            create task -> browser_uuid
    HTTP GET  /metrics                             Prometheus metrics
    ws        /cdp/{browser_uuid}/control          lifecycle + Parsek.*
    ws        /cdp/{browser_uuid}/page/{target_id} CDP proxy (per-target) + Parsek.*
"""

from __future__ import annotations

from .launcher import ChromeLauncher
from .metrics import ServerMetrics
from .proxy import ParsekServer
from .supervisor import BrowserSupervisor

__all__ = [
    "ParsekServer",
    "ChromeLauncher",
    "BrowserSupervisor",
    "ServerMetrics",
]
