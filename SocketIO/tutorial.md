# A Python-SocketIO tutorial 

Функции `def connect(sid, environ)` и `def disconnect(sid)` имеют зарезервированные имена (SocketIO сам их подхватывает)

## События

 Событие при отправке на сервер - это `message` по тому, что указывали в декораторе

```py
@sio.on("message")  # Тут указывается имя события
def incoming_message(sid, data):
    pass
```

Событие при отправке на сервер - это `get_users` по имени функции

```py
@sio.event
def get_users(sid, data):
    pass
```

```py 
@sio.on("*")  # универсальный обработчик событий
def catch_all(event: str, sid, data):
    pass
```


## Отправка событий

В Postman необходимо включить получаемые события во вкладке `events`

```py
sio.emit(event="event_name", data="", to=sid)
```

## Статика SocketIO

```py
static_files = {"/": "static/index.html"}


sio = AsyncServer(async_mode="asgi")
socket_app = ASGIApp(
    socketio_server=sio, 
    static_files=static_files
)
```


## Использование SocketIO с FastAPI

По сути надо просто прокинуть FastAPI (или другое) приложение в ASGI/WSGI-приложение SocketIO

```py
app = FastAPI()

sio = socketio.AsyncServer(async_mode='asgi')
app = socketio.ASGIApp(
    socketio_server=sio,  # sio-сервер
    other_asgi_app=app,  # FastAPI-приложение
)

if __name__ == "__main__":
    uvicorn.run(app, host='', port=80)
```

> Но зачем ??? В микросервисах так делать не стоит, стоит только в монолитах (но это не факт)


## Комнаты в SocketIO

Добавить в комнату `(создает комнату при ее отсутствии)`:  

```py
sio.enter_room(
    sid: str = sid,
    room: str = "room_name",
)
```

Покинуть комнату

```py
sio.leave_room(sid, room: str = "room_name")
```

Удалить комнату

```py
sio.close_room(room: str = "room_name")
```

> `sid` подключения также создает отдельную комнату, **но зачем ???**

Получить все комнаты пользователя

```py
sio.rooms(sid)
```

Отправить сообщение в комнату (просто добавляем параметр `room`):

```py
sio.emit(... , room: str = room)
```


## Сессии в SocketIO

Сессии внутри SocketIO привязаны к `sid`. Данные сессии при переподключении будут потеряны. Сессии не передаются между разными `Namespace`. 

Запись данных в сессию
```py
sio.save_session(sid, session={"name": name})
```

Получение данных из сессии
```py
[await] sio.get_session(sid).get("name")
```


## Клиент SocketIO

```py
import socketio

# Создание клиента сокета
sio = socketio.SimpleClient()

# Подключение к серверу
sio.connect('ws://0.0.0.0:80')
```

Получить или отправить сообшение

```py
event, data = sio.receive()

sio.emit("send_message", {"text": "hello"})
```
