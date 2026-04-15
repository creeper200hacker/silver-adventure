"""
Практическая работа №15
Работа с файлами, датами и временем
"""

from __future__ import annotations

import csv
import string
from collections import Counter
from datetime import datetime, date, timedelta
from pathlib import Path


# -----------------------------
# Задачи 1-10. Работа с файлами
# -----------------------------

def count_unique_words(filepath: str) -> int:
    text = Path(filepath).read_text(encoding="utf-8").lower()
    words = text.translate(str.maketrans("", "", string.punctuation)).split()
    return len(set(words))


def word_frequencies(filepath: str) -> list[tuple[str, int]]:
    text = Path(filepath).read_text(encoding="utf-8").lower()
    words = text.translate(str.maketrans("", "", string.punctuation)).split()
    counter = Counter(words)
    return sorted(counter.items(), key=lambda item: (-item[1], item[0]))


def remove_punctuation(input_file: str, output_file: str) -> None:
    text = Path(input_file).read_text(encoding="utf-8")
    clean_text = text.translate(str.maketrans("", "", string.punctuation))
    Path(output_file).write_text(clean_text, encoding="utf-8")


def average_age(csv_file: str) -> float:
    ages = []
    with open(csv_file, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            ages.append(int(row["age"]))
    return sum(ages) / len(ages) if ages else 0.0


def filter_age_gt_25(input_csv: str, output_csv: str) -> None:
    with open(input_csv, "r", encoding="utf-8", newline="") as infile, \
         open(output_csv, "w", encoding="utf-8", newline="") as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames or ["name", "age"]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            if int(row["age"]) > 25:
                writer.writerow(row)


def longest_line(filepath: str) -> tuple[int, str]:
    lines = Path(filepath).read_text(encoding="utf-8").splitlines()
    longest = max(lines, key=len, default="")
    return len(longest), longest


def find_error_lines(filepath: str) -> list[str]:
    lines = Path(filepath).read_text(encoding="utf-8").splitlines()
    return [line for line in lines if "ERROR" in line]


def count_lines_start_upper(filepath: str) -> int:
    count = 0
    for line in Path(filepath).read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped and stripped[0].isupper():
            count += 1
    return count


def merge_files(input_files: list[str], output_file: str) -> None:
    merged_parts = []
    for filename in input_files:
        merged_parts.append(Path(filename).read_text(encoding="utf-8"))
    Path(output_file).write_text("\n".join(merged_parts), encoding="utf-8")


def write_unique_lines(input_file: str, output_file: str) -> None:
    seen = set()
    unique = []
    for line in Path(input_file).read_text(encoding="utf-8").splitlines():
        if line not in seen:
            seen.add(line)
            unique.append(line)
    Path(output_file).write_text("\n".join(unique), encoding="utf-8")


# ----------------------------------
# Задачи 11-20. Даты, время, журналы
# ----------------------------------

def parse_date(date_string: str) -> tuple[int, int, int]:
    dt = datetime.strptime(date_string, "%Y-%m-%d").date()
    return dt.day, dt.month, dt.year


def working_days_between(start_date: str, end_date: str) -> int:
    start = datetime.strptime(start_date, "%Y-%m-%d").date()
    end = datetime.strptime(end_date, "%Y-%m-%d").date()

    if start > end:
        start, end = end, start

    days = 0
    current = start
    while current <= end:
        if current.weekday() < 5:
            days += 1
        current += timedelta(days=1)
    return days


def next_monday(date_string: str) -> date:
    current_date = datetime.strptime(date_string, "%Y-%m-%d").date()
    days_ahead = (7 - current_date.weekday()) % 7
    if days_ahead == 0:
        days_ahead = 7
    return current_date + timedelta(days=days_ahead)


def age_in_days(birth_date: str, today: date | None = None) -> int:
    birth = datetime.strptime(birth_date, "%Y-%m-%d").date()
    current_day = today or date.today()
    return (current_day - birth).days


def sort_dates(date_list: list[str]) -> list[str]:
    return [
        dt.strftime("%Y-%m-%d")
        for dt in sorted(datetime.strptime(item, "%Y-%m-%d") for item in date_list)
    ]


def format_datetime_string(dt_string: str) -> str:
    dt = datetime.strptime(dt_string, "%Y-%m-%d %H:%M")
    return dt.strftime("%d %B %Y, %H:%M")


def unix_timestamp_roundtrip(dt: datetime | None = None) -> tuple[int, datetime]:
    current_dt = dt or datetime.now()
    timestamp = int(current_dt.timestamp())
    restored = datetime.fromtimestamp(timestamp)
    return timestamp, restored


def is_deadline_expired(deadline_date: str, current: date | None = None) -> bool:
    deadline = datetime.strptime(deadline_date, "%Y-%m-%d").date()
    today = current or date.today()
    return deadline < today


def log_message(filepath: str, message: str, current: datetime | None = None) -> None:
    now = current or datetime.now()
    entry = f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] {message}\n"
    with open(filepath, "a", encoding="utf-8") as file:
        file.write(entry)


def error_counts_by_day(logfile: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for line in Path(logfile).read_text(encoding="utf-8").splitlines():
        parts = line.split(maxsplit=2)
        if len(parts) >= 2 and parts[1] == "ERROR":
            log_date = parts[0]
            counts[log_date] = counts.get(log_date, 0) + 1
    return counts


# -----------------------------
# Демонстрация работы программы
# -----------------------------

if __name__ == "__main__":
    demo_dir = Path("pr15_demo_files")
    demo_dir.mkdir(exist_ok=True)

    input_txt = demo_dir / "input.txt"
    input_txt.write_text(
        "Hello, world! Hello Python.\n"
        "Python is great.\n"
        "World of code, world of Python.\n",
        encoding="utf-8"
    )

    data_csv = demo_dir / "data.csv"
    data_csv.write_text(
        "name,age\n"
        "Alice,23\n"
        "Bob,30\n"
        "Charlie,27\n",
        encoding="utf-8"
    )

    lines_txt = demo_dir / "lines.txt"
    lines_txt.write_text(
        "short\n"
        "This is the longest line in the file.\n"
        "middle line\n",
        encoding="utf-8"
    )

    log_txt = demo_dir / "log.txt"
    log_txt.write_text(
        "2026-04-01 ERROR Something failed\n"
        "2026-04-02 INFO All good\n"
        "2026-04-03 ERROR Crash\n",
        encoding="utf-8"
    )

    upper_txt = demo_dir / "upper.txt"
    upper_txt.write_text(
        "Apple\n"
        "banana\n"
        "Cherry\n"
        "dog\n"
        "Elephant\n",
        encoding="utf-8"
    )

    file1 = demo_dir / "file1.txt"
    file2 = demo_dir / "file2.txt"
    file1.write_text("Первая строка из первого файла.", encoding="utf-8")
    file2.write_text("Вторая строка из второго файла.", encoding="utf-8")

    repeated_txt = demo_dir / "repeated.txt"
    repeated_txt.write_text(
        "one\n"
        "two\n"
        "one\n"
        "three\n"
        "two\n",
        encoding="utf-8"
    )

    clean_txt = demo_dir / "clean.txt"
    filtered_csv = demo_dir / "filtered.csv"
    result_txt = demo_dir / "result.txt"
    unique_txt = demo_dir / "unique.txt"
    messages_log = demo_dir / "messages.log"

    print("Задача 1:", count_unique_words(str(input_txt)))

    print("\nЗадача 2:")
    for word, count in word_frequencies(str(input_txt)):
        print(f"{word}: {count}")

    remove_punctuation(str(input_txt), str(clean_txt))
    print("\nЗадача 3:")
    print(clean_txt.read_text(encoding='utf-8'))

    print("Задача 4:", average_age(str(data_csv)))

    filter_age_gt_25(str(data_csv), str(filtered_csv))
    print("\nЗадача 5:")
    print(filtered_csv.read_text(encoding='utf-8'))

    length, line = longest_line(str(lines_txt))
    print("Задача 6:", length, "-", line)

    print("\nЗадача 7:")
    for error_line in find_error_lines(str(log_txt)):
        print(error_line)

    print("\nЗадача 8:", count_lines_start_upper(str(upper_txt)))

    merge_files([str(file1), str(file2)], str(result_txt))
    print("\nЗадача 9:")
    print(result_txt.read_text(encoding='utf-8'))

    write_unique_lines(str(repeated_txt), str(unique_txt))
    print("Задача 10:")
    print(unique_txt.read_text(encoding='utf-8'))

    day, month, year = parse_date("2024-12-31")
    print("Задача 11:", day, month, year)

    print("Задача 12:", working_days_between("2024-12-30", "2025-01-05"))

    print("Задача 13:", next_monday("2024-12-31"))

    print("Задача 14:", age_in_days("2000-01-01", date(2026, 4, 7)))

    print("Задача 15:", sort_dates(["2024-12-31", "2024-01-15", "2024-06-01"]))

    print("Задача 16:", format_datetime_string("2024-01-01 14:30"))

    timestamp, restored = unix_timestamp_roundtrip(datetime(2026, 4, 7, 14, 30, 0))
    print("Задача 17:", timestamp, restored)

    print("Задача 18:", is_deadline_expired("2026-04-01", date(2026, 4, 7)))

    log_message(str(messages_log), "Message", datetime(2026, 4, 7, 14, 30, 0))
    print("\nЗадача 19:")
    print(messages_log.read_text(encoding='utf-8'))

    print("Задача 20:")
    for log_date, count in error_counts_by_day(str(log_txt)).items():
        print(f"{log_date}: {count}")
