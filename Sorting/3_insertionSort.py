def insertionSort(arr,n):
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key

arr = [50,20,40,60,10,30]
insertionSort(arr,len(arr))
print(arr)