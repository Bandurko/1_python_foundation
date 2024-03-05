'''

Генерация случайных данных и нахождение корней квадратного уравнения.
Создайте функцию generate_csv_file(file_name, rows), которая будет генерировать по три случайны числа в каждой строке,
от 100-1000 строк, и записывать их в CSV-файл. Функция принимает два аргумента:
file_name (строка) - имя файла, в который будут записаны данные.
rows(целое число) - количество строк (записей) данных, которые нужно сгенерировать.
Создайте функцию find_roots(a, b, c), которая будет находить корни квадратного уравнения вида ax^2 + bx + c = 0.
Функция принимает три аргумента:
a, b, c (целые числа) - коэффициенты квадратного уравнения.
Функция возвращает:
None, если уравнение не имеет корней (дискриминант отрицателен).
Одно число, если уравнение имеет один корень (дискриминант равен нулю).
Два числа (корни), если уравнение имеет два корня (дискриминант положителен).
Создайте декоратор save_to_json(func), который будет оборачивать функцию find_roots. Декоратор выполняет следующие
действия:
Читает данные из CSV-файла, переданного в аргументе функции, исходя из аргумента args[0].
Для каждой строки данных вычисляет корни квадратного уравнения с помощью функции find_roots.
Сохраняет результаты в формате JSON в файл results.json. Каждая запись JSON содержит параметры a, b, c и результаты
вычислений.
Таким образом, после выполнения функций generate_csv_file и find_roots в файле results.json будет сохранена
информация о параметрах и результатах вычислений для каждой строки данных из CSV-файла.
Пример
На входе:
generate_csv_file("input_data.csv", 101)
find_roots("input_data.csv")
with open("results.json", 'r') as f:
    data = json.load(f)
if 100<=len(data)<=1000:
    print(True)
else:
    print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")
print(len(data)==101)
На выходе:
True
True

'''

import csv
import random
import math
import json


# Функция для генерации CSV файла с случайными числами
def generate_csv_file(file_name, rows):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        for _ in range(rows):
            # Генерируем три случайных числа и записываем их в CSV файл
            numbers = [random.randint(1, 100) for _ in range(3)]
            writer.writerow(numbers)


# Функция для нахождения корней квадратного уравнения
def find_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        return None
    elif discriminant == 0:
        return -b / (2 * a)
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2


# Декоратор для сохранения результатов в JSON файл
def save_to_json(func):
    def wrapper(file_name):
        results = []

        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                a, b, c = map(int, row)
                result = func(a, b, c)
                results.append({'a': a, 'b': b, 'c': c, 'roots': result})

        with open("results.json", 'w') as file:
            json.dump(results, file, indent=4)

    return wrapper


@save_to_json
def find_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        return None
    elif discriminant == 0:
        root = -b / (2 * a)
        return root
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2


# Генерируем CSV файл
generate_csv_file("input_data.csv", 101)
# Находим корни квадратного уравнения
find_roots("input_data.csv")

# Читаем результаты из JSON файла
with open("results.json", 'r') as file:
    data = json.load(file)

# Проверяем, что количество результатов находится в диапазоне от 100 до 1000
if 100 <= len(data) <= 1000:
    print(True)
else:
    print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")

# Проверяем, что количество результатов равно 101
print(len(data) == 101)


'''

Правильное решение от ГБ

import csv
import json
import random

def save_to_json(func):
    def wrapper(*args):
        result_list = []
        with open(args[0], 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                a, b, c = map(int, row)
                result = func(a, b, c)
                data = {'parameters': [a, b, c], 'result': result}
                result_list.append(data)
        with open('results.json', 'w') as f:
            json.dump(result_list, f)
    return wrapper

@save_to_json
def find_roots(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return None
    elif d == 0:
        return -b / (2 * a)
    else:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        return x1, x2

def generate_csv_file(file_name, rows):
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        for i in range(rows):
            row = [random.randint(1, 1000) for _ in range(3)]
            writer.writerow(row)

'''