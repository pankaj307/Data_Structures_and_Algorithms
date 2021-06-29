import queue
class Graph:
    def __init__(self, data):
        self.nVertices = data
        self.adjList = [[] for i in range(data)]

    def addEdge(self, v1, v2, w):
        # self.adjList[v1].append(v2)
        # self.adjList[v2].append(v1)
        self.adjList[v1].append((v2, w))
    
    def __str__(self):
        c = 0
        for i in self.adjList:
            print(c, ':', *i)
            c += 1
        return ''

    def topo(self):
        indegree = [0 for i in range(self.nVertices)]

        for i in self.adjList:
            for j in i:
                indegree[j[0]] += 1
        
        q = queue.Queue()
        for i in range(self.nVertices):
            if indegree[i] == 0:
                q.put(i)
        
        res = []
        while q.empty() == False:
            u = q.get()
            print(u)
            res.append(u)
            for i in self.adjList[u]:
                indegree[i[0]] -= 1
                if indegree[i[0]] == 0:
                    q.put(i[0])
        return res
    
    def pathDAG(self, s):
        topo = self.topo()
        dist = [float('inf') for i in range(self.nVertices)]
        dist[s] = 0
        for u in topo:
            for v in self.adjList[u]:
                if dist[v[0]] > dist[u] + v[1]:
                    dist[v[0]] = dist[u] + v[1]
        print(dist)
    
        
        
g = Graph(6)
g.addEdge(0, 1, 2)
g.addEdge(0, 4, 1)
g.addEdge(1, 2, 3)
g.addEdge(4, 2, 2)
g.addEdge(4, 5, 4)
g.addEdge(2, 3, 6)
g.addEdge(5, 3, 1)

print(g)
g.pathDAG(0)