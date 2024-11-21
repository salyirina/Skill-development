#Задача "Изменять нельзя получать":
# В этой задаче мы реализуем классы транспорта, в которых нельзя будет просто так поменять цвет,
# мощность двигателя и прочие свойства, т.к. в реальной жизни это чаще всего делается не владельцем,
# а в специальных сервисах. Да, узнать значения этих свойств мы сможем, но вот изменить - нет.
class Vehicle: #это любой транспорт
    # Атрибут класса __COLOR_VARIANTS, в который записан список допустимых цветов для окрашивания. (Цвета написать свои)
    __COLOR_VARIANTS = ['red', 'blue', 'green', 'yellow', 'black', 'white']

    def __init__(self, owner: str, model: str, engine_power: int, color: str):
        self.owner = owner #владелец транспорта. (владелец может меняться)
        self.__model = model  #модель (марка) транспорта. (мы не можем менять название модели)
        self.__engine_power = engine_power #мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)
        self.__color = color #название цвета. (мы не можем менять цвет автомобиля своими руками)

    def get_model(self):
        return f"Модель: {self.__model}" #возвращает строку: "Модель: <название модели транспорта>"

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}' #возвращает строку: "Мощность двигателя: <мощность>"

    def get_color(self):
        return f' Цвет: {self.__color}' # возвращает строку: "Цвет: <цвет транспорта>"

# Метод print_info - распечатывает результаты методов (в том же порядке): get_model, get_horsepower, get_color;
# а так же владельца в конце в формате "Владелец: <имя>"
    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

## Метод set_color - принимает аргумент new_color(str), меняет цвет __color на new_color,
# если он есть в списке __COLOR_VARIANTS, в противном случае выводит на экран надпись:
    # "Нельзя сменить цвет на <новый цвет>".
    def set_color(self, new_color: str):
        # Преобразуем все допустимые цвета в нижний регистр для сравнения
        color_variants_lower = [color.lower() for color in self.__COLOR_VARIANTS]

        # Проверяем, находится ли новый цвет в списке допустимых цветов
        if new_color.lower() in color_variants_lower:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")

#Sedan(седан) - наследник класса VehiVehicle
class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

# II. Класс Sedan наследуется от класса Vehicle, а так же содержит следующие атрибуты:
# Атрибут __PASSENGERS_LIMIT = 5 (в седан может поместиться только 5 пассажиров)

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()