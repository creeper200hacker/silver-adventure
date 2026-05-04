import asyncio

async def say_message():
    await asyncio.sleep(1)
    print("Сообщение после задержки")

asyncio.run(say_message())
