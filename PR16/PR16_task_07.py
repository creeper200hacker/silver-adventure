import re

text = "+37112345678"
pattern = r"^\+371\d{8}$"
result = bool(re.fullmatch(pattern, text))
print(result)
