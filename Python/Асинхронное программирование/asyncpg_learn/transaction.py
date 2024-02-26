import asyncpg
from asyncpg.transaction import Transaction
import asyncio
import os
from dotenv import load_dotenv
import logging

load_dotenv()


async def main():
    connection = await asyncpg.connect(host="localhost",
                                       port=5432,
                                       user="postgres",
                                       database="products",
                                       password=os.getenv("PG_PASSWORD"))

    async with connection.transaction():
        await connection.execute("INSERT INTO brand VALUES(9, 'my_new_brand')")

        try:
            async with connection.transaction():
                await connection.execute("INSERT INTO product_color VALUES(1, 'black')")
        except Exception as ex:
            logging.warning('Ошибка при вставке цвета товара игнорируется', exc_info=ex)

    await connection.close()


# asyncio.run(main())


async def main_2():
    connection = await asyncpg.connect(host="localhost",
                                       port=5432,
                                       user="postgres",
                                       database="products",
                                       password=os.getenv("PG_PASSWORD"))

    transaction: Transaction = connection.transaction()
    await transaction.start
    try:
        await connection.execute("INSERT INTO brand "
                                 "VALUES(DEFAULT, 'brand_1')")
        await connection.execute("INSERT INTO brand "
                                 "VALUES(DEFAULT, 'brand_2')")

    except asyncpg.PostgresError:
        print("Ошибка! транзакция откатывается")
        await transaction.rollback()
    else:
        print("Ошибки нет! транзакция фиксируется")
        await transaction.commit()

    
