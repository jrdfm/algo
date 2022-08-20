#!/usr/bin/python3



def dijkstra(G, s):
    V = len(G)
    dist = [float('inf')] * V
    pred = [None] * V 
    S = []
    dist[s] = 0
    c = 0 
    Q = [(s, 0)]
    while len(S) < V:
        c += 1
        x = Q.pop(0)[0]
        while x in S:
            # print(f'pop')
            x = Q.pop(0)[0]
        for i in range(len(G[x])):
            if G[x][i]  != 0 and dist[x] + G[x][i] < dist[i]:
                dist[i] = dist[x] + G[x][i]
                # print(f'Q {Q}')
                # idx = insort(Q,dist[i])
                # print(f'Q,dist[i] {Q,dist[i]} idx {idx}')
                # Q.insert(idx,(i,dist[i]))
                Q.append((i, dist[i]))
                Q = sorted(Q, key= lambda x :x[1])
                pred[i] = x
        S.append(x)
        print(f'{50 * "*"} \n i{c}:\n S {S} \n Dist {dist}\n pred {pred}')
    return pred


def insort(A,x):
    L = 0
    R = len(A)-1
    while L <= R:
        C = (L+R)//2
        if x < A[C][1]:
            R = C-1
        if x > A[C][1]:
            L = C+1
    return L

if __name__ == "__main__":
    
    import graphviz
    
    G = [[ 0 , 10 , 0 , 20 , 0 , 0 , 0 , 0 , 0] ,
        [ 10 , 0 , 20 , 0 ,100 , 0 , 0 , 0 , 0] ,
        [ 0 , 20 , 0 , 0 , 0 , 50 , 0 , 0 , 0] ,
        [ 20 , 0 , 0 , 0 , 30 , 0 ,120 , 0 , 0] ,
        [ 0 ,100 , 0 , 30 , 0 , 70 ,100 , 30 , 80] ,
        [ 0 , 0 , 60 , 0 , 70 , 0 , 0 , 0 ,100] ,
        [ 0 , 0 , 0 ,120 ,100 , 0 , 0 , 10 , 0] ,
        [ 0 , 0 , 0 , 0 , 30 , 0 , 10 , 0 , 20] ,
        [ 0 , 0 , 0 , 0 , 80 ,100 , 0 , 20 , 0]]

    D = [[ 0 , 10 , 0 , 5 , 0 , 0 , 0 , 0 , 0] ,
        [ 10 , 0 , 10 , 0 ,20 , 0 , 0 , 0 , 0] ,
        [ 0 , 10 , 0 , 0 , 0 , 25 , 0 , 0 , 0] ,
        [ 5 , 0 , 0 , 0 , 30 , 0 ,10 , 0 , 0] ,
        [ 0 ,20 , 0 , 30 , 0 , 10 ,0 , 50 , 0] ,
        [ 0 , 0 , 25 , 0 , 10 , 0 , 0 , 0 ,60] ,
        [ 0 , 0 , 0 ,10 ,0 , 0 , 0 , 5 , 0] ,
        [ 0 , 0 , 0 , 0 , 50 , 0 , 5 , 0 , 10] ,
        [ 0 , 0 , 0 , 0 , 0 ,60 , 0 , 10 , 0]]

    pred = dijkstra(G,0)
    p = dijkstra(D,4)
    print(f'\n\npred {pred} \n p {p}')


    g = graphviz.Graph('G')

    for i in range(len(pred)):
        if pred[i] is not None:
            g.edge(str(pred[i]),str(i), label=str(G[i][pred[i]]))
        
    g.render("G", format="png")


    d = graphviz.Graph('D')

    for i in range(len(p)):
        if p[i] is not None:
            d.edge(str(p[i]),str(i), label=str(D[i][p[i]]))
        
    d.render("D", format="png")