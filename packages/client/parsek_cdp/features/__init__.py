"""Unified features -- one class per feature, runnable as server producer or client view.

Each module here defines a single :class:`~parsek_cdp.core.feature.Feature`
that works in both roles (see :mod:`parsek_cdp.core.feature`): the server
hosts it as a producer (raw CDP -> aggregated ``Parsek.*``), the client hosts it
as a view (``Parsek.*`` -> ergonomic API).  Shared code, shipped in the client
distribution and reused by the server.
"""

from __future__ import annotations

from .request_listener import RequestListener

__all__ = ["RequestListener"]
