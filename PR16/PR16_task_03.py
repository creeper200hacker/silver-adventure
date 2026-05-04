import re

text = "test@example.com"
pattern = r"^[\w.-]+@[\w.-]+\.\w{2,}$"
result = bool(re.fullmatch(pattern, text))
print(result)
