# Решение RomanKostikov с перемешиванием(ожидает ответ пустоту, получает отлично!)
import random
import itertools


def queens():
    for p in itertools.permutations(range(8)):
        yield [x for x in enumerate(p)]


def generate_boards():
    board_list = []
    count = 0

    for q in queens():
        err = False
        for a, b in ((a, b) for a in q for b in q if a[0] < b[0]):
            if abs(a[0] - b[0]) == abs(a[1] - b[1]):
                err = True
                break
        if not err:
            board_list.append(q)
            count += 1
            if count == 4:
                break

    return board_list


print(generate_boards())

board_list = generate_boards()
if len(board_list) != 4:
    print("Вы собрали не то количество комбинаций")
else:
    print("Отлично!")