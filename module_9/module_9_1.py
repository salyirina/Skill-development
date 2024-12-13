import time

start_time = time.time()

def apply_all_func(int_list, *functions):
    # Создаём словарь для результатов
    result = {}

    # Применяем каждую функцию к списку
    for function in functions:
        # чтобы взять название функции обратиться к атрибуту __name__
        result[function.__name__] = function(int_list)

    return result


# Пример работы кода:
print(apply_all_func.__name__)
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))


finish_time = time.time()
print(f'Время в милисекундах: {(finish_time-start_time) * 1000}')