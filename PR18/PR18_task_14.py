with open("input.txt", "r", encoding="utf-8") as source, open("no_empty.txt", "w", encoding="utf-8") as destination:
    for line in source:
        if line.strip():
            destination.write(line)

print("Пустые строки удалены")
