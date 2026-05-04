import asyncio

async def task(name):
    await asyncio.sleep(1)
    print(name)

async def main():
    tasks = [asyncio.create_task(task(f"Task-{i}")) for i in range(1, 4)]
    await asyncio.gather(*tasks)

asyncio.run(main())
