import asyncio
import sys
import os

from util.delay_funtions import delay


# корутина (async функция)
async def add_one(number: int) -> int:
    return number + 1


async def hello_world_message() -> str:
    await delay(1)
    return 'Hello World!'


# Асинхронный код, но выполняется он последовательно
# Чтобы выполнять код конкуретно нужны ЗАДАЧИ
async def main() -> None:
    # Встретив await интерпретатор останавливает родительскую корутину
    # и запускает корутину, помещенную в await

    # Здесь мы ждем выполенения первой корутины, и только после этого выполняется вторая корутина
    # Эти вещи происходят в рамках корутины main
    message = await hello_world_message() # останавливает выполнение корутины main,
                                          # а delay(1) останавливает корутину hello_world_message()

    # После выполнения корутины hello_world_message() возобновляется main()
    one_plus_one = await add_one(1) # тут корутина main() останавливается, и мы ждем завершения корутины add_one()
    # Тут продолжается корутина main()
    print(one_plus_one)
    print(message)


async def hello_every_second():
    for i in range(2):
        await asyncio.sleep(1)
        print("Пока я жду, пока исполняется другой код")


async def main():
    # Создает задачу
    first_delay = asyncio.create_task(delay(3))
    second_delay = asyncio.create_task(delay(3))
    # выполняем задачу
    # Задачи начнутся и закончатся одновременно (ну почти)
    await hello_every_second() # выполняется пока задачи спят
    await first_delay
    await second_delay






# asyncio.run() создает новое событие, все подчищает и закрывает цикл событий
# var = asyncio.run(my_coroutine(4)) # 5

asyncio.run(main())


