# В true_math создайте функцию divide, которая принимает два параметра first и second (первый и второй).
# Функция должна возвращать результат деления first на second, но когда в second записан 0 - возвращать бесконечность.
# Бесконечность можно импортировать из встроенной библиотеки math (from math import inf)

from math import inf


def divide(first, second):
    if second == 0:
        return inf  # возвращать бесконечность
    return first/second
