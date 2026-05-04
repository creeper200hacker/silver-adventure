import re

text = "<p>Hello</p>"
result = re.sub(r"<[^>]+>", "", text)
print(result)
