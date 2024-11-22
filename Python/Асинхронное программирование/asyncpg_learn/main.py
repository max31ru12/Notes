import asyncpg
from asyncpg import Record
import asyncio
from dotenv import load_dotenv, dotenv_values
import os

load_dotenv()


async def select_products(pool):
    stmt = "SELECT * FROM product;"
    async with pool.acquire() as connection:
        return await connection.fetchrow(stmt)


async def main():
    async with asyncpg.create_pool(host="localhost",
                                   port=5432,
                                   user="postgres",
                                   database="products",
                                   password=os.getenv("PG_PASSWORD"),
                                   min_size=6,
                                   max_size=6) as pool:

        result = await asyncio.gather(select_products(pool), select_products(pool))
        print(result)


asyncio.run(main())
