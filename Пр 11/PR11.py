
class Animal:
    def speak(self):
        print("Some sound")


class Dog(Animal):
    def speak(self):
        print("Woof")


class Cat(Animal):
    def speak(self):
        print("Meow")


class Multiplier:
    def multiply(self, a, b=None):
        if b is None:
            return a * a
        return a * b


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position


class Printer:
    def print_message(self, msg, times=1):
        for _ in range(times):
            print(msg)


def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


@logger
def say_hello():
    print("Hello!")


def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat(3)
def greet():
    print("Hi!")


class Adder:
    def add(self, a, b=None):
        if b is None:
            return a + 10
        return a + b


def check_positive(func):
    def wrapper(*args, **kwargs):
        numbers = list(args) + list(kwargs.values())
        for value in numbers:
            if isinstance(value, (int, float)) and value < 0:
                print("Error")
                return
        return func(*args, **kwargs)
    return wrapper


@check_positive
def multiply(a, b):
    print(a * b)


class Worker:
    def work(self):
        print("Working...")


class Teacher(Worker):
    def work(self):
        print("Teaching...")


def excited(func):
    def wrapper(*args, **kwargs):
        print("Let's go!")
        return func(*args, **kwargs)
    return wrapper


class Calculator:
    def calculate(self, x, y=None):
        if y is None:
            return x * x
        return x + y


def log_call(func):
    def wrapper(*args, **kwargs):
        print("Function called")
        return func(*args, **kwargs)
    return wrapper


class AdvancedCalculator(Calculator):
    def calculate(self, x, y=None):
        result = super().calculate(x, y)
        return result + 10


if __name__ == "__main__":
    print("Задача 1")
    animals = [Dog(), Cat(), Animal()]
    for a in animals:
        a.speak()

    print("\nЗадача 2")
    m = Multiplier()
    print(m.multiply(5))
    print(m.multiply(2, 3))

    print("\nЗадача 3")
    e = Employee("Alice", 30, "Teacher")
    print(e.name, e.age, e.position)

    print("\nЗадача 4")
    p = Printer()
    p.print_message("Hello")
    p.print_message("Hi", 3)

    print("\nЗадача 5")
    say_hello()

    print("\nЗадача 6")
    greet()

    print("\nЗадача 7")
    a = Adder()
    print(a.add(5))
    print(a.add(3, 4))

    print("\nЗадача 8")
    multiply(3, 4)
    multiply(3, -1)

    print("\nЗадача 9")
    t = Teacher()
    t.work = excited(t.work)
    t.work()

    print("\nЗадача 10")
    calc = AdvancedCalculator()
    calc.calculate = log_call(calc.calculate)
    print(calc.calculate(5))
    print(calc.calculate(2, 3))
