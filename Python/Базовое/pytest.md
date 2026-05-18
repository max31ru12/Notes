## Параметризация тестов

```python
@pytest.mark.parametrize("x, y",  [(1,2), (3,4)])
async def test_smth(x, y):
	...
```

- `"x, y"` - параметры, каоторые принимает тест
- `[(1,2), (3,4)]` - список кортежей параметров, которые передаются в тест


## Обработка исключений
1. Обработка всех тестов
```python
with pytest.raises(TypeError):
    assert ...
```

2. Переменная для ошибки

```python
@pytest.mark.parametrize("x, y, expectation",
			    [
					(1, 2, do_not_raise()),  # не вызывает ошибку
					(5, "3", pytest.raises(TypeError)),	 # вызывает ошибку
			    ])
```


 `expectation` (передаем переменную для ошибки)

## Фикстуры
- Создают среду для тестирования (БД, токены и прочее)
- Отдают часто используемые данные

 1) Создаем функцию 
 2) Помечаем как фикстуру 
 3) Передаем как параметр в любой тест 
 4) Pytest сам понимает, что это фикстуры

```python
@pytest.fixture(scope="")
async def fixture_func_name():
    return some_data
```

Накидывание фикстур вручную:
```python
@pytest.mark.usefixtures("fixture_func_name")
async def some_smth():
    assert ...
```

### Scope фикстур

1) `session` - для всех прогонов тестов
2) `package` - на уровне папки
3) `module` - на уровне файла
4) `function` - на уровне функции
5) `class` - ???

>  По дефолту `function`






### Mock функций


#### Объекты-заглушки с помощью SimpleNamespace

`SimpleNamespace` — это очень простой объект, в который можно складывать поля “как попало”, почти как в `dict`, но доступ к значениям идет через точку.

```python
from types import SimpleNamespace

user = SimpleNamespace(id=1, name="Max")

print(user.id) # 1  
print(user.name) # Max
```


#### Подмена объекта/функции на время выполнения теста

Патчить надо там, где функция вызывается - `"app.module.get_user_name"`, а не там, где объявляется   

```python
from unittest.mock import patch

with patch("app.module.get_user_name") as mock_get_user_name:
	mock_get_user_name.return_value = "Test User"  
	result = some_function()
```


##### 1. `patch("app.module.get_user_name")`

Это означает: возьми функцию `get_user_name` в модуле `app.module`  
и временно замени её на мок-объект

То есть:

`app.module.get_user_name = Mock()`

##### 2. `as mock_get_user_name`

Это просто ссылка на этот мок

##### 3. `mock_get_user_name.return_value = "Test User"`

Это значит: "когда этот мок вызовут как функцию → верни `'Test User'`"

##### 4. `some_function()` 
Это функция, где внутри выполняется та функция, которую мы замокали (мы замокали выполнение `get_user_name`, которая вызывается в `some_function`)

#### Пример

```python
from types import SimpleNamespace  
from unittest.mock import patch, AsyncMock  
  
fake_user = SimpleNamespace(id=1, name="Max")  
  
with patch("app.use_cases.user_service.get_user", new=AsyncMock(return_value=fake_user)):  
    result = await some_async_function()
```

Тут:

- `fake_user` — простая заглушка-объект
- `patch(...)` — временно заменил `get_user`
- `AsyncMock(...)` — сделал поддельную async-функцию
- при `await get_user()` вернется `fake_user`
- `some_adync_function` - это асинхронная функция, где выполняется та функция, которую мы хотим замокать
