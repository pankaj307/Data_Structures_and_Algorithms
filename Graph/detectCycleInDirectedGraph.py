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
    
    def __detectCycle(self, s, visited, recSt):
        visited[s] = True
        recSt[s] = True
        for i in self.adjList[s]:
            if visited[i] == False and self.__detectCycle(i, visited, recSt):
                return True
            elif recSt[i] == True:
                return True
        recSt[s] = False
        return False
    
    def detectCycle(self):
        visited = [False for i in range(self.nVertices)]
        recSt = [False for i in range(self.nVertices)]
        for i in range(self.nVertices):
            if visited[i] == False:
                if self.__detectCycle(i, visited, recSt):
                    return True
        return False



g = Graph(6)
g.addEdge(0, 1)
g.addEdge(2, 1)
g.addEdge(2, 3)
g.addEdge(3, 4)
g.addEdge(4, 5)
g.addEdge(5, 3)

print(g)

print(g.detectCycle())