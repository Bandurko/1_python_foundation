'''

Пакет для работы с файлами 2


Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для работы с файлами.

Создайте файл __init__.py и запишите в него все функции:
get_dir_size,
save_results_to_json,
save_results_to_csv,
save_results_to_pickle,
traverse_directory.
'''
with open('__init__.py', "w") as init_file:
    init_file.write('''def get_dir_size\ndef save_results_to_json\ndef save_results_to_csv\ndef save_results_to_pickle\
    ndef traverse_directory''')


'''

Правильное решение от ГБ

code_to_write = '''
import os
import json
import csv
import pickle

def get_dir_size(start_path='.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
        for d in dirnames:
            dp = os.path.join(dirpath, d)
            total_size += get_dir_size(dp)
    return total_size

def save_results_to_json(results, file_name):
    with open(file_name, 'w') as f:
        json.dump(results, f)

def save_results_to_csv(results, file_name):
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Path', 'Type', 'Size'])
        for result in results:
            writer.writerow([result['Path'], result['Type'], result['Size']])

def save_results_to_pickle(results, file_name):
    with open(file_name, 'wb') as f:
        pickle.dump(results, f)

def traverse_directory(directory):
    results = []
    for root, dirs, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            size = os.path.getsize(path)
            results.append({'Path': path, 'Type': 'File', 'Size': size})
        for name in dirs:
            path = os.path.join(root, name)
            size = get_dir_size(path)
            results.append({'Path': path, 'Type': 'Directory', 'Size': size})
    return results
'''

with open("__init__.py", "w") as init_file:
    init_file.write(code_to_write)

'''