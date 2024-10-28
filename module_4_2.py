def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    # inner_function глобальной переменной
    global outer_function
    outer_function = inner_function


# Вызываем test_function, чтобы создать и присвоить inner_function глобальной переменной
test_function()
outer_function()  # Вызовем inner_function вне функции test_function через глобальную переменную


# 1. Создайте новую функцию test_function
# 2. Создайте внутри test_function другую функцию - inner_function,
# Эта функция должна печатать значение "Я в области видимости функции test_function"
# 3. Вызовите функцию inner_function внутри функции test_function
# 4. Попробуйте вызывать inner_function вне функции test_function
# и посмотрите на результат выполнения программы
