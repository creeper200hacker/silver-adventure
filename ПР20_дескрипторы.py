# Практическая работа 20 – Дескрипторы

# Задача 1 – Простой дескриптор
class SimpleDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__.get('value')

    def __set__(self, instance, value):
        instance.__dict__['value'] = value

class Example1:
    attr = SimpleDescriptor()

obj1 = Example1()
obj1.attr = 10
print('Задача 1:', obj1.attr)


# Задача 2 – Дескриптор с логированием
class LoggingGetDescriptor:
    def __get__(self, instance, owner):
        print('Getting value')
        return instance.__dict__.get('value')

    def __set__(self, instance, value):
        instance.__dict__['value'] = value

class Example2:
    attr = LoggingGetDescriptor()

obj2 = Example2()
obj2.attr = 20
print('Задача 2:', obj2.attr)


# Задача 3 – Дескриптор с установкой
class LoggingSetDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__.get('value')

    def __set__(self, instance, value):
        print('Setting value')
        instance.__dict__['value'] = value

class Example3:
    attr = LoggingSetDescriptor()

obj3 = Example3()
obj3.attr = 30
print('Задача 3:', obj3.attr)


# Задача 4 – Приватное хранение
class PrivateStorageDescriptor:
    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.private_name)

    def __set__(self, instance, value):
        instance.__dict__[self.private_name] = value

class Example4:
    attr = PrivateStorageDescriptor()

obj4 = Example4()
obj4.attr = 40
print('Задача 4:', obj4.attr)
print('Хранение в __dict__:', obj4.__dict__)


# Задача 5 – Ограничение типа
class IntDescriptor:
    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.private_name)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Значение должно быть int')
        instance.__dict__[self.private_name] = value

class Example5:
    number = IntDescriptor()

obj5 = Example5()
obj5.number = 5
print('Задача 5:', obj5.number)


# Задача 6 – Положительные числа
class PositiveDescriptor:
    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.private_name)

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError('Значение должно быть положительным')
        instance.__dict__[self.private_name] = value

class Example6:
    number = PositiveDescriptor()

obj6 = Example6()
obj6.number = 15
print('Задача 6:', obj6.number)


# Задача 7 – Строковый дескриптор
class StringDescriptor:
    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.private_name)

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError('Значение должно быть строкой')
        instance.__dict__[self.private_name] = value

class Example7:
    text = StringDescriptor()

obj7 = Example7()
obj7.text = 'Python'
print('Задача 7:', obj7.text)


# Задача 8 – Значение по умолчанию
class DefaultDescriptor:
    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.private_name, 'default')

    def __set__(self, instance, value):
        instance.__dict__[self.private_name] = value

class Example8:
    attr = DefaultDescriptor()

obj8 = Example8()
print('Задача 8:', obj8.attr)


# Задача 9 – Счётчик обращений
class AccessCounterDescriptor:
    def __init__(self):
        self.count = 0

    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        self.count += 1
        return instance.__dict__.get(self.private_name)

    def __set__(self, instance, value):
        instance.__dict__[self.private_name] = value

class Example9:
    attr = AccessCounterDescriptor()

obj9 = Example9()
obj9.attr = 'test'
print('Задача 9:', obj9.attr)
print('Количество обращений:', Example9.attr.count)


# Задача 10 – Ограничение длины
class MaxLengthDescriptor:
    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.private_name)

    def __set__(self, instance, value):
        if len(value) > 10:
            raise ValueError('Строка должна быть длиной не более 10 символов')
        instance.__dict__[self.private_name] = value

class Example10:
    text = MaxLengthDescriptor()

obj10 = Example10()
obj10.text = 'Hello'
print('Задача 10:', obj10.text)


# Задача 11 – Email-дескриптор
class EmailDescriptor:
    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.private_name)

    def __set__(self, instance, value):
        if '@' not in value:
            raise ValueError('Email должен содержать символ @')
        instance.__dict__[self.private_name] = value

class Example11:
    email = EmailDescriptor()

obj11 = Example11()
obj11.email = 'student@example.com'
print('Задача 11:', obj11.email)


# Задача 12 – Возраст
class AgeDescriptor:
    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.private_name)

    def __set__(self, instance, value):
        if not 0 <= value <= 120:
            raise ValueError('Возраст должен быть от 0 до 120')
        instance.__dict__[self.private_name] = value

class Example12:
    age = AgeDescriptor()

obj12 = Example12()
obj12.age = 19
print('Задача 12:', obj12.age)


# Задача 13 – Округление
class RoundDescriptor:
    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.private_name)

    def __set__(self, instance, value):
        instance.__dict__[self.private_name] = round(value, 2)

class Example13:
    number = RoundDescriptor()

obj13 = Example13()
obj13.number = 12.34567
print('Задача 13:', obj13.number)


# Задача 14 – Только одно присваивание
class OnceDescriptor:
    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.private_name)

    def __set__(self, instance, value):
        if self.private_name in instance.__dict__:
            raise AttributeError('Значение можно присвоить только один раз')
        instance.__dict__[self.private_name] = value

class Example14:
    code = OnceDescriptor()

obj14 = Example14()
obj14.code = 'ABC'
print('Задача 14:', obj14.code)


# Задача 15 – Лог изменений
class ChangeLogDescriptor:
    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.private_name)

    def __set__(self, instance, value):
        old_value = instance.__dict__.get(self.private_name, None)
        print(f'Старое значение: {old_value}, новое значение: {value}')
        instance.__dict__[self.private_name] = value

class Example15:
    attr = ChangeLogDescriptor()

obj15 = Example15()
obj15.attr = 1
obj15.attr = 2
print('Задача 15:', obj15.attr)


# Задача 16 – Связанные поля
class CelsiusDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__.get('_celsius')

    def __set__(self, instance, value):
        instance.__dict__['_celsius'] = value
        instance.__dict__['_fahrenheit'] = value * 9 / 5 + 32

class Temperature:
    celsius = CelsiusDescriptor()

    @property
    def fahrenheit(self):
        return self.__dict__.get('_fahrenheit')

temp = Temperature()
temp.celsius = 25
print('Задача 16:', temp.celsius, 'C =', temp.fahrenheit, 'F')


# Задача 17 – Кэширование
class CachedDescriptor:
    def __get__(self, instance, owner):
        if '_cached_value' not in instance.__dict__:
            print('Вычисление значения')
            instance.__dict__['_cached_value'] = instance.calculate()
        return instance.__dict__['_cached_value']

class Example17:
    cached = CachedDescriptor()

    def calculate(self):
        return 100 + 50

obj17 = Example17()
print('Задача 17:', obj17.cached)
print('Повторное обращение:', obj17.cached)


# Задача 18 – Список чисел
class NumberListDescriptor:
    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.private_name)

    def __set__(self, instance, value):
        if not isinstance(value, list) or not all(isinstance(i, (int, float)) for i in value):
            raise TypeError('Значение должно быть списком чисел')
        instance.__dict__[self.private_name] = value

class Example18:
    numbers = NumberListDescriptor()

obj18 = Example18()
obj18.numbers = [1, 2, 3.5]
print('Задача 18:', obj18.numbers)


# Задача 19 – Счётчик объектов
class ObjectCounterDescriptor:
    count = 0

    def __get__(self, instance, owner):
        return ObjectCounterDescriptor.count

class CountedClass:
    object_count = ObjectCounterDescriptor()

    def __init__(self):
        ObjectCounterDescriptor.count += 1

first = CountedClass()
second = CountedClass()
third = CountedClass()
print('Задача 19:', first.object_count)


# Задача 20 – Комплексный дескриптор
class ComplexDescriptor:
    def __init__(self, data_type, min_value=None, max_value=None):
        self.data_type = data_type
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, instance, owner):
        print('Getting value')
        return instance.__dict__.get(self.private_name)

    def __set__(self, instance, value):
        print('Setting value')
        if not isinstance(value, self.data_type):
            raise TypeError(f'Значение должно быть {self.data_type.__name__}')
        if self.min_value is not None and value < self.min_value:
            raise ValueError('Значение меньше допустимого')
        if self.max_value is not None and value > self.max_value:
            raise ValueError('Значение больше допустимого')
        instance.__dict__[self.private_name] = value

    def __delete__(self, instance):
        raise AttributeError('Удаление запрещено')

class Example20:
    score = ComplexDescriptor(int, 0, 100)

obj20 = Example20()
obj20.score = 85
print('Задача 20:', obj20.score)
