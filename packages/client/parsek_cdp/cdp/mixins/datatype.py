"""Base machinery for CDP data types.

A ``DataType`` behaves like a :func:`dataclasses.dataclass` but additionally
knows how to serialize/deserialize itself to/from the JSON shapes used on the
wire by the Chrome DevTools Protocol.

Python uses ``snake_case`` identifiers while the protocol uses ``camelCase``
keys, so a plain ``dataclasses.asdict`` is not enough -- every field carries a
:class:`FieldMeta` describing both names plus how nested values are encoded.

To avoid import cycles between domains (CDP has many cross-domain references,
some of them circular) nested enum / object types are resolved lazily at
runtime through :data:`TYPE_REGISTRY` keyed by the fully-qualified protocol
name (``"Domain.TypeName"``).
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, Callable, ClassVar, Optional, TypeVar

# Fully-qualified protocol name ("Domain.TypeName") -> python class.
# Only enums and object data types are registered; aliases to primitives or
# arrays are resolved at generation time and never need a runtime lookup.
TYPE_REGISTRY: dict[str, type] = {}

T = TypeVar("T")


def register(qualified_name: str) -> Callable[[type[T]], type[T]]:
    """Class decorator registering ``cls`` under its protocol name.

    The class's concrete type is preserved so type checkers still see its
    fields after decoration.
    """

    def deco(cls: type[T]) -> type[T]:
        TYPE_REGISTRY[qualified_name] = cls
        return cls

    return deco


@dataclass(frozen=True)
class FieldMeta:
    """Describes how a single field maps between python and the wire format.

    ``kind`` is one of ``"primitive"``, ``"enum"``, ``"object"`` or
    ``"array"``.  ``ref`` holds the fully-qualified protocol name for
    ``enum``/``object`` kinds.  ``inner`` holds the element metadata for
    ``array`` kinds.
    """

    py_name: str
    json_name: str
    optional: bool
    kind: str
    ref: Optional[str] = None
    inner: Optional["FieldMeta"] = None


def decode(meta: FieldMeta, value: Any) -> Any:
    """Convert a raw JSON ``value`` into its python representation."""
    if value is None:
        return None
    if meta.kind == "primitive":
        return value
    if meta.kind == "enum":
        return TYPE_REGISTRY[meta.ref](value)  # type: ignore[index]
    if meta.kind == "object":
        return TYPE_REGISTRY[meta.ref].from_json(value)  # type: ignore[union-attr]
    if meta.kind == "array":
        assert meta.inner is not None
        return [decode(meta.inner, v) for v in value]
    return value


def encode(meta: FieldMeta, value: Any) -> Any:
    """Convert a python ``value`` into its raw JSON representation."""
    if value is None:
        return None
    if meta.kind == "primitive":
        return value
    if meta.kind == "enum":
        return value.value if isinstance(value, Enum) else value
    if meta.kind == "object":
        return value.to_json() if isinstance(value, DataType) else value
    if meta.kind == "array":
        assert meta.inner is not None
        return [encode(meta.inner, v) for v in value]
    return value


class DataType:
    """Mixin providing JSON (de)serialization driven by :data:`__FIELDS__`."""

    __FIELDS__: ClassVar[tuple[FieldMeta, ...]] = ()

    @classmethod
    def from_json(cls, data: dict[str, Any]):
        """Build an instance from a raw protocol object.

        Tolerant of protocol drift: a field the running browser omits (e.g. a
        "required" field renamed in a newer Chrome than the bundled schema) is
        set to ``None`` instead of raising, and unknown extra keys in ``data``
        are ignored since only declared :data:`__FIELDS__` are read.
        """
        kwargs: dict[str, Any] = {}
        for fm in cls.__FIELDS__:
            raw = data.get(fm.json_name)
            kwargs[fm.py_name] = decode(fm, raw) if raw is not None else None
        return cls(**kwargs)

    def to_json(self) -> dict[str, Any]:
        """Serialize to a raw protocol object, dropping unset optionals."""
        out: dict[str, Any] = {}
        for fm in self.__FIELDS__:
            value = getattr(self, fm.py_name)
            if value is None and fm.optional:
                continue
            out[fm.json_name] = encode(fm, value)
        return out
