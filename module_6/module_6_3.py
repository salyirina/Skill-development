import random


class Animal:
    live = True
    sound = None  # звук (изначально отсутствует)
    _DEGREE_OF_DANGER = 0  # степень опасности существа

    def __init__(self, speed):
        """Инициализация животного с его скоростью и начальными координатами."""
        self.speed = speed
        self._cords = [0, 0, 0]

    def move(self, dx, dy, dz):
        """Перемещает животное в зависимости от его скорости и направления (dx, dy, dz)."""
        new_z = self._cords[2] + dz * self.speed
        if new_z < 0:
            print("It's too deep, I can't dive :(")
        else:
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] = new_z

    def get_cords(self):
        """Выводит текущие координаты животного."""
        print(f"X: {self._cords[0]} Y: {self._cords[1]} Z: {self._cords[2]}")

    def attack(self):
        """Определяет, будет ли животное атаковать в зависимости от степени опасности."""
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        """Заставляет животное издать звук."""
        print(self.sound)


class Bird(Animal):
    beak = True

    @staticmethod
    def lay_eggs():
        """Имитирует откладку случайного количества яиц."""
        eggs = random.randint(1, 4)
        print(f"Here are(is) {eggs} eggs for you")


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        """Ныряет в воду в зависимости от скорости и глубины."""
        dz = abs(dz)
        new_z = self._cords[2] + dz * self.speed / 2
        if new_z < 0:
            print("It's too deep, I can't dive :(")
        else:
            self._cords[2] = new_z


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8.


class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    sound = "Click-click-click"
    _DEGREE_OF_DANGER = 8  # Устанавливаем значение степени опасности для Duckbill

    def __init__(self, speed):
        """Инициализация утконоса с его скоростью."""
        super().__init__(speed)



# Пример работы программы
db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()
