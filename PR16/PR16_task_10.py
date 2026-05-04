import re

text = "apple, banana orange,grape"
result = re.split(r"[\s,]+", text.strip())
print(result)
