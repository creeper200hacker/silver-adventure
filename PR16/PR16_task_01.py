import re

text = "I love Python programming"
result = bool(re.search(r"\bPython\b", text))
print(result)
