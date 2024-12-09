first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Генераторная сборка, высчитывает разницу длин строк из списков, если их длины не равны#
first_result = (abs(len(f) - len(s)) for f, s in zip(first, second) if len(f) != len(s))


# Генераторная сборка, которая содержит результаты сравнения длин строк в одинаковых
# позициях из списков
second_result = (len(first[i]) == len(second[i]) for i in range(min(len(first), len(second))))


print(list(first_result))
print(list(second_result))
