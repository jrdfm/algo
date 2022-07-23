def bfs(EL,n,s):
    Q = [s]
    D = [False] * n
    D[s] = True
    V = [s]
    print('Q = ' + str(Q))
    print('V = ' + str(V))
    #print('D = ' + str(D).replace('True','T').replace('False','F'))
    while len(Q) != 0:
        x = Q.pop(0)
        for y in EL[x]:
            if not D[y]:
                D[y] = True
                V.append(y)
                Q.append(y)
        print('Q = ' + str(Q))
        print('V = ' + str(V))
        #print('D = ' + str(D).replace('True','T').replace('False','F'))
    return(V)
EL = [
    [1, 4, 5],
    [0, 2, 6],
    [1, 3, 6, 7],
    [2],
    [0, 8],
    [0, 6, 8, 9],
    [1, 2, 5, 11],
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
visited = bfs(EL,n,s)
print('Visited = ' + str(visited))
