def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

# 2.Распаковка параметров:
# Создайте список values_list с тремя элементами разных типов.
values_list = (1, ['2'], 'Dima')

# Создайте словарь values_dict с тремя ключами, соответствующими параметрам функции print_params, и значениями разных типов.
values_dict =  {'a': 1.2, 'b': 5, 'c': "Hi"}

# Передайте values_list и values_dict в функцию print_params, используя распаковку параметров (* для списка и ** для словаря).
print_params(*values_list)
print_params(**values_dict)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print_params(a=8, b=10, c=False)
print_params(*values_list)
print_params(**values_dict)