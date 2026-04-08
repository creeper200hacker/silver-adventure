from typing import Any


def add(a: int, b: int) -> int:
    return a + b


def greet(name: str) -> str:
    return f"Hello, {name}"


def sum_list(numbers: list[int]) -> int:
    return sum(numbers)


def multiply_all(*args: int) -> int:
    result = 1
    for number in args:
        result *= number
    return result


def print_info(**kwargs: str) -> None:
    for key, value in kwargs.items():
        print(f"{key}: {value}")


def average(*args: float) -> float:
    return sum(args) / len(args)


def process(a: int, b: int, *args: int, **kwargs: int) -> int:
    return a + b + sum(args) + sum(kwargs.values())


if __name__ == "__main__":
    # Задача 1
    print(add(2, 3))

    # Задача 2
    print(greet("Alice"))

    # Задача 3
    print(sum_list([1, 2, 3]))

    # Задача 4
    print(multiply_all(2, 3, 4))

    # Задача 5
    numbers = [4, 5]
    print(add(*numbers))

    # Задача 6
    print_info(name="Alice", city="Paris")

    # Задача 7
    data = {"name": "Bob", "age": "25"}
    print_info(**data)

    # Задача 8
    print(average(2, 4, 6))

    # Задача 9
    numbers = [1, 2, 3, 4, 5]
    first, *middle, last = numbers
    print(first)
    print(middle)
    print(last)

    # Задача 10
    print(process(1, 2, 3, 4, x=5, y=6))
