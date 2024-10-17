# Класс Fraction

import math

class Fraction:
    def __init__(self, numerator, denominator):
        if not isinstance(numerator, int):
            raise TypeError('Numerator', numerator, 'must be an integer')
        if not isinstance(denominator, int):
            raise TypeError('Denominator', denominator, 'must be an integer')

        self.numerator = numerator
        self.denominator = denominator

        # Используем математический пакет, чтобы найти наибольший
        # общий делитель
        greatest_common_divider = math.gcd(self.numerator,
                                           self.denominator)
        if greatest_common_divider > 1:
            self.numerator //= greatest_common_divider
            self.denominator //= greatest_common_divider

        self.value = self.numerator / self.denominator

        # нормализуем знак числителя и знаменателя
        self.numerator = (int(math.copysign(1.0, self.value)) *
                          abs(self.numerator))
        self.denominator = abs(self.denominator)

    def get_value(self):
        return self.value

    def __str__(self):
        """ Создаем строковое представление дроби """
        output = ('Fraction: ' + str(self.numerator) + '/' +
                  str(self.denominator) +
                  '\n' + 'Value: ' + str(self.value) + '\n')
        return output

    def __add__(self, o_other_fraction):
        """ Складываем два объекта Fraction """
        if not isinstance(o_other_fraction, Fraction):
            raise TypeError('Second value in attempt to add is not a Fraction')

        # используем математический пакет, чтобы найти наименьшее
        # общее кратное
        new_dominator = math.lcm(self.denominator,
                                 o_other_fraction.denominator)
        multiplication_factor = new_dominator // self.denominator
        equivalent_numerator = self.numerator * multiplication_factor

        other_multiplication_factor = new_dominator // o_other_fraction.denominator
        other_fraction_equivalent_numerator = (
                o_other_fraction.numerator * other_multiplication_factor)

        new_numerator = (equivalent_numerator +
                         other_fraction_equivalent_numerator)

        o_added_fraction = Fraction(new_numerator, new_dominator)
        return o_added_fraction

    def __eq__(self, o_other_fraction):
        """ Проверяем на равенство """
        if not isinstance(o_other_fraction, Fraction):
            return False  # не сравнимо с дробью
        if (self.numerator == o_other_fraction.numerator) and \
            (self.denominator == o_other_fraction.denominator):
            return True
        else:
            return False

# тестовый код

o_fraction1 = Fraction(1, 3)
o_fraction2 = Fraction(2, 5)
print('Fraction1\n', o_fraction1)  # выводим на экран объект ...
                                   # вызываем метод __str__

print('Fraction2\n', o_fraction2)

o_sum_fraction = o_fraction1 + o_fraction2
print('Sum is\n', o_sum_fraction)

print('Are fractions 1 and 2 equal?', o_fraction1 == o_fraction2)

# ожидаем False
print()

o_fraction3 = Fraction(-20, 80)
o_fraction4 = Fraction(4, -16)
print('Fraction3\n', o_fraction3)
print('Fraction4\n', o_fraction4)

print('Are fractions 3 and 4 equal?', o_fraction3 == o_fraction4)
# Ожидаем True
print()

o_fraction5 = Fraction(5, 2)
o_fraction6 = Fraction(500, 200)
print('Sum of 5/2 and 500/200 is\n', o_fraction5 + o_fraction6)