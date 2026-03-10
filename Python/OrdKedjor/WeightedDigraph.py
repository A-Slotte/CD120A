# Weighted directed graph class, inspired by the corresponding Java
# class in Algorithms, 4th ed. by Sedgewick & Wayne, available at
# https://algs4.cs.princeton.edu/home/
#
# Jesper Larsson, Malmö University, 2018-2020

from collections import namedtuple

Edge = namedtuple('Edge', ['fro', 'to', 'weight'])

class WeightedDigraph:
    def __init__(self, V):
        self.__V = V
        self.__E = 0
        self.__adj = [[] for _ in range(V)]

    def addedge(self, v, w, weight):
        self.__E += 1
        self.__adj[v].append(Edge(v, w, weight))

    @property
    def V(self):
        return self.__V

    @property
    def E(self):
        return self.__E

    def adj(self, v):
        return self.__adj[v]
    
