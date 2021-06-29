def firstOcc_2(arr,low,high,x):
    while low <= high:
        mid = low + (high-low)//2
        if arr[mid] > x:
            high = mid-1
        elif arr[mid] < x:
            low = mid+1
        else:
            if mid == 0 or arr[mid-1] != arr[mid]:
                return mid
            else:
                high = mid-1
    return -1

def lastOcc_2(arr,low,high,x,n):
    while low <= high:
        mid = low + (high-low)//2
        if arr[mid] > x:
            high = mid-1
        elif arr[mid] < x:
            low = mid+1
        else:
            if mid == n-1 or arr[mid+1] != arr[mid]:
                return mid
            else:
                low = mid+1
    return -1

def countOcc(arr,x,n):
    first = firstOcc_2(arr,0,n-1,x)
    if first == -1:
        return 0
    return (lastOcc_2(arr,0,n-1,x,n)-first+1)

arr = [1,2,2,3,3,3,3,3]
x = 3
print(countOcc(arr,x,len(arr)))