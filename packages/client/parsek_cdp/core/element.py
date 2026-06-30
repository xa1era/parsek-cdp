"""A DOM element handle bound to a :class:`~parsek_cdp.core.frames.Frame`.

Returned by :meth:`Frame.select` / :meth:`Frame.select_all`.  Wraps a DOM
``nodeId`` and offers the actions you usually want on a node: real pointer
:meth:`click` / :meth:`mouse_click` (dispatched through the ``Input`` domain at
the node's on-screen centre), keyboard input (:meth:`fill` / :meth:`type` /
:meth:`press`), a :meth:`is_visible` check, text/attribute reads, and a generic
:meth:`apply` to run a JS function with the node as ``this``.
"""

from __future__ import annotations

import asyncio
import functools
import inspect
from typing import TYPE_CHECKING, Any

from ..cdp import DOM, Runtime
from ..cdp.input.types import MouseButton
from .frame import Frame
from .target import ProtocolError

if TYPE_CHECKING:
    from ..cdp import CDP

_KEY_DEFINITIONS: dict[str, tuple[int, str, str]] = {
    "Enter": (13, "Enter", "\r"),
    "Tab": (9, "Tab", "\t"),
    "Backspace": (8, "Backspace", ""),
    "Delete": (46, "Delete", ""),
    "Escape": (27, "Escape", ""),
    "Space": (32, "Space", " "),
    "ArrowLeft": (37, "ArrowLeft", ""),
    "ArrowUp": (38, "ArrowUp", ""),
    "ArrowRight": (39, "ArrowRight", ""),
    "ArrowDown": (40, "ArrowDown", ""),
    "Home": (36, "Home", ""),
    "End": (35, "End", ""),
    "PageUp": (33, "PageUp", ""),
    "PageDown": (34, "PageDown", ""),
}


def _dom_target(args, kwargs):
    """Find the :class:`Target` to drive DOM on, from a ``@with_dom`` call's args.

    Both shapes a ``@with_dom`` method can take are covered: an instance method
    (``self`` is an :class:`Element`) and the ``get_node`` classmethod (``cls``
    plus a ``frame``, passed positionally or by keyword).
    """
    for obj in (*args, *kwargs.values()):
        if isinstance(obj, Element):
            return obj._frame.target
        if isinstance(obj, Frame):
            return obj.target
    raise TypeError("@with_dom needs an Element or Frame argument")


def _dom_enabled(args, kwargs):
    """Return the ``domain_enabled(DOM)`` context for a ``@with_dom`` call."""
    target = _dom_target(args, kwargs)
    return target.domain_enabled(target.cdp.DOM)


def with_dom(method):
    """Run a DOM-touching method with the ``DOM`` domain enabled.

    DOM starts disabled (see :meth:`Target.connect`), so any method that issues
    ``DOM.*`` commands must enable it first.  Decorating with ``@with_dom`` does
    that automatically; nested decorated calls are a no-op because
    :meth:`Target.domain_enabled` only flips a domain that is off.  Works for
    coroutine methods, async-generator methods (those that ``yield``), and the
    ``get_node`` classmethod (place ``@with_dom`` *below* ``@classmethod``).

    Note ``getDocument`` is *not* done here -- it reassigns the whole node-id
    map, so :meth:`Element.refresh` calls it only when it actually needs to mint
    a fresh ``nodeId`` (see there).
    """
    if inspect.isasyncgenfunction(method):

        @functools.wraps(method)
        async def gen_wrapper(*args, **kwargs):
            async with _dom_enabled(args, kwargs):
                async for item in method(*args, **kwargs):
                    yield item

        return gen_wrapper

    @functools.wraps(method)
    async def wrapper(*args, **kwargs):
        async with _dom_enabled(args, kwargs):
            return await method(*args, **kwargs)

    return wrapper


class Element:
    """A handle to a single DOM node in a frame."""

    _object_id: Runtime.RemoteObjectId | None

    def __init__(self, node_info: DOM.Node, frame: Frame) -> None:
        self._node = node_info
        self._frame = frame
        self._object_id = None
        self._children: dict[DOM.BackendNodeId, Element] = {}
        self._generation = -1

    @property
    def text(self):
        return "".join(
            [self._node.node_value]
            + [child.text for child in self.children if child._node.node_type == 3]
        )

    @property
    def attributes(self):
        attrs = self._node.attributes or []
        keys = attrs[0::2]
        values = attrs[1::2]
        return dict(zip(keys, values))

    @property
    def id(self):
        return self._node.node_id

    @property
    def backend_id(self):
        return self._node.backend_node_id

    @property
    def children(self):
        return list(self._children.values())

    @property
    def shadow_roots(self):
        roots = [
            Element(sh_root, self._frame) for sh_root in self._node.shadow_roots or []
        ]
        for child in self.children:
            roots.extend(child.shadow_roots)
        return roots

    @classmethod
    async def get_node(
        cls,
        frame: Frame,
        *,
        node_id: DOM.NodeId | None = None,
        backend_node_id: DOM.BackendNodeId | None = None,
        object_id: Runtime.RemoteObjectId | None = None,
    ):
        kwargs = dict(
            node_id=node_id,
            backend_node_id=backend_node_id,
            object_id=object_id,
        )
        kwargs = dict(filter(lambda row: row[1] is not None, kwargs.items()))
        if len(kwargs.values()) == 0:
            raise ValueError("No identifier provided")
        node = await frame.cdp.DOM.describe_node(
            **kwargs,  # pyright: ignore[reportArgumentType]
            depth=-1,
            pierce=True,
        )
        return node.node

    @classmethod
    async def describe_node(
        cls,
        frame: Frame,
        *,
        node_id: DOM.NodeId | None = None,
        backend_node_id: DOM.BackendNodeId | None = None,
        object_id: Runtime.RemoteObjectId | None = None,
    ):
        node = await cls.get_node(
            frame,
            node_id=node_id,
            backend_node_id=backend_node_id,
            object_id=object_id,
        )
        return cls._from_node(node, frame)

    @classmethod
    def _from_node(cls, node: DOM.Node, frame: Frame) -> "Element":
        """Build an :class:`Element` tree from an already-fetched node.

        ``get_node`` uses ``depth=-1``, so ``node`` already carries its whole
        subtree in ``node.children`` -- no further CDP round-trips are needed.
        """
        instance = cls(node, frame)
        for child in node.children or []:
            instance._children[child.backend_node_id] = cls._from_node(child, frame)
        return instance

    @property
    def _cdp(self) -> "CDP":
        return self._frame.cdp

    @with_dom
    async def refresh(self):
        """Re-read this node's subtree and ensure it carries a live ``nodeId``.

        ``backendNodeId`` is stable across ``DOM.enable``/``disable``; ``nodeId``
        is not.  ``describeNode(backendNodeId)`` doubles as the validity check:
        it returns the live ``nodeId`` when the node is currently pushed to the
        frontend, or ``0`` when it isn't (e.g. a ``disable`` wiped the node map).
        Only in that ``0`` case do we pay for ``getDocument`` (to repopulate the
        map -- which ``push`` requires) + ``pushNodesByBackendIdsToFrontend`` (to
        mint a fresh id); a still-live id needs neither.
        """
        cdp = self._cdp
        if self._generation != self._frame._dom_generation:
            self._object_id = None
            await cdp.DOM.get_document(depth=0)
            node_id = (
                await cdp.DOM.push_nodes_by_backend_ids_to_frontend(
                    backend_node_ids=[self.backend_id]
                )
            ).node_ids[0]
        else:
            node_id = self.id
        self._node = (
            await cdp.DOM.describe_node(node_id=node_id, depth=-1, pierce=True)
        ).node
        self._generation = self._frame._dom_generation
        self._children.clear()
        for child in self._node.children or []:
            self._children[child.backend_node_id] = self._from_node(child, self._frame)

    @with_dom
    async def query_selector(self, selector: str) -> Element | None:
        try:
            await self.refresh()
            data = await self._cdp.DOM.query_selector(
                node_id=self.id, selector=selector
            )
            return await self.describe_node(node_id=data.node_id, frame=self._frame)
        except ProtocolError:
            return None

    @with_dom
    async def query_selector_all(self, selector: str):
        await self.refresh()
        data = await self._cdp.DOM.query_selector_all(
            node_id=self.id, selector=selector
        )
        for node_id in data.node_ids:
            yield await self.describe_node(node_id=node_id, frame=self._frame)

    @with_dom
    async def scroll_into_view(self) -> None:
        """Best-effort scroll so the node is on screen (ignored if it fails)."""
        try:
            await self._cdp.DOM.scroll_into_view_if_needed(
                backend_node_id=self.backend_id
            )
        except Exception:
            pass

    @with_dom
    async def center(self) -> tuple[float, float]:
        """Return the viewport ``(x, y)`` of the node's content-box centre."""
        await self.refresh()
        model = (
            await self._cdp.DOM.get_box_model(backend_node_id=self.backend_id)
        ).model
        quad = model.content  # [x1,y1, x2,y2, x3,y3, x4,y4]
        xs = quad[0::2]
        ys = quad[1::2]
        return sum(xs) / len(xs), sum(ys) / len(ys)

    @with_dom
    async def mouse_click(
        self, button: MouseButton = MouseButton.LEFT, *, count: int = 1
    ) -> None:
        """Click the element with a real pointer sequence (move, press, release)."""
        await self.scroll_into_view()
        x, y = await self.center()
        inp = self._cdp.Input
        await inp.dispatch_mouse_event(type_="mouseMoved", x=x, y=y)
        await inp.dispatch_mouse_event(
            type_="mousePressed", x=x, y=y, button=button, click_count=count
        )
        await inp.dispatch_mouse_event(
            type_="mouseReleased", x=x, y=y, button=button, click_count=count
        )

    click = mouse_click

    @with_dom
    async def focus(self) -> None:
        """Give the node keyboard focus (so key/text events land on it)."""
        await self._cdp.DOM.focus(backend_node_id=self.backend_id)

    async def fill(self, value: str) -> None:
        """Focus the node, clear any existing value, then enter ``value``.

        Works for both form controls (``<input>`` / ``<textarea>``) and
        ``contenteditable`` nodes.  Mirrors Playwright's ``fill``: fast (one
        ``insertText`` rather than per-key events) and fires an ``input`` event,
        so reactive frameworks pick up the change.
        """
        await self.focus()
        await self.apply(
            "function () {"
            "  if (this.value !== undefined) { this.value = ''; }"
            "  else if (this.isContentEditable) { this.textContent = ''; }"
            "  this.dispatchEvent(new Event('input', { bubbles: true }));"
            "}"
        )
        if value:
            await self._cdp.Input.insert_text(text=value)

    async def type(self, text: str, *, delay: float = 0) -> None:
        """Type ``text`` one character at a time, dispatching real key events.

        Slower than :meth:`fill` but exercises ``keydown`` / ``keyup`` handlers
        (autocomplete, key-by-key validation, ...).  ``delay`` is the pause in
        seconds between characters.  Does not focus or clear -- call
        :meth:`focus` / :meth:`fill` first if needed.
        """
        inp = self._cdp.Input
        for char in text:
            await inp.dispatch_key_event(type_="keyDown", text=char, key=char)
            await inp.dispatch_key_event(type_="keyUp", key=char)
            if delay:
                await asyncio.sleep(delay)

    async def press(self, key: str) -> None:
        """Press a single key, e.g. ``"Enter"``, ``"Tab"`` or a character.

        Named keys (see :data:`_KEY_DEFINITIONS`) carry their virtual-key code;
        any other single character is sent as plain text.
        """
        inp = self._cdp.Input
        if key in _KEY_DEFINITIONS:
            vk, code, text = _KEY_DEFINITIONS[key]
            down: dict[str, Any] = {
                "key": key,
                "code": code,
                "windows_virtual_key_code": vk,
            }
            if text:
                down["text"] = text
            await inp.dispatch_key_event(type_="keyDown", **down)
            await inp.dispatch_key_event(type_="keyUp", key=key, code=code)
        else:
            await inp.dispatch_key_event(type_="keyDown", text=key, key=key)
            await inp.dispatch_key_event(type_="keyUp", key=key)

    @with_dom
    async def is_visible(self) -> bool:
        """Whether the node is rendered and visually perceivable.

        Visible means it has a non-empty layout box (so ``display: none``,
        detached and zero-size nodes are excluded) and is not hidden by
        ``visibility`` or ``opacity: 0``.  Never raises -- a detached/unstylable
        node is reported as not visible.
        """
        try:
            model = (await self._cdp.DOM.get_box_model(node_id=self.id)).model
        except Exception:
            return False  # no layout box: display:none, detached, or not rendered
        if model is None or not model.width or not model.height:
            return False
        try:
            async with self._frame.target.domain_enabled(self._frame.target.cdp.CSS):
                styles = (
                    await self._cdp.CSS.get_computed_style_for_node(node_id=self.id)
                ).computed_style
        except Exception:
            return True
        props = {p.name: p.value for p in styles}
        if props.get("visibility") in ("hidden", "collapse"):
            return False
        try:
            if float(props.get("opacity", "1")) <= 0:
                return False
        except ValueError:
            pass
        return True

    @with_dom
    async def _object(self) -> Runtime.RemoteObjectId | None:
        """Resolve (once) a JS object id for this node, for ``callFunctionOn``."""
        if self._object_id is None:
            resolved = await self._cdp.DOM.resolve_node(node_id=self.id)
            self._object_id = resolved.object.object_id
        return self._object_id

    async def apply(self, function_declaration: str) -> Any:
        """Call ``function_declaration`` (e.g. ``"el => el.click()"``) on the node."""
        result = await self._cdp.Runtime.call_function_on(
            function_declaration=function_declaration,
            object_id=await self._object(),
            return_by_value=True,
        )
        return result.result.value if result.result else None

    def __str__(self) -> str:
        return f"<Element node={self.id} back_id={self.backend_id}>"

    __repr__ = __str__
