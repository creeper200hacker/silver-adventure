import asyncio

async def producer(queue):
    for i in range(1, 6):
        await asyncio.sleep(0.5)
        await queue.put(i)
        print("Создано:", i)
    await queue.put(None)

async def consumer(queue):
    while True:
        item = await queue.get()
        if item is None:
            break
        print("Обработано:", item)
        queue.task_done()

async def main():
    queue = asyncio.Queue()
    await asyncio.gather(producer(queue), consumer(queue))

asyncio.run(main())
