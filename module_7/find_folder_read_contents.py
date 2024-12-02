import os


def file_traversal(directory, filename, level=1):
    for item in os.listdir(directory):
        full_path = os.path.join(directory, item)
        if os.path.isdir(full_path):  # Если это папка
            print('Спускаемся в', full_path)
            file_traversal(full_path, filename, level + 1)  # Рекурсивно проходим папку
            print('Возвращаемся в', directory)
        elif os.path.isfile(full_path) and item == filename:  # Если это файл и имя совпадает
            print('Файл найден:', full_path)
            # Читаем содержимое файла
            with open(full_path, 'r', encoding='utf-8') as file:
                content = file.read()
                print('Содержимое файла:')
                print(content)
            return  # Прекращаем поиск, если нашли файл


# Запускаем поиск файла
base_path = os.getcwd()
file_traversal(base_path, '7_5.py')
