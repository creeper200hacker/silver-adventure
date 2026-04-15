class WordCaseSeparator:
    def __init__(self):
        self.upper_case = []
        self.lower_case = []

    def add_word(self, word):
        if word and word[0].isupper():
            self.upper_case.append(word)
        else:
            self.lower_case.append(word)

    def upper_case_words(self):
        return self.upper_case

    def lower_case_words(self):
        return self.lower_case


# Пример 1
separator = WordCaseSeparator()
separator.add_word("Apple")
separator.add_word("banana")
separator.add_word("Cherry")
separator.add_word("date")
print(separator.upper_case_words())  # ['Apple', 'Cherry']
print(separator.lower_case_words())  # ['banana', 'date']
