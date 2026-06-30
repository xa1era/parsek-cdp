"""Attach classes defined in modules onto a class, turning it into a namespace.

Used by features so the feature *class* doubles as its namespace::

    from parsek_cdp.features import RequestListener
    RequestListener.RequestSent     # event
    RequestListener.RequestData     # wire type
    RequestListener.Request         # view type

Only classes *defined in* the given modules are attached (cross-module imports
are skipped via ``__module__``), and existing attributes are never overwritten.

(CDP domains use a different mechanism -- module-level ``import *`` -- because a
domain's public handle is its module, not a class.)
"""

from __future__ import annotations

from types import ModuleType


def attach_namespace(target_cls: type, *modules: ModuleType) -> None:
    """Attach every class defined in ``modules`` onto ``target_cls`` by name."""
    for module in modules:
        for name, obj in vars(module).items():
            if name.startswith("_") or not isinstance(obj, type):
                continue
            if obj.__module__ != module.__name__:
                continue  # imported from elsewhere, not defined here
            if not hasattr(target_cls, name):
                setattr(target_cls, name, obj)
