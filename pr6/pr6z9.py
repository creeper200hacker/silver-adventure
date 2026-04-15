class EvenOddSumTracker:
    def __init__(self):
        self.even_sum_val = 0
        self.odd_sum_val = 0

    def add_number(self, n):
        if n % 2 == 0:
            self.even_sum_val += n
        else:
            self.odd_sum_val += n

    def even_sum(self):
        return self.even_sum_val

    def odd_sum(self):
        return self.odd_sum_val


# Пример 1
tracker = EvenOddSumTracker()
tracker.add_number(2)
tracker.add_number(3)
tracker.add_number(4)
tracker.add_number(5)
print(tracker.even_sum())  # 6
print(tracker.odd_sum())  # 8
