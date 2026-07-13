# parsek-cdp-server

Серверная часть **parsek-cdp**: запуск, надзор и проксирование браузера, а также
серверные *продюсеры* фич, которые переваривают сырой CDP в события `Parsek.*`.

Отдельный дистрибутив от `parsek-cdp` (клиент); ставится через
`pip install parsek-cdp[server]`. Зависит от `parsek-cdp` и переиспользует его
общие слои целиком — сгенерированный протокол `cdp`, примитивы `core`
(`CDPConnection`, `Target`, `DataType`) и контракт `parsek` — добавляя лишь то,
что должно жить рядом с браузером.

> Documentation in English: [README.md](README.md).

## Запуск

```python
import asyncio
from parsek_cdp_server import ParsekServer
from parsek_cdp.features import RequestListener


async def main():
    server = ParsekServer(idle_timeout=300)    # браузер сам закроется после 5 мин простоя
    server.register_feature(RequestListener)   # делаем фичу выбираемой через ?feature=
    await server.start("127.0.0.1", 9333)
    try:
        await asyncio.Event().wait()           # держим сервер живым
    finally:
        await server.stop()


asyncio.run(main())
```

Клиент подключается к этому серверу через
`Browser.get_distant_browser("http://127.0.0.1:9333", ...)` — API такой же, как
у локального браузера (см. README клиента). Каждый `POST /browsers` поднимает
свой надзираемый браузер; `idle_timeout` (на сервере или в теле запроса)
закрывает браузер, простаивающий без подключений.

### Где берётся браузер

`launcher` сам находит Chromium-совместимый бинарник. По умолчанию обходятся
типовые пути установки; переменная `PARSEK_CHROMES_PATH` (каталоги через
`os.pathsep`, как `PATH`) переопределяет поиск — каждый запуск берёт
**случайный** из найденных браузеров. Явный путь и флаги задаются через `LaunchOptions` (`executable`,
`headless`, `extra_args`, ...) — на сервере целиком или per-request в теле
`POST /browsers`.

## Состав

| Модуль | Ответственность |
| --- | --- |
| `launcher` | Запуск Chrome/Chromium, ожидание DevTools-эндпоинта, чтение browser-level websocket из `/json/version`. |
| `supervisor` | Жизненный цикл браузера: здоровье, детект падения, рестарт, закрытие по простою и broadcast `Parsek.browserStateChanged`. |
| `proxy` | Приём клиентских websocket'ов и мост 1:1 к target'у Chrome; хостинг продюсеров фич и раздача поверхности `Parsek.*`. |
| `metrics` | Экспозиция Prometheus на `/metrics`. |
| `reaper` | Отдельный субпроцесс, убивающий утёкшие (зомби/осиротевшие) Chrome-процессы, запущенные нами. |

## Модель соединения

Как и в клиенте, **каждый target — свой websocket** (мультиплексирования по
`sessionId` нет). Один поток парсинга = один `browser_context`; страницы внутри
него подключаются каждая своим websocket'ом. Прокси связывает клиентский сокет
страницы с соответствующим сокетом Chrome **1:1**.

## Эндпоинты

```
HTTP POST /browsers                                   создать задачу -> browser_uuid
HTTP GET  /metrics                                    метрики Prometheus
ws        /cdp/{browser_uuid}/control                 browser-level pipe + Parsek.browserStateChanged
ws        /cdp/{browser_uuid}/page/{target_id}        CDP-прокси (per-page) + Parsek.*
```

### Ответы

`POST /browsers` возвращает `200 application/json` — идентификатор браузера и
его control-канал:

```json
{
  "browserUuid": "1f2ab34cd56e78f9...",
  "wsUrl": "ws://127.0.0.1:9333/cdp/1f2ab34cd56e78f9.../control"
}
```

`GET /metrics` возвращает `200 text/plain` в текстовом формате Prometheus
(см. таблицу метрик ниже).

Websocket-эндпоинты (`/control` и `/page/{target_id}`) отдают апгрейд до
websocket; при неизвестном `browser_uuid` сокет сразу закрывается с кодом
`4040` («unknown browser»).

Control-канал — это сырой pipe к browser-эндпоинту плюс broadcast
`Parsek.browserStateChanged`, чтобы парсер узнавал о падении/рестарте браузера, а
не висел. Browser-level CDP (создание/удаление контекстов и т.п.) проходит сквозь
него как обычный passthrough.

## Фичи

Сервер по умолчанию — **чистый passthrough** (аргумента `features` у
`ParsekServer` нет). Продюсеры фич подключаются через `register_feature(...)` и
выбираются для конкретного браузера запросом `POST /browsers?feature=<имя>`. На
page-pipe продюсер сворачивает пачку сырого CDP в пару агрегированных событий
`Parsek.*` и *подавляет* сырые события, которые переварил; `?raw=1` отключает
подавление.

## Метрики (`GET /metrics`)

| Метрика | Тип | Что |
| --- | --- | --- |
| `parsek_browsers` | gauge | число надзираемых браузеров |
| `parsek_targets{browser,type}` | gauge | targets браузера в разрезе типа |
| `parsek_nested_targets{browser}` | gauge | вложенные targets (с `parentId`) |
| `parsek_browser_cpu_percent{browser}` | gauge | CPU% дерева процессов браузера |
| `parsek_browser_memory_bytes{browser}` | gauge | RSS дерева процессов браузера |
| `parsek_cdp_events_total{browser,target,domain}` | counter | события CDP по target и домену |

Targets и CPU/RAM снимаются фоновой задачей (опрос `/json/list` + `psutil`), так
что scrape лишь читает закэшированные значения и не блокирует event loop. Счётчик
событий помечен id таргета — серии мёртвых таргетов вычищаются при каждом снимке.

## Reaper зомби-процессов

При старте сервер поднимает **отдельный субпроцесс** (`reaper`), который
периодически ищет процессы Chrome, запущенные нами (по маркеру
`--user-data-dir=…parsek-cdp-…`) и ставшие зомби или осиротевшими (`pid == 1`),
и убивает их вместе с поддеревом. Управляется флагами
`ParsekServer(reap_zombies=..., reap_interval=...)`; можно гонять и руками:
`python -m parsek_cdp_server.reaper --once`.

## Примечания

Контракт `Parsek.*` живёт в клиентском дистрибутиве (`parsek_cdp.parsek`) и общий
для обеих сторон.

## Лицензия

Apache-2.0.