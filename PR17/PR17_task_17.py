import csv

users = [
    ["name", "age"],
    ["Amir", 19],
    ["Bulat", 20]
]

with open("users.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(users)

print("CSV-файл создан")
