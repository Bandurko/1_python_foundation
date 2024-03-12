'''
Работа с данными студентов

Создайте класс студента.
○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв. Если ФИО не соответствует
условию, выведите:

ФИО должно состоять только из букв и начинаться с заглавной буквы

○ Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
Если такого предмета нет, выведите:

Предмет {Название предмета} не найден

○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100). В противном случае выведите:

Оценка должна быть целым числом от 2 до 5

Результат теста должен быть целым числом от 0 до 100

○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.

Вам предоставлен файл subjects.csv, содержащий предметы. Сейчас в файл записана следующая информация.

Математика,Физика,История,Литература

Создайте класс Student, который будет представлять студента и его успехи по предметам. Класс должен иметь следующие
методы:
Атрибуты класса:

name (str): ФИО студента. subjects (dict): Словарь, который хранит предметы в качестве ключей и информацию об оценках и
результатах тестов для каждого предмета в виде словаря.

Магические методы (Dunder-методы):

__init__(self, name, subjects_file): Конструктор класса. Принимает имя студента и файл с предметами и их результатами.
Инициализирует атрибуты name и subjects и вызывает метод load_subjects для загрузки предметов из файла.

__setattr__(self, name, value): Дескриптор, который проверяет установку атрибута name. Убеждается, что name начинается с
 заглавной буквы и состоит только из букв.

__getattr__(self, name): Позволяет получать значения атрибутов предметов (оценок и результатов тестов) по их именам.

__str__(self): Возвращает строковое представление студента, включая имя и список предметов.
Студент: Иван Иванов
Предметы: Математика, История

Методы класса:

load_subjects(self, subjects_file): Загружает предметы из файла CSV. Использует модуль csv для чтения данных из файла и
добавляет предметы в атрибут subjects.

add_grade(self, subject, grade): Добавляет оценку по заданному предмету. Убеждается, что оценка является целым числом
от 2 до 5.

add_test_score(self, subject, test_score): Добавляет результат теста по заданному предмету. Убеждается, что результат
теста является целым числом от 0 до 100.

get_average_test_score(self, subject): Возвращает средний балл по тестам для заданного предмета.

get_average_grade(self): Возвращает средний балл по всем предметам.

Пример

На входе:

student = Student("Иван Иванов", "subjects.csv")

student.add_grade("Математика", 4)
student.add_test_score("Математика", 85)

student.add_grade("История", 5)
student.add_test_score("История", 92)

average_grade = student.get_average_grade()
print(f"Средний балл: {average_grade}")

average_test_score = student.get_average_test_score("Математика")
print(f"Средний результат по тестам по математике: {average_test_score}")

print(student)

На выходе:

Средний балл: 4.5
Средний результат по тестам по математике: 85.0
Студент: Иван Иванов
Предметы: Математика, История

'''

import csv


class Student:
    """
    Класс, представляющий студента.

    Атрибуты:
    - name (str): ФИО студента
    - subjects (dict): словарь, содержащий предметы и их оценки и результаты тестов

    Методы:
    - __init__(self, name, subjects_file): конструктор класса
    - __setattr__(self, name, value): дескриптор, проверяющий ФИО на первую заглавную букву и наличие только букв
    - __getattr__(self, name): получение значения атрибута
    - __str__(self): возвращает строковое представление студента
    - load_subjects(self, subjects_file): загрузка предметов из файла CSV
    - get_average_test_score(self, subject): возвращает средний балл по тестам для заданного предмета
    - get_average_grade(self): возвращает средний балл по всем предметам
    - add_grade(self, subject, grade): добавление оценки по предмету
    - add_test_score(self, subject, test_score): добавление результата теста по предмету
    """

    def __init__(self, name, subjects_file):
        self.name = name
        self.subjects = {}
        self.load_subjects(subjects_file)

    def __setattr__(self, name, value):
        if name == 'name':
            if not value.replace(' ', '').isalpha() or not value.istitle():
                raise ValueError("ФИО должно состоять только из букв и начинаться с заглавной буквы")
        super().__setattr__(name, value)

    def __getattr__(self, name):
        if name in self.subjects:
            return self.subjects[name]
        else:
            raise AttributeError(f"Предмет {name} не найден")

    def __str__(self):
        return f"Студент: {self.name}\nПредметы: {', '.join(self.subjects.keys())}"

    def load_subjects(self, subjects_file):
        with open(subjects_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                subject = row[0]
                if subject not in self.subjects:
                    self.subjects[subject] = {'grades': [], 'test_scores': []}

    def add_grade(self, subject, grade):
        if subject not in self.subjects:
            self.subjects[subject] = {'grades': [], 'test_scores': []}
        if not isinstance(grade, int) or grade < 2 or grade > 5:
            raise ValueError("Оценка должна быть целым числом от 2 до 5")
        self.subjects[subject]['grades'].append(grade)

    def add_test_score(self, subject, test_score):
        if subject not in self.subjects:
            self.subjects[subject] = {'grades': [], 'test_scores': []}
        if not isinstance(test_score, int) or test_score < 0 or test_score > 100:
            raise ValueError("Результат теста должен быть целым числом от 0 до 100")
        self.subjects[subject]['test_scores'].append(test_score)

    def get_average_test_score(self, subject):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден")
        test_scores = self.subjects[subject]['test_scores']
        if len(test_scores) == 0:
            return 0
        return sum(test_scores) / len(test_scores)

    def get_average_grade(self):
        total_grades = []
        for subject in self.subjects:
            grades = self.subjects[subject]['grades']
            if len(grades) > 0:
                total_grades.extend(grades)
        if len(total_grades) == 0:
            return 0
        return sum(total_grades) / len(total_grades)


# ТЕСТ_1
student = Student("Иван Иванов", "subjects.csv")
student.add_grade("Математика", 4)
student.add_test_score("Математика", 85)
student.add_grade("История", 5)
student.add_test_score("История", 92)
average_grade = student.get_average_grade()
print(f"Средний балл: {average_grade}")
average_test_score = student.get_average_test_score("Математика")
print(f"Средний результат по тестам по математике: {average_test_score}")
print(student)
# Ожидаемый ответ:
# Средний балл: 4.5
# Средний результат по тестам по математике: 85.0
# Студент: Иван Иванов
# Предметы: Математика, История


# ТЕСТ_2
# student = Student("123 Иван", "subjects.csv")


# ТЕСТ_3
# student = Student("Петров Петр", "subjects.csv")
# student.add_grade("Физика", 6)


# ТЕСТ_4
# student = Student("Сидоров Сидор", "subjects.csv")
# average_history_score = student.get_average_test_score("Биология")
# Ожидаемый ответ:
# ValueError: Предмет Биология не найден
# Ваш ответ:
# KeyError: 'Биология'


'''


Правильное решение от ГБ

import csv

class Student:
    """
    Класс, представляющий студента.

    Атрибуты:
    - name (str): ФИО студента
    - subjects (dict): словарь, содержащий предметы и их оценки и результаты тестов

    Методы:
    - __init__(self, name, subjects_file): конструктор класса
    - __setattr__(self, name, value): дескриптор, проверяющий ФИО на первую заглавную букву и наличие только букв
    - __getattr__(self, name): получение значения атрибута
    - __str__(self): возвращает строковое представление студента
    - load_subjects(self, subjects_file): загрузка предметов из файла CSV
    - get_average_test_score(self, subject): возвращает средний балл по тестам для заданного предмета
    - get_average_grade(self): возвращает средний балл по всем предметам
    - add_grade(self, subject, grade): добавление оценки по предмету
    - add_test_score(self, subject, test_score): добавление результата теста по предмету
    """

    def __init__(self, name, subjects_file):
        self.name = name
        self.subjects = {}
        self.load_subjects(subjects_file)
    def __setattr__(self, name, value):
        if name == 'name':
            if not value.replace(' ', '').isalpha() or not value.istitle():
                raise ValueError("ФИО должно состоять только из букв и начинаться с заглавной буквы")
        super().__setattr__(name, value)


    def __getattr__(self, name):
        if name in self.subjects:
            return self.subjects[name]
        else:
            raise AttributeError(f"Предмет {name} не найден")

    def __str__(self):
        return f"Студент: {self.name}\nПредметы: {', '.join(self.subjects.keys())}"

    def load_subjects(self, subjects_file):
        with open(subjects_file, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                subject = row[0]
                if subject not in self.subjects:
                    self.subjects[subject] = {'grades': [], 'test_scores': []}
    def add_grade(self, subject, grade):
        if subject not in self.subjects:
            self.subjects[subject] = {'grades': [], 'test_scores': []}
        if not isinstance(grade, int) or grade < 2 or grade > 5:
            raise ValueError("Оценка должна быть целым числом от 2 до 5")
        self.subjects[subject]['grades'].append(grade)

    def add_test_score(self, subject, test_score):
        if subject not in self.subjects:
            self.subjects[subject] = {'grades': [], 'test_scores': []}
        if not isinstance(test_score, int) or test_score < 0 or test_score > 100:
            raise ValueError("Результат теста должен быть целым числом от 0 до 100")
        self.subjects[subject]['test_scores'].append(test_score)

    def get_average_test_score(self, subject):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден")
        test_scores = self.subjects[subject]['test_scores']
        if len(test_scores) == 0:
            return 0
        return sum(test_scores) / len(test_scores)

    def get_average_grade(self):
        total_grades = []
        for subject in self.subjects:
            grades = self.subjects[subject]['grades']
            if len(grades) > 0:
                total_grades.extend(grades)
        if len(total_grades) == 0:
            return 0
        return sum(total_grades) / len(total_grades)

'''