# # If array has repeated elements and retutn last occurance

# # Time :  O(log(n)),  Space : O(log(n))

def lastOcc(arr,low,high,x,n):
    mid = low + (high-low)//2
    if low > high:
        return -1
    if arr[mid] > x:
        return lastOcc(arr,low,mid-1,x,n)
    elif arr[mid] < x:
        return lastOcc(arr,mid+1,high,x,n)
    else:
        if mid == n-1 or arr[mid] != arr[mid+1]:
            return mid
        else:
            return lastOcc(arr,mid+1,high,x,n)

arr = [5,10,10,10,10,20,20]
x = 10
print(lastOcc(arr,0,len(arr)-1,x,len(arr)))


# # Time :  O(log(n)),  Space : O(1)

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

arr = [5,10,10,10,10,20,20]
x = 10
print(lastOcc_2(arr,0,len(arr)-1,x,len(arr)))