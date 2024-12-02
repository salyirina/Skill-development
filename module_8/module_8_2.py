def personal_sum(numbers):

    result = 0
    incorrect_data = 0

    for num in numbers:
        try:
            # Проверка, можно ли преобразовать элемент в число (int или float)
            result += float(num)
        except (ValueError, TypeError):  # Перехватываем ошибки при преобразовании
            incorrect_data += 1  # Увеличиваем счётчик некорректных данных
            print(f"Некорректный тип данных для подсчёта суммы - {num}")  # Печатаем, что не удалось обработать

    return result, incorrect_data


def calculate_average(numbers):

    try:
        # Если передано одно число (int или float), преобразуем в список
        if isinstance(numbers, (int, float)):
            numbers = [numbers]

        if not isinstance(numbers, (list, tuple)):  # Проверяем, что numbers является коллекцией
            raise TypeError("В numbers записан некорректный тип данных")

        if len(numbers) == 0:  # Проверяем, что коллекция не пуста
            return 0

        total_sum, incorrect_count = personal_sum(numbers)  # Получаем сумму и количество некорректных данных

        correct_count = len(numbers) - incorrect_count  # Количество корректных данных
        if correct_count == 0:  # Если нет корректных данных, возвращаем 0
            return 0

        return total_sum / correct_count  # Возвращаем среднее арифметическое по корректным данным

    except ZeroDivisionError:  # Если произошло деление на 0, возвращаем 0
        return 0
    except TypeError:
        print("В numbers записан некорректный тип данных")  # Просто выводим сообщение
        return None  # Возвращаем None в случае некорректного типа данных


# Тесты
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Передана строка, её элементы - некорректные типы
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только числа 1 и 3
print(f'Результат 3: {calculate_average([567])}')  # Должно вернуть None
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Передана корректная коллекция чисел
