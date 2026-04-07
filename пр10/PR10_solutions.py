class NumberWrapper:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return NumberWrapper(self.value + other.value)

    def get_value(self):
        return self.value


class NumberWrapperSub:
    def __init__(self, value):
        self.value = value

    def __sub__(self, other):
        return NumberWrapperSub(self.value - other.value)

    def get_value(self):
        return self.value


class Multiplier:
    def __init__(self, value):
        self.value = value

    def __mul__(self, other):
        return Multiplier(self.value * other.value)

    def get_value(self):
        return self.value


class Divider:
    def __init__(self, value):
        self.value = value

    def __truediv__(self, other):
        if other.value == 0:
            raise ZeroDivisionError("Нельзя делить на ноль")
        return Divider(self.value / other.value)

    def get_value(self):
        return self.value


class ComparableNumber:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def get_value(self):
        return self.value


class EqualNumber:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def get_value(self):
        return self.value


class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person: {self.name}"


class BooleanWrapper:
    def __init__(self, value):
        self.value = value

    def __bool__(self):
        return self.value


class Counter:
    def __init__(self, value):
        self.value = value

    def __iadd__(self, number):
        self.value += number
        return self

    def get_value(self):
        return self.value


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"


if __name__ == "__main__":
    print("Задача 1")
    a = NumberWrapper(5)
    b = NumberWrapper(10)
    c = a + b
    print(c.get_value())

    print("\nЗадача 2")
    a = NumberWrapperSub(10)
    b = NumberWrapperSub(3)
    c = a - b
    print(c.get_value())

    print("\nЗадача 3")
    a = Multiplier(4)
    b = Multiplier(5)
    c = a * b
    print(c.get_value())

    print("\nЗадача 4")
    a = Divider(20)
    b = Divider(4)
    c = a / b
    print(c.get_value())

    print("\nЗадача 5")
    a = ComparableNumber(5)
    b = ComparableNumber(10)
    print(a < b)
    print(b < a)

    print("\nЗадача 6")
    a = EqualNumber(5)
    b = EqualNumber(5)
    c = EqualNumber(3)
    print(a == b)
    print(a == c)

    print("\nЗадача 7")
    p = Person("Alice")
    print(p)

    print("\nЗадача 8")
    b = BooleanWrapper(True)
    print(not b)
    c = BooleanWrapper(False)
    print(not c)

    print("\nЗадача 9")
    c = Counter(5)
    c += 3
    print(c.get_value())

    print("\nЗадача 10")
    v1 = Vector2D(1, 2)
    v2 = Vector2D(3, 4)
    v3 = v1 + v2
    v4 = v2 - v1
    print(v3)
    print(v4)
