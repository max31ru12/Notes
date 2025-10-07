
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