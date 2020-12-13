import random
import time
from random import randint

def heapSort(li):
    def downHeap(li, k, n):
        new_elem = li[k]
        while k <= n/2:
            child = 2*k;
            if child < n and li[child] < li[child+1]:
                child += 1
            if new_elem >= li[child]:
                break
            li[k] = li[child]
            k = child
        li[k] = new_elem
        
    size = len(li)
    for i in range(round(size/2-1),-1,-1):
        downHeap(li, i, size-1)
    for i in range(size-1,0,-1):
        temp = li[i]
        li[i] = li[0]
        li[0] = temp
        downHeap(li, 0, i-1)
    return li

li =[]

for i in range(1,101):
    li.append(i)
    random.shuffle(li)
print(li)

print(heapSort(li))