# parsek-cdp

**An async toolkit for driving Chromium at scale, over the
[Chrome DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/).**

The goal is *remote, large-scale* browser control: a fleet of Chromium
instances launched and supervised on server workers, each driven as if it were
local. You write against a typed, local-looking API; the same code runs
unchanged against a browser on another machine, behind a proxy that supervises
it, aggregates its event stream and exposes it for ops.

What makes that practical:

- **Identical local and remote API.** `Browser.connect_http(...)` (local) and
  `Browser.get_distant_browser(...)` (remote, through `parsek-cdp-server`) return
  the same object with the same methods — develop against a local Chrome, deploy
  against a fleet without changing your code.
- **One websocket per target, no `sessionId` multiplexing.** Each browser, page,
  worker and OOPIF gets its own connection. The proxy bridges client↔Chrome 1:1,
  so routing is simple and horizontally scalable — a stateless gateway can fan
  clients out to worker pods purely by the browser's id.
- **Server-side event aggregation.** Feature *producers* collapse a raw CDP burst
  (e.g. all of `Network.*`) into a couple of `Parsek.*` events and suppress the
  raw ones, so a high-traffic page does not flood the wire between worker and
  client.
- **Lifecycle, metrics and cleanup built in.** Crash detection + restart, idle
  shutdown, Prometheus metrics, and a separate reaper for leaked browser
  processes — the parts you need to run hundreds of browsers unattended.

The protocol layer is **fully generated** from the official
[devtools-protocol](https://github.com/ChromeDevTools/devtools-protocol) JSON
definitions — one typed module per domain. The runtime is hand-written.
Requires **Python 3.12+** (the API uses PEP 695 generics).

> Документация на русском: [README.ru.md](README.ru.md).

## Packages

This repository is a monorepo of two separately published distributions:

| Package | Install | Scope |
| --- | --- | --- |
| [`parsek-cdp`](packages/client) | `pip install parsek-cdp` | The client: the generated `cdp` protocol layer, the `core` runtime (browser / page / frame / element), the feature system and the `parsek` contract. |
| [`parsek-cdp-server`](packages/server) | `pip install parsek-cdp[server]` | The server: launch, supervise and proxy a browser; host feature producers; Prometheus metrics; a zombie-process reaper. Depends on `parsek-cdp` and reuses its shared layers. |

The client never depends on the server — only the `[server]` extra links them.
Full usage lives in each package's README:
[client](packages/client/README.md) · [server](packages/server/README.md).

## Quickstart

Drive a local browser (started with `chromium --headless=new --remote-debugging-port=9222`):

```python
import asyncio
from parsek_cdp import Browser, Page, RequestListener


async def main():
    browser = await Browser.connect_http(
        "http://127.0.0.1:9222", page_class=Page[RequestListener]
    )
    page = await browser.new_page()
    requests = page.get_feature(RequestListener)

    await page.navigate("https://example.com", wait_load=True)
    for r in requests.requests:
        print(r.method, r.url, "->", r.response.status_code if r.response else "(pending)")

    await browser.close()


asyncio.run(main())
```

The same code drives a *remote* browser through `parsek-cdp-server` — only the
entry point changes. The server launches and supervises the browser; the
features you declared are aggregated server-side:

```python
browser = await Browser[Page[RequestListener]].get_distant_browser(
    "http://127.0.0.1:9333", headless=True
)
```

## Abstractions

The client runtime (`core/`) is a small set of composable objects. Each layer
adds exactly one concern on top of the one below it.

### `CDPConnection` — one websocket, JSON-RPC

The base of everything: a single websocket carrying one DevTools session. It
owns the receive loop, assigns command ids and matches each response back to the
awaiting future, and dispatches events that arrive unsolicited. It is
deliberately fault-isolating — a malformed frame or a throwing event handler is
logged and skipped, never tearing down the socket — and when the connection does
close, every pending command future is failed with a `ConnectionError` instead
of hanging forever.

### `Target` — a CDP session with its own children

A `Target` *is* a `CDPConnection` (the browser, a page, a worker, an OOPIF), so
every target has its own websocket — `{host}/devtools/{type}/{id}`. The host is
bound once in a `contextvar` when the browser is reached, inherited by every
target connected from within. On top of the raw connection a target adds:

- **the full command surface** via `target.cdp.<Domain>`, one attribute per CDP
  domain, with typed methods and typed results;
- **domain bookkeeping** — every `enable`/`disable` is tracked per-session (and
  process-wide), so `domain_enabled(...)` can ensure a domain for a block and
  restore the prior state, never enabling something twice;
- **event handlers** — `on` / `off` per-target, plus `wait_for(Event)` to
  suspend until one fires; handlers may be sync or async;
- **command hooks** — `on_function(cmd, handler)` fires whenever a given CDP
  command is *sent* (the dual of an event handler);
- **a live child-target tree** — `refresh_targets()` rebuilds the subtree rooted
  at this target from an authoritative `Target.getTargets` snapshot (iframes
  nested under their parent frame, popups under their opener), reusing existing
  `Target` objects so identity and open sockets survive a refresh.

```python
await page.cdp.Network.enable()
info = await page.cdp.Target.get_target_info()

async with page.domain_enabled(page.cdp.Page):       # enable for the block, then restore
    await page.cdp.Page.navigate(url="https://example.com")

from parsek_cdp.cdp import Network
page.on(Network.RequestWillBeSent, lambda e: print(e.request.url))   # per-target

@Network.RequestWillBeSent.add_handler                               # global, every target
async def on_request(e):
    print(e.request.url)

evt = await page.wait_for(Network.ResponseReceived, timeout=10)      # await one event
```

### `Browser` — the endpoint and target discovery

`Browser[T]` connects to the browser-level websocket, turns on target discovery
and exposes page targets as `Page` objects (typed to `T`, the page class you
pass). It is generic over that page class, so `Browser[Page[RequestListener]]`
flows the feature set through to `browser.pages`, `new_page()` and contexts. Two
ways in:

- `Browser.connect_http(endpoint)` — discover the websocket via `/json/version`
  and attach to a **local** Chrome;
- `Browser.get_distant_browser(server, ...)` — `POST /browsers` on a
  `parsek-cdp-server`, then connect to the proxy's control channel; the returned
  browser drives the **remote** one exactly like a local browser, with features
  aggregated server-side (pages run their features as *views*, not producers).

### `BrowserContext` — isolated profiles

Pages are grouped into browser contexts (incognito-like profiles, optionally
with their own proxy). A page registered in a context bubbles up to the
browser's global registry — one `Page` instance shared by both — so you can work
per-context or across the whole browser.

```python
browser = await Browser.connect_http("http://127.0.0.1:9222")
context = await browser.create_context(proxy_server="http://10.0.0.1:8080")
page = await context.new_page("https://example.com")
print(len(browser.pages), "pages across", len(browser.contexts), "contexts")
```

### `Page`, `Frame`, `Element` — the DOM-facing layer

A `Page` is a `Target`, a `FeatureHost` **and** a `Frame`: in CDP the main
frame's id equals the page's target id, so the page *is its own main frame* and
`page.select(...)`, `page.evaluate(...)`, `page.url` all operate on the top
frame without any extra object. The full frame tree — subframes and cross-origin
**OOPIFs**, each transparently routed through its own session — lives on
`page.frames`.

- **`Frame`** scopes querying and evaluation: `select` / `select_all` (CSS *or*
  XPath), `evaluate`, `wait_for_selector`, `wait_for_xpath`. Each query runs in
  that frame's document, so subframes resolve correctly.
- **`Element`** is a live DOM-node handle: `text`, `attributes`, `children`,
  `query_selector(_all)`, plus actions — `mouse_click`, `fill`, `type`, `press`,
  `focus`, `scroll_into_view`, `is_visible`, and `apply(jsFn)` to run a JS
  function with the node as `this`.
- **navigation helpers** on the page: `navigate(url, wait_load=True)` arms the
  load waiter *before* navigating (so a fast load is never missed), and
  `with_same_navigation()` cancels a block the moment the main frame commits a
  new document — so logic never keeps operating on a page that navigated out from
  under it.

```python
el = await page.select(selector="input[name=q]")
await el.fill("parsek")
await el.press("Enter")
print(el.text, el.attributes)

title = await page.evaluate("document.title")

async with page.with_same_navigation():          # cut short if the page navigates
    row = await page.select(selector="#row")
    await row.mouse_click()
```

### `Feature` / `FeatureHost` — opt-in behaviour, write-once, run anywhere

A `Page` attaches **no** behaviour by default; a *feature* is a unit of
behaviour you opt into — `Page[F]` (declarative, typed) or `page.get_feature(F)`
(imperative). The point of the feature system is that one implementation runs in
**three roles** without change:

- **local** — direct to the browser: the feature's producers subscribe to raw
  CDP on the page and reduce it in-process (a plain local `Page`);
- **server** — the proxy feeds raw CDP to the producer, whose output is *emitted*
  to the client as a `Parsek.*` event **and** reduced locally for snapshots;
- **client** — only the reducers run, fed by those `Parsek.*` events off the
  wire.

Because the reducers run in every role, a feature's public API (the state it
builds) is identical whether the browser is local or remote — that is what lets
the same code scale out. `FeatureHost` is the mixin that gives a page the
`[F]` composition and `attach` / `get_feature` / `has_feature`, deferring each
feature's async `start()` until the connection is live. `RequestListener` is the
built-in reference feature; writing your own follows a domain-like package layout
(`types` · `events` · the `Feature` class) — full guide in the
[client README](packages/client/README.md#features).

### `parsek` contract

The small slice of protocol that is *not* plain CDP — the server-supervised
browser lifecycle (`BrowserState`, `BrowserStateChanged`). It ships in the
client distribution (`parsek_cdp.parsek`) so both sides share one wire
definition.

## Server-side abstractions

`parsek-cdp-server` adds the parts that make remote browsers operable; see its
[README](packages/server/README.md) for endpoints and metrics.

- **`ChromeLauncher`** — finds a Chromium-compatible binary (or a random one
  across several installed browsers), launches it, waits for the DevTools port
  and reads back its websocket. Owns the temp profile dir and tears it down.
- **`BrowserSupervisor`** — owns one browser as a "task": health polling, crash
  detection and restart, idle shutdown, and broadcasting every state transition
  so the client reacts instead of hanging on a dead socket.
- **`ParsekServer` / `PageBridge`** — the HTTP/ws front door. A control channel
  pipes the browser endpoint plus `Parsek.browserStateChanged`; each page pipe is
  a `PageBridge` that relays raw CDP 1:1 and hosts the feature producers,
  suppressing the raw events they consume (`?raw=1` opts out).
- **`ServerMetrics`** — Prometheus exposition (browsers, targets by type, nested
  targets, per-target CDP event counts, CPU/RAM of the process tree), sampled off
  the event loop.
- **reaper** — a separate subprocess that kills leaked (zombie/orphaned)
  parsek-launched Chrome processes, recognised by their profile-dir marker.

The intended topology at scale: a **stateless gateway** routes each client
websocket to the worker that owns the browser purely by the browser's id (no
shared store), and each worker runs a `ParsekServer` supervising its browsers.

## Code generation

The `cdp/` package is **not** written by hand — it is generated from the
upstream protocol JSON by `parsek_cdp/generate.py`. Per domain it emits:

| Module | Contents |
| --- | --- |
| `types.py` | enums (`str, Enum`), object types (`@dataclass` over `DataType`), and aliases (PEP 695 `type X = ...`) |
| `functions.py` | each command as a typed `async` method on a domain class bound to a target, returning a generated `…Return` dataclass |
| `events.py` | each event as an `Event` dataclass registered for handler dispatch |
| `__init__.py` | the domain namespace; a top-level `cdp/__init__.py` aggregates every domain into the `CDP` accessor behind `target.cdp` |

How it stays import-cycle-free: every `$ref` is resolved **at generation time**
(alias chains are followed to their concrete shape), so the runtime only looks
up enums and object types — lazily, by fully-qualified name. Cross-domain type
references are emitted as lazy string annotations imported only under
`TYPE_CHECKING`, so the circular cross-domain imports present in the protocol
never materialise at runtime. Each generated type carries a `__FIELDS__` table
of `FieldMeta` describing the `snake_case` ↔ `camelCase` mapping and how nested
values (enums / objects / arrays) are (de)serialized.

### Regenerating / using your own protocol JSON

The generator takes a single argument — a devtools-protocol commit/tag/branch
(downloaded from GitHub) or a path to a local directory holding
`js_protocol.json` + `browser_protocol.json`:

```bash
# pin to an upstream revision (commit, tag or branch) and download it
python -m parsek_cdp.generate master

# or generate from a local copy of the protocol JSON
python -m parsek_cdp.generate path/to/protocol-json/
```

Output is written to `packages/client/parsek_cdp/cdp/`. This is how you target a
specific Chrome version, or a fork/extension of the protocol: point the
generator at the matching JSON and the whole typed surface is rebuilt.

## Development

```bash
python -m venv .venv
.venv/bin/pip install -e packages/client -e packages/server
```

## License

Apache-2.0 — see [LICENSE](LICENSE).
