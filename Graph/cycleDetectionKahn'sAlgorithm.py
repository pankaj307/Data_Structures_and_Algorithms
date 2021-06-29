import queue
class Graph:
    def __init__(self, data):
        self.nVertices = data
        self.adjList = [[] for i in range(data)]

    def addEdge(self, v1, v2):
        self.adjList[v1].append(v2)
        # self.adjList[v2].append(v1)
    
    def removeEdge(self, v1, v2):
        if self.containEdge(v1, v2) == False:
            return
        self.adjList[v1].remove(v2)
        self.adjList[v2].remove(v1)
    
    def containEdge(self, v1, v2):
        return True if v2 in self.adjList[v1] else False
        # if v2 in self.adjList[v1]:
        #     return True
        # return False
    
    def __str__(self):
        c = 0
        for i in self.adjList:
            print(c, ':', *i)
            c += 1
        return ''
    
    def cycleDetect(self):
        indegree = [0 for i in range(self.nVertices)]

        for i in self.adjList:
            for j in i:
                indegree[j] += 1
        
        q = queue.Queue()
        for i in range(self.nVertices):
            if indegree[i] == 0:
                q.put(i)
        
        count = 0
        while q.empty() == False:
            u = q.get()
            for i in self.adjList[u]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.put(i)
            count += 1
        return count != self.nVertices
        
        
g = Graph(5)
g.addEdge(0, 1)
g.addEdge(4, 1)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(3, 1)

print(g)
print(g.cycleDetect())