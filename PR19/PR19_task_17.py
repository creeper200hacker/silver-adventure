import asyncio

async def task(name, delay):
    await asyncio.sleep(delay)
    print(f"{name} завершена через {delay} сек.")

async def main():
    delays = [3, 1, 4, 2, 5]
    tasks = [asyncio.create_task(task(f"Task-{i}", delay)) for i, delay in enumerate(delays, start=1)]
    await asyncio.gather(*tasks)

asyncio.run(main())
