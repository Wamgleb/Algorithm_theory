# Radix sort на Python

import time
import random
from random import randint

start_time = time.time()
# Использование счетной сортировки для сортировки элементов по значимым местам
def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    # Подсчитать количество элементов
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    # Рассчитать совокупный счет
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Разместите элементы в отсортированном порядке
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]


# Основная функция для реализации поразрядной сортировки
def radixSort(array):
    # Получить максимум элемента
    max_element = max(array)

    # Применить сортировку с подсчетом для сортировки элементов по разряду.
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10


data = []
# Создаем втарой массив
date2 = []

# Наполняем массив
for i in range(0, 850):
    data.append(i)
    random.shuffle(data)

#Нполняем второй массив отсортиртированными элементами
for i in range(0, 150):
    date2.append(i)
    random.shuffle(date2)
#print(data)
# Обьединяем массивы 
data_set = date2 + data
#print(data_set)
#print("\n", len(data_set), "\n")
radixSort(data_set)
#print(data_set)
# Выводим время выполнения алгоритма
print("\n", str((time.time() - start_time) * 1000).replace(".", ","), "ms")

