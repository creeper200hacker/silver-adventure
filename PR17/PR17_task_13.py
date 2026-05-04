import os

filename = "data.txt"

if os.path.exists(filename):
    size = os.path.getsize(filename)
    print(size)
else:
    print("Файл не найден")
