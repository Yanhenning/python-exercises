import asyncio


async def print_async_array(array):
    seconds = 1
    for i in range(len(array)):
        print(seconds)
        await asyncio.sleep(seconds)
        seconds = seconds * 2
        print(array[i])


if __name__ == '__main__':
    asyncio.run(print_async_array(['a', 'b', 'c', 'd']))
