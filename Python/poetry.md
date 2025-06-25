
## Инициализация

`poetry init` - инициализировать пакетный менеджер poetry в папке, если уже есть какой-то проект, и хотим добавить poetry


- `pyproject.toml` - автоматически создается файл в зависимостями
- `poetry.lock` - позволяет гораздо быстрее работать с установкой пакетов

`poetry new tmp` - создается структура проекта:
```yaml
pyproject.toml
README.rst
test
    __init__.py
test_tmp.py
tmp
	__init__.py
```

## Poetry для виртуального окружения: 
### Создать виртуальное окружение
 ```shell
 poetry env use python3.11
 ```

### Активировать виртуальное окружение

 ```shell
poetry shell # создать
exit # выйти
 ```

### Запустить команду без активации env

```shell
poetry run uvicorn # запустить команду (или Python, например) из evn
```


## Poetry, библиотеки и зависимости:

### Установить библиотеку

`poetry add requests` 

### Установить пакет определенной версии
`poetry add requests@version` 

### Работа с dev-зависимостями

#### Установить dev-зависимость

```shell
poetry add --dev requests
```

#### Установить пакеты без dev-зависимостей

```shell
poetry install --without dev
```

#### Установить с dev-зависимостями (поведение по умолчанию)

```shell
poetry install --with dev
```

## Обновление либы

### Выпустить новую версию

```shell
poetry version patch   # или: minor / major
```

Примеры:

- **patch** → 0.1.1 → 0.1.2
- **minor** → 0.1.2 → 0.2.0
- **major** → 0.2.5 → 1.0.

### Собрать пакет

```shell
poetry build
```

### Опубликовать пакет

```shell
poetry publish --build # Опционально можно забилдить
```


## Если poetry не видит актуальную версию библиотеки

```shell
poetry cache clear pypi --all
```