import time

start_time = time.time()

# Классы исключений
class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):

    def __init__(self, message):
        self.message = message


class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        # Проверяем vin номер

        # Проверяем vin и устанавливаем только при успешной валидации
        if self.__is_valid_vin(vin):
            self.__vin = vin

        # Проверяем numbers и устанавливаем только при успешной валидации
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers

    # Приватный метод для проверки vin номера

    def __is_valid_vin(self, vin_number):
        # Проверяем, что vin_number - целое число
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber("Некорректный тип vin номер")

        # Проверяем, что vin_number находится в допустимом диапазоне
        if not (1000000 <= vin_number <= 9999999):
            raise IncorrectVinNumber("Неверный диапазон для vin номера")
        # Если исключений не было, возвращаем True
        return True

    # Приватный метод для проверки номера
    def __is_valid_numbers(self, numbers):
        # Проверяем, что numbers - строка
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers("Некорректный тип данных для номеров")

        # Проверяем длину строки numbers
        if len(numbers) != 6:
            raise IncorrectCarNumbers("Неверная длина номера")
        # Если исключений не было, возвращаем True
        return True


# Пример работы с классом и исключениями
try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')

finish_time = time.time()
print(f'Время в милисекундах: {(finish_time-start_time) * 1000}')
