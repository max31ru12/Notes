
### Инициализация

`poetry init` - инициализировать пакетный менеджер poetry в папке 
	    - если уже есть какой-то проект и хотим добавить poetry

+ЭТИ ФАЙЛЫ НАДО ДОБАВЛЯТЬ В РЕПОЗИТОРИЙ

`pyproject.toml` - автоматически создается файл в зависимостями
`poetry.lock` - позволяет гораздо быстрее работать с установкой пакетов
_______________________________________________________________________

poetry new tmp - создается структура проекта:
```yaml
pyproject.toml
README.rst
test
    __init__.py
test_tmp.py
tmp
	__init__.py
```

### Poetry для виртуального окружения: 

`poetry env use python3.11` 	- создать виртуальное окружение
`poetry shell` - активировать виртуальное окружение
`exit` - выйти из evn
`poetry run uvicorn` - запустить команду (или Python, например) из evn


	Poetry, библиотеки и зависимости:

УСТАНОВЛЕННЫЕ БИБЛИОТЕКИ САМИ ЗАПИСЫВАЮТСЯ В ФАЙЛ pyproject.toml

`poetry add requests` - установить библиотеку requests
`poetry add requests@version` - установить пакет определенной версии

`poetry add --dev requests` - установить библиотеку для разработки (в раздел dev-dependencies)


`poetry show --latest`		- версии пакетов и их более новые (если они есть)

`poetry install --with dev` - установить с dev зависимостями


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