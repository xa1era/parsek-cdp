# parsek-cdp

An async [Chrome DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/)
client for driving Chromium-based browsers from Python.

The protocol layer (`cdp/`) is **fully generated** from the official
[devtools-protocol](https://github.com/ChromeDevTools/devtools-protocol) JSON
definitions — one typed module per domain. The runtime (`core/`) is
hand-written: one websocket per target, typed command calls, event handlers and
an opt-in feature system. No `sessionId` multiplexing — every target (browser,
page, worker, OOPIF) gets its own connection.

Requires **Python 3.12+** (the API uses PEP 695 generics) and a running
Chromium/Chrome with remote debugging enabled.

```bash
pip install parsek-cdp
```

> Документация на русском: [README.ru.md](README.ru.md).

## Quickstart

Start a browser with remote debugging:

```bash
chromium --headless=new --remote-debugging-port=9222
```

Then drive it:

```python
import asyncio
from parsek_cdp import Browser, Page, RequestListener


async def main():
    # `page_class` types every page in this browser as Page[RequestListener].
    browser = await Browser.connect_http(
        "http://127.0.0.1:9222", page_class=Page[RequestListener]
    )

    page = await browser.new_page()
    requests = page.get_feature(RequestListener)

    await page.navigate("https://example.com", wait_load=True)

    for r in requests.requests:
        status = r.response.status_code if r.response else "(pending)"
        print(r.method, r.url, "->", status)

    await browser.close()


asyncio.run(main())
```

## Concepts

### Targets and connections

A `Target` *is* a single CDP session on its own websocket. `Browser`, `Page`,
workers and out-of-process iframes are all targets. The DevTools host is bound
once (in a `contextvar`) when the browser is reached, so it is not threaded
through every call.

The full command surface is reached through `target.cdp`, one attribute per CDP
domain, with typed methods and results:

```python
await page.cdp.Network.enable()
info = await page.cdp.Target.get_target_info()
```

Domains enable/disable themselves on use, and `domain_enabled` scopes a domain
to a block:

```python
async with page.domain_enabled(page.cdp.Page):
    await page.cdp.Page.navigate(url="https://example.com")
```

### Events

Register handlers on a specific target, or globally on the event class:

```python
from parsek_cdp.cdp import Network

# per-target
page.on(Network.RequestWillBeSent, lambda e: print(e.request.url))

# globally, for every target
@Network.RequestWillBeSent.add_handler
async def on_request(e):
    print(e.request.url)

# await a single event
loaded = await page.wait_for(Network.ResponseReceived, timeout=10)
```

Handlers may be sync or async; one failing handler never tears down the
connection or stops the others.

### Pages, frames and elements

A `Page` *is its own main frame*, so frame methods work on the top frame
directly:

```python
el = await page.select(selector="h1")      # query the main frame
print(el.text)
await el.fill("hello")
await el.mouse_click()

title = await page.evaluate("document.title")
```

The full frame tree (subframes, cross-origin OOPIFs — each transparently routed
through its own session) lives on `page.frames`. `page.with_same_navigation()`
guards a block against a main-frame navigation cutting it short.

### Browser contexts

Pages are grouped into browser contexts (incognito-like profiles). The default
context holds pages created without an explicit one:

```python
context = await browser.create_context()        # isolated profile
page = await context.new_page("https://example.com")
```

## Features

A `Page` attaches **no** behaviour by default. A *feature* is a unit of
behaviour you opt into, either declaratively or imperatively:

```python
from parsek_cdp import Page, RequestListener

Page[RequestListener]                 # declarative — typed page class
page.get_feature(RequestListener)     # imperative — attached on first use, typed
```

The key idea: a feature is written **once** and runs in three roles —

- **local** — direct to the browser: the producers subscribe to raw CDP on the
  page and reduce it in-process (a plain local `Page`);
- **server** — the proxy feeds raw CDP to the producers, whose output is emitted
  to the client as a `Parsek.*` event *and* reduced locally for snapshots;
- **client** — only the reducers run, fed by those `Parsek.*` events off the wire.

Conceptually that is two *sides* — a *producer* of `Parsek.*` events and a *view*
of them — but the producer side exists both in-process (`local`) and over the
wire (`server`). The reducers run in every role, so the feature's public API is
identical whether the browser is local or behind a `parsek-cdp-server` proxy.

### Writing a custom feature — domain-like structure

A feature mirrors the layout of a generated CDP domain (`cdp/<domain>/` =
*types · functions · events*). Give it its own package with the same three
files, so the feature class doubles as its own namespace:

```
features/<feature>/
  types.py       # wire dataclasses + view types  (@parsek_type)
  events.py      # aggregated Parsek.* events       (@register_event)
  __init__.py    # the Feature class itself: domains + @on/@emit handlers
```

The building blocks (all from `parsek_cdp.core.feature`):

| Block | Where | What |
| --- | --- | --- |
| `domains = (Network, ...)` | feature class | CDP domains the feature owns — auto-enabled, and their raw events are suppressed from client passthrough |
| `@on(Event)` | method | register a handler. A **CDP** event makes it a *producer* (runs server/local); a **`Parsek.*`** event makes it a *reducer* (runs in every role) |
| `@emit(ParsekEvent)` | producer method | its return value is published to the client **and** reduced locally — so state is built by the same code path everywhere |
| `@parsek_type("Parsek.<Feature>.<Type>")` | `types.py` | declare a wire dataclass; `__FIELDS__` are derived from annotations (snake_case ↔ camelCase) |
| `@register_event("Parsek.<Feature>.<event>")` | `events.py` | declare an aggregated event class |
| `snapshot()` | feature class | state handed to a late-joining client (the server may replay it on connect) |
| `attach_namespace(Feat, types, events)` | end of `__init__.py` | expose the types/events as attributes on the feature class (`Feat.RequestData`, `Feat.RequestSent`, ...) |

Sketch — a producer that folds a raw CDP burst into one `Parsek.*` event, plus
the reducer that rebuilds state from it:

```python
# events.py
@register_event("Parsek.MyFeature.thing")
@dataclass
class ThingHappened(Event):
    payload: ThingData
    __FIELDS__ = (FieldMeta("payload", "payload", False, "object",
                            ref="Parsek.MyFeature.ThingData"),)

# __init__.py
class MyFeature(Feature):
    domains = (SomeDomain,)                 # owned + auto-enabled

    @on(SomeDomain.SomethingRaw)            # CDP event -> producer
    @emit(ThingHappened)                    # return is sent to client + reduced
    def _produce(self, e) -> ThingHappened:
        return ThingHappened(payload=ThingData(...))

    @on(ThingHappened)                      # Parsek event -> reducer (both roles)
    def _reduce(self, e: ThingHappened) -> None:
        self._things.append(e.payload)

    @property
    def things(self):                       # the ergonomic public API
        return list(self._things)

attach_namespace(MyFeature, _types, _events)
```

`RequestListener` (below) is the reference implementation of exactly this shape.

### `RequestListener`

The built-in feature: aggregated network observation. It records every request
of the current document with its response, headers and timing:

```python
requests = page.get_feature(RequestListener)
await page.navigate("https://example.com", wait_load=True)

# all requests of the current document
for r in requests.requests:
    print(r.method, r.url, r.response.status_code)

# find / await a specific one (substring or compiled regex against the URL)
r = await requests.wait_for_response("/api/orders", timeout=30, load_body=True)
print(r.response.status_code, await r.response.body())
```

By default the log is cleared on main-frame navigation (like DevTools with
*Preserve log* off); pass `preserve_log=True` to keep it across documents.

## Remote browsers (with `parsek-cdp-server`)

Install the optional server distribution to launch and supervise browsers
behind a proxy:

```bash
pip install parsek-cdp[server]
```

Then connect to a running server instead of a local Chrome — the API is
identical, and the declared features are aggregated server-side:

```python
browser = await Browser[Page[RequestListener]].get_distant_browser(
    "http://127.0.0.1:9333", headless=True
)
page = await browser.new_page("https://example.com")
```

See the [`parsek-cdp-server`](https://github.com/xa1era/parsek-cdp) package for
running the server, lifecycle supervision, metrics and the zombie reaper.

## License

Apache-2.0.