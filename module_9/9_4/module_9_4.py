from random import choice


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')

print(first_ball())
print(first_ball())
print(first_ball())


"""Здесь lambda x, y: x == y проверяет, равны ли символы в соответствующих позициях строк."""

first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: x == y, first, second))
print(result)


# Функция get_advanced_writer возвращает функцию write_everything.
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for item in data_set:
                if isinstance(item, list):  # Обрабатываем списки, записывая каждый элемент
                    file.write(' '.join(map(str, item)) + '\n')
                else:
                    file.write(str(item) + '\n')
    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# ' '.join(...) объединяет элементы последовательности (в данном случае, список строк)
# в одну строку, вставляя между ними пробелы.