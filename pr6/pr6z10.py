class AlternatingCounter:
    def __init__(self):
        self.a_count = 0
        self.b_count = 0
        self._toggle = True  # True для a, False для b

    def count(self):
        if self._toggle:
            self.a_count += 1
        else:
            self.b_count += 1
        self._toggle = not self._toggle
        return (self.a_count, self.b_count)

    def reset(self):
        self.a_count = 0
        self.b_count = 0
        self._toggle = True


# Пример 1
counter = AlternatingCounter()
print(counter.count())  # (1, 0)
print(counter.count())  # (1, 1)
print(counter.count())  # (2, 1)
counter.reset()
print(counter.count())  # (1, 0)
