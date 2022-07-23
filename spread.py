#!/usr/local/bin/python
import random
import math

def spread(A):
    spread = - math.inf
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            # print(f'spread_ {spread}')
            if abs(A[i] - A[j]) > spread:
                spread = abs(A[i] - A[j])
    return spread


if __name__ == "__main__":
    
    A = random.sample(range(100), 10)

    # A = [3,5,1,4,600]


    print(f'A {A} \n')

    print(f'spread {spread(A)}')

    n = 10
    A = [i for i in range(1,n)]
    tmp = 1 
    f = [tmp := i * tmp for i in A]