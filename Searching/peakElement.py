def peak(arr,n):
    low = 0
    high = n-1
    while low <= high:
        mid = low + (high-low)//2
        if (mid == 0 or arr[mid-1] <= arr[mid]) and (mid == n-1 or arr[mid+1] <= arr[mid]):
            return mid
        if mid > 0 and arr[mid-1] >= arr[mid]:
            high = mid-1
        else:
            low = mid+1
    return -1

arr = [5,20,40,30,20,50,60]
print(peak(arr,len(arr)))