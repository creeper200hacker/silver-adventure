import asyncio

async def worker(name, queue):
    while True:
        task = await queue.get()
        if task is None:
            queue.task_done()
            break
        print(f"{name} начал задачу {task}")
        await asyncio.sleep(1)
        print(f"{name} завершил задачу {task}")
        queue.task_done()

async def main():
    queue = asyncio.Queue()

    for i in range(1, 11):
        await queue.put(i)

    workers = [asyncio.create_task(worker(f"Worker-{i}", queue)) for i in range(1, 4)]

    for _ in workers:
        await queue.put(None)

    await queue.join()
    await asyncio.gather(*workers)

asyncio.run(main())
