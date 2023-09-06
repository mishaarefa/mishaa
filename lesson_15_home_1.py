
"""
>>> Calculator.stepen(2, -1)
Возведение в отрицательную степень
>>> Calculator.delenie(2, 0)
Деление на ноль
>>> Calculator.umnozhenie(2, 3)
2  *  3  =  6
"""

class StepenExeption(Exception):
    def __init__(self, message="Возведение в отрицательную степень"):
        super().__init__(message)


class Calculator:
    def plus(self, other):
        try:
            c = self + other
            print(self, " + ", other, " = ", c)
        except:
            print("ошибка")

    def minus(self, other):
        try:
            c = self - other
            print(self, " - ", other, " = ", c)
        except:
            print("ошибка")

    def delenie(self, other):
        try:
            c = self / other
            print(c)
        except ZeroDivisionError:
            print("Деление на ноль")
        except:
            print("ошибка")

    def stepen(self, other):
        try:
            if other < 0:
                raise StepenExeption
            else:
                try:
                    c = self ** other
                    print(self, " ** ", other, " = ", c)
                except Exception:
                    print("ошибка")
        except StepenExeption:
            print("Возведение в отрицательную степень")

    def umnozhenie(self, other):
        try:
            c = self * other
            print(self, " * ", other, " = ", c)
        except:
            print("ошибка")


Calculator.stepen(2, -1)

Calculator.delenie(2, 0)

Calculator.umnozhenie(2, 3)

import doctest
doctest.testmod()

import unittest


class TestDelenie(unittest.TestCase):

    def test_delenie(self):
        self.assertEqual(Calculator.delenie(6, 2), 3)
        self.assertNotEqual(Calculator.delenie(2, 2), 0)

    def test_plus(self):
        self.assertEqual(Calculator.plus(6, 2), 8)
        self.assertEqual(Calculator.plus(6, 2), 10)
