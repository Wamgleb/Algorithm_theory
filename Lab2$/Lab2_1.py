from random import randint
import time
import random

#Засекаем время
start_time = time.time()

#реализацыя алгоритма
def sel_sort(array):
    for i in range(len(array) - 1):
        m = i
        j = i + 1
        while j < len(array):
            if array[j] < array[m]:
                m = j
            j = j + 1
        array[i], array[m] = array[m], array[i]

a = []
#sort_list2 = [1,2,3,4,5,6,7,8,9,10,11,12]#13,14,15,16,17,18,19,20,21,22,23,24,25,26]
#for i in range(88): #74
#    a.append(randint(13,101)) #24,100

#Генерируем список уникальных значений и рандомно перемешиваем его 
for i in range(1,101):
    a.append(i)
    random.shuffle(a)
print(a)
#тут я создаю список частично отсортированый, использую уже готовый список 
#a1 = sort_list2 + a
#print(a1)
sel_sort(a)
print(a)
print(len(a))

#время выполнения алгоритма
print("\n",time.time() - start_time, "seconds")