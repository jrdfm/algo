#!/usr/local/bin/python


import random
A = []
for i in range(0,10):
    A.append(random.randint(0,100))
A = [4,2,1,5,3]
n = len(A)

print('Start: '+str(A))
for i in range(0,n):
    for j in range(0,n-i-1):
        if A[j] > A[j+1]:
            temp = A[j]
            A[j] = A[j+1]
            A[j+1] = temp
    print('Iterate: '+str(A))
print(A)
