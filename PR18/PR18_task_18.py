with open("log.txt", "r", encoding="utf-8") as file:
    error_count = sum(1 for line in file if "ERROR" in line)

print("Количество ошибок:", error_count)
