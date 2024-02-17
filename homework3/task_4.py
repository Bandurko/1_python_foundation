'''
Cписок повторяющихся элементов

Дан список повторяющихся элементов lst. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.

Пример

На входе:

lst = [1, 1, 2, 2, 3, 3]

На выходе:

[1, 2, 3]
'''

# Мое решение
def find_duplicates(lst):
    return list(set([x for x in lst if lst.count(x) > 1]))

lst = [1, 1, 2, 2, 3, 3]
print(find_duplicates(lst))

'''
Правильное решение

duplicates = set()

for item in lst:
    if lst.count(item) >= 2:
        duplicates.add(item)

result = list(duplicates)
print(result)
'''