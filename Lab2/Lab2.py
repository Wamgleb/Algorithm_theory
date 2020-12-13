from random import randint
import time
import random

N = 100
#sort_list2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
sort_list = []
start_time = time.time()

for i in range(1,101):
    sort_list.append(i)
    random.shuffle(sort_list)
print(sort_list)



#for i in range(N):
 #   sort_list.append(randint(1,100))
#print(sort_list)


#sort_list = sort_list2 + sort_list1
#print(sort_list)

for i in range(N-1):
    for j in range(N - i -1):
        if sort_list[j] > sort_list[j+1]:
            sort_list[j], sort_list[j+1] = sort_list[j+1], sort_list[j]

print(sort_list)
print("\n",time.time() - start_time, "seconds")

