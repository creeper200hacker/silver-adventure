import re

text = "I am learning Python in IT"
result = re.sub(r"\b\w{1,2}\b", "***", text)
print(result)
