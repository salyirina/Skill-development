immutable_var = (1, 2, 'a', 'b')  # Создание кортежа из нескольких элементов разных типов
print('Immutable tuple:', immutable_var)

# immutable_var[1] = "World" # Попытка изменить элемент кортежа
# print( immutable_var)
# Объяснение:
# Кортежи в Python являются неизменяемыми(immutable_var), поэтому их элементы нельзя
# изменить после присвоения. Если попытаться изменить элемент, будет вызвано исключение
# TypeError. В примере мы обрабатываем эту ошибку и выводим сообщение об ошибке на экран.


# Создание списка, который является изменяемой структурой данных
mutable_list = [1, 2, 'a', 'b']
# Изменение элементов списка
mutable_list[1] = 'Hello!'
mutable_list[3] = 'pyton'
print("mutable_list:", mutable_list)

# Изменение последнего элемента списка
mutable_list = [1, 2, 'a', 'b']
mutable_list.append('Modified')
print('mutable_list', mutable_list)


