import re

text = "Apple and banana are amazing"
words = re.findall(r"\b[aA]\w*", text)
print(words)
