import asyncio


async def print_async_array(array):
    seconds = 1
    for i in range(len(array)):
        print(seconds)
        seconds = seconds * 2
        await asyncio.sleep(seconds)
        print(array[i])
