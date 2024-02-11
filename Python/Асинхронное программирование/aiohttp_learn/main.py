import asyncio
import aiohttp


async def main():
    # Тайм-Аут для установления соединения с адресом (connect=.1)
    # Тайм-Аут для для сеанса
    timeout = aiohttp.ClientTimeout(total=1, connect=.1)
    # Создаем асинхронную сессию
    async with aiohttp.ClientSession(timeout=timeout) as session:
        url = "https://www.example.com"
        response = await session.get(url)
        status = response.status
        print(f"{status=}")


asyncio.run(main())
