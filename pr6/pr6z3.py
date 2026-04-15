class SeeSaw:
    def __init__(self):
        self.left_weight = 0
        self.right_weight = 0

    def add_right(self, weight):
        self.right_weight += weight

    def add_left(self, weight):
        self.left_weight += weight

    def balance(self):
        if self.left_weight == self.right_weight:
            return '='
        elif self.right_weight > self.left_weight:
            return 'R'
        else:
            return 'L'


# Пример 1
seesaw = SeeSaw()
seesaw.add_right(8)
seesaw.add_left(5)
seesaw.add_left(4)
print(seesaw.balance())  # L
