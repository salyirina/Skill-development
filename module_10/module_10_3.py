import random
import time
import threading

lock = threading.Lock()


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    @staticmethod
    def _log_and_wait(message):
        """Общий метод для вывода сообщений и ожидания."""
        print(message)
        time.sleep(0.001)

    def deposit(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            self.balance += amount
            self._log_and_wait(f"Пополнение: {amount}, Баланс: {self.balance}")

            # Разблокировать замок, если баланс >= 500 и замок заблокирован
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

            # Имитация времени пополнения
            time.sleep(0.001)

    # соблюсти верную блокировку: в take замок закрывается
    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            print(f"Запрос на {amount}")

            if amount <= self.balance:
                self.balance -= amount
                self._log_and_wait(f"Снятие: {amount}, Баланс: {self.balance}")
            else:
                self._log_and_wait("Запрос отклонён, недостаточно средств")
                self.lock.acquire()


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

# Запускаем потоки
th1.start()
th2.start()

# Ожидаем завершения потоков
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
