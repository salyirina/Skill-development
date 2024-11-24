class WordsFinder:
    def __init__(self, *file_names):
        # Сохраняем названия файлов как кортеж
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        punctuations = {',', '.', '=', '!', '?', ';', ':', ' - '}

        # Перебираем файлы
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    # Считываем содержимое файла
                    content = file.read().lower()
                    # Удаляем пунктуацию
                    for punc in punctuations:
                        content = content.replace(punc, ' ')
                    # Разделяем строки на слова
                    words = content.split()
                    # Добавляем данные в словарь
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f'Файл {file_name} не найден.')

                all_words[file_name] = []  # Если файла нет, записываем пустой список

        return all_words

    def find(self, word):
        #  Подготовка данных из файла
        all_words = self.get_all_words()
        word = word.lower()
        positions = {}

        for name, words in all_words.items():
            # Находим индекс первого вхождения
            if word in words:
                positions[name] = words.index(word) + 1  # Индексация начинается с 1
            else:
                positions[name] = None  # Если слово не найдено

        return positions

    def count(self, word):
        # Метод для подсчета количества слова в файлах
        all_words = self.get_all_words()
        word = word.lower()
        counts = {}

        for name, words in all_words.items():
            # Считаем количество вхождений слова
            counts[name] = words.count(word)

        return counts


# Можно использовать класс WordsFinder в других проектах, импортируя его,
# а тестовый код из блока if __name__ == "__main__": не будет мешать работе.
if __name__ == "__main__":

    finder2 = WordsFinder(
        'test_file.txt',
        'Mother Goose - Monday’s Child.txt',
        'Walt Whitman - O Captain! My Captain!.txt'
    )

    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
