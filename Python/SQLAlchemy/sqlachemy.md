
## Конфигурация SQLAlchemy

1. Создаем движок

```python
from sqlalchemy.ext.asyncio import create_async_engine

engine = create_async_engine(url=f"postgresql+asyncpg://user:password@host:port/db_name")
```

Соединение через движок: `async with engine.connect()`

2. Создаем метаданные

```python
from sqlachemy import MetaData

metadata = MetaData()
```

Вариант через `declarative_base`
```python
from sqlalchemy.orm import declarative_base()

Base = declarative_base()  # затем наследуем Base в моделях 
```

Вариант через класс
```python
from sqlachemy.orm import DeclarativeBase

class Base(DeclarativeBase):  # класс Base родитель для таблиц
    ...
```


3. Создать таблицы через metadata

```python
# Синхронный вариант 
metadata.create_all(engine)

# Асинхронный вариант
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(meta_data.create_all)
```
Метадату можно взять из `Base.metadata`





# Результаты выполнения

```python
res = await conn.execute(stmt) # тут что-то непонятное
res.all()                      # тут список кортежей [(), ]
res.scalar()                   # выводим сразу строчку без списков (что-то одно)
res.scalars()                  # много объектов (нечитабельно)
res.scalars().all()            # список объектов (читабельно)

```

# Метаданные

**Метаданные** - это информация о том, как мы вставляем данные в таблицы и как работает с данными

Один объект **метаданных** отвечает за одну базу данных (за одну схему). **Метаданные** содержат информацию о таблицах (и не только).


# Поля таблицы

```python
class User(Base):
    __tablename__ = "users"

    # можно переопределить тип поля: mapped_column(String(100), primary_key=True)
    id: Mapped[int] = mapped_column()  # Базовый способ
```

Можно использовать общие поля с помощью `Annotated`:
```python
intpk = Annotated[int, mapped_column(primary_key=True)]  # общее поле

id: Mapped[intpk] = ...  # в таблице
```


# Вставка данных

## Core

```python
from sqalchemy import insert

stmt = insert(table).values(name="", ...)
```

## ORM

```python
# Синхронный вариант
with session_factory() as session:
    session.add(user_obj)
    session.commit()


# Асинхронный вариант
async with async_session_factory() as session:
    session.add(user_obj)
    await session.commit()
```

# Выборка данных

```python
from sqlalchemy import select

# можно указывать несколько условий в формате table.c.column ==
select(table).where(table.c.name == "Test", ...)
```

### Выборка столбцов, алиасы
```python
# Выборка двух полей таблицы
select(table.c.column_1, table.c.column_2)
# Объединить две колонки
select(table.c.column_1 + table.c.column_2)
# Добавить Alias
select(table.c.column).label("ALIAS")
```

### Условия выборки `table.c.column`:
- `startswith("Test")`
- `contains("3")`
- `in_([1, 2, ...])`

### Условия AND и OR
``` python
select(table).where(or_(conditions))  # OR

select(table).where(and_(conditions))  # AND
```

### Сортировка `ORDER BY`

```python
# первый вариант
select(table).order_by(table.c.column)  # ASC
# второй вариант (ИМХО БОЛЕЕ ЛАКОНИЧНЫЙ)
select(table).order_by("column")

# Обратный порядок
select(table).order_by(desc(table.c.column))  # DESC
# второй вариант DESC (ИМХО БОЛЕЕ ЛАКОНИЧНЫЙ)
select(table).order_by(table.c.column.desc())  # DESC
```

### Группировка `GROUP BY`
```python
# всё как у order_by
select(table).group_by("column")
```

### Соединения таблиц `JOIN'ы`

Есть также `outerjoin()`, `outerjoin_from()`

#### Явное задание двух таблиц для соединения
```python
# Указываем обе таблицы (без условия)
select(table_1.c.email, table_2.c.name).join_from(table_1, table_2)
# Явно указываем условия
select(...).join_from(table_1, table_2, table_1.c.id == table_2.c.user_id)
```

#### 
```python
select(table_1, table_2).join(table_2)
```

## Удаление и обновление (UPDATE, DELETE)

**UPDATE** - обновление данных
```python
update(table).where(table.c.column == "...").values(column="new")
```

**DELETE** - удаление данных
```python
stmt = delete(table).where(condition)  # удаление
conn.execute(stmt).rowcount  # кол-во удаленных строчек
```

**RETURNING** - есть у INSERT, UPDATE, DELETE
```python
delete(table).where(condition).returning(table.c.column)
```
дальше пременяем scalars, all и тд.




# ORM SQLACHEMY

## Сессии

Сессия `Session` нужна для транзакций. Входим в сессию - открываем транзакицю, затем завершаем тразакцию (закрываем сессию). 

**Без фабрики:**

```python
from sqlachemy.orm import Session

with Session(engine) as session:
    ...
```

**Фабрика сессий:**

```python
# from sqlachemy.ext.asyncio import async_sessionmaker
from sqlachemy.orm import sessionmaker 

session = sessionmake(engine)

with session() as session:
    ...
```


`session.flush()` - перекинуть данные из объектов в транзакцию

`session.commit()` - завершить транзакицю

`session.rollback()` - откатить транзакцию

Состояния объектов в сессии:

- **Transient (временный)** - до добаления в сессию (объект в питоне, но не в БД)
- **Pending (ожидающий)** - добавлен в сессию `session.add`, но еще не в БД 
- **Persistent (постоянный)** - находится в сессии и имеет ассоциацию с записью в БД
- **Deleted (удаленный)** - в БД запись существует, но объект помечен для удаления
- **Detached (отсоединенный)** - отсединен от сессии и не факт, что эти данные актуальны

## Вставка данных с помощью сессий

```python
# Синхронный вариант
with session_factory() as session:
    session.add(user_obj)
    session.commit()


# Асинхронный вариант
async with async_session_factory() as session:
    session.add(user_obj)
    await session.commit()
```




# Relationships

[Видео по связям в SQLAchemy](https://www.youtube.com/watch?v=kFp9fdv9i_I&list=PLN0sMOjX-lm5Pz5EeX1rb3yilzMNT6qLM&index=10)

## Lazy Load (N + 1 Problem)

Получим записи из таблицы `A`. Пройдемся по полученным записям циклом и для каждой из них делаем отдельный запрос в таблицу `B`, чтобы получить связанные записи из таблицы B для полученных записей из таблицы `A`. 

В результате получается `1 запрос` для таблицы `A` = `N записей` и `N запросов` для таблицы `B` (по одному запросу для каждой полученной записи из таблицы `A`)


[Calculate timestamps within your DB, not your client
For sanity, you probably want to have all datetimes calculated by your DB server, rather than the application server. Calculating the timestamp in the application can lead to problems because network latency is variable, clients experience slightly different clock drift, and different programming languages occasionally calculate time slightly differently.

SQLAlchemy allows you to do this by passing func.now() or func.current_timestamp() (they are aliases of each other) which tells the DB to calculate the timestamp itself.

Use SQLALchemy's server_default
Additionally, for a default where you're already telling the DB to calculate the value, it's generally better to use server_default instead of default. This tells SQLAlchemy to pass the default value as part of the CREATE TABLE statement.

For example, if you write an ad hoc script against this table, using server_default means you won't need to worry about manually adding a timestamp call to your script--the database will set it automatically.

### [Understanding SQLAlchemy's onupdate/server_onupdate](https://stackoverflow.com/questions/13370317/sqlalchemy-default-datetime)


