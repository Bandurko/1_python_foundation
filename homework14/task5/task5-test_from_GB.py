''' Правильное решение от ГБ '''

import pytest

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


# Тестирование инициализации ширины
def test_width():
    r1 = Rectangle(5)
    assert r1.width == 5


# Тестирование инициализации ширины и высоты
def test_height():
    r2 = Rectangle(3, 4)
    assert r2.height == 4


# Тестирование вычисления периметра
def test_perimeter():
    r1 = Rectangle(5)
    assert r1.perimeter() == 20


# Тестирование вычисления площади
def test_area():
    r2 = Rectangle(3, 4)
    assert r2.area() == 12


# Тестирование операции сложения
def test_addition():
    r1 = Rectangle(5)
    r2 = Rectangle(3, 4)
    r3 = r1 + r2
    assert r3.width == 8
    assert r3.height == 6.0


# Тестирование инициализации отрицательной ширины
def test_negative_width():
    with pytest.raises(NegativeValueError):
        Rectangle(-5)


# Тестирование инициализации отрицательной высоты
def test_negative_height():
    with pytest.raises(NegativeValueError):
        Rectangle(5, -4)


# Тестирование изменения ширины
def test_set_width():
    r1 = Rectangle(5)
    r1.width = 10
    assert r1.width == 10


# Тестирование изменения отрицательной ширины
def test_set_negative_width():
    r1 = Rectangle(5)
    with pytest.raises(NegativeValueError):
        r1.width = -10


# Тестирование изменения высоты
def test_set_height():
    r2 = Rectangle(3, 4)
    r2.height = 6
    assert r2.height == 6


# Тестирование изменения отрицательной высоты
def test_set_negative_height():
    r2 = Rectangle(3, 4)
    with pytest.raises(NegativeValueError):
        r2.height = -6


# Тестирование операции вычитания
def test_subtraction():
    r1 = Rectangle(10)
    r2 = Rectangle(3, 4)
    r3 = r1 - r2
    assert r3.width == 7
    assert r3.height == 6.0


# Тестирование операции вычитания с отрицательным результатом
def test_subtraction_negative_result():
    r1 = Rectangle(3, 4)
    r2 = Rectangle(10)
    with pytest.raises(NegativeValueError):
        r3 = r1 - r2


# Тестирование операции вычитания с одинаковым периметром
def test_subtraction_same_perimeter():
    r1 = Rectangle(5)
    r2 = Rectangle(4, 3)
    r3 = r1 - r2
    assert r3.width == 1
    assert r3.height == 1.0
