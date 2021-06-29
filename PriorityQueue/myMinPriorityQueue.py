class PQNode:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

class MinPriorityQueue:
    def __init__(self):
        self.pq = []
    
    def getSize(self):
        return len(self.pq)
    
    def isEmpty(self):
        return self.getSize() == 0
    
    def getMin(self):
        if self.isEmpty():
            return None
        return self.pq[0].value
    
    def __percolateUp(self):
        childInd = self.getSize()-1
        while childInd > 0:
            parentInd = (childInd-1)//2
            if self.pq[childInd].priority < self.pq[parentInd].priority:
                self.pq[childInd], self.pq[parentInd] = self.pq[parentInd], self.pq[childInd]
                childInd = parentInd
            else:
                break

    def insertMin(self, value, priority):
        newNode = PQNode(value, priority)
        self.pq.append(newNode)
        self.__percolateUp()
    
    def __percolateDown(self):
        parentInd = 0
        leftChildInd = 2*parentInd + 1
        rightChildInd = 2*parentInd + 2

        while leftChildInd < self.getSize():
            minInd = parentInd
            if self.pq[minInd].priority > self.pq[leftChildInd].priority:
                minInd = leftChildInd
            if rightChildInd < self.getSize() and self.pq[minInd].priority > self.pq[rightChildInd].priority:
                minInd = rightChildInd
            if minInd == parentInd:
                break
            self.pq[parentInd], self.pq[minInd] = self.pq[minInd], self.pq[parentInd]
            parentInd = minInd
            leftChildInd = 2*parentInd + 1
            rightChildInd = 2*parentInd + 2

    def removeMin(self):
        if self.isEmpty():
            return None
        ele = self.pq[0].value
        self.pq[0] = self.pq[self.getSize()-1]
        self.pq.pop()
        self.__percolateDown()
        return ele

pq = MinPriorityQueue()
pq.insertMin('A', 10)
pq.insertMin('C', 5)
pq.insertMin('B', 19)
pq.insertMin('D', 4)
for _ in range(4):
    print(pq.removeMin())