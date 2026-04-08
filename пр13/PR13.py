# Практическая работа №13
# Тема: Лямбда-функции, classmethod и staticmethod

# Задача 1 — Лямбда-функция square
square = lambda x: x ** 2

print(square(5))

print("-" * 30)

# Задача 2 — Лямбда-функция add
add = lambda a, b: a + b

print(add(3, 7))

print("-" * 30)

# Задача 3 — Сортировка строк по длине
words = ["apple", "kiwi", "banana"]
result = sorted(words, key=lambda word: len(word))

print(result)

print("-" * 30)

# Задача 4 — Чётные числа через filter и lambda
numbers = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 == 0, numbers))

print(result)

print("-" * 30)

# Задача 5 — staticmethod в классе MathUtils
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b


print(MathUtils.add(3, 4))

print("-" * 30)

# Задача 6 — staticmethod в классе Validator
class Validator:
    @staticmethod
    def is_positive(n):
        return n > 0


print(Validator.is_positive(5))
print(Validator.is_positive(-3))

print("-" * 30)

# Задача 7 — classmethod в классе Person
class Person:
    def __init__(self, name):
        self.name = name

    @classmethod
    def from_string(cls, s):
        return cls(s)


p = Person.from_string("Alice")
print(p.name)

print("-" * 30)

# Задача 8 — classmethod и счётчик объектов
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def get_count(cls):
        return cls.count


c1 = Counter()
c2 = Counter()
print(Counter.get_count())

print("-" * 30)

# Задача 9 — Обработка списка через staticmethod и lambda
class ListProcessor:
    @staticmethod
    def double(numbers):
        return list(map(lambda x: x * 2, numbers))


print(ListProcessor.double([1, 2, 3]))

print("-" * 30)

# Задача 10 — Calculator с staticmethod, classmethod и lambda
class Calculator:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def create_zero(cls):
        return cls(0)

    def square(self, x):
        func = lambda n: n ** 2
        return func(x)


c = Calculator.create_zero()
print(c.square(5))
print(Calculator.add(2, 3))
