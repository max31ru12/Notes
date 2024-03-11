ПАРАМЕТРИЗАЦИЯ ТЕСТОВ:

@pytest.mark.parametrize("x, y", 		- какие аргументы принимает тест
			 [(1,2), (3,4)])	- какие значения подставляем
async def test_smth(x, y)



ОБРАБОТКА ИСКЛЮЧЕНИЙ:
1. Обработка всех тестов
with pytest.raises(TypeError):
    assert ...

2. @pytest.mark.parametrize("x, y, expectation", 	- expectation: (передаем переменную для ошибки)
			    [
				(1, 2, do_not_raise()),			- не вызывает ошибку
				(5, "3", pytest.raises(TypeError)),	- вызывает ошибку
			    ])


ФИКСТУРЫ:

1) Создают среду для тестирования (БД, токены и прочее)
2) Отдают часто используемые данные

# Создаем функцию -> помечаем как фикстуру -> передаем как параметр в любой тест
# Pytest сам понимает, что это фикстуры


@pytest.fixture(scope="")
async def fixture_func_name():
    return some_data


накидывание фикстур вручную:
@pytest.mark.usefixtures("fixture_func_name")
async def some_smth():
    assert ...


SCOPE

1) session 	- для всех прогонов тестов
2) package 	- на уровне папки
3) module 	- на уровне файла
4) function 	- на уровне функции
5) class	- ???

# по дефолту "function"

















