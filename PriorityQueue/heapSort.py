def downHeapify(arr, i, n):
    parentInd = i
    leftChildInd = 2*parentInd + 1
    rightChildInd = 2*parentInd + 2

    while leftChildInd < n:
        minInd = parentInd
        if arr[minInd] > arr[leftChildInd]:
            minInd = leftChildInd
        if rightChildInd < n and arr[minInd] > arr[rightChildInd]:
            minInd = rightChildInd
        if minInd == parentInd:
            return
        arr[minInd], arr[parentInd] = arr[parentInd], arr[minInd]
        parentInd = minInd
        leftChildInd = 2*parentInd + 1
        rightChildInd = 2*parentInd + 2
    return

def heapSort(arr):
    n = len(arr)
    for i in range(n//2-1, -1, -1):
        downHeapify(arr, i, n)
    
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        downHeapify(arr, 0, i)
    
    return


arr = [12,3,2,5,7,4,1,9,6,]
heapSort(arr)
print(arr[::-1])