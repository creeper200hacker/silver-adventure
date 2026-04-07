def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Division by zero"


def to_int(s):
    try:
        return int(s)
    except ValueError:
        return "Invalid input"


def safe_operation(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError:
        return "Type error"


def read_number(s):
    try:
        return int(s)
    except ValueError:
        return "Error"
    finally:
        print("Done")


def check_age(age):
    try:
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным")
        return "OK"
    except ValueError:
        return "Invalid age"


def safe_sum(lst):
    total = 0
    for item in lst:
        try:
            total += item
        except TypeError:
            pass
    return total


def get_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index error"


def process_data(a, b):
    try:
        try:
            a = float(a)
            b = float(b)
        except ValueError:
            return "Conversion error"
        return a / b
    except ZeroDivisionError:
        return "Division by zero"


def safe_print_number(s):
    try:
        number = int(s)
    except ValueError:
        print("Error")
    else:
        print(number)


def calculator(a, b, op):
    try:
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return a / b
        else:
            return "Unknown operation"
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError:
        return "Type error"


if __name__ == "__main__":
    print("Задача 1")
    print(safe_divide(10, 2))
    print(safe_divide(5, 0))

    print("\nЗадача 2")
    print(to_int("123"))
    print(to_int("abc"))

    print("\nЗадача 3")
    print(safe_operation(10, 2))
    print(safe_operation(5, 0))
    print(safe_operation(5, "a"))

    print("\nЗадача 4")
    print(read_number("10"))
    print(read_number("abc"))

    print("\nЗадача 5")
    print(check_age(20))
    print(check_age(-5))

    print("\nЗадача 6")
    print(safe_sum([1, 2, "a", 3]))

    print("\nЗадача 7")
    print(get_element([1, 2, 3], 1))
    print(get_element([1, 2, 3], 5))

    print("\nЗадача 8")
    print(process_data("10", "2"))
    print(process_data("10", "0"))
    print(process_data("a", "2"))

    print("\nЗадача 9")
    safe_print_number("5")
    safe_print_number("abc")

    print("\nЗадача 10")
    print(calculator(5, 3, "+"))
    print(calculator(5, 0, "/"))
    print(calculator(5, 3, "^"))
    print(calculator(5, "a", "+"))
