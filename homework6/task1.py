# На вход будет подаваться дата в формате "день.месяц.год". Ваша задача - создать программу,
# которая проверяет, является ли введенная дата корректной или нет.
# Ваша программа должна предоставить ответ "True" (дата корректна) или "False" (дата некорректна) в
# зависимости от результата проверки.
# Пример использования На входе:
# date_to_prove = 15.4.2023
# На выходе:
# True
# На входе:
# date_to_prove = 31.6.2022
# На выходе:
# False
# На входе(на самом деле!!!:
# date_to_prove = '31.6.2022'
# На выходе:
# False
from datetime import datetime


def is_valid_date(date: str):
    try:
        datetime.strptime(date, '%d.%m.%Y')
        return True
    except ValueError:
        return False


# date_to_prove = '31.6.2022'
# date_to_prove = '0.5.2022'
# date_to_prove = '12.0.2022'
# date_to_prove = '12.5.-2022'
# date_to_prove = '29.2.2020'
# date_to_prove = '31.12.9999'
# date_to_prove = '32.5.2022'
# date_to_prove = '12.13.2022'
date_to_prove = "24.2.2024"

is_valid = is_valid_date(date_to_prove)
print(is_valid)

'''
Правильное решение:

from sys import argv

def is_leap(year: int) :
    return not (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0))

def valid(full_date: str) :
    date, month, year = (int(item) for item in full_date.split('.'))
    if year < 1 or year > 9999 or month < 1 or month > 12 or date < 1 or date > 31:
        return False
    if month in (4, 6, 9, 11) and date > 30:
        return False
    if month == 2 and is_leap(year) and date > 29:
        return False
    if month == 2 and not is_leap(year) and date > 28:
        return False
    return True

if len(argv) > 1:
    print(valid(argv[1]))
else:
    print(valid(date_to_prove ))

'''