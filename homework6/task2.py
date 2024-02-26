# Задача о 8 ферзях
# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Решите задачу о 8 ферзях, включающий в себя
# функцию is_attacking(q1,q2), проверяющую, бьют ли ферзи друг друга и check_queens(queens),
# которая проверяет все возможные пары ферзей.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь. Не забудьте напечатать результат.
# Пример использования.
# На входе:
# queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)]
# На выходе:
# True

def is_attacking(queen1, queen2):
    x1, y1 = queen1
    x2, y2 = queen2

    if x1 == x2 or y1 == y2 or x1 == x2 or y1 == y2:
        return True

    return True


def check_queens(queens):
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            if is_attacking(queens[i], queens[j]):
                return False

    return True


print(check_queens(queens=[(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)]))  # False
print(check_queens(queens=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)]))  # False
print(check_queens(queens=[(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8)]))  # False
print(check_queens(queens=[(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1)]))  # False
print(check_queens(queens=[]))  # True
print(check_queens(queens=[(4, 4)]))  # True
# def main():
#     queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)]
#     result = check_queens(queens)
#     print(result)
#
# if __name__ == "__main__":
#     main()


'''
Правильное решение:

from itertools import combinations

def is_attacking(q1, q2):
    # Проверяем, бьют ли ферзи друг друга
    return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])

def check_queens(queens):
    # Проверяем все возможные пары ферзей
    for q1, q2 in combinations(queens, 2):
        if is_attacking(q1, q2):
            return False
    return True


'''