#Работа со словарями
#Выведите на экран словарь
my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print('Dict:', my_dict)

#Выведите на экран одно значение по существующему ключу, одно по отсутствующему из словаря
print('Existing value:', my_dict ['Masha'])

#Добавьте ещё две произвольные пары того же формата в словарь
my_dict.update({'Stela': 1948,
                'Vladimir': 1966})
print('Modified dictionary: ', my_dict)

#Удалите одну из пар в словаре по существующему ключу из словаря my_dict и выведите значение из этой пары на экран.

my_dict = {'Masha': 1985, 'Sasha': 2000, 'Vlad': 1945, 'Stela': 1948, 'Vladimir': 1966}
del my_dict['Masha']
print('Not existing value:', my_dict.get ('Slava'))

x = my_dict.pop('Sasha')
print('Deleted value:', x)

#Создайте переменную и присвойте ей множество, состоящее из разных типов данных с повторяющимися значениями.
my_set = {1, 'Яблоко', 42.314}
print ('Set:', my_set)

#Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
my_set.update({(5, 6, 1.6)})
print(my_set)

#Удалите один любой элемент из множества my_set.
my_set.discard(1)
print('Modified set:', my_set )