class NumberDivider:
    def __init__(self):
        self.divisible_by_3 = []
        self.not_divisible_by_3 = []

    def add_number(self, n):
        if n % 3 == 0:
            self.divisible_by_3.append(n)
        else:
            self.not_divisible_by_3.append(n)

    def divisible(self):
        return self.divisible_by_3

    def not_divisible(self):
        return self.not_divisible_by_3


# Пример 1
divider = NumberDivider()
divider.add_number(1)
divider.add_number(3)
divider.add_number(4)
divider.add_number(6)
divider.add_number(7)
print(divider.divisible())  # [3, 6]
print(divider.not_divisible())  # [1, 4, 7]
