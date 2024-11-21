
first = number = int(input('Введите любое число '))
second = number = int(input('Введите второе число '))
third = number = int(input('Введите третье число '))

# Если все числа равны между собой, то вывести 3

if first == second and third:
    print(3)

# Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2

if first == second or first == third or second == third:
    print(2)

# Если равных чисел среди 3-х вообще нет, то вывести 0
else:
    print(0)


