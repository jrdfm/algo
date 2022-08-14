#!/usr/bin/python3

import heapq


class PriorityQueue:    
    def __init__(self):
        self._data = []
        self._len = 0    
    def push(self, node):
        heapq.heappush(self._data, (node.dist, node))
        self._len += 1
    def pop(self):
        print(f'fffffffffff')
        return heapq.heappop(self._data)[1]
    def peak(self):
        return self._data[0]