from sqlalchemy import text, insert, select, update, func, cast, Integer, and_
from database import sync_engine, async_engine, session_factory, async_session_factory, Base
from models import metadata_obj, WorkersOrm, ResumesOrm


# это синхронная операция (никаой запрос в БД не отправляет), поэтому без await
# session.expire(obj) - отменить все изменения в объекте
# session.expire_all() - отменить все изменения во всех объектах

# session.refresh(obj) - обновить данные объекта до того состояния, которое сейчас в БД


class SyncOrm:

    @staticmethod
    def create_tables():
        sync_engine.echo = False
        Base.metadata.drop_all(sync_engine)
        Base.metadata.create_all(sync_engine)
        sync_engine.echo = True

    @staticmethod
    def insert_workers():
        with session_factory() as session:
            worker_jack = WorkersOrm(username="Mack")
            worker_michael = WorkersOrm(username="Michael")
            session.add_all([worker_jack, worker_michael])
            session.flush()
            session.commit()

    @staticmethod
    def select_workers(worker_id: int):
        with session_factory() as session:
            # Получаем одного работника
            # Передаем сначала таблицу (объект), а затем первичный ключ
            worker = session.get(WorkersOrm, worker_id)
            # второй способ
            # worker = session.get(WorkersOrm, {"id": worker_id})
            query = select(WorkersOrm)
            result = session.execute(query)
            # вернет список кортежей: [(object_addr_1, ), (object_addr_2, ), ...]
            # workers = result.all()
            # вернет список объектов [object_addr_1, object_addr_2, object_addr_3, ...]
            workers = result.scalars.all()
            print(f"{workers=}")

    @staticmethod
    def update_worker(worker_id: int, new_username: str):
        with session_factory() as session:
            worker = session.get(WorkersOrm, worker_id)
            worker.username = new_username
            session.commit()

    @staticmethod
    def select_resumes_avg_compensation():
        # SELECT workload, avg(compensation)::int as avg_compensation FROM resumes WHERE title
        # LIKE '%Python%' and compensation > 40000 GROUP BY workload;
        with session_factory() as session:
            query = (
                select(
                    ResumesOrm.workload,
                    # func.функция_из_СУБД (типа AVG(), SUM())
                    # cast(объект, тип (импорт типа из sqlalchemy))
                    # label("avg_compensation") - создать alias (AS avg_compensation)
                    cast(func.avg(ResumesOrm.compensation), Integer).label("avg_compensation")
                    # Можно не указывать явно таблицу с помощью .select_from(ResumesOrm)
                )
                    .select_from(ResumesOrm)
                    # and_ - для объединения условий с помощью AND
                    # .contains("Python")
                    .filter(and_(ResumesOrm.title.contains("Python"),
                                 ResumesOrm.compensation > 40000,
                                 ))
                    .group_by(ResumesOrm.workload)
                    # .having(...)
            )
            res = session.execute(query)
            result = res.all()
            print(result)


class AsyncOrm:

    @staticmethod
    async def create_tables():
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

    @staticmethod
    async def insert_workers():
        async with async_session_factory() as session:
            worker_jack = WorkersOrm(username="Jack")
            worker_michael = WorkersOrm(username="Michael")
            session.add_all([worker_jack, worker_michael])
            # flush взаимодействует с БД, поэтому await
            # flush нужен для того, чтобы отправить изменения в базу данных, но транзакция не завершается,
            # нкжно для того, когда мы создаем один объект, а потом его надо сразу же использовать, допустим, для
            # создания второго объекта, который ссылается на только что созданный объект
            await session.flush()
            await session.commit()

    @staticmethod
    async def select_workers():
        async with async_session_factory() as session:
            query = select(WorkersOrm)
            result = await session.execute(query)
            workers = result.scalars().all()
            print(f"{workers=}")

    @staticmethod
    async def update_worker(worker_id: int, new_username: str):
        async with async_session_factory() as session:
            query = update(WorkersOrm).values(username=new_username).filter_by(id=worker_id)
            await session.execute(query)
            await session.commit()

    @staticmethod
    async def select_resumes_avg_compensation():
        async with async_session_factory() as session:
            # SELECT workload, avg(compensation)::int as avg_compensation FROM resumes WHERE title
            # LIKE '%Python%' and compensation > 40000 GROUP BY workload;
            query = select(
                ResumesOrm.workload,
                cast(func.avg(ResumesOrm.compensation), Integer).label("avg_compensation"))\
                .filter(and_(ResumesOrm.title.contains("Python"),
                             ResumesOrm.compensation > 40000))\
                .group_by(ResumesOrm.workload)

            result = await session.execute(query)
            res = result.all()
            print(res)