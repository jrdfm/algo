import random
A = []
for i in range(0,13):
    A.append(random.randint(0,100))
n = len(A)
print(A)
def quicksort(l,r,indent):
    if l<r:
        pivotindex = partition(l,r,indent+2)
        quicksort(l,pivotindex-1,indent+2)
        quicksort(pivotindex+1,r,indent+2)
        print(indent*'_' + 'Recombine: '+str(A[l:r+1]))
def partition(l,r,indent):
    print(indent*'_' + 'Subarray: ' + str(A[l:r+1]))
    p = random.randint(l,r)
    temp = A[p]
    A[p] = A[r]
    A[r] = temp
    pivot = A[r]
    t = l
    for i in range(l,r):
        if A[i] <= pivot:
            temp = A[t]
            A[t] = A[i]
            A[i] = temp
            t = t + 1
    temp = A[t]
    A[t] = A[r]
    A[r] = temp
    print(indent*'_' + 'Pivot around index ' + str(p-l))
    print(indent*'_' + 'Result: ' + str(A[l:r+1]))
    return(t)
quicksort(0,n-1,0)
print(A)
