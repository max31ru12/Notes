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


















