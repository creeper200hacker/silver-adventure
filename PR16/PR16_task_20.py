import re
from collections import Counter

logs = """2026-04-01 ERROR Failed
2026-04-01 INFO OK
2026-04-02 ERROR Crash"""

error_lines = re.findall(r"^\d{4}-\d{2}-\d{2}\s+ERROR\s+.+$", logs, flags=re.MULTILINE)
dates = [re.match(r"\d{4}-\d{2}-\d{2}", line).group(0) for line in error_lines]
error_count = Counter(dates)

print("Строки с ERROR:")
for line in error_lines:
    print(line)

print("Даты:", dates)
print("Количество ошибок по датам:", dict(error_count))
