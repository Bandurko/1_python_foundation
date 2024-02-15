'''
На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.
Напишите программу, которая должна возвращать сумму и произведение дробей. Дроби упрощать не нужно.

Для проверки своего кода используйте модуль fractions.

Пример

На входе:

frac1 = "1/2"
frac2 = "1/3"

На выходе:

Сумма дробей: 5/6
Произведение дробей: 1/6
Сумма дробей: 5/6
Произведение дробей: 1/6
'''

#Мое решение не правильное - ПРЕОБРАЗОВАНИЕ дроби из строк в числа (напр 23/127 - преобразует не правильно)

import fractions

# Пример
frac1 = "1/2"
frac2 = "1/3"

# Преобразуем дроби из строк в числа
num_1 = int(frac1[0])
den_1 = int(frac1[2])
num_2 = int(frac2[0])
den_2 = int(frac2[2])

# Вычисляем сумму дробей
sum_frac_num = num_1 * den_2 + num_2 * den_1
sum_frac_den = den_1 * den_2

# Вычисляем произведение дробей
prod_frac_num = num_1 * num_2
prod_frac_den = den_1 * den_2

print(f'Сумма дробей: {sum_frac_num}/{sum_frac_den}')
print(f'Произведение дробей: {prod_frac_num}/{prod_frac_den}')

# Проверяем используя модуль fractions.
f1 = fractions.Fraction(num_1, den_1)
f2 = fractions.Fraction(num_2, den_2)

print(f'Сумма дробей: {f1 + f2}')
print(f'Произведение дробей: {f1 * f2}')


'''
Правильное решение

from fractions import Fraction
#frac1 = '2/5'
#frac2 = '3/5'

# Разбиваем строки на числитель и знаменатель без использования map
numerator1_str, denominator1_str = frac1.split('/')
numerator2_str, denominator2_str = frac2.split('/')

# Преобразуем строки в целые числа
numerator1 = int(numerator1_str)
denominator1 = int(denominator1_str)
numerator2 = int(numerator2_str)
denominator2 = int(denominator2_str)

common_denominator = denominator1 * denominator2

new_numerator1 = numerator1 * denominator2
new_numerator2 = numerator2 * denominator1

summation_numerator = new_numerator1 + new_numerator2
multiplication_numerator = numerator1 * numerator2

print(f"Сумма дробей: {summation_numerator}/{common_denominator}")
print(f"Произведение дробей: {multiplication_numerator}/{common_denominator}")

# Преобразуем введенные строки в объекты Fraction
fraction1 = Fraction(frac1)
fraction2 = Fraction(frac2)

# Вычисляем сумму и произведение дробей
summation = fraction1 + fraction2
multiplication = fraction1 * fraction2

print(f"Сумма дробей: {summation}")
print(f"Произведение дробей: {multiplication}")

'''