class UserName:
    def __init__(self):
        self.__name = ""

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name.upper()


# Пример 1
user = UserName()
user.set_name('alex')
print(user.get_name())  # ALEX
