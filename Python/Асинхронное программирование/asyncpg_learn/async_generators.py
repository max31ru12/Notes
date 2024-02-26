import asyncpg
import asyncio
import os
from dotenv import load_dotenv


load_dotenv()


async def main():
    connection = await asyncpg.connect(host="localhost",
                                       port=5432,
                                       user="postgres",
                                       database="products",
                                       password=os.getenv("PG_PASSWORD"))

    query = 'SELECT product_id, product_name FROM product'

    # Прикол использования connection.cursor() в том, что в память загружается небольшой объем данных
    async with connection.transaction():
        # connection.cursor() возвращает асинхронный генератор
        async for product in connection.cursor(query):
            print(product)

    await connection.close()


asyncio.run(main())
