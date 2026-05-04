with open("input.txt", "r", encoding="utf-8") as source:
    with open("copy.txt", "w", encoding="utf-8") as destination:
        destination.write(source.read())

print("Файл скопирован")
