# Блокировки и обработка ошибок
import random
import threading
import time


class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            increase = random.randint(50, 500)
            if self.balance > 500 and self.lock.locked():
                self.lock.release()
            self.balance += increase
            print(f"Пополнение: {increase}. Баланс: {self.balance}.")
            time.sleep(0.001)

    def take(self):
        for j in range(100):
            reduce = random.randint(50, 500)
            print(f"Запрос на {reduce}.")
            if reduce <= self.balance:
                self.balance -= reduce
                print(f"Снятие: {reduce}. Баланс: {self.balance}.")
            else:
                self.lock.acquire()
                print(f"Запрос отклонён, недостаточно средств")


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
