# Класс Vector
import math

class Vector:
    ''' Класс Vector представляет два значения в качестве вектора,
     разрешая многие математические вычисления '''
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'This vector has the value ({self.x}, {self.y})'

    def __add__(self, o_other):  # вызываем оператор +
        return Vector(self.x + o_other.x, self.y + o_other.y)

    def __sub__(self, o_other):  # вызываем оператор -
        return Vector(self.x - o_other.x, self.y - o_other.y)

    def __mul__(self, o_other):  # вызываем оператор *
        if isinstance(o_other, Vector):
            return Vector((self.x * o_other.x), (self.y * o_other.y))
        elif isinstance(o_other, (int, float)):
            return Vector((self.x * o_other), (self.y * o_other))
        else:
            raise TypeError('Second value must be a vector or scalar')

    def __abs__(self):
        return math.sqrt((self.x**2) + (self.y**2))

    def __eq__(self, o_other):  # вызываем оператор ==
        return (self.x == o_other.x) and (self.y == o_other.y)

    def __ne__(self, o_other):  # вызываем оператор !=
        return not (self == o_other)  # вызываем метод __eq__

    def __lt__(self, o_other):  # вызываем оператор <
        if abs(self) < abs(o_other):  # вызываем метод __abs__
            return True
        else:
            return False

    def __gt__(self, o_other):  # вызываем оператор >
        if abs(self) > abs(o_other):  # вызываем метод __abs__
            return True
        else:
            return False


o_vector1 = Vector(3, 2)
o_vector2 = Vector(1, 3)

o_new_vector = o_vector1 + o_vector2  # Используем оператор +
                                      # для сложения векторов

print(o_new_vector)