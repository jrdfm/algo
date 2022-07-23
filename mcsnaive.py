import random
A = []
for i in range(0,7):
    A.append(random.randint(-10,10))
n = len(A)
print(A)

max = A[0]
for i in range(0,n):
    sum = 0
    for j in range(i,n):
        sum = sum + A[j]
        if sum > max:
            max = sum
        print('Max of ' + str(A[i:j+1]) + ': ' + str(max))

print('Overall max: ' + str(max))
