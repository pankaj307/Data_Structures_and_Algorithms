def selectionSort(arr,n):
    for i in range(n-1):
        mid_ind = i
        for j in range(i+1,n):
            if arr[j] < arr[mid_ind]:
                mid_ind = j
        arr[i],arr[mid_ind] = arr[mid_ind],arr[i]

arr = [10,5,8,20,2,18]
selectionSort(arr,len(arr))
print(arr)