from util.delay_funtions import delay
import asyncio
from asyncio import CancelledError


async def main():
    long_task = asyncio.create_task(delay(10))
    seconds_elapsed = 0
    # Проверяем закончилась ли задача
    while not long_task.done():
        print('Задача не закончилась, следующая проверка через секунду.')
        await asyncio.sleep(1)
        seconds_elapsed += 1
        if seconds_elapsed == 5:
            # Отменяем задачу при выполнении условия
            long_task.cancel()

    try:
        await long_task
    # CancelledError может быть возбуждено только внутри await
    except CancelledError:
        print("Задача была снята")


# Функция с wait_for
# wait_for
async def main():
    delay_task = asyncio.create_task(delay(10))
    try:
        # Даем время на выполнение задачи
        # result = await asyncio.wait_for(delay_task, timeout=3)
        # Для предовтарщения снятия задачи можно использовать asyncio.shield(delay_task)
        result = await asyncio.wait_for(asyncio.shield(delay_task), timeout=5)
        print(result)
        # dealy_task.cancelled показывает, была ли задача снята
        print(f'Задача была снята? {delay_task.cancelled()}')
    except asyncio.exceptions.TimeoutError:
        print('Тайм-аут!')
        # вручную ждем завершения задачи!!!
        result = await delay_task
        print(result)
        print(f'Задача была снята? {delay_task.cancelled()}')


asyncio.run(main())


