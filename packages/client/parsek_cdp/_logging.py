"""Logging helpers for parsek_cdp.

Adds a ``TRACE`` level (below ``DEBUG``) for the very verbose wire-level dumps
(every CDP frame sent/received) so they can be enabled independently of normal
debug logging.  Use :func:`get_logger` per module::

    from .._logging import get_logger

    logger = get_logger(__name__)
    logger.trace("send %s", payload)   # only emitted when TRACE is enabled

The library never configures handlers itself (a ``NullHandler`` is attached to
the package logger in ``__init__``); the application decides where logs go, e.g.
``logging.basicConfig(level=parsek_cdp.TRACE)``.
"""

from __future__ import annotations

import logging
from typing import Any

#: Numeric level for wire-level tracing, below ``logging.DEBUG`` (10).
TRACE = 5
logging.addLevelName(TRACE, "TRACE")


class TraceLogger(logging.Logger):
    """A :class:`logging.Logger` with an extra :meth:`trace` method."""

    def trace(self, msg: object, *args: Any, **kwargs: Any) -> None:
        """Log at :data:`TRACE` level (cheap no-op when not enabled)."""
        if self.isEnabledFor(TRACE):
            self._log(TRACE, msg, args, **kwargs)


# Loggers obtained from now on are TraceLogger instances.
logging.setLoggerClass(TraceLogger)


def get_logger(name: str) -> TraceLogger:
    """Return the module logger, typed so ``logger.trace`` is visible."""
    return logging.getLogger(name)  # type: ignore[return-value]


# The websockets library logs every frame at DEBUG, which drowns out our own
# logs once the app sets a DEBUG/TRACE root level.  Cap it at WARNING by
# default; re-enable explicitly with
# ``logging.getLogger("websockets").setLevel(logging.DEBUG)``.
logging.getLogger("websockets").setLevel(logging.WARNING)
