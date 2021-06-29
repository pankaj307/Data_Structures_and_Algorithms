class PQNode:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

class MaxPriorityQueue:
    def __init__(self):
        self.pq = []

    def getSize(self):
        return len(self.pq)
    
    def isEmpty(self):
        return self.getSize() == 0
    
    def getMax(self):
        if self.isEmpty():
            return None
        return self.pq[0].value
    
    def __percolateUp(self):
        childInd = self.getSize()-1
        while childInd > 0:
            parentInd = (childInd-1)//2
            if self.pq[childInd].priority > self.pq[parentInd].priority:
                self.pq[childInd], self.pq[parentInd] = self.pq[parentInd], self.pq[childInd]
                childInd = parentInd
            else:
                break

    def insertMax(self, value, priority):
        newNode = PQNode(value, priority)
        self.pq.append(newNode)
        self.__percolateUp()
    
    def __percolateDown(self):
        parentInd = 0
        leftChildInd = 2*parentInd + 1
        rightChildInd = 2*parentInd + 2

        while leftChildInd < self.getSize():
            maxInd = parentInd
            if self.pq[maxInd].priority < self.pq[leftChildInd].priority:
                maxInd = leftChildInd
            if rightChildInd < self.getSize() and self.pq[maxInd].priority < self.pq[rightChildInd].priority:
                maxInd = rightChildInd
            
            if maxInd == parentInd:
                break
            self.pq[parentInd], self.pq[maxInd] = self.pq[maxInd], self.pq[parentInd]
            parentInd = maxInd
            leftChildInd = 2*parentInd + 1
            rightChildInd = 2*parentInd + 2 
    
    def removeMax(self):
        if self.isEmpty():
            return None
        ele = self.pq[0].value
        self.pq[0] = self.pq[self.getSize()-1]
        self.pq.pop()
        self.__percolateDown()
        return ele


pq = MaxPriorityQueue()
pq.insertMax('A', 10)
pq.insertMax('C', 5)
pq.insertMax('B', 19)
pq.insertMax('D', 4)
for _ in range(4):
    print(pq.removeMax())