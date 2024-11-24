def custom_write(file_name, strings):
    strings_positions = {}

    # Открываем файл для записи
    file = open(file_name, 'w', encoding='utf-8')
    try:
        for line_number, string in enumerate(strings, start=1):
            # Получаем текущую позицию в байтах перед записью строки
            byte_position = file.tell()
            # Записываем строку в файл
            file.write(string + '\n')
            # Добавляем в словарь данные о строке
            strings_positions[(line_number, byte_position)] = string
    finally:
        file.close()
    return strings_positions



info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('text.txt', info)
for elem in result.items():
  print(elem)

# Создайте функцию custom_write(file_name, strings), которая принимает аргументы file_name -
# название файла для записи, strings - список строк для записи.
# Функция должна:
# Записывать в файл file_name все строки из списка strings, каждая на новой строке.
# Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>),
# а значением - записываемая строка. Для получения номера байта начала строки используйте метод tell() перед записью.
# Пример полученного словаря:
# {(1, 0): 'Text for tell.', (2, 16): 'Используйте кодировку utf-8.'}
# Где:
# 1, 2 - номера записанных строк.
# 0, 16 - номера байт, на которых началась запись строк.
# 'Text for tell.', 'Используйте кодировку utf-8.' - сами строки.



