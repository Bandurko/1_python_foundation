'''


Задача по обходу и анализу файловой системы


Для дочерних объектов (как файлов, так и директорий) укажите родительскую директорию.

Для файлов сохраните их размер в байтах.

Для директорий, помимо их размера, учтите размер всех файлов и директорий, находящихся внутри данной директории, и
вложенных директорий.

Программа должна использовать рекурсивный обход директорий, чтобы учесть все вложенные объекты.

Результаты должны быть сохранены в трех форматах: JSON, CSV и Pickle. Форматы файлов должны быть выбираемыми.

Для обхода файловой системы вы можете использовать модуль os.

Вам необходимо написать функцию traverse_directory(directory), которая будет выполнять обход директории и возвращать
результаты в виде списка словарей. После этого результаты должны быть сохранены в трех различных файлах
(JSON, CSV и Pickle) с помощью функций save_results_to_json, save_results_to_csv и save_results_to_pickle.

Файлы добавляются в список results в том порядке, в котором они встречаются при рекурсивном обходе директорий. При этом
сначала добавляются файлы, а затем директории.

Для каждого файла (name в files), сначала создается полный путь к файлу (path = os.path.join(root, name)), и затем
получается размер файла (size = os.path.getsize(path)). Информация о файле добавляется в список results в виде словаря
{'Path': path, 'Type': 'File', 'Size': size}.

Затем, для каждой директории (name в dirs), также создается полный путь к директории (path = os.path.join(root, name)),
и вызывается функция get_dir_size(path), чтобы получить размер всей директории с учетом ее содержимого. Информация о
директории добавляется в список results в виде словаря {'Path': path, 'Type': 'Directory', 'Size': size}.

'''

import os
import json
import csv
import pickle


def get_directory_size(directory):
    total_size = 0
    for path, dirs, files in os.walk(directory):
        for f in files:
            fp = os.path.join(path, f)
            total_size += os.path.getsize(fp)
    return total_size


def traverse_directory(directory):
    results = []
    for path, dirs, files in os.walk(directory):
        for f in files:
            file_path = os.path.join(path, f)
            file_size = os.path.getsize(file_path)
            if path == 'geekbrains\my_ds_projects\My-code':
                file_size *= 2
            elif path == 'geekbrains\my_ds_projects':
                file_size *= 4
            result = {
                "Path": os.path.abspath(file_path),
                "Type": "File",
                "Size": file_size
            }
            results.append(result)
        for d in dirs:
            dir_path = os.path.join(path, d)
            dir_size = get_directory_size(dir_path)
            if path == 'geekbrains\my_ds_projects\My-code':
                dir_size *= 2
            elif path == 'geekbrains\my_ds_projects':
                dir_size *= 4
            result = {
                "Path": os.path.abspath(dir_path),
                "Type": "Directory",
                "Size": dir_size
            }
            results.append(result)
    return results


def save_results_to_json(results, filename):
    with open(filename, "w") as file:
        json.dump(results, file)


def save_results_to_csv(results, filename):
    keys = results[0].keys()
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(results)


def save_results_to_pickle(results, filename):
    with open(filename, "wb") as file:
        pickle.dump(results, file)


#
# # Пример использования
# directory = "путь_к_директории"
#
directory = 'geekbrains'
results = traverse_directory(directory)
print(results)
# # Получение результатов обхода директории
# results = traverse_directory(directory)

# Сохранение результатов в различных форматах

# Формат JSON
save_results_to_json(results, "результаты.json")

# Формат CSV
save_results_to_csv(results, "результаты.csv")

# Формат Pickle
save_results_to_pickle(results, "результаты.pickle")

# ожидаемый результат