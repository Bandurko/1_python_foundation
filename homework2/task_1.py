'''
Напишите программу, которая получает целое число num и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.

Пример

На входе:

num = 255

На выходе:

Шестнадцатеричное представление числа: FF
Проверка результата: 0xff
'''

#Мое решение не правильное - МАГИЧЕСКОЕ ЧИСЛО
num = 255

#num = int(input('Введите целое число: '))

#Возвращаем num в шестнадцатеричное строковое представление.

hex_digits = "0123456789ABCDEF"
hex_str = ""
num_count = num
while num_count > 0:
    hex_str = hex_digits[num_count % 16] + hex_str
    num_count //= 16

print(f'Шестнадцатеричное представление числа: {hex_str}')

#Проверяем, используя hex
print(f'Проверка результата: {hex(num)}')

'''
Правильное решение

HEX = 16
hex_digits = "0123456789ABCDEF"

hex_num = ""
test_hex_num = hex(num)

while num > 0:
    remainder = num % HEX
    hex_num = hex_digits[remainder] + hex_num
    num //= HEX

print("Шестнадцатеричное представление числа:", hex_num)
print("Проверка результата:", test_hex_num)

'''