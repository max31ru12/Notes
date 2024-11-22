from asyncio import Future
import asyncio


my_future = Future()

# True или False
# print(f"Какой result хранится в my_future? {my_future.result()}")

# Устанаваливаем значение в помощью метода set_result()
my_future.set_result(42)

# True или False
print(f"my_muture готов? {my_future.done()}")

# result можно применить только к объекту Future() с установелнным значением с помощью set_result()
print(f"Какой result хранится в my_future? {my_future.result()}")


def make_request() -> Future:
    future = Future()
    # Создать задачу, которая асинхронно установит значение future
    asyncio.create_task(set_future_value(future))
    return future


async def set_future_value(future) -> None:
    await asyncio.sleep(1)
    future.set_result(46)


async def main():
    future = make_request()
    print(f"Будущий объект готов? {future.done()}")
    value = await future
    print(f'Будущий объект готов? {future.done()}')
    print(value)


asyncio.run(main())
