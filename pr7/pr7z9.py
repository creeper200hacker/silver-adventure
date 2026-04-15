class LimitedCounter:
    def __init__(self, max_value):
        self.__max_value = max_value
        self.__value = 0

    def increment(self):
        if self.__value < self.__max_value:
            self.__value += 1

    def decrement(self):
        if self.__value > 0:
            self.__value -= 1

    def get_value(self):
        return self.__value


# Пример 1
counter = LimitedCounter(3)
counter.increment()
counter.increment()
counter.increment()
counter.increment()
print(counter.get_value())  # 3
counter.decrement()
print(counter.get_value())  # 2
