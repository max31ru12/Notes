from models import metadata_obj, workers_table
from database import sync_engine, async_engine
from sqlalchemy import text, insert, select, update


def create_tables():
    # Сначала удаляем все таблицы
    metadata_obj.drop_all(sync_engine)
    # Передаем движок базы данных
    metadata_obj.create_all(sync_engine)


class SyncCore:
    @staticmethod
    def create_tables():
        sync_engine.echo = False
        metadata_obj.drop_all(sync_engine)
        metadata_obj.create_all(sync_engine)
        sync_engine.echo = True

    @staticmethod
    def insert_workers():
        with sync_engine.connect() as conn:
            stmt = insert(workers_table).values(
                [
                    {"username": "Jack"},
                    {"username": "Michael"},
                ]
            )
            conn.execute(stmt)
            conn.commit()

    @staticmethod
    def select_workers():
        with sync_engine.connect() as conn:
            query = select(workers_table) # SELECT * FROM WORKERS
            result = conn.execute(query)
            workers = result.all() # .one, .one_or_none
            print(workers)

    @staticmethod
    def update_worker(worker_id: int, new_username: str):
        with sync_engine.connect() as conn:
            # сырой запрос
            # stmt = text("UPDATE workers SET username=:new_username WHERE id=:id;")
            # stmt.bindparams(new_username=new_username, id=worker_id)
            stmt = update(workers_table)\
                .values(username=new_username).filter_by(id=worker_id)
                # неудобный вариант фильтра c - column (обязательно именно 'c')
                # .where(workers_table.c.id == worker_id)\

            conn.execute(stmt)
            conn.commit()
            pass



class AsyncCore:
    # Асинхронный вариант, не показанный в видео
    @staticmethod
    async def create_tables():
        async with async_engine.begin() as conn:
            await conn.run_sync(metadata_obj.drop_all)
            await conn.run_sync(metadata_obj.create_all)
            async_engine.echo = True

    @staticmethod
    async def insert_workers():
        async with async_engine.connect() as conn:
            stmt = insert(workers_table).values(
                [
                    {"username": "Jack"},
                    {"username": "Michael"},
                ]
            )
            await conn.execute(stmt)
            await conn.commit()

    @staticmethod
    async def select_workers():
        async with async_engine.connect() as conn:
            query = select(workers_table)
            result = await conn.execute(query)
            workers = result.all()
            print(f"{workers=}")

    @staticmethod
    async def update_worker(worker_id: int, new_username):
        async with async_engine.connect() as conn:
            stmt = update(workers_table)\
                .values(username=new_username)\
                .filter_by(id=worker_id)
            await conn.execute(stmt)
            await conn.commit()

