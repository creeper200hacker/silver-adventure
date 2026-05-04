import re

log = "2026-04-01 ERROR Failed"
pattern = r"^(\d{4}-\d{2}-\d{2})\s+(INFO|ERROR)\s+(.+)$"
match = re.search(pattern, log)

if match:
    date, level, message = match.groups()
    print("Дата:", date)
    print("Уровень:", level)
    print("Сообщение:", message)
