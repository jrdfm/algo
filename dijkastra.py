#!/usr/bin/python3



def dijkstra(G, s):
    V = len(G)
    dist = [float('inf')] * V
    pred = [None] * V 
    S = []
    dist[s] = 0
    
    Q = [(s, 0)]
    while len(S) < V:
        x = Q.pop(0)[0]
        while x in S:
            # print(f'pop')
            x = Q.pop(0)[0]
        for i in range(len(G[x])):
            if G[x][i]  != 0 and dist[x] + G[x][i] < dist[i]:
                dist[i] = dist[x] + G[x][i]
                Q.append((i, dist[i]))
                Q = sorted(Q, key= lambda x :x[1])
                pred[i] = x
        S.append(x)
    return pred

if __name__ == "__main__":
    
    import graphviz
    
    G = [[ 0 , 10 , 0 , 20 , 0 , 0 , 0 , 0 , 0] ,
        [ 10 , 0 , 20 , 0 ,100 , 0 , 0 , 0 , 0] ,
        [ 0 , 20 , 0 , 0 , 0 , 60 , 0 , 0 , 0] ,
        [ 20 , 0 , 0 , 0 , 30 , 0 ,120 , 0 , 0] ,
        [ 0 ,100 , 0 , 30 , 0 , 70 ,100 , 30 , 80] ,
        [ 0 , 0 , 60 , 0 , 70 , 0 , 0 , 0 ,100] ,
        [ 0 , 0 , 0 ,120 ,100 , 0 , 0 , 10 , 0] ,
        [ 0 , 0 , 0 , 0 , 30 , 0 , 10 , 0 , 20] ,
        [ 0 , 0 , 0 , 0 , 80 ,100 , 0 , 20 , 0]]

    pred = dijkstra(G,0)

    print(f'pred {pred}')


    g = graphviz.Graph('G')

    for i in range(len(pred)):
        if pred[i] is not None:
            g.edge(str(pred[i]),str(i))
        
    g.render("G", format="png")
