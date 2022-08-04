#!/usr/local/bin/python


def quicksort(l,r,indent, A = None):
    if l<r:
        print(f'{A}')
        resultingpivotindex = partition(l,r,indent+2)
        quicksort(l,resultingpivotindex-1,indent+2)
        quicksort(resultingpivotindex+1,r,indent+2)
        print(indent*'_' + 'Recombine: '+str(A[l:r+1]))


def partition(l,r,indent):
    print(indent*'_' + 'Subarray: ' + str(A[l:r+1]))
    # To use a different pivotvalue
    # swap it with A[r] here.
    pivotvalue = A[r]
    t = l
    for i in range(l,r):
        if A[i] <= pivotvalue:
            temp = A[t]
            A[t] = A[i]
            A[i] = temp
            t = t + 1
    temp = A[t]
    A[t] = A[r]
    A[r] = temp
    print(indent*'_' + 'Pivot around final element.')
    print(indent*'_' + 'Result: ' + str(A[l:r+1]))
    return(t)



if __name__ == "__main__":
    
    import random
    A = []
    for i in range(0,7):
        A.append(random.randint(0,100))
    # A = [10,6,7,2,4,3]
    A = [54, 98, 85, 17, 82, 87, 86]
    n = len(A)

    print(A)
    quicksort(0,n-1,0)
    print(A)
