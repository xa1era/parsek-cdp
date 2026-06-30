#!/usr/bin/env python3
"""Code generator for the ``cdp/`` package.

Reads the Chrome DevTools Protocol JSON definitions and emits, per domain:

    cdp/{domain}/types       custom types + enums
    cdp/{domain}/functions   commands as typed methods on a domain class
    cdp/{domain}/events      event classes with handler registration

Every ``$ref`` is resolved at generation time (alias chains are followed to
their concrete shape) so the runtime only ever needs to look up enums and
object types -- which it does lazily by fully-qualified name, sidestepping the
circular cross-domain imports present in the protocol.

Usage::

    python -m parsek_cdp.generate <commit>         # download a devtools-protocol ref
    python -m parsek_cdp.generate path/to/json     # local JSON directory

The single argument is a devtools-protocol commit/tag/branch (downloaded from
GitHub) when it is not an existing directory; otherwise it is treated as a path
to a directory holding ``js_protocol.json`` + ``browser_protocol.json``. Output
goes to ``packages/client/parsek_cdp/cdp``.
"""

from __future__ import annotations

import argparse
import json
import keyword
import os
import re
import urllib.request
from typing import Optional

# this file lives at <repo>/packages/client/parsek_cdp/generate.py
CLIENT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PY_OUT = os.path.join(CLIENT, "parsek_cdp", "cdp")

#: Raw protocol JSON for a given commit/tag/branch of the upstream repo.
UPSTREAM = (
    "https://raw.githubusercontent.com/ChromeDevTools/devtools-protocol/"
    "{ref}/json/{name}"
)

PROTOCOL_FILES = ("js_protocol.json", "browser_protocol.json")


def load_domains(json_dir: str) -> list[dict]:
    """Read the two protocol JSON files from a local directory."""
    domains: list[dict] = []
    for name in PROTOCOL_FILES:
        with open(os.path.join(json_dir, name)) as fh:
            domains += json.load(fh)["domains"]
    return domains


def fetch_domains(ref: str) -> list[dict]:
    """Download the protocol JSON for a devtools-protocol commit/tag/branch."""
    domains: list[dict] = []
    for name in PROTOCOL_FILES:
        url = UPSTREAM.format(ref=ref, name=name)
        print(f"fetching {url}")
        with urllib.request.urlopen(url) as resp:  # noqa: S310 -- fixed https host
            domains += json.load(resp)["domains"]
    return domains


def classify_type(t: dict) -> str:
    """Return ``"enum"``, ``"object"`` or ``"alias"`` for a top-level type."""
    if "enum" in t:
        return "enum"
    if t.get("type") == "object" and t.get("properties"):
        return "object"
    return "alias"


# qualified name "Domain.Type" -> {"kind", "domain", "spec"}
TYPES: dict[str, dict] = {}


def index_types(domains: list[dict]) -> None:
    for d in domains:
        dom = d["domain"]
        for t in d.get("types", []):
            TYPES[f"{dom}.{t['id']}"] = {
                "kind": classify_type(t),
                "domain": dom,
                "spec": t,
            }


def qualify(ref: str, domain: str) -> str:
    return ref if "." in ref else f"{domain}.{ref}"


def snake(name: str) -> str:
    s = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s)
    return s.lower()


def py_ident(name: str) -> str:
    s = snake(name)
    if keyword.iskeyword(s) or keyword.issoftkeyword(s) or s in ("self", "cls"):
        s += "_"
    return s


def camel(name: str) -> str:
    if name and name[0].isupper():
        return name[0].lower() + name[1:]
    return name


def pascal(name: str) -> str:
    return name[0].upper() + name[1:] if name else name


def enum_member(value: str) -> str:
    s = re.sub(r"[^0-9a-zA-Z]+", "_", value).strip("_")
    if not s or s[0].isdigit():
        s = "V_" + s
    return s.upper()


def docstring(text: Optional[str], indent: str = "    ") -> str:
    if not text:
        return ""
    text = text.replace("\\", "\\\\").replace('"""', "'''")
    lines = text.split("\n")
    if len(lines) == 1:
        return f'{indent}"""{lines[0]}"""\n'
    body = "\n".join(indent + ln for ln in lines)
    return f'{indent}"""\n{body}\n{indent}"""\n'


def resolve_meta(spec: dict, domain: str) -> tuple[str, Optional[str], Optional[tuple]]:
    """Resolve a value spec to ``(kind, ref, inner)`` following alias chains."""
    if "$ref" in spec:
        q = qualify(spec["$ref"], domain)
        desc = TYPES[q]
        if desc["kind"] == "enum":
            return ("enum", q, None)
        if desc["kind"] == "object":
            return ("object", q, None)
        return resolve_meta(desc["spec"], desc["domain"])  # alias -> follow
    t = spec.get("type")
    if t == "array":
        return ("array", None, resolve_meta(spec["items"], domain))
    return ("primitive", None, None)


PY_PRIMITIVES = {
    "string": "str",
    "integer": "int",
    "number": "float",
    "boolean": "bool",
    "object": "Dict[str, Any]",
    "any": "Any",
}


class PyTypeCtx:
    """Collects cross-domain references needed for TYPE_CHECKING imports."""

    def __init__(self, domain: str):
        self.domain = domain
        self.crossrefs: set[tuple[str, str]] = set()  # (domain, TypeName)
        self.localrefs: set[str] = set()  # same-domain TypeName

    def py_type(self, spec: dict) -> str:
        if "$ref" in spec:
            q = qualify(spec["$ref"], self.domain)
            dom, tname = q.split(".", 1)
            if dom == self.domain:
                self.localrefs.add(tname)
                return tname
            self.crossrefs.add((dom, tname))
            return f"{dom}_{tname}"
        if "enum" in spec:
            return "Literal[" + ", ".join(repr(e) for e in spec["enum"]) + "]"
        t = spec["type"]
        if t == "array":
            return f"List[{self.py_type(spec['items'])}]"
        return PY_PRIMITIVES[t]


def fm_inner_literal(meta: tuple) -> str:
    kind, ref, inner = meta
    parts = [repr(""), repr(""), "False", repr(kind)]
    if ref:
        parts.append(f"ref={ref!r}")
    if inner:
        parts.append(f"inner={fm_inner_literal(inner)}")
    return "FieldMeta(" + ", ".join(parts) + ")"


def fm_literal(py_name: str, json_name: str, optional: bool, meta: tuple) -> str:
    kind, ref, inner = meta
    parts = [repr(py_name), repr(json_name), repr(optional), repr(kind)]
    if ref:
        parts.append(f"ref={ref!r}")
    if inner:
        parts.append(f"inner={fm_inner_literal(inner)}")
    return "FieldMeta(" + ", ".join(parts) + ")"


def py_crossref_imports(ctx: PyTypeCtx) -> str:
    """Explicit, aliased cross-domain type imports under ``TYPE_CHECKING``.

    Kept type-check-only so the (string, lazy) annotations resolve without
    risking the circular runtime imports present across domains.
    """
    if not ctx.crossrefs:
        return ""
    lines = ["if TYPE_CHECKING:"]
    for dom, tname in sorted(ctx.crossrefs):
        lines.append(f"    from ..{dom.lower()}.types import {tname} as {dom}_{tname}")
    return "\n".join(lines) + "\n"


def py_typing_import(ctx: PyTypeCtx, *, include_local: bool = False) -> str:
    """The ``from typing import ...`` line, including TYPE_CHECKING only if used."""
    names = ["Any", "ClassVar", "Dict", "List", "Literal", "Optional"]
    needs_tc = bool(ctx.crossrefs) or (include_local and bool(ctx.localrefs))
    if needs_tc:
        names = ["TYPE_CHECKING", *names]
    return "from typing import " + ", ".join(names)


def py_type_imports(ctx: PyTypeCtx) -> str:
    """Explicit same-domain + cross-domain type imports, all under TYPE_CHECKING.

    Annotations are lazy strings (``from __future__ import annotations``) and the
    runtime resolves nested types via the registry by name, so no type import is
    needed at runtime -- keeping them type-check-only also rules out any import
    cycle.  No star imports.
    """
    if not ctx.localrefs and not ctx.crossrefs:
        return ""
    lines = ["if TYPE_CHECKING:"]
    if ctx.localrefs:
        names = sorted(ctx.localrefs)
        if len(names) == 1:
            lines.append(f"    from .types import {names[0]}")
        else:
            lines.append("    from .types import (")
            lines += [f"        {n}," for n in names]
            lines.append("    )")
    for dom, tname in sorted(ctx.crossrefs):
        lines.append(f"    from ..{dom.lower()}.types import {tname} as {dom}_{tname}")
    return "\n".join(lines) + "\n"


def gen_py_dataclass(
    name: str,
    qualified: str,
    properties: list,
    domain: str,
    ctx: PyTypeCtx,
    base: str,
    decorators: list[str],
    description: Optional[str],
) -> str:
    """Emit a ``@dataclass`` subclass with a ``__FIELDS__`` table."""
    fields = []  # (py_name, json_name, type_str, optional, meta)
    for p in properties:
        json_name = p["name"]
        py_name = py_ident(json_name)
        type_str = ctx.py_type(p)
        optional = bool(p.get("optional"))
        meta = resolve_meta(p, domain)
        fields.append(
            (py_name, json_name, type_str, optional, meta, p.get("description"))
        )
    # required first, optionals last (dataclass ordering)
    fields.sort(key=lambda f: f[3])

    out = []
    out += decorators
    out.append(f"class {name}({base}):")
    body = docstring(description)
    for py_name, json_name, type_str, optional, meta, _desc in fields:
        if optional:
            body += f"    {py_name}: Optional[{type_str}] = None\n"
        else:
            body += f"    {py_name}: {type_str}\n"
    # __FIELDS__ table
    body += "    __FIELDS__: ClassVar[tuple] = (\n"
    for py_name, json_name, type_str, optional, meta, _desc in fields:
        body += "        " + fm_literal(py_name, json_name, optional, meta) + ",\n"
    body += "    )\n"
    if not fields:
        body = docstring(description) or "    pass\n"
        body += "    __FIELDS__: ClassVar[tuple] = ()\n"
    out.append(body)
    return "\n".join(out)


def gen_py_types(domain: dict) -> str:
    dom = domain["domain"]
    ctx = PyTypeCtx(dom)
    blocks: list[str] = []

    for t in domain.get("types", []):
        kind = classify_type(t)
        qualified = f"{dom}.{t['id']}"
        if kind == "enum":
            block = [f'@register("{qualified}")', f"class {t['id']}(str, Enum):"]
            ds = docstring(t.get("description"))
            body = ds
            for v in t["enum"]:
                body += f"    {enum_member(v)} = {v!r}\n"
            block.append(body)
            blocks.append("\n".join(block))
        elif kind == "object":
            blocks.append(
                gen_py_dataclass(
                    t["id"],
                    qualified,
                    t["properties"],
                    dom,
                    ctx,
                    base="DataType",
                    decorators=[f'@register("{qualified}")', "@dataclass"],
                    description=t.get("description"),
                )
            )
        else:  # alias -- PEP 695 lazy alias avoids evaluating cross-domain refs
            type_str = ctx.py_type(t)
            ds = ""
            if t.get("description"):
                ds = f"  # {t['description'].splitlines()[0]}"
            blocks.append(f"type {t['id']} = {type_str}{ds}\n")

    header = [
        '"""Custom types and enums for the {} domain (generated)."""'.format(dom),
        "from __future__ import annotations",
        "",
        "from dataclasses import dataclass",
        "from enum import Enum",
        py_typing_import(ctx),
        "",
        "from ..mixins.datatype import DataType, FieldMeta, register",
        "",
        py_crossref_imports(ctx),
        "",
    ]
    names = sorted(t["id"] for t in domain.get("types", []))
    all_block = "__all__ = [" + ", ".join(f'"{n}"' for n in names) + "]\n"
    body = "\n".join(header) + "\n\n".join(blocks)
    return body.rstrip("\n") + "\n\n" + all_block


def gen_py_events(domain: dict) -> str:
    dom = domain["domain"]
    ctx = PyTypeCtx(dom)
    blocks: list[str] = []
    for e in domain.get("events", []):
        qualified = f"{dom}.{e['name']}"
        name = pascal(e["name"])
        blocks.append(
            gen_py_dataclass(
                name,
                qualified,
                e.get("parameters", []),
                dom,
                ctx,
                base="Event",
                decorators=[f'@register_event("{qualified}")', "@dataclass"],
                description=e.get("description"),
            )
        )
    header = [
        '"""Events for the {} domain (generated)."""'.format(dom),
        "from __future__ import annotations",
        "",
        "from dataclasses import dataclass",
        py_typing_import(ctx, include_local=True),
        "",
        "from ..mixins.datatype import FieldMeta",
        "from ..mixins.event import Event, register_event",
        "",
        py_type_imports(ctx),
        "",
    ]
    names = sorted(pascal(e["name"]) for e in domain.get("events", []))
    all_block = "__all__ = [" + ", ".join(f'"{n}"' for n in names) + "]\n"
    if not blocks:
        blocks = ["# This domain defines no events.\n"]
    body = "\n".join(header) + "\n\n".join(blocks)
    return body.rstrip("\n") + "\n\n" + all_block


def gen_py_functions(domain: dict) -> str:
    dom = domain["domain"]
    ctx = PyTypeCtx(dom)
    return_classes: list[str] = []
    methods: list[str] = []

    for c in domain.get("commands", []):
        method_name = f"{dom}.{c['name']}"
        py_method = py_ident(c["name"])
        params = c.get("parameters", [])
        returns = c.get("returns", [])

        # parameters sorted: required first so the signature is valid
        sig_params = []
        for p in params:
            json_name = p["name"]
            pid = py_ident(json_name)
            tstr = ctx.py_type(p)
            optional = bool(p.get("optional"))
            meta = resolve_meta(p, dom)
            sig_params.append((pid, json_name, tstr, optional, meta))
        sig_params.sort(key=lambda x: x[3])

        # return type
        ret_type = "None"
        ret_cls_name = None
        if returns:
            ret_cls_name = f"{pascal(c['name'])}Return"
            ret_type = ret_cls_name
            return_classes.append(
                gen_py_dataclass(
                    ret_cls_name,
                    f"{method_name}.return",
                    returns,
                    dom,
                    ctx,
                    base="DataType",
                    decorators=["@dataclass"],
                    description=f"Return value of :meth:`{dom}.{py_method}`.",
                )
            )

        # signature
        # annotations are lazy strings thanks to ``from __future__ import
        # annotations``, so cross-domain names only imported under TYPE_CHECKING
        # are never evaluated at runtime.
        sig = "self"
        if sig_params:
            sig += ", *"
            for pid, _jn, tstr, optional, _m in sig_params:
                if optional:
                    sig += f", {pid}: Optional[{tstr}] = None"
                else:
                    sig += f", {pid}: {tstr}"

        body = f"    async def {py_method}({sig}) -> {ret_type}:\n"
        # docstring with param descriptions
        doc_lines = []
        if c.get("description"):
            doc_lines.append(c["description"])
        if c.get("deprecated"):
            doc_lines.append("\n.. deprecated::")
        for p in params:
            d = p.get("description", "")
            doc_lines.append(f":param {py_ident(p['name'])}: {d}".rstrip())
        if doc_lines:
            body += docstring("\n".join(doc_lines), indent="        ")
        body += "        _params: Dict[str, Any] = {}\n"
        for pid, json_name, _tstr, optional, meta in sig_params:
            enc = f"encode({fm_inner_literal(meta)}, {pid})"
            if optional:
                body += f"        if {pid} is not None:\n"
                body += f"            _params[{json_name!r}] = {enc}\n"
            else:
                body += f"        _params[{json_name!r}] = {enc}\n"
        body += f"        _result = await self._target.send({method_name!r}, _params)\n"
        if ret_cls_name:
            body += f"        return {ret_cls_name}.from_json(_result)\n"
        else:
            body += "        return None\n"
        methods.append(body)

    header = [
        '"""Commands for the {} domain (generated)."""'.format(dom),
        "from __future__ import annotations",
        "",
        "from dataclasses import dataclass",
        py_typing_import(ctx, include_local=True),
        "",
        "from ..mixins.datatype import DataType, FieldMeta, encode",
        "",
        py_type_imports(ctx),
        "",
    ]

    cls = [
        f"class {dom}:",
        f'    """Commands of the {dom} domain, bound to a target."""',
        "",
        "    def __init__(self, target: Any) -> None:",
        "        self._target = target",
        "",
    ]
    if not methods:
        cls.append("    # This domain defines no commands.\n")
    out = "\n".join(header) + "\n\n".join(return_classes)
    if return_classes:
        out += "\n\n"
    out += "\n".join(cls) + "\n\n" + "\n".join(methods)
    return out


def gen_py_domain_init(domain: dict) -> str:
    dom = domain["domain"]
    return (
        f'"""The {dom} CDP domain (generated).\n\n'
        f"Importing ``{dom}`` from ``parsek_cdp.cdp`` gives a namespace with this\n"
        f"domain's events and types as attributes (``{dom}.SomeEvent`` /\n"
        f"``{dom}.SomeType``); commands run on a target via ``page.cdp.{dom}``.\n"
        '"""\n'
        "from . import events, functions, types\n"
        f"from .functions import {dom}\n"
        "from .events import *  # noqa: F401,F403 -- expose events on the namespace\n"
        "from .types import *  # noqa: F401,F403 -- expose types on the namespace\n\n"
        f"#: Protocol domain name (used by features that declare ``domains=({dom},)``).\n"
        f'DOMAIN = "{dom}"\n\n'
        '__all__ = ["events", "functions", "types", "' + dom + '", "DOMAIN"]\n'
    )


def gen_py_cdp_init(domains: list[dict]) -> str:
    lines = [
        '"""Generated CDP package: every protocol domain.',
        "",
        "Each domain is importable as a namespace::",
        "",
        "    from parsek_cdp.cdp import Network",
        "    Network.RequestWillBeSent        # an event class",
        "    Network.ResourceType             # a type / enum",
        "    await page.cdp.Network.enable()  # a command (target-bound)",
        '"""',
        "",
        "from __future__ import annotations",
        "",
        "from typing import TYPE_CHECKING",
        "",
    ]

    # Imports are emitted in isort order (alphabetical by module name). The
    # explanatory comments stay attached above the first protocol domain's
    # import, which is where they land once the block is sorted.
    first_mod = domains[0]["domain"].lower()
    sorted_doms = sorted(domains, key=lambda d: d["domain"].lower())

    for d in sorted_doms:
        mod = d["domain"].lower()
        if mod == first_mod:
            lines.append("")
            lines.append("# Domain namespaces (events + types + command class).")
        lines.append(f"from . import {mod} as {d['domain']}")
    for d in sorted_doms:
        mod = d["domain"].lower()
        if mod == first_mod:
            lines.append("")
            lines.append("# Command classes for the per-target aggregator below.")
        line = f"from .{mod}.functions import {d['domain']} as _{d['domain']}"
        if len(line) > 88:  # black wraps over-long single imports
            lines.append(f"from .{mod}.functions import (")
            lines.append(f"    {d['domain']} as _{d['domain']},")
            lines.append(")")
        else:
            lines.append(line)

    lines.append("")
    lines.append("if TYPE_CHECKING:")
    lines.append("    from ..core.target import CDPConnection")
    lines.append("")
    lines.append("")
    lines.append("class CDP:")
    lines.append(
        '    """Access every CDP domain through a single target (commands)."""'
    )
    lines.append("")
    lines.append('    def __init__(self, target: "CDPConnection") -> None:')
    lines.append("        self.connection = target")
    for d in domains:
        lines.append(f"        self.{d['domain']} = _{d['domain']}(target)")
    lines.append("")
    lines.append("")
    names = ['"CDP"'] + [f'"{d["domain"]}"' for d in domains]
    lines.append("__all__ = [")
    for n in names:
        lines.append(f"    {n},")
    lines.append("]")
    return "\n".join(lines) + "\n"


# ============================================================================ #
# Driver
# ============================================================================ #


def write(path: str, content: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as fh:
        fh.write(content)


def generate(domains: list[dict]) -> None:
    """Emit the whole ``cdp/`` package from the parsed protocol domains."""
    index_types(domains)

    for d in domains:
        dom = d["domain"].lower()
        write(os.path.join(PY_OUT, dom, "types.py"), gen_py_types(d))
        write(os.path.join(PY_OUT, dom, "events.py"), gen_py_events(d))
        write(os.path.join(PY_OUT, dom, "functions.py"), gen_py_functions(d))
        write(os.path.join(PY_OUT, dom, "__init__.py"), gen_py_domain_init(d))

    write(os.path.join(PY_OUT, "__init__.py"), gen_py_cdp_init(domains))

    print(f"Generated {len(domains)} domains -> {PY_OUT}")


def main(argv: Optional[list[str]] = None) -> None:
    parser = argparse.ArgumentParser(
        prog="python -m parsek_cdp.generate",
        description="Generate the cdp/ package from a Chrome DevTools Protocol "
        "revision (downloaded by commit/tag/branch) or a local JSON directory.",
    )
    parser.add_argument(
        "source",
        help="devtools-protocol commit/tag/branch to download, or a path to a "
        "local directory holding js_protocol.json + browser_protocol.json.",
    )
    args = parser.parse_args(argv)

    if os.path.isdir(args.source):
        domains = load_domains(args.source)
    else:
        domains = fetch_domains(args.source)

    generate(domains)


if __name__ == "__main__":
    main()
