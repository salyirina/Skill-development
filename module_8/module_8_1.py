def add_everything_up(a, b):
    try:
        # Проверяем, является ли объект, а экземпляром того же типа, что и объект b
        # isinstance поддерживает вложенные проверки. Например, isinstance(a, (int, float))
        if not isinstance(a, type(b)):
            raise TypeError("a и b должны быть одного типа")

        # Если a и b числа, возвращаем сумму
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a + b

        # Если a и b строки, возвращаем конкатенацию
        if isinstance(a, str) and isinstance(b, str):
            return a + b

        # Для других типов данных
        raise TypeError("Недопустимые типы данных")

    except TypeError:
        # Возвращаем строковое представление, если типы разные
        return f"{a}{b}"


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
