import asyncio

async def work(number):
    await asyncio.sleep(1)
    return number * 2

async def main():
    results = await asyncio.gather(work(1), work(2), work(3))
    print(results)

asyncio.run(main())
