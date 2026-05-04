import re

password = "qwerty12"
result = bool(re.fullmatch(r"(?=.*\d).{8,}", password))
print(result)
