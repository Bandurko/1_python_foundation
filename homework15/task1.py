'''
Возьмите любые 1-3 задания из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации. Также
реализуйте возможность запуска из командной строки с передачей параметров.


Возьмем первую задачу из ДЗ 5-го семинара

Информация о файле

Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

Пример использования.
На входе:

file_path = "C:/Users/User/Documents/example.txt"

На выходе:

('C:/Users/User/Documents/', 'example', '.txt')
'''


import logging
import argparse


def get_file_info(file_path):
    file_name = file_path.split("/")[-1]
    file_extension = file_name.split(".")[-1]
    path = file_path[:-len(file_name)]
    result = (path, file_name[:-len(file_extension)-1], "." + file_extension)
    logging.basicConfig(filename='path.log', filemode='a', encoding='utf-8', level=logging.DEBUG)
    logging.info(str(result))
    return (result)

file_path = r"C:/Users/User/Documents/example.txt"

print(get_file_info(file_path))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Парсер для определения пути к файлу, имени файла и его расширения')
    parser.add_argument('path', metavar='path for file', type=str, nargs='+', help='Enter path')
    args = parser.parse_args()
    print(get_file_info(*args.path))
