# Задача "Range - это просто":

class StepValueError(ValueError):
    """
    Исключение, которое вызывается, если шаг для итератора равен нулю.
    """
    pass


class Iterator:
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError("Шаг итерации не может быть равен нулю.")

        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start  # метод, сбрасывающий значение pointer на start и возвращающий сам объект итератора

    def __iter__(self):
        """
        Метод возвращает сам итератор.
        """
        self.pointer = self.start  # Сбрасываем pointer при начале итерации
        return self


    # __next__ - метод, увеличивающий атрибут pointer на step. В зависимости
    # от знака атрибута step итерация завершится либо когда pointer станет больше stop,
    # либо меньше stop. Учтите это при описании метода.
    def __next__(self):
        """Метод для получения следующего значения итератора."""
        if (self.step > 0 and self.pointer >= self.stop) or (self.step < 0 and self.pointer <= self.stop):
            raise StopIteration
        value = self.pointer
        self.pointer += self.step
        return value

    def __next__(self):
        """Метод для получения следующего значения итератора."""
        if (self.step > 0 and self.pointer >= self.stop) or (self.step < 0 and self.pointer <= self.stop):
            raise StopIteration
        value = self.pointer
        self.pointer += self.step
        return value


# Пример выполняемого кода:
try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()
