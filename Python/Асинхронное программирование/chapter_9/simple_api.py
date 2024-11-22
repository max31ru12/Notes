import asyncpg
import os
from aiohttp import web
from aiohttp.web_app import Application
from aiohttp.web_request import Request
from aiohttp.web_response import Response
from dotenv import load_dotenv
from asyncpg.pool import Pool
from typing import List, Dict

load_dotenv()

routes = web.RouteTableDef()
DB_KEY: str = 'database'


async def create_database_pool(app: Application):
    print("Создается пул подключений!")
    pool: Pool = await asyncpg.create_pool(host='localhost',
                                           port=5432,
                                           user='postgres',
                                           password=os.getenv("PG_PASSWORD"),
                                           database='products',
                                           min_size=6,
                                           max_size=6)
    app[DB_KEY] = pool


async def destroy_database_pool(app: Application):
    print("Уничтодается пул подключений")
    pool: Pool = app[DB_KEY]
    await pool.close()


@routes.get('/products')
async def get_products(request: Request) -> Response:
    connection: Pool = request.app[DB_KEY]
    query = "SELECT * FROM product;"
    results = await connection.fetch(query)
    result_as_dict: List[Dict] = [dict(product) for product in results]
    return web.json_response(result_as_dict)


@routes.get('/products/{id}')
async def get_product(request: Request) -> Response:
    try:
        str_id = request.match_info['id']
        product_id = int(str_id)
        query = "SELECT * FROM product WHERE id = $1"

        connection: Pool = request.app[DB_KEY]
        result = await connection.fetchrow(query, product_id)

        if result is not None:
            return web.json_response(dict(result))
        else:
            raise web.HTTPNotFound()
    except ValueError:
        raise web.HTTPBadRequest()


@routes.post('/products')
async def create_product(request: Request):
    PRODUCT_NAME = 'product'
    BRAND = 'brand'
    # if not request.can_read_body:
    #     raise web.HTTPBadRequest()
    body = await request.json()
    return body
    # if PRODUCT_NAME in body and BRAND in body:
    #     db = request.app[DB_KEY]
    #     await db.execute('''INSERT INTO product(product_id,
    #                          product_name,
    #                          brand_id)
    #                          VALUES(DEFAULT, $1, $2)''',
    #                      body[PRODUCT_NAME],
    #                      body[BRAND])
    #     return web.Response(status=201)
    # else:
    #     raise web.HTTPBadRequest()


app = web.Application()
app.on_startup.append(create_database_pool)
app.on_cleanup.append(destroy_database_pool)

app.add_routes(routes)
web.run_app(app)
