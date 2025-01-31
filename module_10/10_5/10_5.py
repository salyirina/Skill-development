
import time
import multiprocessing

def read_info(name):
    """Функция для построчного чтения файла."""
    all_data = []  # Локальный список для хранения данных

    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:  # Если строка пустая, значит конец файла
                break
            all_data.append(line)  # Добавляем строку в список

# Список названий файлов
filenames = [f'file{number}.txt' for number in range(1, 5)]

# # Линейный вызов
# start_time = time.time()
# for filename in filenames:
#     read_info(filename)
# end_time = time.time()
# print(f"Линейное выполнение заняло: {end_time - start_time:.6f} секунд")

# Многопроцессный вызов
if __name__ == '__main__':
    start_time = time.time()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end_time = time.time()
    print(f"Многопроцессное выполнение заняло: {end_time - start_time:.6f} секунд")