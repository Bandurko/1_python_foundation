'''
Обработка исключений в Archive

Допишите в вашу задачу Archive обработку исключений.

Добавьте исключение в ваш код InvalidTextError, которые будет вызываться, когда текст не является строкой или является
пустой строкой.

Текст ошибки: Invalid text: {введенный текст}. Text should be a non-empty string.'

И InvalidNumberError, которое будет вызываться, если число не является положительным целым числом или числом с
плавающей запятой.

Текст ошибки: 'Invalid number: {введенное число}. Number should be a positive integer or float.'

----------------------------

from typing import Union
class Archive:
    """
    Класс, представляющий архив текстовых и числовых записей.

    Атрибуты:
    - archive_text (list): список архивированных текстовых записей.
    - archive_number (list): список архивированных числовых записей.
    - text (str): текущая текстовая запись для добавления в архив.
    - number (int или float): текущая числовая запись для добавления в архив.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        else:
            cls._instance.archive_text.append(cls._instance.text)
            cls._instance.archive_number.append(cls._instance.number)
        return cls._instance

    def __init__(self, text: str, number: Union[int, float]):
        self.text = text
        self.number = number

    def __str__(self):
        return f'Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}'

    def __repr__(self):
        return f'Archive("{self.text}", {self.number})'
'''

from typing import Union


class Archive:
    """
    Класс, представляющий архив текстовых и числовых записей.

    Атрибуты:
    - archive_text (list): список архивированных текстовых записей.
    - archive_number (list): список архивированных числовых записей.
    - text (str): текущая текстовая запись для добавления в архив.
    - number (int или float): текущая числовая запись для добавления в архив.
    """

'''
НЕ ПРАВИЛЬНОЕ!!!


    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        else:
            cls._instance.archive_text.append(cls._instance.text)
            cls._instance.archive_number.append(cls._instance.number)
        return cls._instance

    def __init__(self, text: str, number: Union[int, float]):
        self.text = text
        self.number = number

    def __str__(self):
        return f'Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}'

    def __repr__(self):
        return f'Archive("{self.text}", {self.number})'

    def __init__(self, text: str, number: Union[int, float]):
        if not isinstance(text, str) or text == "":
            raise InvalidTextError(f"Invalid text: {text}. Text should be a non-empty string.")
        if not isinstance(number, (int, float)) or number <= 0:
            raise InvalidNumberError(f"Invalid number: {number}. Number should be a positive integer or float.")

        self.text = text
        self.number = number


class InvalidTextError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class InvalidNumberError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


try:
    # Valid input
    archive1 = Archive("Sample text", 10)
    print(archive1)
except (InvalidTextError, InvalidNumberError) as e:
    print(f"Error: {str(e)}")

try:
    # Invalid text
    archive2 = Archive("", 10)
    print(archive2)
except (InvalidTextError, InvalidNumberError) as e:
    print(f"Error: {str(e)}")

try:
    # Invalid number
    archive3 = Archive("Sample text", -5)
    print(archive3)
except (InvalidTextError, InvalidNumberError) as e:
    print(f"Error: {str(e)}")

'''



''' Правильное от ГБ '''

class InvalidTextError(ValueError):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return f'Invalid text: {self.text}. Text should be a non-empty string.'


class InvalidNumberError(ValueError):
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f'Invalid number: {self.number}. Number should be a positive integer or float.'


class Archive:
    """Документация для класса Архив"""

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        else:
            cls._instance.archive_text.append(cls._instance.text)
            cls._instance.archive_number.append(cls._instance.number)
        return cls._instance

    def __init__(self, text, number):
        if not isinstance(text, str) or len(text.strip()) == 0:
            raise InvalidTextError(text)
        if not (isinstance(number, int) or isinstance(number, float)) or number <= 0:
            raise InvalidNumberError(number)
        self.text = text
        self.number = number

    def __str__(self):
        return f'Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}'

    def __repr__(self):
        return f'Archive("{self.text}", {self.number})'


# ТЕСТ 1
# archive_instance = Archive("Sample text", 42.5)
# print(archive_instance)

# ТЕСТ 2
# invalid_archive_instance = Archive("", -5)
# print(invalid_archive_instance)

# ТЕСТ 3
# invalid_archive_instance = Archive("Sample text", -5)
# print(invalid_archive_instance)