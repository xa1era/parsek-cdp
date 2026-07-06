"""Launching a browser process and locating its DevTools websocket.

The launcher is the lowest server layer: it knows how to start Chrome/Chromium
with the right flags, wait until its DevTools endpoint is up, and read the
browser-level websocket url from ``/json/version``.  Lifecycle decisions
(restart on crash, etc.) belong to :class:`~parsek_cdp_server.supervisor`, which
drives this class.
"""

from __future__ import annotations

import asyncio
import contextlib
import json
import os
import random
import shutil
import tempfile
import urllib.error
import urllib.request
from pathlib import Path
from typing import List, Optional

import psutil
from parsek_cdp.core.browser import LaunchOptions

#: Env var naming *directories* to search for browser binaries,
#: ``os.pathsep``-separated (like ``PATH``), e.g. ``/opt/browsers/chrome:/opt/browsers/brave``.
#: Each directory is walked recursively; every executable file whose name is a
#: known Chromium browser (see :data:`_BROWSER_NAMES`) becomes a candidate, and
#: each launch runs a randomly chosen one -- a cheap way to spread load (and
#: fingerprints) across several installed browsers.  When unset,
#: :data:`_KNOWN_PATHS` is searched as the default.
CHROMES_PATH_ENV = "PARSEK_CHROMES_PATH"

#: Prefix of the temp profile directories the launcher creates (``tempfile``
#: prefix).  It doubles as an ownership *marker*: the reaper recognises a browser
#: as parsek-launched by finding ``--user-data-dir=<...PROFILE_PREFIX...>`` in its
#: argv, so it only ever kills processes we started.
PROFILE_PREFIX = "parsek-cdp-"

#: Recognised Chromium-browser executable names (matched case-insensitively, with
#: any ``.exe`` suffix stripped).  Restricting the recursive search to these
#: avoids picking up helper binaries (``chrome_crashpad_handler``, ``chrome_sandbox``).
_BROWSER_NAMES = frozenset(
    {
        "chrome",
        "google-chrome",
        "google-chrome-stable",
        "chromium",
        "chromium-browser",
        "msedge",
        "microsoft-edge",
        "microsoft-edge-stable",
        "brave",
        "brave-browser",
        "vivaldi",
        "vivaldi-bin",
        "opera",
    }
)

#: Default directories searched when :data:`CHROMES_PATH_ENV` is unset.  Any
#: Chromium-based browser works -- they all speak the same DevTools Protocol.
#: Non-existent dirs are skipped, so listing every platform here is harmless.
_KNOWN_PATHS = (
    # Linux
    "/usr/bin",
    "/usr/local/bin",
    "/opt",
    "/snap/bin",
    # macOS
    "/Applications/Google Chrome.app/Contents/MacOS",
    "/Applications/Chromium.app/Contents/MacOS",
    "/Applications/Microsoft Edge.app/Contents/MacOS",
    "/Applications/Brave Browser.app/Contents/MacOS",
    # Windows
    r"C:\Program Files\Google\Chrome\Application",
    r"C:\Program Files (x86)\Google\Chrome\Application",
    r"C:\Program Files (x86)\Microsoft\Edge\Application",
    r"C:\Program Files\BraveSoftware\Brave-Browser\Application",
)

#: Executable names tried on ``PATH`` as a last resort when neither
#: :attr:`LaunchOptions.executable` nor a directory search yields a binary.
_CANDIDATES = (
    "google-chrome",
    "google-chrome-stable",
    "chromium",
    "chromium-browser",
    "microsoft-edge",
    "microsoft-edge-stable",
    "brave-browser",
    "brave",
    "chrome",
)


def _is_browser(filename: str) -> bool:
    name = filename[:-4] if filename.lower().endswith(".exe") else filename
    return name.lower() in _BROWSER_NAMES


def _find_in_dirs(dirs: List[str]) -> List[str]:
    """Collect browser executables directly under ``dirs`` (non-recursive)."""
    found: List[str] = []
    for directory in dirs:
        directory = directory.strip()
        if not directory or not os.path.isdir(directory):
            continue
        for filename in os.listdir(directory):
            if not _is_browser(filename):
                continue
            full = os.path.join(directory, filename)
            if os.path.isfile(full) and os.access(full, os.X_OK):
                found.append(full)
    return found


def _detect_executable() -> str:
    """Pick a Chromium-based binary, or raise if none is available.

    Precedence: a random browser executable found directly in the directories
    listed in :data:`CHROMES_PATH_ENV` (defaulting to :data:`_KNOWN_PATHS`),
    else the first :data:`_CANDIDATES` name resolvable on ``PATH``.
    """
    raw = os.environ.get(CHROMES_PATH_ENV)
    search_dirs = raw.split(os.pathsep) if raw else list(_KNOWN_PATHS)
    matches = _find_in_dirs(search_dirs)
    if matches:
        return random.choice(matches)
    for name in _CANDIDATES:
        resolved = shutil.which(name)
        if resolved:
            return resolved
    raise FileNotFoundError(
        f"no Chrome/Chromium executable found; set {CHROMES_PATH_ENV} "
        "(os.pathsep-separated directories to search) or LaunchOptions.executable"
    )


class ChromeLauncher:
    """Spawn a browser process and expose its browser-level websocket url.

    Responsibilities:

    * build the argv (``--remote-debugging-port``, ``--user-data-dir``,
      ``--headless=new``, ``--no-first-run``, ...);
    * start the subprocess; with ``port == 0`` Chrome writes the port it chose to
      the ``DevToolsActivePort`` file in the profile dir, which we poll;
    * poll ``/json/version`` until ``webSocketDebuggerUrl`` is available;
    * expose :attr:`pid` and :attr:`ws_url`; provide :meth:`terminate`.
    """

    def __init__(self, options: Optional[LaunchOptions] = None) -> None:
        self.options = options or LaunchOptions()
        self.pid: Optional[int] = None
        self.ws_url: Optional[str] = None
        self._proc: Optional[asyncio.subprocess.Process] = None
        #: Temp profile dir we created (and must clean up); None if caller supplied one.
        self._owned_user_data_dir: Optional[str] = None

    def _resolve_user_data_dir(self) -> str:
        if self.options.user_data_dir is not None:
            return self.options.user_data_dir
        path = tempfile.mkdtemp(prefix=PROFILE_PREFIX)
        self._owned_user_data_dir = path
        return path

    def _build_argv(self, user_data_dir: str) -> List[str]:
        executable = self.options.executable or _detect_executable()
        argv = [executable, f"--remote-debugging-port={self.options.port}"]
        if self.options.use_default_args:
            argv += [
                f"--user-data-dir={user_data_dir}",
                "--no-first-run",
                "--no-default-browser-check",
                "--disable-background-networking",
                "--disable-popup-blocking",
                "--remote-allow-origins=*",
            ]
            if self.options.headless:
                argv += ["--headless=new", "--disable-gpu"]
        argv += self.options.extra_args
        return argv

    async def launch(self) -> str:
        """Start the browser and return its browser-level websocket url."""
        user_data_dir = self._resolve_user_data_dir()
        argv = self._build_argv(user_data_dir)
        self._proc = await asyncio.create_subprocess_exec(
            *argv,
            stdout=asyncio.subprocess.DEVNULL,
            stderr=asyncio.subprocess.DEVNULL,
        )
        self.pid = self._proc.pid
        try:
            port = await self._await_devtools_port(Path(user_data_dir))
            self.ws_url = await self._await_ws_url(port)
        except Exception:
            await self.terminate()
            raise
        return self.ws_url

    async def _await_devtools_port(
        self, user_data_dir: Path, *, timeout: float = 30.0
    ) -> int:
        """Wait for Chrome to write the chosen port to ``DevToolsActivePort``.

        The file's first line is the port; it appears once the DevTools endpoint
        is listening, so its presence doubles as a readiness signal.  When a
        fixed port was requested we still wait for the file to confirm liveness.
        """
        active_port_file = user_data_dir / "DevToolsActivePort"
        loop = asyncio.get_running_loop()
        deadline = loop.time() + timeout
        while True:
            if self._proc is not None and self._proc.returncode is not None:
                raise RuntimeError(
                    f"browser exited during startup (code {self._proc.returncode})"
                )
            try:
                first_line = active_port_file.read_text().splitlines()[0]
                return int(first_line)
            except (FileNotFoundError, IndexError, ValueError):
                pass
            if loop.time() >= deadline:
                raise TimeoutError("browser did not open its DevTools port in time")
            await asyncio.sleep(0.05)

    async def _await_ws_url(self, port: int, *, timeout: float = 10.0) -> str:
        """Poll ``/json/version`` until ``webSocketDebuggerUrl`` is served."""
        endpoint = f"http://127.0.0.1:{port}/json/version"
        loop = asyncio.get_running_loop()
        deadline = loop.time() + timeout
        while True:
            try:
                info = await asyncio.to_thread(self._read_json, endpoint)
                return info["webSocketDebuggerUrl"]
            except (urllib.error.URLError, KeyError, ConnectionError, OSError):
                if loop.time() >= deadline:
                    raise TimeoutError(f"{endpoint} did not become available")
                await asyncio.sleep(0.05)

    @staticmethod
    def _read_json(url: str) -> dict:
        with urllib.request.urlopen(url, timeout=2) as resp:
            return json.loads(resp.read())

    def is_alive(self) -> bool:
        """Whether the browser process is still running (used by the supervisor)."""
        if self._proc is not None and self._proc.returncode is not None:
            return False
        if self.pid is None:
            return False
        return psutil.pid_exists(self.pid)

    async def terminate(self, *, timeout: float = 5.0) -> None:
        """Terminate the browser process tree gracefully, then kill survivors.

        Chrome frequently re-execs or forks the real browser into a *separate*
        process (headed mode, wrapper launch scripts, the relauncher), after which
        the process we spawned has already exited.  Signalling only that direct
        child would then leave the real browser running as an orphan, so we walk
        the whole tree rooted at :attr:`pid` (parent + recursive children) and
        SIGTERM it, escalating to SIGKILL for anything still alive after the grace
        period.
        """
        procs = self._process_tree()
        for p in procs:
            with _suppress_lookup():
                p.terminate()  # SIGTERM
        # psutil.wait_procs is blocking, so run it off the event loop.
        _gone, alive = await asyncio.to_thread(
            psutil.wait_procs, procs, timeout=timeout
        )
        for p in alive:
            with _suppress_lookup():
                p.kill()  # SIGKILL
        # Reap the asyncio child so its transport doesn't warn about a lost process.
        proc = self._proc
        if proc is not None and proc.returncode is None:
            with contextlib.suppress(ProcessLookupError):
                await proc.wait()
        self._cleanup_profile()

    def _process_tree(self) -> List[psutil.Process]:
        """The browser process and all its descendants (empty if already gone)."""
        if self.pid is None:
            return []
        try:
            parent = psutil.Process(self.pid)
        except psutil.NoSuchProcess:
            return []
        try:
            children = parent.children(recursive=True)
        except psutil.NoSuchProcess:
            children = []
        return [parent, *children]

    def _cleanup_profile(self) -> None:
        if self._owned_user_data_dir is not None:
            shutil.rmtree(self._owned_user_data_dir, ignore_errors=True)
            self._owned_user_data_dir = None


class _suppress_lookup:
    """Context manager swallowing "process already gone" errors.

    Covers both :class:`ProcessLookupError` (from ``asyncio``/``os`` signalling)
    and :class:`psutil.NoSuchProcess` (from the process-tree walk), which race
    naturally: a process can exit between being listed and being signalled.
    """

    def __enter__(self) -> "_suppress_lookup":
        return self

    def __exit__(self, exc_type, exc, tb) -> bool:
        return exc_type is not None and issubclass(
            exc_type, (ProcessLookupError, psutil.NoSuchProcess)
        )
