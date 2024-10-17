# FastAPI + SQLAlchemy configuration

## Создать таблицы или подхватить, если они есть

```py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import home
from app.setup_db import async_engine, Base

from app.db_models.skill import Skill  # noqa

app = FastAPI(title="Portfolio API")


@app.on_event("startup")
async def init_database():
    async with async_engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
```
