# parsek-cdp-server

The server side of **parsek-cdp**: launching, supervising and proxying a
browser, plus the server-side feature *producers* that digest raw CDP into
`Parsek.*` events.

A separate distribution from `parsek-cdp` (the client); installed via
`pip install parsek-cdp[server]`. It depends on `parsek-cdp` and reuses its
shared layers wholesale — the generated `cdp` protocol, the `core` primitives
(`CDPConnection`, `Target`, `DataType`) and the `parsek` contract — adding only
what must live next to the browser.

> Документация на русском: [README.ru.md](README.ru.md).

## Running

```python
import asyncio
from parsek_cdp_server import ParsekServer
from parsek_cdp.features import RequestListener


async def main():
    server = ParsekServer(idle_timeout=300)    # a browser self-closes after 5 min idle
    server.register_feature(RequestListener)   # make the feature selectable via ?feature=
    await server.start("127.0.0.1", 9333)
    try:
        await asyncio.Event().wait()           # keep the server alive
    finally:
        await server.stop()


asyncio.run(main())
```

A client connects to this server with
`Browser.get_distant_browser("http://127.0.0.1:9333", ...)` — the API is
identical to a local browser (see the client README). Every `POST /browsers`
spins up its own supervised browser; `idle_timeout` (on the server or in the
request body) closes a browser that sits with no connection.

### Where the browser comes from

`launcher` finds a Chromium-compatible binary on its own. By default it walks
the usual install paths; the `PARSEK_CHROMES_PATH` env var (directories
separated by `os.pathsep`, like `PATH`) overrides the search — each launch picks
a **random** one of the browsers it finds (a cheap way to spread load and
fingerprints). An explicit path and flags go through `LaunchOptions`
(`executable`, `headless`, `extra_args`, ...) — either on the server or
per-request in the `POST /browsers` body.

## Modules

| Module | Responsibility |
| --- | --- |
| `launcher` | Start Chrome/Chromium, wait for the DevTools endpoint, read the browser-level websocket from `/json/version`. |
| `supervisor` | Browser lifecycle: health, crash detection, restart, idle shutdown, and `Parsek.browserStateChanged` broadcast. |
| `proxy` | Accept client websockets and bridge each 1:1 to a Chrome target; host feature producers and serve the `Parsek.*` surface. |
| `metrics` | Prometheus exposition at `/metrics`. |
| `reaper` | A separate subprocess that kills leaked (zombie/orphaned) parsek-launched Chrome processes. |

## Connection model

As in the client, **every target gets its own websocket** (no `sessionId`
multiplexing). One parsing flow = one `browser_context`; pages within it each
connect over their own websocket. The proxy bridges a page's client socket to
the corresponding Chrome socket **1:1**.

## Endpoints

```
HTTP POST /browsers                                   create a task -> browser_uuid
HTTP GET  /metrics                                    Prometheus metrics
ws        /cdp/{browser_uuid}/control                 browser-level pipe + Parsek.browserStateChanged
ws        /cdp/{browser_uuid}/page/{target_id}        CDP proxy (per-page) + Parsek.*
```

### Responses

`POST /browsers` returns `200 application/json` — the browser id and its
control-channel endpoint:

```json
{
  "browserUuid": "1f2ab34cd56e78f9...",
  "wsUrl": "ws://127.0.0.1:9333/cdp/1f2ab34cd56e78f9.../control"
}
```

`GET /metrics` returns `200 text/plain` in the Prometheus text exposition
format (see the metrics table below).

The websocket endpoints (`/control` and `/page/{target_id}`) respond with a
websocket upgrade; for an unknown `browser_uuid` the socket is closed
immediately with code `4040` ("unknown browser").

The control channel is a raw pipe to the browser endpoint plus the
`Parsek.browserStateChanged` broadcast, so a parser learns when its browser
crashed/restarted instead of hanging; browser-level CDP (creating/disposing
contexts, etc.) passes straight through it.

## Features

The server is **pure passthrough** by default (`ParsekServer` has no `features`
argument). Feature producers are added with `register_feature(...)` and selected
per browser with `POST /browsers?feature=<name>`. On a page pipe a producer
digests the raw CDP burst into a couple of aggregated `Parsek.*` events and
*suppresses* the raw events it consumed; `?raw=1` opts out of suppression.

## Metrics (`GET /metrics`)

| Metric | Type | What |
| --- | --- | --- |
| `parsek_browsers` | gauge | number of supervised browsers |
| `parsek_targets{browser,type}` | gauge | targets per browser, by type |
| `parsek_nested_targets{browser}` | gauge | nested targets (with a `parentId`) |
| `parsek_browser_cpu_percent{browser}` | gauge | CPU% of the browser process tree |
| `parsek_browser_memory_bytes{browser}` | gauge | RSS of the browser process tree |
| `parsek_cdp_events_total{browser,target,domain}` | counter | CDP events by target and domain |

Targets and CPU/RAM are sampled by a background task (polling `/json/list` +
`psutil`), so a scrape only reads cached values and does not block the event
loop. The event counter is labelled by target id — series for dead targets are
pruned on every snapshot.

## Zombie reaper

On start the server spawns a **separate subprocess** (`reaper`) that
periodically scans for Chrome processes we launched (recognised by the
`--user-data-dir=…parsek-cdp-…` marker) that became zombies or orphans
(`ppid == 1`), and kills them along with their subtree. Controlled by
`ParsekServer(reap_zombies=..., reap_interval=...)`; it can also be run by hand:
`python -m parsek_cdp_server.reaper --once`.

## Notes

The `Parsek.*` contract lives in the client distribution (`parsek_cdp.parsek`)
and is shared by both sides.

## License

Apache-2.0.