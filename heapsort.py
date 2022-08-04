#!/usr/bin/python3
#!/usr/local/bin/python



# In order to work with the Python array as tree nodes starting at 1,
# We create a list A[0,...,n] and ignore the 0th entry.

def maxheapify(i):
    leftnode = 2*i
    rightnode = 2*i+1
    largestnode = i
    if leftnode <= heapsize and A[leftnode] > A[largestnode]:
        largestnode = leftnode
    if rightnode <= heapsize and A[rightnode] > A[largestnode]:
        largestnode = rightnode
    if largestnode != i:
        temp = A[i]
        A[i] = A[largestnode]
        A[largestnode] = temp
        maxheapify(largestnode)

def converttomaxheap():
    for i in range(math.floor(heapsize/2),0,-1):
        maxheapify(i)

def heapsort():
    global heapsize
    converttomaxheap()
    print('After converttomaxheap:')
    print(A[1:])
    for i in range(nodecount,1,-1):
        temp = A[1]
        A[1] = A[i]
        A[i] = temp
        print('After switch:')
        print(A[1:])
        heapsize = heapsize - 1
        maxheapify(1)
        print('After maxheapify:')
        print(A[1:])



if __name__ == "__main__":
    import random
    import math
    A = []
    for i in range(0,10):
        A.append(random.randint(0,100))
    A = [0,1,101,4,3,8,2,9,10,6,5,100,17]
    heapsize = len(A)-1;
    nodecount = len(A)-1
    print(A[1:])
    heapsort()
    print(A[1:])