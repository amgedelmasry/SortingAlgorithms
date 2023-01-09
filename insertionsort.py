import time
import random
# insertion sort
def insertionSort(x):
    n = len(x)
    for i in range(1, n):
        key = x[i]
        j = i-1
        while j >= 0 and x[j] > key:
           x[j+1] = x[j]
           j = j-1
        x[j+1] = key


numlist=[]
for i in range(0,10):
    numlist.append(random.randrange(0,200,1))
begin = time.time()
insertionSort(numlist)
end = time.time()
print(f"Total runtime of the program is {end - begin}")
print(numlist)