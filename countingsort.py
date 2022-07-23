import random
A = []
k = 5
n = 10
for i in range(0,n):
    A.append(random.randint(0,k))
print(A)
ANEW = [0] * n
LOC = [0] * (k+1)
for i in range(0,n):
    LOC[A[i]] = LOC[A[i]] + 1
print('Count array: '+str(LOC))
for i in range(1,k+1):
    LOC[i] = LOC[i] + LOC[i-1]
print('Cumulative count array: '+str(LOC))
for i in range(n-1,-1,-1):
    ANEW[LOC[A[i]]-1] = A[i]
    LOC[A[i]] = LOC[A[i]] - 1
    print('Positioning A['+str(i)+'] in position '+str(LOC[A[i]]-1))
    print('Result: '+str(ANEW))
for i in range(0,n):
    A[i] = ANEW[i]
print(A)
