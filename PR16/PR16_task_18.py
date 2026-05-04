import re

card = "1234 5678 9012 3456"
result = re.sub(r"\d(?=(?:\D*\d){4})", "*", card)
print(result)
