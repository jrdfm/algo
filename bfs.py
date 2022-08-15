#!/usr/bin/python3


def bfs(EL,n,s):
    Q = [s]
    D = [False] * n
    D[s] = True
    V = [s]
    c = f = w = 0
    print('Q = ' + str(Q))
    print('V = ' + str(V))
    #print('D = ' + str(D).replace('True','T').replace('False','F'))
    while len(Q) != 0:
        w += 1
        x = Q.pop(0)
        for y in EL[x]:
            c += 1
            if not D[y]:
                f += 1
                D[y] = True
                V.append(y)
                Q.append(y)
        print('Q = ' + str(Q))
        print('V = ' + str(V))
        print('c = ' + str(c))
        #print('D = ' + str(D).replace('True','T').replace('False','F'))
    return(V,(c,f,w))


if __name__ == "__main__":    
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


    A = [[1,2],[0,3,4],[0,5,6],[1,7,8],[1,9,10],[2,11,12],[2,13,14],[3],[3],[4],[4],[5],[5],[6],[6]]
    n = 15
    s = 0
    visited, (c,f,w) = bfs(A,n,s)
    print(f'Visited = {visited} for {c} if {f} while {w}')
