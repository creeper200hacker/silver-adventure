class StepCounter:
    def __init__(self):
        self.__steps = 0

    def walk(self, steps):
        self.__steps += steps

    def reset(self):
        self.__steps = 0

    def get_steps(self):
        return self.__steps


# Пример 1
counter = StepCounter()
counter.walk(5)
counter.walk(3)
print(counter.get_steps())  # 8
counter.reset()
print(counter.get_steps())  # 0
