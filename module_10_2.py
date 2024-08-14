# Потоки на классах
from threading import Thread
from time import sleep


class Knight(Thread):
    name = ''
    power = 0
    count_day = 0

    def __init__(self, name, power):
        self.name = name
        self.power = power
        super().__init__()

    def run(self):
        print(f"{self.name}, на нас напали!")
        count_warrior = 100
        self.count_day = 0
        while count_warrior > 0:
            sleep(1)
            count_warrior -= self.power
            self.count_day += 1
            print(f"{self.name} сражается {self.count_day} день(дня)..., осталось {count_warrior} воинов.")
        print(f"{self.name} одержал победу спустя {self.count_day} дней(дня)!")


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

# Вывод строки об окончании сражения
print("Все битвы закончились!")
