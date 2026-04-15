class BoundingBox2D:
    def __init__(self):
        self.points = []

    def add_point(self, x, y):
        self.points.append((x, y))

    def left_x(self):
        return min(p[0] for p in self.points)

    def right_x(self):
        return max(p[0] for p in self.points)

    def bottom_y(self):
        return min(p[1] for p in self.points)

    def top_y(self):
        return max(p[1] for p in self.points)

    def width(self):
        return self.right_x() - self.left_x()

    def height(self):
        return self.top_y() - self.bottom_y()


# Пример 1
box = BoundingBox2D()
box.add_point(-2, -3)
box.add_point(4, 5)
print(box.left_x(), box.right_x())  # -2 4
print(box.bottom_y(), box.top_y())  # -3 5
print(box.width(), box.height())  # 6 8
