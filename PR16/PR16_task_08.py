import re

text = "Dates: 2024-01-01 and 2025-12-31"
dates = re.findall(r"\b\d{4}-\d{2}-\d{2}\b", text)
print(dates)
