from pydantic import BaseModel
from models import Workload
import datetime


# Прикол в том, чтобы получать объекты с помощью запросов SQLAlchemy, а потом приводить их к
# читаемому виду с помощью классов Pydantic, которые тут определены
# FOR EXAMPLE: Workers.model_validate(object)

# query = select(WorkersOrm).limit()
# res = session.execute(query)
# result = res.scalars().all()
# results_dto = [Workerl.model_validate(obj, from_attributes=True) for obj in result]

# from_attributes=True - обязательная штука, что метод .model_validate обращался к объекту алхимии как к объекту,
# а не как к словарю


# DTO - Data Transfer Object

# Сначала лучше добавить модель для POST-запроса (если делаем для API)
class WorkersPost(BaseModel):
    username: str


# Наследуемся от модели POST-запроса
class Workers(WorkersPost):
    id: int


# Опять сначала делает для POST-запросов
class ResumesPost(BaseModel):
    title: str
    compensation: int | None
    workload: Workload
    worker_id: int


class Resumes(ResumesPost):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime


class ResumesRelDTO(Resumes):
    worker: "Workers"


class WorkerRelDTO(Workers):
    resumes: list["ResumesRelDTO"]



