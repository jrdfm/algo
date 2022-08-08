#!/usr/local/bin/python


def shortestpath(AL,W,n,u,up):
    dist = [float('inf')] * n
    pred = [None] * n
    Q = []
    dist[u] = 0
    print('Dist: '+str(dist))
    Q.append(u)
    print('Queue: '+str(Q))
    while len(Q) != 0:
        x = Q.pop(0)
        print('* Pop '+str(x)+' and process vertices '+str(AL[x]))

        for y in AL[x]:
            t = dist[x] + W[x][AL[x].index(y)]
            if dist[y] > t:
                print('__Process: '+str(y))
                # print(f'W[x] {W[x]} y {y} W[x][AL[x].index(y)] {W[x][AL[x].index(y)]}')
                dist[y] = t
                print('__Dist: '+str(dist))
                pred[y] = x
                if y == up:
                    return(dist,pred)
                Q.append(y)
                print('__Queue: '+str(Q))
            # else:
            #     print('__Already done: '+str(y))

    return (dist,pred)
if __name__ == "__main__":

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
    W = [[1,2],[1,4,2],[4,1],[2,2,3],[2,2,1],[1,7],[3,2],[1],[7,2]]
    n = len(AL)
    u = 0
    up = 0
    [dist,pred] = shortestpath(AL,W,n,u,up)
    print(f'pred {pred} dist {dist}')
    path = []
    x = up
    l = 0 
    while x != None:

        path.append(x)
        x = pred[x]
    path.reverse()
    for i in range(len(path) - 1):
        l += W[path[i]][AL[path[i]].index(path[i+1])]
        # print(f'l {l}')
        # print(f'i {i}: path[i] {path[i]} path[i+1] {path[i+1]} W[path[{i}]] {W[path[i]]} AL[{path[i]}] {AL[path[i]]} ')
        # print(f'AL[{path[i]}].index(path[i+1]) {AL[path[i]].index(path[i+1])}')
    print('\nPath: '+str(path))
    print(f'Length: {l}')
