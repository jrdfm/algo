#!/usr/bin/python3
import math
import heapq
from PQ import PriorityQueue

class Node:    
    def __init__(self,i,d):
        self.index = i
        self.dist = d
    
    def idx(self):
        return self.index
    def __str__(self):
        return f'i: {self.index}, d: {self.dist}'

def dijkstra(G, s):
    V = len(G)
    dist = [float('inf')] * V
    pred = [None] * V 
    S = []
    dist[s] = 0
    
    Q = PriorityQueue() # Create Priority queue
    Q.push(Node(s, dist[s]))
    # Q = dist.copy()
    # heapq.heapify(Q)

    # print(f'Q {Q}')
    while len(S) < V:
        x = Q.pop().idx()
        while x in S:
            print(f'pop')
            x = Q.pop().idx()

        print(f'x {x} type {type(x)} dist {dist} S {S} \n ')
        for i in range(len(G[x])):
            print(f'type i {type(i)}  type dist[i] {type(dist[i])} Q len {Q._len}')
            if G[x][i]  != 0 and dist[x] + G[x][i] < dist[i]:
                dist[i] = dist[x] + G[x][i]

                Q.push(Node(i, dist[i]))
                pred[i] = x
        S.append(x)


if __name__ == "__main__":

    G = [[ 0 , 10 , 0 , 20 , 0 , 0 , 0 , 0 , 0] ,
        [ 10 , 0 , 20 , 0 ,100 , 0 , 0 , 0 , 0] ,
        [ 0 , 20 , 0 , 0 , 0 , 60 , 0 , 0 , 0] ,
        [ 20 , 0 , 0 , 0 , 30 , 0 ,120 , 0 , 0] ,
        [ 0 ,100 , 0 , 30 , 0 , 70 ,100 , 30 , 80] ,
        [ 0 , 0 , 60 , 0 , 70 , 0 , 0 , 0 ,100] ,
        [ 0 , 0 , 0 ,120 ,100 , 0 , 0 , 10 , 0] ,
        [ 0 , 0 , 0 , 0 , 30 , 0 , 10 , 0 , 20] ,
        [ 0 , 0 , 0 , 0 , 80 ,100 , 0 , 20 , 0]]
    dijkstra(G,0)