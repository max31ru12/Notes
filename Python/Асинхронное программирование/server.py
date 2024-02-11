import asyncio
import logging
import socket
import selectors
from asyncio import AbstractEventLoop
from selectors import SelectorKey
from typing import List, Tuple

tasks = []


async def listen_for_connection(server_socket: socket,
                                loop: AbstractEventLoop):
    while True:
        connection, address = await loop.sock_accept(server_socket)
        connection.setblocking(False)
        print(f"Получено сообщение от {address}")
        tasks.append(asyncio.create_task(echo(connection, loop)))


async def echo(connection: socket,
    loop: AbstractEventLoop) -> None:
    try:
        while data := await loop.sock_recv(connection, 1024):
            print('получены данные!')
            if data == b'boom\r\n':
                raise Exception("Неожиданная ошибка сети")
            await loop.sock_sendall(connection, data)
    except Exception as ex:
        logging.exception(ex)
    finally:
        connection.close()


async def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Такая штука позволяет повторно использовать номер порта, после перезапуска приложения
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    address = ("127.0.0.1", 8000)
    server_socket.bind(address)
    server_socket.setblocking(False)
    server_socket.listen()

    await listen_for_connections(server_socket, asyncio.get_event_loop())
    asyncio.run(main())
