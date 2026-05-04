with open("input.txt", "r", encoding="utf-8") as source:
    content = source.read()

with open("uppercase.txt", "w", encoding="utf-8") as destination:
    destination.write(content.upper())

print("Данные записаны в верхнем регистре")
