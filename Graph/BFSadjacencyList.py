import queue
class Graph:
    def __init__(self, data):
        self.nVertices = data
        self.adjList = [[] for i in range(data)]

    def addEdge(self, v1, v2):
        self.adjList[v1].append(v2)
        self.adjList[v2].append(v1)
    
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

    # # First version, when starting is given and graph is connected
    def __bfs(self, s, visited):
        # visited = [False for i in range(self.nVertices)]
        q = queue.Queue()
        q.put(s)
        visited[s] = True
        while q.empty() == False:
            u = q.get()
            print(u)
            for i in self.adjList[u]:
                if visited[i] == False:
                    visited[i] = True
                    q.put(i)
        print()

    
    # # Second version, when starting is not given and graph
    # # may be disconnected
    def bfsDis(self):
        visited = [False for i in range(self.nVertices)]
        for i in range(self.nVertices):
            if visited[i] == False:
                self.__bfs(i, visited)
    



g = Graph(7)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(2, 3)
# g.addEdge(3, 4)
g.addEdge(4, 5)
g.addEdge(4, 6)
g.addEdge(5, 6)
print(g)
g.bfsDis()