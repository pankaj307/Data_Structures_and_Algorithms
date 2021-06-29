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
        ele = self.pq[0]
        self.pq[0] = self.pq[self.getSize()-1]
        self.pq.pop()
        self.__percolateDown()
        return ele

def show(pq):
    for i in pq.pq:
        print(i.value, i.priority, end=' -> ')
    print()


arr = [[10, 20, 30], [5, 15, 18], [4, 9, 12]]
k = 3

pq = MinPriorityQueue()

for i in range(k):
    pq.insertMin([i, 0], arr[i][0])


# show(pq)

res = []

while True:
    ele = pq.removeMin()
    res.append(ele.priority)
    poa, poe = ele.value
    # print(poa, poe)

    if len(res) == k*k:
        break

    if poe == k-1:
        continue
    else:
        pq.insertMin([poa, poe+1], arr[poa][poe+1])
        # show(pq)
    # break
print(res)





# # Using heapq library of python


from heapq import merge
def mergeKArrays(arr, k):
    l = arr[0]
    for i in range(k-1):
        l = list(merge(l, arr[i + 1]))
    return l

arr = [[10, 20, 30], [5, 15, 18], [4, 9, 12]]
k = 3
print(mergeKArrays(arr, k))

