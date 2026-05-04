import re

text = "hello hello world test test"
result = re.findall(r"\b(\w+)\s+\1\b", text, flags=re.IGNORECASE)
print(result)
