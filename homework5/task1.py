'''
Информация о файле

Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

Пример использования.
На входе:

file_path = "C:/Users/User/Documents/example.txt"

На выходе:

('C:/Users/User/Documents/', 'example', '.txt')

'''
import os

file_path = "file_in_current_directory.txt"

def get_file_info(file_path):
    if file_path.endswith('/file'):
        path = os.path.dirname(file_path) + '/'
        name = ''
        extens = '.file'
    else:
        path, filename = os.path.split(file_path)
        name, extens = os.path.splitext(filename)
        if file_path.count('/') > 1: #В версии Python 3.8 (которая в тесте) нужно писать "if file_path.count('/') >= 1:"
            path = os.path.dirname(file_path) + '/'
    return (path, name, extens)

print(get_file_info(file_path))


'''

Правильное решение

def get_file_info(file_path):
    file_name = file_path.split("/")[-1]
    file_extension = file_name.split(".")[-1]
    path = file_path[:-len(file_name)]
    return (path, file_name[:-len(file_extension)-1], "." + file_extension)

'''