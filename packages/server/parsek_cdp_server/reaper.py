"""A standalone reaper subprocess that kills leaked Chrome processes.

The supervisor terminates the browsers it owns, but a process can still leak:
a relaunch whose ``terminate()`` raced the crash, a server killed with ``-9``
before it cleaned up, a renderer subtree the parent never reaped.  Those linger
as **zombies** (defunct, status ``Z``) or **orphans** (reparented to PID 1 once
their launching server died) and pile up holding RAM and profile dirs.

This module is a *separate OS process* (spawned via :func:`multiprocessing`,
``daemon=True`` so it dies with the server) that periodically scans the process
table and reaps those leaks.  It is deliberately self-sufficient -- it does not
talk to the server -- so it only targets processes that are unambiguously
abandoned:

* recognised as **parsek-launched** -- the argv carries
  ``--user-data-dir=<...PROFILE_PREFIX...>`` (see :data:`launcher.PROFILE_PREFIX`),
  so a live, properly-parented browser of ours is never in scope; and
* **zombie** (``status == Z``) *or* **orphaned** (``ppid == 1``).

Run it standalone for ops/debugging::

    python -m parsek_cdp_server.reaper --interval 30 --once
"""

from __future__ import annotations

import argparse
import os
import signal
import subprocess
import sys
import time
from typing import List

import psutil

from parsek_cdp._logging import get_logger
from .launcher import PROFILE_PREFIX, _is_browser

logger = get_logger(__name__)

#: Default seconds between reap sweeps.
DEFAULT_INTERVAL = 30.0


def _is_parsek_chrome(proc: psutil.Process) -> bool:
    """Whether ``proc`` is a browser *we* launched (matched by the profile marker)."""
    try:
        if not _is_browser(proc.name()):
            return False
        return any(
            arg.startswith("--user-data-dir=") and PROFILE_PREFIX in arg
            for arg in proc.cmdline()
        )
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        return False


def _is_abandoned(proc: psutil.Process) -> bool:
    """A parsek browser is abandoned if it is defunct or reparented to init."""
    try:
        if proc.status() == psutil.STATUS_ZOMBIE:
            return True
        return proc.ppid() == 1
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        return False
    except psutil.ZombieProcess:
        return True


def find_leaked_chromes() -> List[psutil.Process]:
    """Return the parsek-launched browser processes that are zombies or orphans."""
    leaked: List[psutil.Process] = []
    for proc in psutil.process_iter():
        if _is_parsek_chrome(proc) and _is_abandoned(proc):
            leaked.append(proc)
    return leaked


def _kill_tree(proc: psutil.Process) -> int:
    """SIGKILL ``proc`` and its descendants; return how many we signalled.

    Zombies cannot be killed (only reaped by their parent), but ``waitpid`` on a
    child of ours clears it; for orphans, init reaps them once we kill the tree.
    """
    killed = 0
    try:
        victims = proc.children(recursive=True) + [proc]
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        victims = [proc]
    for victim in victims:
        try:
            victim.kill()
            killed += 1
        except psutil.NoSuchProcess:
            pass
        except psutil.AccessDenied:
            logger.warning("reaper: access denied killing pid %s", victim.pid)
    # Reap any of our own now-dead children so they do not become zombies.
    try:
        os.waitpid(proc.pid, os.WNOHANG)
    except (ChildProcessError, OSError):
        pass
    return killed


def reap_once() -> int:
    """Run one sweep; return the number of processes signalled."""
    total = 0
    for proc in find_leaked_chromes():
        pid = proc.pid
        n = _kill_tree(proc)
        if n:
            logger.info("reaper: killed leaked chrome tree (root pid %s, %d procs)", pid, n)
        total += n
    return total


def run_reaper(interval: float = DEFAULT_INTERVAL) -> None:
    """Reap loop for the subprocess: sweep, sleep, repeat until signalled."""
    stop = {"flag": False}

    def _handle(_signum, _frame) -> None:
        stop["flag"] = True

    signal.signal(signal.SIGTERM, _handle)
    signal.signal(signal.SIGINT, _handle)
    logger.info("chrome reaper started (interval=%.1fs, pid=%s)", interval, os.getpid())
    while not stop["flag"]:
        try:
            reap_once()
        except Exception:
            logger.exception("reaper sweep failed")
        # Sleep in small slices so a SIGTERM is honoured promptly.
        slept = 0.0
        while slept < interval and not stop["flag"]:
            time.sleep(min(0.5, interval - slept))
            slept += 0.5
    logger.info("chrome reaper stopped")


def spawn_reaper(interval: float = DEFAULT_INTERVAL) -> subprocess.Popen:
    """Launch the reaper as a separate ``python -m`` subprocess and return it.

    A real subprocess (rather than a fork) keeps the reaper independent of the
    server's event loop and avoids the spawn/forkserver re-import of the entry
    module.  The parent's ``sys.path`` is forwarded via ``PYTHONPATH`` so it also
    works from a source checkout, not just an installed package.
    """
    env = dict(os.environ)
    env["PYTHONPATH"] = os.pathsep.join(p for p in sys.path if p)
    # ``-c`` rather than ``-m`` so importing the package (which pulls in this
    # module) before execution does not trigger runpy's double-import warning.
    code = f"from parsek_cdp_server.reaper import run_reaper; run_reaper({float(interval)!r})"
    return subprocess.Popen([sys.executable, "-c", code], env=env)


def _main() -> None:
    parser = argparse.ArgumentParser(description="Reap leaked parsek Chrome processes.")
    parser.add_argument("--interval", type=float, default=DEFAULT_INTERVAL,
                        help="seconds between sweeps (loop mode)")
    parser.add_argument("--once", action="store_true",
                        help="run a single sweep and exit")
    args = parser.parse_args()
    if args.once:
        killed = reap_once()
        print(f"reaped {killed} process(es)")
    else:
        run_reaper(args.interval)


if __name__ == "__main__":
    _main()
