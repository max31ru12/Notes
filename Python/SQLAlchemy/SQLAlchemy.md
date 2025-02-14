
## Конфигурация SQLAlchemy

### 1\. Создаем движок

```python
from sqlalchemy.ext.asyncio import create_async_engine

async_engine = create_async_engine(  
    url=f"postgresql+asyncpg://user:password@host:port/db_name",
    echo=True,  
    pool_size=10,  
    max_overflow=20,  
)
```

10 подключений к БД, + 20 дополнительных при необходимости. Соединение через движок: `async with engine.connect()`

### 2\. Создаем метаданные

```python
from sqlachemy import MetaData

metadata = MetaData()
```

Вариант через `declarative_base`:

```python
from sqlalchemy.orm import declarative_base()

Base = declarative_base()  # затем наследуем Base в моделях 
```

Вариант через класс:

```python
from sqlachemy.orm import DeclarativeBase

class Base(DeclarativeBase):  # класс Base родитель для таблиц
    ...
```


### 3\. Создать таблицы через metadata

```python
# Синхронный вариант 
metadata.create_all(engine)

# Асинхронный вариант
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(meta_data.create_all)
```

Метадату можно взять из `Base.metadata`

### 4\. Создать `sessionmaker`

```python
from sqlalchemy.ext.asyncio import async_sessionmaker

session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(  
    bind=async_engine,  
    autoflush=False,  
    autocommit=False,  
    expire_on_commit=False,  
)
```

##### Параметры только для асинхронной алхимии

- `expire_on_commit` - при коммите все модели в сессии помечаются как **expired**, это значит, что при обращении к атрибуту автоматически делается запрос в базу с помощью `await`
- `autoflush`
- `autocommit`


5. Создать все таблицы (Для FastAPI)

```python
from app.setup_db import async_engine, Base


@app.on_event("startup")  
async def init_database():  
    async with async_engine.begin() as connection:  
        await connection.run_sync(Base.metadata.create_all)
```


### Требования уникальных ограничений

Для того, чтобы в миграция имена ограничений были не `None`, необходимо задать **naming_conventions** в классе **Base**:

```python
CONVENTION = {  
    "ix": "ix_%(column_0_label)s",  
    "uq": "uq_%(table_name)s_%(column_0_name)s",  
    "ck": "ck_%(table_name)s_%(constraint_name)s",  
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",  
    "pk": "pk_%(table_name)s",  
}

class Base(DeclarativeBase):  
    metadata = MetaData(naming_convention=CONVENTION)
```

По умолчанию есть convention только для (то есть для первичного ключа)





# Результаты выполнения

```python
res = await conn.execute(stmt) # тут что-то непонятное
res.all()                      # тут список кортежей [(), ]
res.scalar()                   # выводим сразу строчку без списков (что-то одно)
res.scalars()                  # много объектов (нечитабельно)
res.scalars().all()            # список объектов (читабельно)

# Когда возвращается одна запись
res.scalar_one_or_none() # Вернут None при отсутствии
res.scalar_one() # Вызовет исключение при отсутствии
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


### Атрибуты mapped_column

- `default` - когда создается на стороне алхимии
- `server_default` - когда создается на стороне сервера БД (если пишем, например, с помощью чистого SQL-запроса)
- `nullable` - может быть **NULL**


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
select(table.column_1, table.c.column_2)
# Объединить две колонки
select(table.column_1 + table.c.column_2)
# Добавить Alias
select(table.column).label("ALIAS")
```

### Условия выборки `table.column`:
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

## Соединения таблиц `JOIN'ы`

| Способ          | Когда использовать?                        | SQL-запрос                  |
|----------------|--------------------------------|----------------------------|
| `joinedload()` | Если **всегда нужен** `Brand` (быстро) | `JOIN` в одном SQL-запросе |
| `selectinload()` | Если `Car` **много** (экономит память) | Два SQL-запроса (меньше дубликатов) |
| `join()` | Если нужен `JOIN` + фильтр (`WHERE`, `GROUP BY`) | `INNER JOIN` |
| `outerjoin()` | Если у некоторых `Car` нет `Brand` | `LEFT JOIN` |


### joinedload()

```python
select(Car).options(joinedload(Car.brand))
```

- join делается на уровне SQL-запроса
- без дополнительных запросов к БД

### selectinload()

Отложенная загрузка. Не использует `join`, поэтому работает быстрее для больших таблиц

```python
select(Car).options(selectinload(Car.brand))
```

- загружает *car*
- потом загружает *brand*

Делает запрос вида:

```sql
SELECT * FROM cars;
SELECT * FROM brands WHERE brands.id IN (1, 2, 3, ...);
```

### Явный join()
`
```python
select(Car).join(Brand).where(Brand.name == brand_name)
```

- делает `INNER JOIN`
- Позволяет фильтровать данные по `Brand`
- Используется для отчетов, агрегации, сложных фильтров

Есть также `outerjoin()`, `outerjoin_from()`

### outerjoin()

`outerjoin()` делает SQL `LEFT JOIN`, что включает `Car`, даже если у него нет `Brand`

```python
select(Car, Brand).outerjoin(Brand)
```

## Удаление и обновление (UPDATE, DELETE)

**UPDATE** - обновление данных
```python
update(table).where(Model.column == "...").values(column="new")
```

**DELETE** - удаление данных
```python
stmt = delete(Model).where(condition)  # удаление
conn.execute(stmt).rowcount  # кол-во удаленных строчек
```

**RETURNING** - есть у INSERT, UPDATE, DELETE
```python
delete(Model).where(condition).returning(table.c.column)
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



