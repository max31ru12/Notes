import asyncio
from util.async_decorator import async_timed
from util.delay_funtions import delay


@async_timed()
async def main():
    await asyncio.sleep(1)


def call_later():
    print("Меня вызовут в ближайшем будущем")


loop = asyncio.new_event_loop()

try:
    loop.run_until_complete(main())
finally:
    loop.close()


# get_running_loop
def call_later():
    print("Меня вызовут в ближайшем будущем!")


async def main():
    loop = asyncio.get_running_loop()
    loop.call_soon(call_later)
    await delay(1)
