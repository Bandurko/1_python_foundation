'''
Задача о матричных операциях

Разработать класс Matrix, представляющий матрицу и обеспечивающий базовые операции с матрицами.

Атрибуты класса:

rows (int): Количество строк в матрице.
cols (int): Количество столбцов в матрице.
data (list): Двумерный список, содержащий элементы матрицы.

Методы класса:

__init__(self, rows, cols): Конструктор класса, который инициализирует атрибуты rows и cols, а также создает двумерный
список data размером rows x cols и заполняет его нулями.

__str__(self): Метод, возвращающий строковое представление матрицы. Возвращаемая строка представляет матрицу, где
элементы разделены пробелами, а строки разделены символами новой строки. Например:

1 2 3
4 5 6

__repr__(self): Метод, возвращающий строковое представление объекта, которое может быть использовано для создания
нового объекта того же класса с такими же размерами и данными.

__eq__(self, other): Метод, определяющий операцию "равно" для двух матриц. Сравнивает две матрицы и возвращает True,
если они имеют одинаковое количество строк и столбцов, а также все элементы равны. Иначе возвращает False.

__add__(self, other): Метод, определяющий операцию сложения двух матриц. Проверяет, что обе матрицы имеют одинаковые
размеры (количество строк и столбцов). Если размеры совпадают, создает новую матрицу, где каждый элемент равен сумме
соответствующих элементов входных матриц.

__mul__(self, other): Метод, определяющий операцию умножения двух матриц. Проверяет, что количество столбцов в первой
матрице равно количеству строк во второй матрице. Если условие выполняется, создает новую матрицу, где элемент на
позиции [i][j] равен сумме произведений элементов соответствующей строки из первой матрицы и столбца из второй матрицы.

Пример

На входе:

# Создаем матрицы
matrix1 = Matrix(2, 3)
matrix1.data = [[1, 2, 3], [4, 5, 6]]

matrix2 = Matrix(2, 3)
matrix2.data = [[7, 8, 9], [10, 11, 12]]

# Выводим матрицы
print(matrix1)

print(matrix2)

На выходе:

1 2 3
4 5 6
7 8 9
10 11 12

На входе:

# Сравниваем матрицы
print(matrix1 == matrix2)

На выходе:

False

На входе:

# Выполняем операцию сложения матриц
matrix_sum = matrix1 + matrix2
print(matrix_sum)

На выходе:

8 10 12
14 16 18

На входе:

# Выполняем операцию умножения матриц
matrix3 = Matrix(3, 2)
matrix3.data = [[1, 2], [3, 4], [5, 6]]

matrix4 = Matrix(2, 2)
matrix4.data = [[7, 8], [9, 10]]

result = matrix3 * matrix4
print(result)

На выходе:

25 28
57 64
89 100
'''
class Matrix:
    '''Конструктор класса, инициализирующий атрибуты rows и cols, а также создающий двумерный список data
    размером rows x cols и заполняющий его нулями.'''

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    # Метод, возвращающий строковое представление матрицы. Возвращаемая строка представляет матрицу, где элементы
    # разделены пробелами, а строки разделены символами новой строки.
    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    # Метод, возвращающий строковое представление объекта, которое может быть использовано для создания нового объекта
    # того же класса с такими же размерами и данными.
    def __repr__(self):
        return f'Matrix({self.rows}, {self.cols})'

    # Метод, определяющий операцию "равно" для двух матриц. Сравнивает две матрицы и возвращает True, если они имеют
    # одинаковое количество строк и столбцов, а также все элементы равны. Иначе возвращает False.
    def __eq__(self, other):
        if isinstance(other, Matrix) and self.rows == other.rows and self.cols == other.cols:
            return all(self.data[i][j] == other.data[i][j] for i in range(self.rows) for j in range(self.cols))
        return False

    # Метод, определяющий операцию сложения двух матриц. Проверяет, что обе матрицы имеют одинаковые размеры
    # (количество строк и столбцов). Если размеры совпадают, создает новую матрицу, где каждый элемент равен сумме
    # соответствующих элементов входных матриц.
    def __add__(self, other):
        if isinstance(other, Matrix) and self.rows == other.rows and self.cols == other.cols:
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result.data[i][j] = self.data[i][j] + other.data[i][j]
            return result
        else:
            raise ValueError("Матрицы должны иметь одинаковые размеры для сложения.")

    # Метод, определяющий операцию умножения двух матриц. Проверяет, что количество столбцов в первой матрице равно
    # количеству строк во второй матрице. Если условие выполняется, создает новую матрицу, где элемент
    # на позиции [i][j] равен сумме произведений элементов соответствующей строки из первой матрицы и столбца из в
    # торой матрицы.
    def __mul__(self, other):
        if isinstance(other, Matrix) and self.cols == other.rows:
            result = Matrix(self.rows, other.cols)
            for i in range(self.rows):
                for j in range(other.cols):
                    for k in range(self.cols):
                        result.data[i][j] += self.data[i][k] * other.data[k][j]
            return result
        else:
            raise ValueError(
                "Количество столбцов в первой матрице должно быть равно количеству строк во второй матрице для выполнения умножения.")


# Создаем матрицы
matrix1 = Matrix(2, 3)
matrix1.data = [[1, 2, 3], [4, 5, 6]]

matrix2 = Matrix(2, 3)
matrix2.data = [[7, 8, 9], [10, 11, 12]]

# Выводим матрицы
print(matrix1)
print(matrix2)
# Сравниваем матрицы
print(matrix1 == matrix2)
# Выполняем операцию сложения матриц
matrix_sum = matrix1 + matrix2
print(matrix_sum)
# Выполняем операцию умножения матриц
matrix3 = Matrix(3, 2)
matrix3.data = [[1, 2], [3, 4], [5, 6]]

matrix4 = Matrix(2, 2)
matrix4.data = [[7, 8], [9, 10]]

result = matrix3 * matrix4
print(result)




'''


Правильное решение от ГБ


class Matrix:
    """
    Класс, представляющий матрицу.

    Атрибуты:
    - rows (int): количество строк в матрице
    - cols (int): количество столбцов в матрице
    - data (list): двумерный список, содержащий элементы матрицы

    Методы:
    - __str__(): возвращает строковое представление матрицы
    - __repr__(): возвращает строковое представление матрицы, которое может быть использовано для создания нового объекта
    - __eq__(other): определяет операцию "равно" для двух матриц
    - __add__(other): определяет операцию сложения двух матриц
    - __mul__(other): определяет операцию умножения двух матриц
    """

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for j in range(cols)] for i in range(rows)]

    def __str__(self):
        """
        Возвращает строковое представление матрицы.

        Возвращает:
        - str: строковое представление матрицы
        """
        return '\n'.join([' '.join([str(self.data[i][j]) for j in range(self.cols)]) for i in range(self.rows)])

    def __repr__(self):
        """
        Возвращает строковое представление матрицы, которое может быть использовано для создания нового объекта.

        Возвращает:
        - str: строковое представление матрицы
        """
        return f"Matrix({self.rows}, {self.cols})"

    def __eq__(self, other):
        """
        Определяет операцию "равно" для двух матриц.

        Аргументы:
        - other (Matrix): вторая матрица

        Возвращает:
        - bool: True, если матрицы равны, иначе False
        """
        if self.rows != other.rows or self.cols != other.cols:
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                if self.data[i][j] != other.data[i][j]:
                    return False
        return True

    def __add__(self, other):
        """
        Определяет операцию сложения двух матриц.

        Аргументы:
        - other (Matrix): вторая матрица

        Возвращает:
        - Matrix: новая матрица, полученная путем сложения двух исходных матриц
        """
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны иметь одинаковые размеры")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def __mul__(self, other):
        """
        Определяет операцию умножения двух матриц.

        Аргументы:
        - other (Matrix): вторая матрица

        Возвращает:
        - Matrix: новая матрица, полученная путем умножения двух исходных матриц
        """
        if self.cols != other.rows:
            raise ValueError("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы")
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result



'''