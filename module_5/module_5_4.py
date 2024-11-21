
#В классе House создайте атрибут houses_history = []
class House:
    houses_history = []
    # Дополните метод __new_
    def __new__(cls, *args, **kwargs):
#Название объекта добавлялось в список cls.houses_history
        isinstance = super().__new__(cls)
        cls.houses_history.append(args[0])
        return isinstance

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f'House {self.name} снесён, но он останется в истории')





h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3