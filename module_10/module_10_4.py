import random
import time
import threading
from queue import Queue


# Класс Table
class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None  # Гость за столом, по умолчанию None


# Класс Guest
class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time_to_wait = random.randint(3, 10)  # Случайное время ожидания от 3 до 10 секунд
        print(f"{self.name} начал(а) есть.")
        time.sleep(time_to_wait)  # Ожидание
        print(f"{self.name} закончил(а) есть.")


# Класс Cafe
class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()  # Очередь для гостей
        self.tables = tables  # Список столов

    def guest_arrival(self, *guests):
        for guest in guests:
            # Ищем свободный стол
            free_table = next((table for table in self.tables if table.guest is None), None)

            if free_table:
                # Если стол есть, назначаем гостя и запускаем его поток
                free_table.guest = guest
                guest.start()
                print(f"{guest.name} сел(-а) за стол номер {free_table.number}")
            else:
                # Если нет свободного стола, помещаем гостя в очередь
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():  # Если гость закончил есть
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None  # Освобождаем стол

            # Если очередь не пуста и есть свободный стол, сажаем следующего гостя
            if not self.queue.empty():
                free_table = next((table for table in self.tables if table.guest is None), None)
                if free_table:
                    guest_from_queue = self.queue.get()
                    free_table.guest = guest_from_queue
                    guest_from_queue.start()  # Запускаем поток гостя
                    print(f"{guest_from_queue.name} вышел(-ла) из очереди и сел(-а) за стол номер {free_table.number}")
            time.sleep(1)  # Пауза для имитации времени обслуживания


# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()
