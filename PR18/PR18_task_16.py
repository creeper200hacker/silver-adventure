from datetime import datetime

message = "Program started"

with open("log.txt", "a", encoding="utf-8") as file:
    file.write(f"{datetime.now()} INFO {message}
")

print("Лог записан")
