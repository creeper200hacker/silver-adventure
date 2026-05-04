import re

text = "There are 12 apples and 5 bananas"
numbers = re.findall(r"\d+", text)
print(numbers)
