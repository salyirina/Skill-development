def get_matrix(n, m, value):
    # Создать пустой список
    matrix = []

    # цикл for для кол-ва строк матрицы, n повторов.
    for i in range(n):
        # добавляйте пустой список в список matrix.
        line = []

        # цикл for для кол-ва столбцов матрицы, m повторов
        for j in range(m):
            line.append(value)

        # Добавляем строку в матрицу. Пополняйте ранее добавленный пустой
        # список значениями value
        matrix.append(line)
    # Возвращаем готовую матрицу
    return matrix

# Примеры использования функции
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

# Вывод результата на экран
print(result1)
print(result2)
print(result3)


