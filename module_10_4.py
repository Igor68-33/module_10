# Очереди для обмена данными между потоками.
from threading import Thread
from queue import Queue
from random import randint
from time import sleep


class Table:
    guest = None

    def __init__(self, number):
        self.number = number


class Guest(Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        sleep(randint(3, 10))
        # print(self.name, "поел")


class Cafe:
    tables = []
    queue = Queue()

    def __init__(self, *args):
        for table in args:
            self.tables.append(table)

    def guest_arrival(self, *guests):
        for person in guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest = person
                    print(f"{person.name} сел(-а) за стол номер {table.number}")
                    person.start()
                    break
            else:
                self.queue.put(person)
                print(f"{person.name} в очереди")

    def discuss_guests(self):
        while not self.queue.empty() or sum(table.guest is not None for table in self.tables):
            for table in self.tables:
                if (table.guest is not None) and (table.guest.is_alive() is False):
                    print(f"{table.guest.name} за {table.number} столом покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None
            for table in self.tables:
                if table.guest is None:
                    if self.queue.empty() is False:
                        person = self.queue.get()
                        table.guest = person
                        print(f"{person.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                        person.start()
        print("Все гости поели.")


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# print(guests)
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
