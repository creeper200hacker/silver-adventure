import re

text = "abc123def45"
result = re.sub(r"\d", "", text)
print(result)
