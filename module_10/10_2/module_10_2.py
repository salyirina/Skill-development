import threading
import time

# Глобальная блокировка для синхронизации вывода
lock = threading.Lock()


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100
        self.days = 0

    @staticmethod
    def print_message(message):
        """Статическая функция для вывода сообщений с блокировкой"""
        with lock:
            print(message)

    def fight(self):
        """Метод для симуляции сражений с уменьшением количества врагов"""
        while self.enemies > 0:
            time.sleep(1)  # Задержка на 1 секунду для имитации дня сражения
            self.enemies -= self.power
            self.days += 1

            # Ограничение на минимальное количество врагов
            self.enemies = max(self.enemies, 0)

            # Вывод информации о текущем сражении
            self.print_message(f"{self.name}, сражается {self.days} день(дня)..., осталось {self.enemies} воинов.")

    def run(self):
        self.print_message(f"{self.name}, на нас напали!")

        # Вызов метода сражения
        self.fight()

        # Сообщение о победе
        self.print_message(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


# Создание рыцарей
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

# Запуск потоков
first_knight.start()
second_knight.start()

# Ожидание завершения потоков
first_knight.join()
second_knight.join()

# Завершение программы
print("Все битвы закончились!")
