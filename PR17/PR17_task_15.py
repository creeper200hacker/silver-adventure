import json

data = {
    "name": "Amir",
    "age": 19,
    "city": "Kazan"
}

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("Данные сохранены")
