'''

Rectangle тесты unittest

Возьмите код из прошлой задачи "Класс Rectangle".

Напишите к ней тесты, используя unittest и лежать в class TestRectangle(unittest.TestCase)

Тесты:

test_width: Тестирование инициализации ширины. Создайте прямоугольник с шириной 5 и убедитесь, что атрибут width
корректно установлен на 5.

test_height: Тестирование инициализации ширины и высоты. Создайте прямоугольник с шириной 3 и высотой 4 и убедитесь,
что атрибут height корректно установлен на 4.

test_perimeter: Тестирование вычисления периметра. Создайте прямоугольник с шириной 5 и вычислите его периметр.
Убедитесь, что результат равен 20.

test_area: Тестирование вычисления площади. Создайте прямоугольник с шириной 3 и высотой 4 и вычислите его площадь.
Убедитесь, что результат равен 12.

test_addition: Тестирование операции сложения. Создайте два прямоугольника: один с шириной 5, другой с шириной 3 и
высотой 4. Выполните операцию сложения r1 + r2 и убедитесь, что полученный прямоугольник имеет правильные значения
ширины и высоты (8 и 6.0 соответственно).

Используйте модуль unittest для запуска тестов. Все тесты должны выполняться успешно и не вызывать ошибок.

Запускать тесты не надо, автотест это сделает сам:

unittest.main()

На выходе после автоматической обрезки информации в тестах вы должны получить:

FAILED (failures=1)


----------------


import unittest

class NegativeValueError(ValueError):
    pass

class Rectangle:

    def __init__(self, width, height=None):
        if width <= 0:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')
        self._width = width
        if height is None:
            self._height = width
        else:
            if height <= 0:
                raise NegativeValueError(f'Высота должна быть положительной, а не {height}')
            self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {value}')

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise NegativeValueError(f'Высота должна быть положительной, а не {value}')

    def perimeter(self):
        return 2 * (self._width + self._height)

    def area(self):
        return self._width * self._height

    def __add__(self, other):
        width = self._width + other._width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self._width - other._width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

# Введите ваше решение ниже

'''

import unittest


class NegativeValueError(ValueError):
    pass


class Rectangle:

    def __init__(self, width, height=None):
        if width <= 0:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')
        self._width = width
        if height is None:
            self._height = width
        else:
            if height <= 0:
                raise NegativeValueError(f'Высота должна быть положительной, а не {height}')
            self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {value}')

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise NegativeValueError(f'Высота должна быть положительной, а не {value}')

    def perimeter(self):
        return 2 * (self._width + self._height)

    def area(self):
        return self._width * self._height

    def __add__(self, other):
        width = self._width + other._width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self._width - other._width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

# Введите ваше решение ниже


class TestRectangle(unittest.TestCase):

    def test_width(self):
        r1 = Rectangle(5)
        self.assertEqual(r1.width, 5)

    def test_height(self):
        r2 = Rectangle(3, 4)
        self.assertEqual(r2.height, 4)

    def test_perimeter(self):
        r1 = Rectangle(5)
        self.assertEqual(r1.perimeter(), 20)

    def test_area(self):
        r2 = Rectangle(3, 4)
        self.assertEqual(r2.area(), 12)

    def test_addition(self):
        r1 = Rectangle(5)
        r2 = Rectangle(3, 4)
        r3 = r1 + r2
        self.assertEqual(r3.width, 8)
        self.assertEqual(r3.height, 6.0)


if __name__ == '__main__':
    unittest.main()