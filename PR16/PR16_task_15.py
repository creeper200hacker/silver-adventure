import re

text = "hello world python"
result = re.sub(r"\b\w", lambda match: match.group(0).upper(), text)
print(result)
