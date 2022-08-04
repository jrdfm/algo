#!/usr/local/bin/python
import random
import math

def comp(A):
    i = 0
    if A[0] > A[1]:
        A[0], A[1] = A[1], A[0]
        i += 1
        # print(f'i {i}: A {A}')
    if A[2] > A[3]:
        A[2], A[3] = A[3], A[2]
        i += 1
        # print(f'i {i}: A {A}')
    if A[0] > A[2]:
        A[0], A[2] = A[2], A[0]
        i += 1
        # print(f'i {i}: A {A}')
    if A[1] > A[3]:
        A[1], A[3] = A[3], A[1]
        i += 1
        # print(f'i {i}: A {A}')
    if A[1] > A[2]:
        A[1], A[2] = A[2], A[1]
        i += 1
        # print(f'i {i}: A {A}')        



if __name__ == "__main__":
    


    # A = [3,5,4,600]

    for i in range(10):
        A = [random.randrange(0,100) for _ in range(4)]
        print(f'A {A}')
        comp(A)
        print(f'A sorted {A}\n')

