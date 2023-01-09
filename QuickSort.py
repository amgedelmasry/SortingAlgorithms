import random
import time

def partition(unsorted, first, last):
    pivot=random.randrange(first,last,1)
    unsorted[first], unsorted[pivot] = unsorted[pivot], unsorted[first]
    lasts1 = first
    firstunknown = first + 1
    while (firstunknown <= last):
        if unsorted[firstunknown] < unsorted[first]:
            lasts1 += 1
            unsorted[firstunknown], unsorted[lasts1] = unsorted[lasts1], unsorted[firstunknown]
        firstunknown += 1
    unsorted[first], unsorted[lasts1] = unsorted[lasts1], unsorted[first]
    return lasts1


def quickSort(unsorted, first, last):
    if first<last:
        x=partition(unsorted,first,last)
        quickSort(unsorted,first,x-1)
        quickSort(unsorted,x+1,last)

numlist=[0]*20
for i in range(0,20):
    numlist[i]=random.randrange(0,20,1)
begin = time.time()
print(numlist)
quickSort(numlist,0,len(numlist)-1)
end = time.time()
print(f"Total runtime of the program is {end - begin}")
print(numlist)

