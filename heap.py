#!/usr/local/bin/python
#!/usr/bin/python3




# In order to work with the Python array as tree nodes starting at 1,
# We create a list A[0,...,n] and ignore the 0th entry.

def maxheapify(i):
    c = 1
    leftnode = 2*i
    rightnode = 2*i+1
    largestnode = i
    if leftnode <= heapsize and A[leftnode] > A[largestnode]:
        largestnode = leftnode
    if rightnode <= heapsize and A[rightnode] > A[largestnode]:
        largestnode = rightnode
    # print(f'heapsize {heapsize}')
    # print(f'largest node = {largestnode}, i = {i}\nabs(largestnode - i) = {abs(largestnode - i) }')
    if abs(largestnode - i) > 4:
        c *= 4
    elif abs(largestnode - i) == 0:
        c = 0
    else:
        c *= 1
    # print(f'c {c}')
    if largestnode != i:
        temp = A[i]
        A[i] = A[largestnode]
        A[largestnode] = temp
        return c + maxheapify(largestnode)
    return c

def converttomaxheap():
    for i in range(math.floor(heapsize/2),0,-1):
        maxheapify(i)

def heapsort():
    global heapsize
    #converttomaxheap()
    print('After converttomaxheap:')
    print(f'A {A[1:]}')

    for i in range(nodecount,1,-1):
        print(f'i : {i}')
        temp = A[1]
        A[1] = A[i]
        A[i] = temp
        print('After switch:')
        print(A[1:])
        heapsize = heapsize - 1
        c = maxheapify(1)
        print(f'After maxheapify: c = {c}')
        print(A[1:])



if __name__ == "__main__":
    import random
    import math
    # A = []
    # for i in range(1,16):
    #     A.append(random.randint(0,100))
    A = [i for i in range(0,16)]
    # tmp = A[8]
    # A[8] = A[9] 
    # A[9] = tmp

    heapsize = len(A)-1;
    nodecount = len(A)-1
    print(f'A {A[1:]}')

    # c = maxheapify(4)
    # print(f'A {A[1:]}')
    # print(f'Total work maxheapify(4) = {c}C')

    # heapsort()
    # print(f'A[1:] {A[1:]}')


    A = [i for i in range(0,16)]
    # c = maxheapify(1)
    print(f'A {A[1:]}')
    tmp = A[15]
    A[15] = A[1] 
    A[1] = tmp
    print(f'A {A[1:]}')
    heapsort()
    print(f'A[1:] {A[1:]}')
    # print(f'Total work maxheapify(1) = {c}C')
    # A = [0,1,101,4,3,8,2,9,10,6,5,100,17]
    # heapsize = len(A)-1;
    # nodecount = len(A)-1
    # print(f'A {A[1:]}')
    # i = [6,5,4,3,2,1]
    # for j in i:
    #     maxheapify(j)
    #     print(f'maxheapify(A, {j}){A[1:]}')

