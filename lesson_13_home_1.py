
# Для рассмотренного на уроке класса Circle реализовать метод
# производящий вычитание двух окружностей, вычитание радиусов
# произвести по модулю. Если вычитаются две окружности с одинаковым
# значением радиуса, то результатом вычитания будет точка класса Point.


import math
from task_01 import Point


class Circle(Point):
    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return math.pi * self.radius

    def __str__(self):
        return f'Circle(radius - {self.radius}, {self.x}, {self.y})'

    def __sub__(self, other):
        r = abs(self.radius - other.radius)
        x = self.x - other.x
        y = self.y - other.y
        if r == 0:
            return Point(self.x, self.y)
        else:
            return Circle(r, x, y)


a = Circle(9, 3, 6)
b = Circle(5, 1, 4)
print(a - b)
