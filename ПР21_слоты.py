# Практическая 21 - Слоты
import math
from datetime import datetime

# Задача 1
class Person:
    __slots__ = ('name', 'age')

person = Person()
person.name = 'Амир'
person.age = 19
print('Задача 1:', person.name, person.age)


# Задача 2
class Animal:
    __slots__ = ('type', 'weight')

animal = Animal()
animal.type = 'Кот'
animal.weight = 4.5
try:
    animal.color = 'Серый'
except AttributeError as error:
    print('Задача 2: новый атрибут добавить нельзя:', error)


# Задача 3
class WithSlots:
    __slots__ = ('name',)

class WithoutSlots:
    pass

obj_slots = WithSlots()
obj_slots.name = 'Объект со слотами'
obj_no_slots = WithoutSlots()
obj_no_slots.name = 'Объект без слотов'
obj_no_slots.new_attr = 'Можно добавить'
print('Задача 3: без __slots__ новый атрибут:', obj_no_slots.new_attr)
try:
    obj_slots.new_attr = 'Нельзя добавить'
except AttributeError:
    print('Задача 3: с __slots__ новый атрибут добавить нельзя')


# Задача 4
class Car:
    __slots__ = ('brand', 'model', 'year')

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

car = Car('Toyota', 'Camry', 2020)
print('Задача 4:', car.brand, car.model, car.year)


# Задача 5
class Book:
    __slots__ = ('title', 'author')

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def info(self):
        return f'Книга: {self.title}, автор: {self.author}'

book = Book('Преступление и наказание', 'Ф. М. Достоевский')
print('Задача 5:', book.info())


# Задача 6
class StudentGrade:
    __slots__ = ('name', 'grade')

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def change_grade(self, new_grade):
        self.grade = new_grade

student = StudentGrade('Иван', 4)
student.change_grade(5)
print('Задача 6:', student.name, student.grade)


# Задача 7
class Point:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def coordinates(self):
        return f'({self.x}, {self.y})'

point = Point(10, 20)
print('Задача 7:', point.coordinates())


# Задача 8
class Rectangle:
    __slots__ = ('width', 'height')

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rectangle = Rectangle(5, 8)
print('Задача 8:', rectangle.area())


# Задача 9
class Circle:
    __slots__ = ('radius',)

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

circle = Circle(3)
print('Задача 9:', round(circle.area(), 2))


# Задача 10
class Employee:
    __slots__ = ('name', 'salary')

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * percent / 100

employee = Employee('Пётр', 50000)
employee.increase_salary(10)
print('Задача 10:', employee.name, employee.salary)


# Задача 11
class Product:
    __slots__ = ('name', 'price')

    def __init__(self, name, price):
        self.name = name
        self.set_price(price)

    def set_price(self, price):
        if price < 0:
            raise ValueError('Цена не может быть отрицательной')
        self.price = price

product = Product('Ноутбук', 70000)
print('Задача 11:', product.name, product.price)


# Задача 12
class User:
    __slots__ = ('login', 'password')

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def change_password(self, new_password):
        self.password = new_password

user = User('admin', '12345')
user.change_password('qwerty')
print('Задача 12:', user.login, user.password)


# Задача 13
class BasePerson:
    __slots__ = ('name',)

    def __init__(self, name):
        self.name = name

class StudentFromPerson(BasePerson):
    __slots__ = ('grade',)

    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

student2 = StudentFromPerson('Анна', 5)
print('Задача 13:', student2.name, student2.grade)


# Задача 14
class Vector:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f'({self.x}, {self.y})'

v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1.add(v2)
print('Задача 14:', v3)


# Задача 15
class BankAccount:
    __slots__ = ('balance',)

    def __init__(self, balance=0):
        if balance < 0:
            raise ValueError('Начальный баланс не может быть отрицательным')
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Сумма пополнения должна быть положительной')
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError('Недостаточно средств')
        self.balance -= amount

account = BankAccount(1000)
account.deposit(500)
account.withdraw(300)
print('Задача 15:', account.balance)


# Задача 16
class Temperature:
    __slots__ = ('value',)

    def __init__(self, value):
        self.value = value

    def to_fahrenheit(self):
        return self.value * 9 / 5 + 32

temperature = Temperature(25)
print('Задача 16:', temperature.to_fahrenheit())


# Задача 17
class Timer:
    __slots__ = ('start', 'end')

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def difference(self):
        return self.end - self.start

start_time = datetime(2026, 5, 5, 12, 0, 0)
end_time = datetime(2026, 5, 5, 13, 30, 0)
timer = Timer(start_time, end_time)
print('Задача 17:', timer.difference())


# Задача 18
class Message:
    __slots__ = ('text', 'author')

    def __init__(self, text, author):
        self.text = text
        self.author = author

    def format_message(self):
        return f'{self.author}: {self.text}'

message = Message('Привет!', 'Амир')
print('Задача 18:', message.format_message())


# Задача 19
class Order:
    __slots__ = ('items',)

    def __init__(self, items):
        self.items = items

    def total(self):
        return sum(self.items)

order = Order([100, 250, 50])
print('Задача 19:', order.total())


# Задача 20
class Student:
    __slots__ = ('name', 'age', 'grades')

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def add_grade(self, value):
        self.grades.append(value)

    def average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

students = [Student('Алексей', 18), Student('Мария', 19), Student('Олег', 20)]
students[0].add_grade(5)
students[0].add_grade(4)
students[1].add_grade(4)
students[1].add_grade(4)
students[1].add_grade(5)
students[2].add_grade(3)
students[2].add_grade(5)

for current_student in students:
    print(f'Задача 20: {current_student.name}, средний балл: {current_student.average():.2f}')

try:
    students[0].group = 'ИС-31'
except AttributeError:
    print('Задача 20: новый атрибут добавить нельзя')
