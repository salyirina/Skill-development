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
        if not self.__is_valid_vin(vin):
            raise IncorrectVinNumber(f'Некорректный vin номер')
        self.__vin = vin
        # Проверяем номера автомобиля
        if not self.__is_valid_numbers(numbers):
            raise IncorrectCarNumbers("Некорректные номера автомобиля")
        self.__numbers = numbers


    # Приватный метод для проверки vin номера
    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber("Некорректный тип vin номер")
        if vin_number < 1000000 or vin_number > 9999999:
            raise IncorrectVinNumber("Неверный диапазон для vin номера")
        return True

    # Приватный метод для проверки номеров автомобиля
    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers(f'Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumbers(f'Неверная длина номера')
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
