#!/usr/local/bin/python

# use kidane's algo to find the length of the longest string of 1s
def kidane(A):
    max_o = max_i = A[0]
    for i in A:
        max_i = max((max_i + 1) * i, i)
        max_o = max(max_o,max_i)
        print(f'Best sum ending with index i={i} is {max_o}')
    return max_o

# kidane 1 liner

def kid(A):
    tmp = A[0]
    return max([tmp := max(tmp + i, i) for i in A[1:]])


if __name__ == "__main__":
    import random

    # A  = [random.randint(0,1) for i in range(20)]

    # print(f'A {A}')
    # print(f'len = {kidane(A)}')

    A = [4, 3, -10, 3, -1, 2, 0, -3, 5, 7, -4, -8, -10, 4, 7, -30, -2, -6, 4, 7]

    # A = [2,3,-4,5,1,2,-8,3]
    print(f'A: {A}')
    print(f'MCS = {kid(A)}')



    