#!/usr/bin/python3

import random
def mergesort(A,indent):
    print(indent * '_' + 'Mergesort:' + str(A))
    if len(A) > 1:
        m = len(A) // 2
        L = A[:m]
        R = A[m:]
        mergesort(L,indent+2)
        mergesort(R,indent+2)
        i = 0
        j = 0
        k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1
        print(indent * '_' + 'Merge:' + str(L) + ' and ' + str(R))
        print(indent * '_' + 'Result: ' + str(A))
A = []
for i in range(0,11):
    A.append(random.randint(0,100))

A = [5,0,7,10,3,8,10,4,1]
print(A)
mergesort(A,0)
print(A)
