"""A single frame -- the mandatory browser abstraction.

A :class:`Frame` is self-contained: it binds to the CDP session that owns it
(:attr:`Frame.target` -- a dedicated session of its own for a cross-origin
OOPIF, the page's session otherwise) and exposes :meth:`Frame.select` /
:meth:`Frame.evaluate` and the ``wait_for_*`` helpers, all scoped to that frame.
Everything routes through :attr:`Frame.cdp` so same- and cross-origin frames
behave identically.

Tracking the *tree* of frames (parent/child links, attach/detach, OOPIF
discovery) is a separate, optional concern handled by a tree-manager feature --
a :class:`Frame` never depends on it.
"""

from __future__ import annotations

import asyncio
from enum import Enum
from typing import TYPE_CHECKING, List, Optional, Tuple

from ..cdp import DOM, Page
from .target import ProtocolError, Target

if TYPE_CHECKING:
    from .element import Element


class ElementState(Enum):
    """Condition awaited by :meth:`Frame.wait_for_selector` / :meth:`Frame.wait_for_xpath`."""

    ATTACHED = "attached"
    VISIBLE = "visible"
    HIDDEN = "hidden"
    DETACHED = "detached"


class LoadState(Enum):
    """A page lifecycle milestone; values are the CDP ``Page.lifecycleEvent`` names."""

    LOAD = "load"
    DOMCONTENTLOADED = "DOMContentLoaded"
    NETWORKIDLE = "networkIdle"


class Frame:
    """A single frame, bound to the CDP session that owns it.

    Holds the protocol :class:`~parsek_cdp.cdp.page.types.Frame` fields that
    matter day to day (``url``, ``name``, ``loader_id``) and offers
    :meth:`evaluate` / :meth:`select` scoped to it.  A cross-origin frame is
    bound to its own dedicated CDP session (:attr:`target`); everything routes
    through :attr:`cdp` so same- and cross-origin frames behave identically.

    ``target`` is the session this frame runs on (the page for same-origin
    frames; for the main frame the page *is* the frame).  ``parent_id`` is kept
    as raw protocol data, but resolving it to a parent frame -- and listing
    children -- is the job of the optional tree-manager feature.
    """

    _head_elem: Element | None

    def __init__(
        self,
        target: "Target",
        frame_info: Page.Frame,
        parent: Frame | None = None,
    ) -> None:
        self.target = target
        self._frame = frame_info
        self._parent = parent
        self._frames: dict[Page.FrameId, Frame] = {}

        self._dom_generation = 0
        self._head_elem = None

        self._bind_frame_tracking()
        self._bind_dom_tracking()

    def _bind_frame_tracking(self) -> None:
        self.target.on(Page.FrameAttached, self._on_page_attach_frame)
        self.target.on(Page.FrameNavigated, self._on_page_navigated_frame)
        self.target.on(Page.FrameDetached, self._on_page_dettached_frame)

    def _unbind_frame_tracking(self) -> None:
        self.target.off(Page.FrameAttached, self._on_page_attach_frame)
        self.target.off(Page.FrameNavigated, self._on_page_navigated_frame)
        self.target.off(Page.FrameDetached, self._on_page_dettached_frame)

    def _bind_dom_tracking(self) -> None:
        """Track every event that invalidates this frame's ``nodeId`` map.

        ``DOM.enable``/``DOM.disable`` rebuild (or drop) the whole node-id map and
        ``DOM.documentUpdated`` fires when the document is replaced -- each leaves
        previously minted ``nodeId``s stale.  Which one happened doesn't matter,
        only that the map changed, so all three bump a single monotonic counter;
        an :class:`Element` whose ``_generation`` lags re-mints its id from the
        stable ``backendNodeId`` (see :meth:`Element.refresh`).
        """
        self.target.on_function(self.target.cdp.DOM.disable, self._bump_dom_generation)
        self.target.on_function(self.target.cdp.DOM.enable, self._bump_dom_generation)
        self.target.on(DOM.DocumentUpdated, self._bump_dom_generation)

    def _unbind_dom_tracking(self) -> None:
        self.target.off_function(self.target.cdp.DOM.disable, self._bump_dom_generation)
        self.target.off_function(self.target.cdp.DOM.enable, self._bump_dom_generation)
        self.target.off(DOM.DocumentUpdated, self._bump_dom_generation)

    def _bump_dom_generation(self, _) -> None:
        self._dom_generation += 1

    def dispose(self) -> None:
        """Unregister this frame's (and its subtree's) target-level handlers.

        Same-origin frames share one target, so the handlers bound in
        :meth:`_bind_dom_tracking` / :meth:`_bind_frame_tracking` outlive the
        frame unless removed explicitly.  Call this whenever a frame leaves the
        tree (see :meth:`detach_frame` / :meth:`refresh_frame`) so recreated
        frames don't pile up dead handlers on the target.
        """
        self._unbind_frame_tracking()
        self._unbind_dom_tracking()
        for child in list(self._frames.values()):
            child.dispose()
        self._frames.clear()

    @property
    def id(self) -> Page.FrameId:
        return self._frame.id

    @property
    def url(self) -> str:
        return self._frame.url

    @property
    def name(self) -> Optional[str]:
        return self._frame.name

    @property
    def loader_id(self) -> str:
        return self._frame.loader_id

    @property
    def is_main(self) -> bool:
        return self._frame.parent_id is None

    @property
    def is_oopif(self) -> bool:
        """``True`` when this frame is a cross-origin frame with its own session.

        A frame keeps its own identity (:attr:`id`); this only asks whether the
        session it is *bound* to is dedicated to it (an out-of-process iframe).
        """
        return self.target.id == self._frame.id

    @property
    def raw_frame(self) -> Page.Frame:
        return self._frame

    @property
    def frames(self):
        return list(self._frames.values())

    @property
    def cdp(self):
        """The CDP entry point of the session this frame is bound to."""
        return self.target.cdp

    async def _get_head_elem(self):
        if (
            self._head_elem is None
            or self._dom_generation != self._head_elem._generation
        ):
            from .element import Element

            document = await self.cdp.DOM.get_document(depth=0)
            self._head_elem = Element._from_node(document.root, frame=self)
            self._head_elem._generation = self._dom_generation
        return self._head_elem

    @classmethod
    def from_frame_tree(cls, origin_frame: Frame, frame_tree: Page.FrameTree):
        frame_id = frame_tree.frame.id
        target = origin_frame.target._targets.get(frame_id, origin_frame.target)
        instance = cls(target, frame_tree.frame, origin_frame)
        for frame_tree in frame_tree.child_frames or []:
            child = Frame.from_frame_tree(instance, frame_tree)
            instance._frames[child.id] = child
        return instance

    async def refresh_frame(self):
        tree = await self.cdp.Page.get_frame_tree()
        self._merge_frame_tree(tree.frame_tree)

    def _merge_frame_tree(self, frame_tree: Page.FrameTree) -> None:
        """Reconcile this frame's children against a fresh ``Page.getFrameTree``.

        Only frames absent from ``frame_tree`` are disposed; survivors keep their
        identity (and their bound DOM-tracking handlers), so we neither leak
        handlers by recreating them nor throw away their per-frame state (DOM
        generation, cached head element).  New frames are built fresh.
        """
        self._frame = frame_tree.frame
        children = frame_tree.child_frames or []
        live_ids = {child.frame.id for child in children}
        for frame_id in list(self._frames):
            if frame_id not in live_ids:
                self._frames.pop(frame_id).dispose()
        for child_tree in children:
            existing = self._frames.get(child_tree.frame.id)
            if existing is not None:
                existing._merge_frame_tree(child_tree)
            else:
                child = Frame.from_frame_tree(self, child_tree)
                self._frames[child.id] = child

    async def select(
        self, *, selector: Optional[str] = None, xpath: Optional[str] = None
    ) -> Optional[Element]:
        """Find the first node matching a CSS ``selector`` or an ``xpath``.

        Returns its :class:`Element`, or ``None`` if nothing matches.  The query
        runs in this frame's document, so subframes are resolved correctly.
        """
        from .element import Element

        if xpath is not None:
            node_ids = await self._perform_search(xpath)
            if not node_ids:
                return None
            return await Element.describe_node(node_id=node_ids[0], frame=self)
        if selector is None:
            raise ValueError("select() needs either selector= or xpath=")
        head_node = await self._get_head_elem()
        return await head_node.query_selector(selector=selector)

    async def select_all(self, selector: str) -> List[Element]:
        """Return an :class:`Element` for every node matching ``selector``."""

        head_node = await self._get_head_elem()
        res = []
        async for elem in head_node.query_selector_all(selector=selector):
            res.append(elem)
        return res

    async def _perform_search(self, query: str) -> List[int]:
        """Run a DevTools DOM search (text / attributes / markup / XPath)."""
        dom = self.cdp.DOM
        search = await dom.perform_search(
            query=query, include_user_agent_shadow_dom=True
        )
        try:
            if not search.result_count:
                return []
            results = await dom.get_search_results(
                search_id=search.search_id,
                from_index=0,
                to_index=min(search.result_count, 50),
            )
            return [n for n in results.node_ids if n]
        finally:
            try:
                await dom.discard_search_results(search_id=search.search_id)
            except Exception:
                pass

    async def evaluate(self, expression: str, *, await_promise: bool = False):
        """Evaluate JavaScript in this frame and return the value.

        Runs in the frame's own execution context, so subframes (including
        cross-origin ones) are evaluated correctly rather than against the main
        page.  Raises :class:`RuntimeError` if a non-main frame has no context
        yet (e.g. before it has loaded).
        """
        result = await self.cdp.Runtime.evaluate(
            expression=expression,
            await_promise=await_promise,
            return_by_value=True,
        )  # TODO: Сделать по контексту
        return result.result.value if result.result else None

    async def wait_for_selector(
        self,
        selector: str,
        *,
        state: ElementState = ElementState.VISIBLE,
        timeout: float = 30,
        poll_interval: float = 0.1,
    ) -> Optional[Element]:
        """Poll until a node matching the CSS ``selector`` reaches ``state``.

        Returns the :class:`Element` for ``ATTACHED`` / ``VISIBLE`` (or ``None``
        for ``HIDDEN`` / ``DETACHED``).  Raises :class:`asyncio.TimeoutError` if
        the state is not reached within ``timeout`` seconds.  Each poll
        re-queries, so a re-mounted node (fresh ``nodeId``) is handled correctly.
        """
        return await self._wait_for_query(
            {"selector": selector}, state, timeout, poll_interval
        )

    async def wait_for_xpath(
        self,
        xpath: str,
        *,
        state: ElementState = ElementState.VISIBLE,
        timeout: float = 30,
        poll_interval: float = 0.1,
    ) -> Optional[Element]:
        """Like :meth:`wait_for_selector` but matching an XPath expression."""
        return await self._wait_for_query(
            {"xpath": xpath}, state, timeout, poll_interval
        )

    async def _wait_for_query(
        self,
        query: dict,
        state: ElementState,
        timeout: float,
        poll_interval: float,
    ) -> Optional[Element]:
        loop = asyncio.get_running_loop()
        deadline = loop.time() + timeout
        while True:
            try:
                element = await self.select(**query)
            except ProtocolError:
                element = None
            done, result = await self._state_satisfied(element, state)
            if done:
                return result
            if loop.time() >= deadline:
                target = query.get("selector") or query.get("xpath")
                raise asyncio.TimeoutError(
                    f"waiting for {target!r} to be {state.value} timed out after {timeout}s"
                )
            await asyncio.sleep(poll_interval)

    @staticmethod
    async def _state_satisfied(
        element: Optional[Element], state: ElementState
    ) -> Tuple[bool, Optional[Element]]:
        """Whether ``element`` meets ``state`` (and what to return on success)."""
        if state is ElementState.ATTACHED:
            return element is not None, element
        if state is ElementState.DETACHED:
            return element is None, None
        visible = element is not None and await element.is_visible()
        if state is ElementState.VISIBLE:
            return visible, element
        return not visible, element

    async def _on_page_attach_frame(self, event: Page.FrameAttached):
        if event.parent_frame_id == self.id:
            await self.refresh_frame()

    def _on_page_navigated_frame(self, event: Page.FrameNavigated):
        if event.frame.id == self.id:
            self._frame = event.frame

    def _on_page_dettached_frame(self, event: Page.FrameDetached):
        if event.frame_id in self._frames:
            self._frames.pop(event.frame_id, None)

    def attach_frame(self, frame: Frame):
        self._frames[frame.id] = frame

    def detach_frame(self, frame: Frame):
        detached = self._frames.pop(frame.id)
        detached.dispose()
        return detached

    def __str__(self) -> str:
        kind = "oopif" if self.is_oopif else ("main" if self.is_main else "child")
        return f"<Frame {kind} {self.target.url!r}>"

    __repr__ = __str__
