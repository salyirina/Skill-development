import threading
from time import sleep, time


def write_words(word_count, file_name):
    with open(file_name, 'w') as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


# Измерение времени выполнения синхронных вызовов
start_time = time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

sync_end_time = time()
print(f"Время выполнения синхронных вызовов: {sync_end_time - start_time:.2f} секунд")

# Функция для потоков
threads = []
thread_args = [
    (10, 'example5.txt'),
    (30, 'example6.txt'),
    (200, 'example7.txt'),
    (100, 'example8.txt')
]


# Создание потоков
for args in thread_args:
    thread = threading.Thread(target=write_words, args=args)
    threads.append(thread)

# Измерение времени выполнения потоков
thread_start_time = time()

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

thread_end_time = time()

print(f"Время выполнения многопоточных вызовов: {thread_end_time - thread_start_time:.2f} секунд")

# Общее время выполнения программы
total_end_time = time()
print(f"Общее время выполнения программы: {total_end_time - start_time:.2f} секунд")
