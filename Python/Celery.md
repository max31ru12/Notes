
#### Полезные ссылки

- [Конфигурация бэкенда](https://docs.celeryq.dev/en/stable/userguide/configuration.html#conf-database-result-backend)
- [Подружить Celery и асинхронный SQLAlchemy](https://habr.com/ru/articles/721186/)



## Простое использование

### "shared_task" decorator







## Базовая конфигурация

`Celery` требует брокер сообщений для отправки и получения сообщений, например, `RabbitMQ` или `Redis`.

```python
from celery import Celery  
  
  
app = Celery(
			 "tasks", 
			 broker="pyamqp://guest@localhost//",
			 backend="db+postgresql://test:test@localhost/test",
			 )  
  
  
@app.task  
def add(x, y):  
    return x + y
```

- `tasks` - имя текущего модуля
- `pyamqp://guest@localhost//` - аргумент, который указывает URL брокера (в данном случае для RabbitMQ) 
- `backend` - база данных, куда складывается результат работы тасок

### Запустить celery-worker

```shell
celery -A tasks worker --loglevel=INFO
```

### Вызвать таску 

```python
from app.tasks import add


add.delay(4, 4)
```

Вызов таски с помощью `delay()` вернет `AsyncResult`. Результат не доступен по дефолту. Для получения результата необходимо прописать параметр `backend` для инстанса **Celery**.


