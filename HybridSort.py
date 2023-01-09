import time
import random
def insertionSort(x):
    n = len(x)
    for i in range(1, n):
        key = x[i]
        j = i-1
        while j >= 0 and x[j] > key:
           x[j+1] = x[j]
           j = j-1
        x[j+1] = key


def selectionSort(x):
    n = len(x)
    for i in range(0, n):
        min = i
        for j in range(i+1, n):
            if x[j] < x[min]:
                min =  j
        x[min], x[i] = x[i], x[min]
def hybrid(arr,TH):
    if (len(arr) > 1):
        mid = (len(arr)) // 2
        L = arr[mid:]
        R = arr[:mid]
        if(len(L)<=TH):
            insertionSort(L)
        else:
            hybrid(L,TH)

        if (len(R) <= TH):
            insertionSort(R)
        else:
            hybrid(R,TH)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


numlist=[0]*10
for i in range(0,10):
    numlist[i]=random.randrange(0,10,1)
begin = time.time()
hybrid(numlist,7)
# time.sleep(1)
end = time.time()

# total time taken
print(f"Total runtime of the program is {end - begin}")
print(numlist)