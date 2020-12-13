import time 

#Алгоритм стека
class Stack:
    def __init__(self):
        self.elements = []
    def push(self, element):
        self.elements.append(element)
    def pop(self):
        return self.elements.pop()
    def size(self):
        return len(self.elements)

s = Stack()

#Добавляем элемент 
s.push("Tom")
s.push("Bill")
s.push("Deriel")
s.push("Gleb")
s.push("Ann")
s.push("Pola")
s.push("Mary")

#Проверяем длину стека
print(s.size())
#Удаляем элемент
print(s.pop())
