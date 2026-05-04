with open("input.txt", "r", encoding="utf-8") as source, open("numbered.txt", "w", encoding="utf-8") as destination:
    for number, line in enumerate(source, start=1):
        destination.write(f"{number}: {line}")

print("Строки пронумерованы")
