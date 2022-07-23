def dfs(EL,n,x,depth):
    print('_'*depth + 'Recursive depth = ' + str(depth))
    D[x] = True
    V.append(x)
    print('_'*depth + 'V = ' + str(V))
    print('_'*depth + 'D = ' + str(D).replace('True','T').replace('False','F'))
    for y in EL[x]:
        if not D[y]:
            dfs(EL,n,y,depth+1)
EL = [
    [1, 4, 5],
    [0, 2, 6],
    [1, 3, 6, 7],
    [2],
    [0, 8],
    [0, 8, 9],
    [1, 2, 11],
    [2],
    [4, 5, 13],
    [5, 10],
    [9, 14],
    [6, 15],
    [13],
    [8, 12],
    [10],
    [11]
]
n = 16
s = 0
D = [False] * n
V = []
dfs(EL,n,s,0)
