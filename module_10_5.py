# Многопроцессное программирование
import multiprocessing
import datetime


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        str_file = file.readline()
        while str_file:
            all_data.append(str_file)  # формируем список
            str_file = file.readline()  # \n убирать не будем


if __name__ == "__main__":
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    # Линейный вызов
    start = datetime.datetime.now()
    for i in range(4):
        read_info(filenames[i])
    end = datetime.datetime.now()
    print(end - start, "Линейный")

    # Многопроцессный
    start = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print(end - start, "Многопроцессный")
