# Celery: `delay()` vs `apply_async()`

## Кратко

- `delay()` — простой способ поставить задачу в очередь.
- `apply_async()` — полный API для отправки задач с дополнительными настройками.

Фактически:

```python
task.delay(arg1, arg2)
```

эквивалентно:

```python
task.apply_async(args=(arg1, arg2))
```

---

# delay()

## Когда использовать

Используй `delay()`, если:

- нужно просто выполнить задачу в фоне;
- не нужны отдельные очереди;
- не нужны задержки выполнения;
- не нужны приоритеты;
- не нужны дополнительные настройки.

## Пример

```python
send_email_task.delay(
    to="user@example.com",
    subject="Welcome",
    body="Hello!"
)
```

Celery:

1. сериализует аргументы;
2. кладёт задачу в очередь;
3. worker её забирает и выполняет.

---

# apply_async()

## Когда использовать

Используй `apply_async()`, если нужно:

- отправить задачу в конкретную очередь;
- выполнить задачу позже;
- выполнить задачу в конкретное время;
- задать приоритет;
- задать срок жизни задачи;
- использовать дополнительные возможности Celery.

## Пример

```python
send_email_task.apply_async(
    kwargs={
        "to": "user@example.com",
        "subject": "Welcome",
        "body": "Hello!"
    }
)
```

---

# Основные возможности apply_async()

## Передача аргументов

Позиционные аргументы:

```python
task.apply_async(
    args=(1, 2)
)
```

Именованные аргументы:

```python
task.apply_async(
    kwargs={
        "a": 1,
        "b": 2,
    }
)
```

---

## Отправка в конкретную очередь

```python
task.apply_async(
    kwargs={...},
    queue="emails",
)
```

Полезно, когда есть несколько worker'ов:

```text
emails-worker
reports-worker
notifications-worker
```

---

## Выполнить через N секунд

```python
task.apply_async(
    kwargs={...},
    countdown=60,
)
```

Задача начнёт выполняться через минуту.

---

## Выполнить в конкретное время

```python
from datetime import datetime, timedelta

task.apply_async(
    kwargs={...},
    eta=datetime.utcnow() + timedelta(hours=1),
)
```

Задача выполнится через час.

---

## Приоритет задачи

```python
task.apply_async(
    kwargs={...},
    priority=5,
)
```

Требует настройки брокера и очередей.

---

## Срок жизни задачи

```python
task.apply_async(
    kwargs={...},
    expires=3600,
)
```

Если worker не успеет взять задачу за час — задача будет удалена.

---

# Когда что использовать

## Используй delay()

Если нужно просто:

```python
send_email_task.delay(...)
```

или

```python
generate_pdf_task.delay(...)
```

---

## Используй apply_async()

Если нужно:

```python
send_email_task.apply_async(
    kwargs={...},
    queue="emails",
)
```

или

```python
send_email_task.apply_async(
    kwargs={...},
    countdown=300,
)
```

или

```python
send_email_task.apply_async(
    kwargs={...},
    eta=some_datetime,
)
```

---

# Практическое правило

### Для большинства задач

```python
task.delay(...)
```

### Как только нужна хоть одна дополнительная настройка

```python
task.apply_async(...)
```

---

# Что чаще встречается в реальных проектах

Простые проекты:

```python
task.delay(...)
```

Проекты с несколькими очередями:

```python
task.apply_async(
    queue="emails",
)
```

Проекты с отложенными задачами:

```python
task.apply_async(
    countdown=300,
)
```

или

```python
task.apply_async(
    eta=some_datetime,
)
```

Во всех остальных случаях `apply_async()` является базовым и наиболее гибким способом постановки задач в очередь.