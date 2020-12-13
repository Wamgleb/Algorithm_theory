import random
from random import randint
import time

start_time = time.time()

l = [] #пустой массив
b = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]#,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
#наполнение масива и его перемешка 
for i in range(1,101):
    l.append(i)
    random.shuffle(l)
print(l)
print('\n',"Длина списка: ", len(l), "\n")

#L = b + l #Обьеденям массивы
#print(L)
#print("\n", "Длина списка: ", len(L), "\n")

#алгоритм быстрой сортировки
def quicksort(nums):
   if len(nums) <= 1:
       return nums
   else:
       q = random.choice(nums)
   l_nums = [n for n in nums if n < q]
 
   e_nums = [q] * nums.count(q)
   b_nums = [n for n in nums if n > q]
   return quicksort(l_nums) + e_nums + quicksort(b_nums)

print(quicksort(l))
#Виводим время в секундах, переводим в милсек, преобразуем тип данных int в str
# и меняем точку на запяту, это сделано для удобства помещения данных в гугл таблицу
print("\n",str((time.time() - start_time) * 1000).replace('.', ','), "ms", "\n")