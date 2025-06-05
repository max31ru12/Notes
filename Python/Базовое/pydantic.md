


```python
user.model_dump()           # создает словарь полей и значений модели
user.model_copy()           # создает неглубокую копию модели
user.model_dump_json()      # создает JSON-строку модели
```


#### Описание полей
```python
user.model_fields           # возвращает множество имен полей модели
```

## Валидация данных из ORM своих классов

Задаем `model_config`:

```python
class UserData(BaseModel):
	username: str
	password: str
	
	model_config = {
		"from_attributes": True
	}
```

Получаем **Pydantic-модель** из модели **User**:

```python
user = await get_user_db(...)  # Модель алхимии
user_pydantic_model = User.from_orm(user)  # Модель pydantic
```


Остальные ограничения для разных типов - https://docs.pydantic.dev/latest/concepts/fields/

### 🧩 Основные параметры `model_config`

Настройка поведения модели

| Параметр               | Описание                                                       |
| ---------------------- | -------------------------------------------------------------- |
| `str_strip_whitespace` | Автоматически убирает пробелы у всех строк (`str`)             |
| `extra`                | Контроль лишних полей: `"ignore"`, `"allow"`, `"forbid"`       |
| `populate_by_name`     | Позволяет использовать имена полей Python вместо alias         |
| `from_attributes`      | Позволяет создавать модель из ORM-объекта (`.from_orm`)        |
| `json_schema_extra`    | Добавляет описание и примеры в OpenAPI                         |
| `frozen`               | Делает модель иммутабельной (как `frozen=True` в dataclass)    |
| `strict`               | Включает строгую типизацию (напр., `int("1")` вызывает ошибку) |





