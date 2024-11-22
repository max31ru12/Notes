import asyncio
from concurrent.futures import Future
from asyncio import AbstractEventLoop
from typing import Callable
from aiohttp import ClientSession


class StressTest:

    def __init__(self,
                 loop: AbstractEventLoop,
                 url: str,
                 total_requests: int,
                 callback: Callable[[int, int], None]) -> None:
        self._completed_requests: int = 0
        self._load_test_future: Future | None = None
        self._loop = loop
        self._url = url
        self._total_requests = total_requests
        self._callback = callback
        self._refresh_rate = total_requests // 100

    def start(self) -> None:
        future = asyncio.run_coroutine_threadsafe(self._make_requests(),
                                                  self._loop)
        self._load_test_future = future

    def cancel(self) -> None:
        if self._load_test_future:
            self._loop.call_soon_threadsafe(self._load_test_future.cancel)

    async def _get_url(self, session: ClientSession, url: str) -> None:
        try:
            await session.get(url)
        except Exception as e:
            print(e)
        self._completed_requests += 1
        # После того как отправка 1 % запросов завершена, вызвать функцию обратного вызова,
        # передав ей число завершенных запросов и общее число запросов
        if self._completed_requests % self._refresh_rate == 0 \
                or self._completed_requests == self._total_requests:
            self._callback(self._completed_requests, self._total_requests)

    async def _make_requests(self) -> None:
        async with ClientSession() as session:
            reqs = [self._get_url(session, self._url) for _ in range(self._total_requests)]
            await asyncio.gather(*reqs)




