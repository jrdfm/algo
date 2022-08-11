#!/usr/local/bin/python


# adjacency matrix to adjacency list
def AM_AL(A):
    AL = []
    for i in range(len(A)):
        L = []
        for j in range(len(A[i])):
            if A[i][j] == 1:
                L.append(j)
        AL.append(L)   
    # print(f'AL {AL}')
    return AL

# adjacency list to adjacency matrix
def AL_AM(A):
    AM = [[0]*len(A) for _ in range(len(A))]
    c = 0 

    for i in range(len(A)):
        # print(f'i {i}')
        for j in range(len(A[i])):
            # print(f'j {j}')
            # print(f'A[i][j] {A[i][j]}')
            # print(f'AM[i][A[i][j]] {AM[i][A[i][j]]}')
            AM[i][A[i][j]] = 1
            c += 1

    # print(f'AM {AM} c {c}')
    return AM

# adjacency matrix walk?
def walk(A, V):
    for i in range(len(V) - 1):
        # print(f'i {i}')
        # print(f'A[V[{i}]][V[{i+1}]] = {A[V[i]][V[i+1]]}')
        if A[V[i]][V[i+1]] != 1:
            return False
    return True
# adjacency list walk?
def walk_al(AL, V):
    for i in range(len(V) - 1):
        if not V[i+1] in AL[V[i]]:
            return False 
    return True

# adjacency matrix path?
def path(A, V):
    if walk(A,V):
        for i in range(len(V)):
            if in_list(V[i],V[i+1:]) and (V[i+1:].index(V[i]) - i + 1) != len(V) - 1:
                # print(f'V[i] {V[i]} i {i} {(V[i+1:].index(V[i]) - i + 1) == len(V) - 1}')
                return False 
    return True

# adjacency matrix trail?
def trail(A,V):
    t = [(V[i],V[i+1]) for i in range(len(V)-1)]
    if walk(A, V):
        for i in range(len(t)):
            rev = (t[i][1],t[i][0])
            if in_list(t[i],t[i+1:]) or in_list(rev,t[i+1:]):
                return False
    return True
# helper 
def in_list(x,lst):
    return x in lst


if __name__ == "__main__":
    A = [[0,1,1,0],[1,0,1,0],[1,1,0,1],[0,0,1,0]]
    print(f'A {A}')
    AM_AL(A)
    AL  = [[1, 2], [0, 2], [0, 1, 3], [2]]
    AL_AM(AL)

    #v = [[3,2,0,2,1],[2,1,2,3],[3,2,1,0],[0,1,2,0]]
    v = [3,2,0,2,1]

    print(f'walk {walk(A,v)}')

    print(f'trail {trail(A,v)}')








# def path(A, V):
#     t = [(V[i],V[i+1]) for i in range(len(V)-1)]
#     # print(f't {t}')
#     b = False
#     for i in range(len(t)):
#         rev = (t[i][1],t[i][0])
#         # print(f'i {i} t[:i] {t[:i]} t[i+1:] {t[i+1:]} \n t[i] {t[i]} rev {rev}')
#         if b:
#             return not b
#         b = b or in_list(t[i],t[:i]) or in_list(t[i],t[i+1:]) or in_list(rev,t[:i]) or in_list(rev,t[i+1:])
#         # print(f'b {b}')
#     return walk(A, V) and not b

#  and V[i+1:].index(V[i]) != len(V) - 1