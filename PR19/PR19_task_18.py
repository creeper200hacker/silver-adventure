import asyncio

async def read_file(filename):
    print(f"Чтение {filename} началось")
    await asyncio.sleep(1)
    print(f"Чтение {filename} завершено")

async def main():
    files = ["file1.txt", "file2.txt", "file3.txt"]
    await asyncio.gather(*(read_file(file) for file in files))

asyncio.run(main())
