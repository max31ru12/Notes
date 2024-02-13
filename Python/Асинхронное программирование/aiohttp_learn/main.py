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


async def main_gather():
    timeout = aiohttp.ClientTimeout(total=10, connect=0.1)
    url = "https://www.example.com"
    urls = [url for i in range(1000)]
    async with aiohttp.ClientSession(timeout=timeout) as session:
        requests = [session.get(l_url) for l_url in urls]
        status_codes = await asyncio.gather(*requests, return_exceptions=True)
        print(status_codes)
        print(len(status_codes))


asyncio.run(main_gather())
