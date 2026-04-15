class Point2D:
    def __init__(self):
        self.__x = 0
        self.__y = 0

    def set_coordinates(self, x, y):
        self.__x = x
        self.__y = y

    def get_coordinates(self):
        return (self.__x, self.__y)

    def distance_from_origin(self):
        return (self.__x ** 2 + self.__y ** 2) ** 0.5


# Пример 1
point = Point2D()
point.set_coordinates(3, 4)
print(point.get_coordinates())  # (3, 4)
print(point.distance_from_origin())  # 5.0
