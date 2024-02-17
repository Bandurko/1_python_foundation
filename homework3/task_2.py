'''
Часто встречающиеся слова

В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки
препинания и регистр символов.

Слова разделяются пробелами. Такие слова как don t, it s, didn t итд (после того, как убрали знак препинания апостроф)
считать двумя словами.
Цифры за слова не считаем.

Отсортируйте по убыванию значения количества повторяющихся слов. Слова выведите в обратном алфавитном порядке.

Пример

На входе:

text = 'Hello world. Hello Python. Hello again.'

На выходе:

[('hello', 3), ('world', 1), ('python', 1), ('again', 1)]
'''

import re
from collections import Counter

def top_10_words(text):
    new_text = re.sub(r'[^\w\s]', ' ', text)
    words1 = list(sorted((new_text.lower()).split()))

    words1.reverse()
    rev_text = " ".join([i for i in words1 if not i.isdigit()])

    res = re.sub(r"\d", '', rev_text)
    words = re.findall(r'\b\w+\b', res.lower())
    return Counter(words).most_common(10)

text = "Python is python, is, IS, and PYTHON."
print(top_10_words(text))

'''

Правильное решение

import re
from collections import Counter

# Удаляем знаки препинания и приводим текст к нижнему регистру
cleaned_text = ''.join(char.lower() if char.isalpha() or char.isspace() else ' ' for char in text)

# Разбиваем текст на слова и считаем их количество
words = cleaned_text.split()
word_counts = {}

for word in words:
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1

# Получаем 10 самых часто встречающихся слов
top_words = sorted(word_counts.items(), key=lambda x: (x[1], x[0]), reverse=True)[:10]

print(top_words)

'''