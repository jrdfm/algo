#!/usr/local/bin/python



def bubble(A):
    for i in range(0,n):
        swap = False
        for j in range(0,n-i-1):
            if A[j] > A[j+1]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
                print(f'swapped ({j},{j+1})')
                swap = True
        if not swap:
            break
        print('Iterate: '+str(A))
    return A



if __name__ == "__main__":
    import random
    A = []
    for i in range(0,10):
        A.append(random.randint(0,100))
    A = [4,2,1,5,3]
    n = len(A)

    print('Start: '+str(A))

    print(bubble(A))