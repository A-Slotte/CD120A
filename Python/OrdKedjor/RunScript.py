import WeightedDigraph
import heapq

def ReadData(path, words):
    with open(path) as f:
        words = [w.strip() for w in f.readlines()]

def FindPaths(path):
    with open(path) as f:
        for line in f.readlines():
            start = line[0:5]
            goal = line[6:11]
            # ... sök väg från start till goal här

def Run():
    words = []
    path = "q"
    ReadData(path, words)


    