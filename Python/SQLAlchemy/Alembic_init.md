
## Configuration 

Initialize alembic with **asynchronous** support:

```shell
alembic init -t async alembic-dir-name
```

Default alembic initialization:

```shell
alembic init alembic-dir-name
```

### File `alembic.ini`

Rewrite (set database url). Лучше не трогать, а задать через `env.py` :

`sqlalchemy.url = driver://test:test@localhost:5432/test`

Set path to alembic directory

`# prepend_sys_path = . path_to_migrations_dir`


### File `env.py`

Set the following options

```python
# Async version (Добавить строчку)
config.set_main_option("sqlalchemy.url", DB_URL + "?async_fallback=True")

# Sync version 
...?

# metadata
target_metadata = db_meta
```

## Alembic commands

Create migrations:

```shell
alembic revision --autogenerate -m "Initial" --rev-id "001"
```

Migrate:

```shell
alembic upgrade head
```

Откатить все миграции:

```shell
alembic downgrade base
```

Посмотреть текущую примененную миграцию:

```shell
docker compose -f .\local.yml run --rm backend alembic current
```

## Конфликт Alembic с ручным созданием таблиц

Для управления БД с помощью Alembic не стоит вручную создавать базу данных с помощью:

```python
@app.on_event("startup")  
async def init_database():  
    async with async_engine.begin() as connection:  
        await connection.run_sync(Base.metadata.create_all)
```

