import time

start_time = time.time()
# Список созданный при помощи сборки состоящий из длин строк списка
# при условии, что длина строк не менее 5 символов.
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
first_result = [len(f_s) for f_s in first_strings if len(f_s) > 5]

# Список созданный при помощи сборки состоящий из пар слов(кортежей) одинаковой длины.
# Каждое слово из списка first_strings должно сравниваться с каждым из second_strings.

second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
second_result = [(f_s, s_s) for f_s in first_strings for s_s in second_strings if len(f_s) == len(s_s)]
# Словарь созданный при помощи сборки, где парой ключ-значение будет строка-длина строки.
# Значения строк будут перебираться из объединённых вместе списков first_strings и second_strings.
# Условие записи пары в словарь - чётная длина строки.
third_result = {strings: len(strings) for strings in first_strings + second_strings if len(strings) % 2 == 0}


print(first_result)
print(second_result)
print(third_result)




finish_time = time.time()
print(f'Время в милисекундах: {(finish_time-start_time) * 1000}')