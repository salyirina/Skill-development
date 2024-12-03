def add_everything_up(a: str | float | int, b: str | float | int) -> str | float:
    try:
        # Попытка сложить два значения
        return a + b
    except TypeError:
        # Если возникает TypeError, возвращаем строковое представление двух данных
        return f"{a}{b}"


# Тестирование
print(add_everything_up(123.456, 'строка'))  # 123.456строка
print(add_everything_up('яблоко', 4215))     # яблоко4215
print(add_everything_up(123.456, 7))         # 130.456
