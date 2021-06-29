class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None

class Graph:
    def __init__(self, nVertives):
        self.nVertices = nVertives
        self.graph = [None]*nVertives

    def addEdge(self, v1, v2):
        node = AdjNode(v2)
        node.next = self.graph[v1]
        self.graph[v1] = node

        node = AdjNode(v1)
        node.next = self.graph[v2]
        self.graph[v2] = node
    
    # def removeEdge(self, v1, v2):
    #     if self.containEdge(v1, v2) == False:
    #         return
    #     self.adjList[v1].remove(v2)
    #     self.adjList[v2].remove(v1)
    
    # def containEdge(self, v1, v2):
    #     return True if v2 in self.adjList[v1] else False
    #     # if v2 in self.adjList[v1]:
    #     #     return True
    #     # return False
    
    def print_graph(self):
        for i in range(self.nVertices):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")

g = Graph(5)
g.addEdge(0, 1)
g.addEdge(0, 4)
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(2, 3)
g.addEdge(3, 4)
g.print_graph()
