def maxHeapify(arr,n,i):
    largest = i
    left = 2*i+1
    right = 2*i+2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[largest],arr[i] = arr[i],arr[largest]
        maxHeapify(arr,n,largest)

def buildHeap(arr,n):
    for i in range((n-2)//2,-1,-1):
        maxHeapify(arr,n,i)

def heapSort(arr,n):
    buildHeap(arr,n)
    for i in range(n-1,0,-1):
        arr[0],arr[i] = arr[i],arr[0]
        maxHeapify(arr,i,0)

arr = [10,15,50,4,20]
heapSort(arr,len(arr))
print(arr)
