with open("input.txt", "r", encoding="utf-8") as source, open("filtered.txt", "w", encoding="utf-8") as destination:
    for line in source:
        if len(line.strip()) > 5:
            destination.write(line)

print("Строки отфильтрованы")
