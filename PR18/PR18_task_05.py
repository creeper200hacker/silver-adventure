with open("input.txt", "r", encoding="utf-8") as file:
    lines_count = sum(1 for line in file)

print("Количество строк:", lines_count)
