class SecretNumber:
    def __init__(self):
        self.__number = 0

    def set_number(self, n):
        self.__number = n

    def get_number(self):
        return self.__number


# Пример 1
sn = SecretNumber()
sn.set_number(42)
print(sn.get_number())  # 42
