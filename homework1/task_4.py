"""
Пользователь задумывает число
Программа пытается угадать число за 10 попыток
компьтер выводит свое предположение и запрашивает у пользователя информацию:

Если компьтер угадал число введите =
Если Ваше число больше, введите >
Если Ваше число меньше, введите <
"""

from random import randint
print()
print("Задумайте число от 0 до 1000, компьютер попытается угадать число с 10-ти попыток")

left = 0
right = 1000
current = (left + right) // 2
answer = None
counter = 0
while answer != '=' and counter < 10:
    if right < left:
        print("Похоже Вы забыли, какое число загадали.")
        counter = 0
        break
    print(f"Попытка №{counter + 1}: Вы загадали {current}?")
    answer = input("Если компьтер угадал число введите = \nЕсли Ваше число больше, введите >\nЕсли Ваше "
                   "число меньше, введите <\n  ")
    if answer == '=':
        print(f"Я угадал c {counter + 1}-й попытки!")
        counter = 0
        break
    elif answer == '>':
        left = current + 1
        counter += 1
    elif answer == '<':
        right = current - 1
        counter += 1
    else:
        print('Повторите ввод (>, <, =)!')
    current = (left + right) // 2

if counter:
    print("Жаль, но я не угадал число за 10 попыток.")