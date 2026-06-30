"""Generated CDP package: every protocol domain.

Each domain is importable as a namespace::

    from parsek_cdp.cdp import Network
    Network.RequestWillBeSent        # an event class
    Network.ResourceType             # a type / enum
    await page.cdp.Network.enable()  # a command (target-bound)
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from . import accessibility as Accessibility
from . import animation as Animation
from . import audits as Audits
from . import autofill as Autofill
from . import backgroundservice as BackgroundService
from . import bluetoothemulation as BluetoothEmulation
from . import browser as Browser
from . import cachestorage as CacheStorage
from . import cast as Cast

# Domain namespaces (events + types + command class).
from . import console as Console
from . import css as CSS
from . import debugger as Debugger
from . import deviceaccess as DeviceAccess
from . import deviceorientation as DeviceOrientation
from . import dom as DOM
from . import domdebugger as DOMDebugger
from . import domsnapshot as DOMSnapshot
from . import domstorage as DOMStorage
from . import emulation as Emulation
from . import eventbreakpoints as EventBreakpoints
from . import extensions as Extensions
from . import fedcm as FedCm
from . import fetch as Fetch
from . import filesystem as FileSystem
from . import headlessexperimental as HeadlessExperimental
from . import heapprofiler as HeapProfiler
from . import indexeddb as IndexedDB
from . import input as Input
from . import inspector as Inspector
from . import io as IO
from . import layertree as LayerTree
from . import log as Log
from . import media as Media
from . import memory as Memory
from . import network as Network
from . import overlay as Overlay
from . import page as Page
from . import performance as Performance
from . import performancetimeline as PerformanceTimeline
from . import preload as Preload
from . import profiler as Profiler
from . import pwa as PWA
from . import runtime as Runtime
from . import schema as Schema
from . import security as Security
from . import serviceworker as ServiceWorker
from . import storage as Storage
from . import systeminfo as SystemInfo
from . import target as Target
from . import tethering as Tethering
from . import tracing as Tracing
from . import webaudio as WebAudio
from . import webauthn as WebAuthn
from .accessibility.functions import Accessibility as _Accessibility
from .animation.functions import Animation as _Animation
from .audits.functions import Audits as _Audits
from .autofill.functions import Autofill as _Autofill
from .backgroundservice.functions import BackgroundService as _BackgroundService
from .bluetoothemulation.functions import BluetoothEmulation as _BluetoothEmulation
from .browser.functions import Browser as _Browser
from .cachestorage.functions import CacheStorage as _CacheStorage
from .cast.functions import Cast as _Cast

# Command classes for the per-target aggregator below.
from .console.functions import Console as _Console
from .css.functions import CSS as _CSS
from .debugger.functions import Debugger as _Debugger
from .deviceaccess.functions import DeviceAccess as _DeviceAccess
from .deviceorientation.functions import DeviceOrientation as _DeviceOrientation
from .dom.functions import DOM as _DOM
from .domdebugger.functions import DOMDebugger as _DOMDebugger
from .domsnapshot.functions import DOMSnapshot as _DOMSnapshot
from .domstorage.functions import DOMStorage as _DOMStorage
from .emulation.functions import Emulation as _Emulation
from .eventbreakpoints.functions import EventBreakpoints as _EventBreakpoints
from .extensions.functions import Extensions as _Extensions
from .fedcm.functions import FedCm as _FedCm
from .fetch.functions import Fetch as _Fetch
from .filesystem.functions import FileSystem as _FileSystem
from .headlessexperimental.functions import (
    HeadlessExperimental as _HeadlessExperimental,
)
from .heapprofiler.functions import HeapProfiler as _HeapProfiler
from .indexeddb.functions import IndexedDB as _IndexedDB
from .input.functions import Input as _Input
from .inspector.functions import Inspector as _Inspector
from .io.functions import IO as _IO
from .layertree.functions import LayerTree as _LayerTree
from .log.functions import Log as _Log
from .media.functions import Media as _Media
from .memory.functions import Memory as _Memory
from .network.functions import Network as _Network
from .overlay.functions import Overlay as _Overlay
from .page.functions import Page as _Page
from .performance.functions import Performance as _Performance
from .performancetimeline.functions import PerformanceTimeline as _PerformanceTimeline
from .preload.functions import Preload as _Preload
from .profiler.functions import Profiler as _Profiler
from .pwa.functions import PWA as _PWA
from .runtime.functions import Runtime as _Runtime
from .schema.functions import Schema as _Schema
from .security.functions import Security as _Security
from .serviceworker.functions import ServiceWorker as _ServiceWorker
from .storage.functions import Storage as _Storage
from .systeminfo.functions import SystemInfo as _SystemInfo
from .target.functions import Target as _Target
from .tethering.functions import Tethering as _Tethering
from .tracing.functions import Tracing as _Tracing
from .webaudio.functions import WebAudio as _WebAudio
from .webauthn.functions import WebAuthn as _WebAuthn

if TYPE_CHECKING:
    from ..core.target import CDPConnection


class CDP:
    """Access every CDP domain through a single target (commands)."""

    def __init__(self, target: "CDPConnection") -> None:
        self.connection = target
        self.Console = _Console(target)
        self.Debugger = _Debugger(target)
        self.HeapProfiler = _HeapProfiler(target)
        self.Profiler = _Profiler(target)
        self.Runtime = _Runtime(target)
        self.Schema = _Schema(target)
        self.Accessibility = _Accessibility(target)
        self.Animation = _Animation(target)
        self.Audits = _Audits(target)
        self.Autofill = _Autofill(target)
        self.BackgroundService = _BackgroundService(target)
        self.BluetoothEmulation = _BluetoothEmulation(target)
        self.Browser = _Browser(target)
        self.CSS = _CSS(target)
        self.CacheStorage = _CacheStorage(target)
        self.Cast = _Cast(target)
        self.DOM = _DOM(target)
        self.DOMDebugger = _DOMDebugger(target)
        self.DOMSnapshot = _DOMSnapshot(target)
        self.DOMStorage = _DOMStorage(target)
        self.DeviceAccess = _DeviceAccess(target)
        self.DeviceOrientation = _DeviceOrientation(target)
        self.Emulation = _Emulation(target)
        self.EventBreakpoints = _EventBreakpoints(target)
        self.Extensions = _Extensions(target)
        self.FedCm = _FedCm(target)
        self.Fetch = _Fetch(target)
        self.FileSystem = _FileSystem(target)
        self.HeadlessExperimental = _HeadlessExperimental(target)
        self.IO = _IO(target)
        self.IndexedDB = _IndexedDB(target)
        self.Input = _Input(target)
        self.Inspector = _Inspector(target)
        self.LayerTree = _LayerTree(target)
        self.Log = _Log(target)
        self.Media = _Media(target)
        self.Memory = _Memory(target)
        self.Network = _Network(target)
        self.Overlay = _Overlay(target)
        self.PWA = _PWA(target)
        self.Page = _Page(target)
        self.Performance = _Performance(target)
        self.PerformanceTimeline = _PerformanceTimeline(target)
        self.Preload = _Preload(target)
        self.Security = _Security(target)
        self.ServiceWorker = _ServiceWorker(target)
        self.Storage = _Storage(target)
        self.SystemInfo = _SystemInfo(target)
        self.Target = _Target(target)
        self.Tethering = _Tethering(target)
        self.Tracing = _Tracing(target)
        self.WebAudio = _WebAudio(target)
        self.WebAuthn = _WebAuthn(target)


__all__ = [
    "CDP",
    "Console",
    "Debugger",
    "HeapProfiler",
    "Profiler",
    "Runtime",
    "Schema",
    "Accessibility",
    "Animation",
    "Audits",
    "Autofill",
    "BackgroundService",
    "BluetoothEmulation",
    "Browser",
    "CSS",
    "CacheStorage",
    "Cast",
    "DOM",
    "DOMDebugger",
    "DOMSnapshot",
    "DOMStorage",
    "DeviceAccess",
    "DeviceOrientation",
    "Emulation",
    "EventBreakpoints",
    "Extensions",
    "FedCm",
    "Fetch",
    "FileSystem",
    "HeadlessExperimental",
    "IO",
    "IndexedDB",
    "Input",
    "Inspector",
    "LayerTree",
    "Log",
    "Media",
    "Memory",
    "Network",
    "Overlay",
    "PWA",
    "Page",
    "Performance",
    "PerformanceTimeline",
    "Preload",
    "Security",
    "ServiceWorker",
    "Storage",
    "SystemInfo",
    "Target",
    "Tethering",
    "Tracing",
    "WebAudio",
    "WebAuthn",
]
