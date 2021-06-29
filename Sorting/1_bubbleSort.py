def bubbleSort(arr,n):
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

arr = [2,10,8,7]
bubbleSort(arr,len(arr))
print(arr)






## For sorted array or almost sorted array

def optimizedBubbleSort(arr,n):
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if swapped == False:
            break

arr = [10,8,20,5]
optimizedBubbleSort(arr,len(arr))
print(arr)