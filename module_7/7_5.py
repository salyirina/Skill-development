import os
import time

directory = os.getcwd()  # Получаем текущую рабочую директорию

# Проверим, существует ли директория
if not os.path.exists(directory):
    print(f"Ошибка: Директория {directory} не существует.")
else:
    print(f"Начинаем обход директории: {directory}")

    # os.walk рекурсивно обходит все директории и файлы в указанной папке
    for root, dirs, files in os.walk(directory):
        if files:  # Проверим, есть ли файлы в текущей директории
            for file in files:
                # Полный путь к файлу
                filepath = os.path.join(root, file)

                # Время последнего изменения файла
                filetime = os.path.getmtime(filepath)

                # Преобразование времени в читаемый формат
                formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

                # Размер файла
                filesize = os.path.getsize(filepath)

                # Родительская директория
                parent_dir = os.path.dirname(filepath)

                # Выводим информацию о файле
                print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
        else:
            print(f"В директории {root} нет файлов.")
