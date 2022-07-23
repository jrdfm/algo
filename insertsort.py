#!/usr/local/bin/python
import random
import math

# a shitty wrapper
class num:
    def __init__(self, n):
        self.n = n

def insert_sort(A):
    n = len(A)
    inv = []
    for i in range(0,n):    
        key = A[i]
        print('key = ' + str(key) + ' at index ' + str(i))
        j = i-1
        howmanytoleft = 0
            
        while j>=0 and key<A[j]:
            print(f'{key} < {A[j]}')
            howmanytoleft = howmanytoleft + 1
            inv.append((A[j], key))
            A[j+1] = A[j]
            
            
            j = j - 1
        if howmanytoleft == 0:
            pass
            print('There are 0 larger elements to the left. Leave alone.')
        else:
            A[j+1] = key
            print('There are ' + str(howmanytoleft) + ' larger elements to the left.')
            print('Shift and insert: ' + str(A) )
    print(f'sorted {A}')
    print(f'inversions {inv}')

# Sorts num objects which is just a shitty wrapping for ints
def insert_sort_o(A):
    inv = []
    for i in range(len(A)):    
        key = A[i]
        j = i
        while j - 1 >= 0 and key.n < A[j - 1].n:
            # print(f'(A[j - 1].n, key) {(A[j - 1].n, key.n)}')
            inv.append((A[j - 1].n, key.n))
            A[j] = A[j - 1]
            j -= 1
        A[j] = key
        # print(f'(A[j].n, key.n) {(A[j].n, key.n)}')
        if A[j].n != key.n:
            inv.append((key.n, A[i].n))
    return len(inv)
    print(f'inv {inv} len inv {len(inv)} C(n,2)/2 = {math.comb(len(A), 2)/2}')

if __name__ == "__main__":

    A = random.sample(range(10), 10)
    # print(f'r type {type(r)} r {r}')
    # A = []
    # for i in range(0,10):
    #     A.append(random.randint(0,10))
    # A = [random.randint(0,10) for _ in range(0,10)]
    # A = [4,3,1,8,3]
    A = [3,5,1,4,600]
    A_ = [num(i) for i in A]
    # addr = [hex(id(i)) for i in A]
    print(f'A {A} \n')


    insert_sort(A)
    # addr = [hex(id(i)) for i in A]
    # print(f'A sorted {A} \naddress {addr}')

    # print(f'A_ {[i.n for i in A_]}')
    # addr = [hex(id(i)) for i in A_]
    # # print(f'A_ addr\n{addr}\n')
    # insert_sort_o(A_)
    # addr = [hex(id(i)) for i in A_]
    # print(f'A_ sorted {[i.n for i in A_]}')
    # # print(f'A_ sorted addr\n{addr}\n')


    # # print(inv)
    # inv = 0
    # n = 1000
    # for i in range(n):
    #     A = random.sample(range(10), 10)
    #     A_ = [num(i) for i in A]
    #     inv += insert_sort_o(A_)

    # print(f'avg inv {inv/n}')
        

                
