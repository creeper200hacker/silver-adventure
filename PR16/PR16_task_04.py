import re

text = "Hello world Python"
result = re.sub(r"\s+", "_", text)
print(result)
