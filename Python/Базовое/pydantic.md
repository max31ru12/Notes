


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







