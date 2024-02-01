import asyncio
import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from queries.core import SyncCore, AsyncCore
from queries.orm import SyncOrm, AsyncOrm


create = AsyncOrm.create_tables
insert = AsyncOrm.insert_workers
select = AsyncOrm.select_workers
update = AsyncOrm.update_worker
avg_salary = AsyncOrm.select_resumes_avg_compensation


async def main():
    await create()
    await insert()
    sel = asyncio.create_task(select())
    await sel
    await update(1, "Max")
    sel = asyncio.create_task(select())
    await sel


# asyncio.run(main())
asyncio.run(avg_salary())

# SyncOrm.insert_workers()
# SyncOrm.update_worker(1)
# SyncOrm.select_resumes_avg_compensation()