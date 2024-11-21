# Создайте:
# 2 класса родителя: Animal, Plant
# Для класса Animal(Животное) атрибуты alive = True(живой) и fed = False(накормленный),
# name - индивидуальное название каждого животного.
class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False

# Для класса Plant(Растение) атрибут edible = False(съедобность),
# name - индивидуальное название каждого растения
class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = False #(съедобность)
class Mammal(Animal): #(Млекопитающее)
    def __init__(self,name):
        super().__init__(name)
    def eat(self, food):  # Метод для поедания
        if food.edible:  # Проверка съедобности
            print(f'{self.name} съел {food.name}')
            self.fed = True  # Обновление статуса накормленности

# Если переданное растение (food) не съедобное - выводит на экран "<self.name> не стал есть <food.name>",
# меняется атрибут alive на False.
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False  # Обновление статуса жизни, если растение несъедобно

# Класс Predator (Хищник) наследуется от Animal
class Predator(Animal):
    def __init__(self,name):
        super().__init__(name)
    def eat(self, food):  # Метод для поедания
        if food.edible:  # Проверка съедобности
            print(f'{self.name} съел {food.name}')
            self.fed = True  # Обновление статуса накормленности
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False  # Обновление статуса жизни, если р

# Класс Flower (Цветок) наследуется от Plant
class Flower(Plant):
    def __init__(self,name):
        super().__init__(name)

# Класс Fruit (Фрукты) наследуется от Plant
class Fruit(Plant):
    def __init__(self,name):
        super().__init__(name)
# У каждого объекта Fruit должен быть атрибут edible(съедобный) = True (переопределить при наследовании)
        self.edible = True

# Выполняемый код(для проверки):
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(p1.name)  # Вывод имени цветка

print(a1.alive)  # Проверка живого состояния хищника
print(a2.fed)    # Проверка статуса накормленности млекопитающего

a1.eat(p1)       # Хищник пытается съесть цветок
a2.eat(p2)       # Млекопитающее съедает фрукт

print(a1.alive)  # Проверка живого состояния хищника после попытки поедания цветка
print(a2.fed)    # Проверка статуса накормленности млекопитающего после еды

