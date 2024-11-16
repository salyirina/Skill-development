import math


class Figure:
    sides_count = 0  # Число сторон, зависит от конкретной фигуры

    def __init__(self, color=(0, 0, 0), *sides):
        # Установка цвета с проверкой
        if self.__is_valid_color(*color):
            self.__color = color
        else:
            self.__color = (0, 0, 0)  # Цвет по умолчанию

        # Проверка сторон
        if len(sides) == self.sides_count and self.__is_valid_sides(*sides):
            self.__sides = list(sides)
        else:
            self.__sides = [1] * self.sides_count  # Стороны по умолчанию

        # Публичный атрибут
        self.filled = False

    @staticmethod
    def __is_valid_color(r, g, b):
        # Проверка каждого компонента цвета по отдельности
        if not isinstance(r, int) or not (0 <= r <= 255):
            return False
        if not isinstance(g, int) or not (0 <= g <= 255):
            return False
        if not isinstance(b, int) or not (0 <= b <= 255):
            return False
        return True

    @staticmethod
    def __is_valid_sides(*sides):
        # Проверка каждого элемента в списке сторон
        for side in sides:
            if not isinstance(side, int):  # Проверка, что это целое число
                return False
            if side <= 0:  # Проверка, что сторона положительная
                return False
        return True

        # получение значения для цвета
    def get_color(self):
        return self.__color

        # изменение значения для цвета
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

        # получение значения для сторон
    def get_sides(self):
        return self.__sides

    # получение значения для новых сторон
    def set_sides(self, *new_sides):
        # Проверяем, что количество новых сторон соответствует
        if len(new_sides) != self.sides_count:
            return  # Если количество сторон не совпадает, ничего не меняем

        # Проверка на валидность всех сторон
        for side in new_sides:
            if not isinstance(side, int) or side <= 0:
                return  # Если хотя бы одна сторона невалидна, ничего не меняем

        # Если проверка прошла, обновляем список сторон
        self.__sides = list(new_sides)

    # Метод для получения периметра фигуры
    def __len__(self):
        return sum(self.__sides)


# Класс Circle (наследник Figure)
class Circle(Figure):
    sides_count = 1

    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color, *sides)
        self.__radius = self.__calculate_radius()

    def __calculate_radius(self):
        circumference = self.get_sides()[0]
        return circumference / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.__radius ** 2)


# Класс Triangle (наследник Figure)
class Triangle(Figure):
    sides_count = 3

    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color, *sides)

    # Метод для получения площади треугольника
    def get_square(self):
        a, b, c = self.get_sides()
        s = sum(self.get_sides()) / 2  # Полупериметр
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


# Класс Cube (наследник Figure)
class Cube(Figure):
    sides_count = 12

    def __init__(self, color=(0, 0, 0), side_length=1):
        sides = [side_length] * self.sides_count  # Заполняем стороны куба
        super().__init__(color, *sides)

    def get_volume(self):
        side = self.get_sides()[0]  # Стороны должны быть равны
        return side ** 3



# Проверочный код:
circle1 = Circle((200, 200, 100), 10)  # Цвет, стороны
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
