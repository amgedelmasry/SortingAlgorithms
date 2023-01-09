import time
import random
def selectionSort(x):
    n = len(x)
    for i in range(0, n):
        min = i
        for j in range(i+1, n):
            if x[j] < x[min]:
                min =  j
        x[min], x[i] = x[i], x[min]
numlist=[0]*20
for i in range(0,20):
    numlist[i]=random.randrange(0,20,1)
begin = time.time()
selectionSort(numlist)
end = time.time()
print(f"Total runtime of the program is {end - begin}")
print(numlist)
