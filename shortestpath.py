def shortestpath(AL,n,u,up):
    dist = [float('inf')] * n
    pred = [None] * n
    Q = []
    dist[u] = 0
    print('Dist: '+str(dist))
    Q.append(u)
    print('Queue: '+str(Q))
    while len(Q) != 0:
        x = Q.pop(0)
        print('Pop '+str(x)+' and process vertices '+str(AL[x]))
        for y in AL[x]:
            if dist[y] == float('inf'):
                print('__Process: '+str(y))
                dist[y] = dist[x] + 1
                print('__Dist: '+str(dist))
                pred[y] = x
                if y == up:
                    return(dist,pred)
                Q.append(y)
                print('__Queue: '+str(Q))
            else:
                print('__Already done: '+str(y))

AL = [
    [1, 3],
    [0, 2, 4],
    [1, 5],
    [0, 4, 6],
    [1, 3, 7],
    [2, 8],
    [3, 8],
    [4],
    [5, 6]
]
n = 9

u = 0
up = 7
[dist,pred] = shortestpath(AL,n,u,up)

path = []
x = up
while x != None:
    path.append(x)
    x = pred[x]
path.reverse()
print('Path: '+str(path))
print('Length: '+str(len(path)-1))
