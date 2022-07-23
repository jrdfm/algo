import random

A = []
for i in range(0,20):
    A.append(random.randint(-10,10))

n = len(A)
print(A)

maxoverall = A[0]
maxendingati = A[0]
for i in range(1,n):
    maxendingati = max(maxendingati+A[i],A[i])
    maxoverall = max(maxoverall,maxendingati)
    print('Best sum ending with index i='+str(i)+' is '+str(maxoverall))

print(maxoverall)
