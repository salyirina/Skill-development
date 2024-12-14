def all_variants(text):
    """
    Генератор возвращает все подпоследовательности строки text.
    Подпоследовательности включают строки любой длины (от 1 до len(text)).
    """
    for start in range(len(text)):
        for end in range(start + 1, len(text) + 1):
            # Возвращаем срез строки от start до end
            yield text[start:end]


# Пример работы функции:

a = all_variants("abc")
for i in a:
    print(i)
