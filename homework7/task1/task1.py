'''
Напишите функцию группового переименования файлов в папке test_folder под названием rename_files. Она должна:
a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
b. принимать параметр количество цифр в порядковом номере.
c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
d. принимать параметр расширение конечного файла.
e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из
исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
f. Папка test_folder доступна из текущей директории
На входе:
rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")
На выходе:
(new_file_008.doc, test.doc, new_file_004.doc, new_file_005.doc, new_file_007.doc, new_file_001.doc, new_file_006.doc,
 new_file_003.doc, new_file_002.doc, new_file_009.doc, new_file_010.doc)
'''

import os
import shutil

# Создать тестовую папку
folder_name = "test_folder"
folder_path = os.path.join(os.getcwd(), folder_name)
if os.path.exists(folder_path):
    shutil.rmtree(folder_path)
os.makedirs(folder_path)

# Заполнить тестовую папку
for i in range(10):
    file_name = f"test{i}.txt"
    file_path = os.path.join(folder_path, file_name)

    with open(file_path, "w") as file:
        file.write("This is a test file.\n")
        file.close()

file_name = "test.doc"
file_path = os.path.join(folder_path, file_name)

with open(file_path, "w") as file:
    file.write("This is a test file.\n")
    file.close()

# ===================== Начало кода для теста ============================
def rename_files(desired_name, num_digits, source_ext, target_ext):
    # Get the list of files in the test_folder directory - Получить список файлов в каталоге test_folder
    files = os.listdir("test_folder")

    # Sort the files to ensure consistent order - Отсортировать файлы, чтобы обеспечить последовательный порядок
    files.sort()

    # Initialize a counter for the new file names - Инициализировать счетчик для новых имен файлов
    counter = 1

    # Iterate over each file in the directory - Выполнить итерацию по каждому файлу в каталоге
    for file in files:
        # Check if the file has the specified source extension - Проверить, имеет ли файл указанное расширение источника
        if file.endswith(source_ext):
            # Create the new file name with the desired name and the counter
            # Создать новое имя файла с желаемым именем и счетчиком
            new_file_name = f"{desired_name}{str(counter).zfill(num_digits)}.{target_ext}"

            # Rename the file - Переименовать файл
            os.rename(os.path.join("test_folder", file), os.path.join("test_folder", new_file_name))

            # Increment the counter - Увеличить значение счетчика
            counter += 1

# ===================== Конец кода для теста ============================

rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")

folder_content = ""
files = os.listdir(folder_path)
separator = ", "
files_as_string = separator.join(files)
print(files_as_string)

shutil.rmtree(folder_path)

# Ожидаемый ответ:
# new_file_008.doc, test.doc, new_file_004.doc, new_file_005.doc, new_file_007.doc, new_file_001.doc, new_file_006.doc,
# new_file_003.doc, new_file_002.doc, new_file_009.doc, new_file_010.doc
# Ваш ответ:
# new_file_008.doc, test.doc, new_file_011.doc, new_file_005.doc, new_file_007.doc, new_file_001.doc, new_file_006.doc,
# new_file_003.doc, new_file_002.doc, new_file_009.doc, new_file_010.doc


'''
Правильное решение:

import os

def rename_files(desired_name, num_digits, source_ext, target_ext, name_range=None):
    new_names = []

    # Получаем список файлов в текущей директории
    files = os.listdir('test_folder')

    # Фильтруем только нужные файлы с указанным расширением
    filtered_files = [file for file in files if file.endswith(source_ext)]

    # Сортируем файлы по имени
    filtered_files.sort()

    # Задаем начальный номер для порядкового номера
    num = 1

    # Переименовываем файлы
    for file in filtered_files:
        # Получаем имя файла без расширения
        name = os.path.splitext(file)[0]

        # Если задан диапазон, обрезаем имя файла
        if name_range:
            name = name[name_range[0]-1:name_range[1]]

        # Создаем новое имя с желаемым именем, порядковым номером и новым расширением
        new_name = desired_name + str(num).zfill(num_digits) + '.' + target_ext

        # Переименовываем файл
        path_old = os.path.join(os.getcwd(), folder_name, file)
        path_new = os.path.join(os.getcwd(), folder_name, new_name)
        os.rename(path_old, path_new)

        # Увеличиваем порядковый номер
        num += 1

'''

