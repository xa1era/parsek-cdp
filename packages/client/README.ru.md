# parsek-cdp

Асинхронный клиент [Chrome DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/)
для управления браузерами на базе Chromium из Python.

Слой протокола (`cdp/`) **полностью генерируется** из официальных JSON-описаний
[devtools-protocol](https://github.com/ChromeDevTools/devtools-protocol) — по
одному типизированному модулю на домен. Рантайм (`core/`) написан руками: один
websocket на каждый target, типизированные вызовы команд, обработчики событий и
опциональная система фич. Никакого мультиплексирования по `sessionId` — у каждого
target'а (браузер, страница, worker, OOPIF) своё соединение.

Требуется **Python 3.12+** (API использует дженерики PEP 695) и запущенный
Chromium/Chrome с включённой удалённой отладкой.

```bash
pip install parsek-cdp
```

## Быстрый старт

Запустите браузер с удалённой отладкой:

```bash
chromium --headless=new --remote-debugging-port=9222
```

И управляйте им:

```python
import asyncio
from parsek_cdp import Browser, Page, RequestListener


async def main():
    # `page_class` типизирует все страницы этого браузера как Page[RequestListener].
    browser = await Browser.connect_http(
        "http://127.0.0.1:9222", page_class=Page[RequestListener]
    )

    page = await browser.new_page()
    requests = page.get_feature(RequestListener)

    await page.navigate("https://example.com", wait_load=True)

    for r in requests.requests:
        status = r.response.status_code if r.response else "(ещё нет ответа)"
        print(r.method, r.url, "->", status)

    await browser.close()


asyncio.run(main())
```

## Концепции

### Targets и соединения

`Target` — это и есть одна CDP-сессия на собственном websocket'е. `Browser`,
`Page`, worker'ы и кросс-доменные iframe'ы (OOPIF) — всё это target'ы. Хост
DevTools привязывается один раз (в `contextvar`) в момент подключения к браузеру,
поэтому его не нужно прокидывать в каждый вызов.

Вся командная поверхность доступна через `target.cdp` — по атрибуту на каждый
CDP-домен, с типизированными методами и результатами:

```python
await page.cdp.Network.enable()
info = await page.cdp.Target.get_target_info()
```

Домены сами регистрируют своё включение/выключение при использовании, а
`domain_enabled` ограничивает домен областью блока:

```python
async with page.domain_enabled(page.cdp.Page):
    await page.cdp.Page.navigate(url="https://example.com")
```

### События

Регистрируйте обработчики на конкретном target'е или глобально на классе события:

```python
from parsek_cdp.cdp import Network

# на конкретном target'е
page.on(Network.RequestWillBeSent, lambda e: print(e.request.url))

# глобально, для каждого target'а
@Network.RequestWillBeSent.add_handler
async def on_request(e):
    print(e.request.url)

# дождаться одного события
loaded = await page.wait_for(Network.ResponseReceived, timeout=10)
```

Обработчики могут быть синхронными или асинхронными; падение одного обработчика
никогда не рушит соединение и не останавливает остальные.

### Страницы, фреймы и элементы

`Page` *сама является своим главным фреймом*, поэтому методы фрейма работают по
верхнему фрейму напрямую:

```python
el = await page.select(selector="h1")      # запрос к главному фрейму
print(el.text)
await el.fill("hello")
await el.mouse_click()

title = await page.evaluate("document.title")
```

Полное дерево фреймов (вложенные фреймы, кросс-доменные OOPIF — каждый прозрачно
маршрутизируется через свою сессию) живёт в `page.frames`. Контекстный менеджер
`page.with_same_navigation()` защищает блок от прерывания навигацией главного
фрейма.

### Контексты браузера

Страницы группируются в контексты браузера (профили в духе инкогнито). Контекст
по умолчанию хранит страницы, созданные без явного контекста:

```python
context = await browser.create_context()        # изолированный профиль
page = await context.new_page("https://example.com")
```

## Фичи

`Page` по умолчанию не подключает **никакого** поведения. *Фича* — это единица
поведения, которую вы подключаете явно, декларативно или императивно:

```python
from parsek_cdp import Page, RequestListener

Page[RequestListener]                 # декларативно — типизированный класс страницы
page.get_feature(RequestListener)     # императивно — подключается при первом обращении, типизировано
```

Ключевая идея: фича пишется **один раз** и работает в трёх ролях —

- **local** — напрямую к браузеру: продюсеры подписываются на сырой CDP на
  странице и редьюсят его в процессе (обычная локальная `Page`);
- **server** — прокси скармливает сырой CDP продюсерам, чей вывод эмитится
  клиенту как событие `Parsek.*` *и* редьюсится локально для снимков;
- **client** — выполняются только редьюсеры, питаемые этими событиями `Parsek.*`
  с провода.

Концептуально это две *стороны* — *producer* событий `Parsek.*` и *view* по ним, —
но producer-сторона существует и в процессе (`local`), и через провод (`server`).
Редьюсеры выполняются в каждой роли, поэтому публичный API фичи одинаков и для
локального браузера, и для браузера за прокси `parsek-cdp-server`.

### Кастомная фича — структура «как домен»

Фича повторяет раскладку сгенерированного CDP-домена (`cdp/<domain>/` =
*types · functions · events*). Оформляйте её отдельным пакетом из тех же трёх
файлов — тогда сам класс фичи становится её пространством имён:

```
features/<feature>/
  types.py       # wire-датаклассы + view-типы   (@parsek_type)
  events.py      # агрегированные события Parsek.* (@register_event)
  __init__.py    # сам класс Feature: domains + обработчики @on/@emit
```

Строительные блоки (всё из `parsek_cdp.core.feature`):

| Блок | Где | Что |
| --- | --- | --- |
| `domains = (Network, ...)` | класс фичи | CDP-домены, которыми владеет фича — авто-включаются, а их сырые события подавляются в passthrough к клиенту |
| `@on(Event)` | метод | регистрирует обработчик. **CDP**-событие делает его *producer* (server/local); событие **`Parsek.*`** делает его *reducer* (во всех ролях) |
| `@emit(ParsekEvent)` | метод-producer | возвращаемое значение публикуется клиенту **и** редьюсится локально — состояние строится одним и тем же кодом везде |
| `@parsek_type("Parsek.<Feature>.<Type>")` | `types.py` | объявляет wire-датакласс; `__FIELDS__` выводятся из аннотаций (snake_case ↔ camelCase) |
| `@register_event("Parsek.<Feature>.<event>")` | `events.py` | объявляет класс агрегированного события |
| `snapshot()` | класс фичи | состояние для поздно подключившегося клиента (сервер может переиграть его при коннекте) |
| `attach_namespace(Feat, types, events)` | конец `__init__.py` | выносит типы/события атрибутами на класс фичи (`Feat.RequestData`, `Feat.RequestSent`, ...) |

Набросок — producer, сворачивающий пачку сырого CDP в одно событие `Parsek.*`,
и редьюсер, восстанавливающий из него состояние:

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
    domains = (SomeDomain,)                 # во владении + авто-включение

    @on(SomeDomain.SomethingRaw)            # CDP-событие -> producer
    @emit(ThingHappened)                    # return уходит клиенту + редьюсится
    def _produce(self, e) -> ThingHappened:
        return ThingHappened(payload=ThingData(...))

    @on(ThingHappened)                      # Parsek-событие -> reducer (обе роли)
    def _reduce(self, e: ThingHappened) -> None:
        self._things.append(e.payload)

    @property
    def things(self):                       # удобный публичный API
        return list(self._things)

attach_namespace(MyFeature, _types, _events)
```

`RequestListener` (ниже) — эталонная реализация ровно этой структуры.

### `RequestListener`

Встроенная фича: агрегированное наблюдение за сетью. Записывает каждый запрос
текущего документа вместе с ответом, заголовками и таймингами:

```python
requests = page.get_feature(RequestListener)
await page.navigate("https://example.com", wait_load=True)

# все запросы текущего документа
for r in requests.requests:
    print(r.method, r.url, r.response.status_code)

# найти / дождаться конкретного (подстрока или скомпилированный regex по URL)
r = await requests.wait_for_response("/api/orders", timeout=30, load_body=True)
print(r.response.status_code, await r.response.body())
```

По умолчанию лог очищается при навигации главного фрейма (как в DevTools с
выключенным *Preserve log*); передайте `preserve_log=True`, чтобы сохранять его
между документами.

## Удалённые браузеры (с `parsek-cdp-server`)

Установите опциональный серверный дистрибутив, чтобы запускать браузеры и
надзирать за ними за прокси:

```bash
pip install parsek-cdp[server]
```

Затем подключайтесь к запущенному серверу вместо локального Chrome — API
идентичен, а объявленные фичи агрегируются на стороне сервера:

```python
browser = await Browser[Page[RequestListener]].get_distant_browser(
    "http://127.0.0.1:9333", headless=True
)
page = await browser.new_page("https://example.com")
```

Про запуск сервера, надзор за жизненным циклом, метрики и reaper зомби-процессов
см. пакет [`parsek-cdp-server`](https://github.com/xa1era/parsek-cdp).

## Лицензия

Apache-2.0.