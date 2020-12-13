import time
import random
from random import randint

#Реализация очереди
class Queue:
    def __init__(self):
        self.people = []
    
    def add(self, person):
        self.people.insert(0, person)
    def remove(self):
        return self.people.pop()
    def size(self):
        return len(self.people)

q = Queue()
start_time = time.time()

#Добавление в очередь
for i in range(1000):
    q.add(i)

#Выводим длину очереди
print(q.size())
#Удаляем элемнт с очереди
#print(q.remove())
#Проверяем блину очереди
#print(q.size())

print("\nВремя выполнения алгоритма: ", str((time.time() - start_time) * 1000).replace(".", ","), "ms")


