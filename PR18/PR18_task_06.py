with open("input.txt", "r", encoding="utf-8") as file:
    text = file.read()

words_count = len(text.split())
print("Количество слов:", words_count)
