with open("input.txt", "r", encoding="utf-8") as file:
    content = file.read()

if content == "":
    print("Empty")
else:
    print("Файл не пустой")
