import os
import random
from datetime import datetime

numbers = [random.randint(1, 100) for _ in range(5)]

with open("numbers.txt", "w", encoding="utf-8") as file:
    file.write("Дата записи: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "
")
    file.write("Числа: " + ", ".join(map(str, numbers)) + "
")

if os.path.exists("numbers.txt"):
    with open("numbers.txt", "r", encoding="utf-8") as file:
        print(file.read())
else:
    print("Файл не найден")
