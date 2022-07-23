#!/usr/local/bin/python
import random
A = []
for i in range(0,23):
    A.append(random.randint(0,100))
n = len(A)
print(A)

for i in range(0,n-1):
    minindex = i
    maxindex = i
    for j in range(i+1,n):
       if A[j] < A[minindex]:
          minindex = j
       elif A[j] > A[maxindex]:
          maxindex = j
    print('In A['+str(i)+','+str(n-1)+'] the index of the minimum is '+str(minindex))
    temp = A[i]
    A[i] = A[minindex]
    A[minindex] = temp
    print('Swap indices ' + str(minindex) + ' and ' + str(i))
    print('Now: ' + str(A))

print(A)

A.reverse()
print(f'\n\n')

# A = [65, 70, 64, 18, 56, 69, 82, 21, 15, 15, 10, 60]
print(A)

for i in range(0,n // 2):
    minindex = maxindex = i
    for j in range(i+1,n - i):
        if A[j] < A[minindex]:
            minindex = j
        elif A[j] > A[maxindex]:
            maxindex = j
    print(f'\nA[{i},{n- i - 1}] = {A[i:n-i]}')
    print(f'min is {A[minindex]} @ {minindex} max is {A[maxindex]} @ {maxindex}')
    if i == maxindex:
        A[i], A[minindex]  = A[minindex], A[i]
        A[n - i - 1], A[minindex] = A[minindex], A[n - i - 1]
    else:
        A[i], A[minindex]  = A[minindex], A[i]
        A[n - i - 1], A[maxindex] = A[maxindex], A[n - i - 1]
    print(f'A {A}')

