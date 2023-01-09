import time
import random
def mergesort(arr):
    if(len(arr)>1):
        mid=(len(arr))//2
        R=arr[mid:]
        L=arr[:mid]
        mergesort(L)
        mergesort(R)
        i=j=k=0
        while i<len(L) and j<len(R):
            if L[i] < R[j]:
                arr[k]=L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i<len(L):
            arr[k]=L[i]
            i+=1
            k+=1

        while j<len(R):
            arr[k]=R[j]
            j+=1
            k+=1

numlist=[0]*10
for i in range(0,10):
    numlist[i]=random.randrange(0,2000,1)
begin = time.time()
mergesort(numlist)
#time.sleep(1)
end = time.time()
# total time taken
print(f"Total runtime of the program is {end - begin}")
print(numlist)






