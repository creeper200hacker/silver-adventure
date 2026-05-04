import random
from datetime import date, timedelta

start = date(2024, 1, 1)
end = date(2024, 12, 31)
days_count = (end - start).days
random_date = start + timedelta(days=random.randint(0, days_count))

print(random_date)
