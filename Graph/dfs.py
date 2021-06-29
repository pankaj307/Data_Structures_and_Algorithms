class Graph:
    def __init__(self, nVertives):
        self.nVertices = nVertives
        self.adjMatrix = [[0 for i in range(nVertives)] for j in range(nVertives)]

    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
    
    def removeEdge(self, v1, v2):
        if self.containEdge(v1, v2) == False:
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0
    
    def containEdge(self, v1, v2):
        return True if self.adjMatrix[v1][v2] > 0 else False
    
    def __str__(self):
        for i in self.adjMatrix:
            print(i)
        return 'Done'
        # return str(self.adjMatrix)
    
    def __dfsHelper(self, sv, visited):
        print(sv)
        visited[sv] = True
        for i in range(self.nVertices):
            if self.adjMatrix[sv][i] > 0 and visited[i] == False:
                self.__dfsHelper(i, visited)
    
    def dfs(self):
        visited = [False for i in range(self.nVertices)]
        for i in range(self.nVertices):
            if visited[i] == False:
                self.__dfsHelper(i, visited)

g = Graph(7)
g.addEdge(0, 1)
g.addEdge(1, 3)
g.addEdge(2, 4)
g.addEdge(2, 3)
g.addEdge(0, 2)
g.addEdge(5, 6)
g.dfs()
