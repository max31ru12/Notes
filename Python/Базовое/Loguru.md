
## Логирование

```python
logger.add(
	"logs/errors.log", 
	rotaion="30 days",
	level="INFO",
	backtrace=True,
	diagnose=True,
)
```

- `backtrace` - красивый traceback
- `diagnose` - добавляет локальные переменные в **traceback**


### Функции логирования

- `logger.error(f"Error happened: {e}")` - только текст ошибки
- `logger.exception("Exception occurred")` - текст + traceback
- 

### Уровни
1. DEBUG - что происходит под капотом
2. INFO - что-то произошло в бизнес логике
3. WARNING - подозрительно, но не критично
4. ERROR - операция не удалась
5. CRITICAL - сервис упал



##### Что логировать в FastAPI-проектах

###### Входящие HTTP-запросы

- метод
- путь
- статус ответа
- время обработки
- request_id / correlation_id

```
INFO  GET /users/42 200 15ms
```

###### Ошибки и исключения

- stack trace
- тип ошибки
- контекст запроса

```
ERROR  DB timeout user_id=42
```


###### Бизнес-события

- создание пользователя
- успешная оплата
- изменение статуса заказа

###### Вызовы внешних сервисов

- URL / сервис
- тайминги
- таймауты
- коды ответа

```
WARNING  payment-service timeout 3s
```

