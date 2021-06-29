class Graph:
    def __init__(self, nVertives):
        self.nVertices = nVertives
        self.adjList = [[] for i in range(nVertives)]

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
            print(c, '->', *i)
            c += 1
        return ''
        # return str(self.adjList)

g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(1, 3)
print(g)
g.removeEdge(1, 2)
print(g)
print(g.containEdge(1,2))