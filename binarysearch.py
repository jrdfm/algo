#!/usr/local/bin/python
import random
import numpy as np

def binarysearch(A,TARGET):
    L = 0
    R = len(A)-1
    while L <= R:
        # print('Checking: '+str(A[L:R+1]))
        C = (L+R)//2
        if A[C] == TARGET:
            # print('Checking: [' + str(A[C]) + ']')
            return(C)
        elif TARGET < A[C]:
            R = C-1
        elif TARGET > A[C]:
            L = C+1
    return(False)


def binaryserch_2d(A, target):
    lx = ly = 0
    rx = ry = A.shape[0]  - 1
    cx , cy = (lx + rx) // 2 , (ly + ry) // 2
    row , col = cy , cx
    if A[cx][cy] == target:
        return (cx,cy)
    elif target < A[cx][cy]:
        row = cy - 1
        while 0 <= row < A.shape[0] - 1 and 0 <= col < A.shape[1] - 1:
            res =  binarysearch(A[row,],target)
            if type(res).__name__ == 'int':
                return (row, res)
            else:
                r_c = binarysearch(A[:,col],target)
            if type(r_c).__name__ == 'int':
                return (r_c, col)
            else:
                row -= 1
                col -= 1
    elif target > A[cx][cy]:
        row = cy + 1
        while 0 <= row < A.shape[0] and 0 <= col < A.shape[1]:
            res =  binarysearch(A[row,],target)
            if type(res).__name__ == 'int':
                return (row, res)
            else:
                r_c = binarysearch(A[:,col],target)
            if type(r_c).__name__ == 'int':
                return (r_c, col)
            else:
                row += 1
                col += 1


# def binaryserch_2d(A, target):
#     print(f'A \n{A}')
#     print(f'A.shape {A.shape}')
#     lx = ly = 0
#     rx = ry = A.shape[0]  - 1

#     cx , cy = (lx + rx) // 2 , (ly + ry) // 2
#     row , col = cy , cx

#     if A[cx][cy] == target:
#         return (cx,cy)
#     elif target < A[cx][cy]:
#         print(f'target < A[cx][cy] {target < A[cx][cy]}')
#         row = cy - 1
#         while 0 <= row < A.shape[0] - 1 and 0 <= col < A.shape[1] - 1:
#             print(f'while_1')
#             print(f'searching row {row}  {A[row,]} col {col}')
#             res =  binarysearch(A[row,],target)
#             print(f'res {res} type res {type(res).__name__}')
#             if type(res).__name__ == 'int':
#                 return (row, res)
#             else:
#                 print(f'searching column {col}  {A[:,col]}')
#                 r_c = binarysearch(A[:,col],target)
#                 print(f'row {row} r_c {r_c}')
#             if type(r_c).__name__ == 'int':
#                 return (r_c, col)
#             else:
#                 row -= 1
#                 col -= 1
#             print(f'row {row} col {col}')
#     elif target > A[cx][cy]:
#         print(f'target > A[cx][cy] {target > A[cx][cy]}')
#         row = cy + 1
#         while 0 <= row < A.shape[0] and 0 <= col < A.shape[1]:
#             print(f'while_2')
#             print(f'searching row {row}  {A[row,]} col {col}')
#             res =  binarysearch(A[row,],target)
#             print(f'res {res}')
#             if type(res).__name__ == 'int':
#                 return (row, res)
#             else:
#                 print(f'searching column {col}  {A[:,col]}')
#                 r_c = binarysearch(A[:,col],target)
#                 print(f'row {row} r_c {r_c}')
#             if type(r_c).__name__ == 'int':
#                 return (r_c, col)
#             else:
#                 row += 1
#                 col += 1
            print(f'row {row} col {col}')


if __name__ == "__main__":
    # r = random.randint(0,50)
    # A = []
    # for i in range(0,20):
    #     A.append(random.randint(0,50))
    # A = [r for _ in range(25)]

    # A = np.arange(20)
    np.random.seed(np.random.randint(100))
    # A = np.random.randint(10, size=20)
    AA = np.sort(np.random.randint(10,size = 25))
    AA = np.sort(AA).reshape(5,5)
    target = np.random.randint(10)
    res = binaryserch_2d(AA, target)
    print(f'A \n {AA} \ntarget {target} @ index {res}')
    if res:
        print(f'AA[res] {AA[res]}')
    # print(f'AA \n{AA}')
    # print(f'A {A}')
    # A = np.sort(A)
    # print(A)
    # TARGET = 10
    # print(f'TARGET {TARGET}')
    # result = binarysearch(A,TARGET)
    # if result == False:
    #     print('Not Found')
    # else:
    #     print('Found at index ' + str(result))
