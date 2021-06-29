def count_1s(arr,low,high,x):
    n = len(arr)
    while low <= high:
        mid = low + (high-low)//2
        if arr[mid] == 0:
            low = mid+1
        else:
            if mid == 0 or arr[mid-1] == 0:
                return n-mid
            else:
                high = mid-1
    return 0

arr = [0,0,1,1,1,1,1]
x = 1
print(count_1s(arr,0,len(arr)-1,1))