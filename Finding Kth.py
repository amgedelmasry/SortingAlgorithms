import random

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
def findingK(unsorted,first,last,k):
    if first==last:
        return unsorted[first] #if the array is one element
    l = partition(unsorted, first, last)
    if l+1==k:
        return unsorted[l]
    elif l+1<k:
        return findingK(unsorted,l+1,last,k)
    else:
        return findingK(unsorted,first,l-1,k)

unsorted=[3,5,9,7,4,6,12,15,19,34,65,0,-1]
print(findingK(unsorted,0,len(unsorted)-1,3))

