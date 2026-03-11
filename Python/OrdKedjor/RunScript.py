import WeightedDigraph
import DijkstraSP
import heapq
import InData

def ReadData(fnam):
    with open(fnam) as f:
        words = [w.strip() for w in f.readlines()]
    return words

def FindPaths(fnam, G):
    with open(fnam) as f:
        for line in f.readlines():
            start = line[0:5]
            goal = line[6:11]
            dsp = DijkstraSP(G, start)
            print(f"Path from {start} to {goal} {dsp.path_to(goal)}")

            # ... sök väg från start till goal här

def CreateGraph(words):
    l = len(words)
    cList = ['']*l
    for i in range(l):
        c = list(words[i])
        cList[i] = c
    for i in 

        
    


def Run(path, pair_data):
    words = ReadData(path)
    CreateGraph(words)
    wDigraf = WeightedDigraph(words)
    FindPaths(pair_data, words)


Run("Python/OrdKedjor/InData/Indata_1", "Python/OrdKedjor/InData/Ordpar_1")

print("a")
    