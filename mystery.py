#!/usr/local/bin/python
import random
import math

def mystery(A):
    count =  0
    for i in range(len(A)):
        # print(f'i {i} count {count}')
        for j in range(len(A)):
            # print(f'j {j} count {count}')
            if i < j and A[i] > A[j]:
                count += 1
            if i > j and A[i] < A[j]:
                count += 1
    return count

def mys(A):
    count =  0
    for i in range(len(A)):
        # print(f'i {i} count {count}')
        for j in range(len(A)):
            # print(f'j {j} count {count}')
            if (j - i)* (A[i] - A[j]) > 0:
                count += 1
    return count

if __name__ == "__main__":
    
    # A = [1,2,3,4,5]
    # # A = [5,4,3,2,1]
    A = [1,4,3,5,2]


    print(f'A {A} \n')
    print(f'count {mystery(A)}')

    print(f'count_mys {mys(A)}')
