import os

path = os.getcwd()

def file_traversal(path, name, level=1):
    # Проходимся по содержимому директории
    for i in os.listdir(path):
        full_path = os.path.join(path, i)
        if os.path.isdir(full_path):  # Если это папка
            print('Спускаемся в', full_path)
            file_traversal(full_path, name, level + 1)  # Рекурсивно проходим папку
            print('Возвращаемся в', path)
        elif os.path.isfile(full_path) and i == name:  # Если это файл и имя совпадает
            print('Файл найден:', full_path)
            return  # Прекращаем поиск, если нашли файл

file_traversal(path, '1.py')
