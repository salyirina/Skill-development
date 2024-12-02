# single_root_words - однокоренные слова
# root_word - корневое слово
# other_words -другие слова
# same_words - одинаковые слова

def single_root_words(root_word, *other_words):
    # При проверке наличия одного слова в составе другого стоит учесть,
    # что регистр символов не должен влиять ни на что.
    root_word_lower = root_word.lower()
    same_words = []

    for word in other_words:
        word_lower = word.lower()

        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_words.append(word)
    return same_words


# Пример вызова функции с нужным выводом
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'richies', 'poor', 'dog')
result2 = single_root_words('Able', 'Disable', 'Enable', 'Table', 'Dog')

print(result1)
print(result2)
