def insertionSort(arr): 
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i - 1
        while j >=0 and arr[j] > key:  
            arr[j+1] = arr[j] 
            j -= 1
        arr[j+1] = key      
    return arr
            
def bucketSort(arr,n,k): 
    mx_val = max(arr)+1
    bkt = []
    for _ in range(k):
        bkt.append([])

    for i in range(n):
        bi = (k*arr[i])//mx_val
        bkt[bi].append(arr[i])

    for i in range(k):
        bkt[i] = insertionSort(bkt[i])
        # insertionSort(bkt[i])

    ind = 0
    for i in range(k):
        for j in range(len(bkt[i])):
            arr[ind] = bkt[i][j]
            ind += 1
    # return arr

arr = [30,40,10,80,5,12,70]
k = 4
bucketSort(arr,len(arr),k)
print(arr)