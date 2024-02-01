import datetime
import enum
from typing import Annotated

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, func, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column
from database import Base


# Mapped - позволяет использовать типы
# mapped_column() - позволяет устанавливать первичный ключ,
# unique,
# insert_default
# autoincrement
# default - задаётся на уровне python-приложения
# server_default - значение устанвливает сама СУБД
# onupdate - обновление


# Это общий тип первичного ключа:
# аналог id: Mapped[int] = mapped_column(primary_key=True)
# только теперь можно указывать просто id id: Mapped[int] = mapped_column(primary_key=True)Mapped[intpk]
intpk = Annotated[int, mapped_column(primary_key=True)]
# Можно избавиться от дублирования кода
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"),
                                                        onupdate=datetime.datetime.utcnow)]


# Декларативный стиль определения таблицы
class WorkersOrm(Base):
    __tablename__ = "workers"

    id: Mapped[intpk]
    # можно не указывать mapped_column
    username: Mapped[str] = mapped_column()


# перечисление двух графиков работы (типа выбор из существующих)
class Workload(enum.Enum):
    parttime = "parttime"
    fulltime = "fulltime"


class ResumesOrm(Base):
    __tablename__ = "resumes"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    # Поле может быть пустым
    compensation: Mapped[int | None]
    # Аналогиная запись для верхней строки
    # compensation: Mapped[int | None] = mapped_column(nullable=True)
    workload: Mapped[Workload]
    # Назначаем внешний ключ (from sqlalchemy import ForeignKey)
    worker_id: Mapped[int] = mapped_column(ForeignKey(WorkersOrm.id, ondelete="CASCADE"))
    # Второй способ назначения внешнего ключа
    # worker_id: Mapped[int] = mapped_column(ForeignKey("workers.id"))
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
    # from sqlalchemy import func - выберет мой часовой пояс (можно передать text("TIMEZONE('utc', now())"))
    updated_at: Mapped[datetime.datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"),
                                                          onupdate=datetime.datetime.utcnow)

# class WorkersOrm(Base):
#     __tablename__ = "workers"
#
#     id = Column(Integer, primary_key=True)
#     username = Column(String)


# # Здесь хранится инфомрация о всех таблицах, которые мы создали из python'а
# # Императивный стиль
metadata_obj = MetaData()

# Просто сделали модель таблицы
workers_table = Table('workers', metadata_obj,
                      Column("id", Integer, primary_key=True),
                      Column("username", String),
                      )
# # Создание таблицы происходит через объект Metadata (metadata_obj)
