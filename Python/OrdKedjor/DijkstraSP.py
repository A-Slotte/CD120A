import heapq

class DijkstraSP:


    def __init__(self, G, s):
        # Check vikter > 0
        for e in G.V:
            if e.weight < 0:
                raise ValueError("Negative Weight")

        self.edge_to = [] * G.V
        self.dist_to = [float('inf')] * G.V #Sätter vikten till "oändliga" 
        self.dist_to[s] = 0.0 #Source har avstånd 0 till sig själv
        self.pq = []
        heapq.heappush(self.pq, (0.0, s))
        while (len(self._pq) > 0):
            dist, node = heapq.heappop(self.pq)
            if dist > self.dist_to[node]:
                 continue
            else:
                 self.relax(G, node)
            
    
    def relax(self, G, v): 
           for e in G.adj(v):
                w = e.to
                if self.dist_to[w] > self.dist_to[v] + e.weight:
                     self.dist_to[w] = self.dist_to[v] + e.weight
                     self.edge_to[w] = e
                     heapq.heappush(self.pq, (self.dist_to[w], w))
    
    def dist_to(self, v):
         return self.dist_to[v]
    
    def has_path_to(self, v):
         if self.dist_to[v] < float("inf"):
              return False
         else:
              return True
    
    def path_to(self, v):
        if not self.has_path_to:
              return None
        path = []
        edge = self.edge_to[v]
        x = v
        while x != self.s:
            x = self.edge_to[x]
            path.append(x)
        path.append(self.s)
