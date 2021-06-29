# # If array has repeated elements and retutn first occurance

# # Time :  O(log(n)),  Space : O(log(n))

def firstOcc_1(arr,low,high,x):
    if low > high:
        return -1
    mid = low + (high-low)//2
    if arr[mid] == x:
        if mid == 0 or arr[mid-1] != arr[mid]:
            return mid
        else:
            return firstOcc_1(arr,low,mid-1,x)
    elif arr[mid] > x:
        return firstOcc_1(arr,low,mid-1,x)
    else:
        return firstOcc_1(arr,mid+1,high,x)

arr = [1,10,10,10,20,20,40]
x = 20
print(firstOcc_1(arr,0,len(arr)-1,x))


#-------------------------------------------------------

# # If array has repeated elements and retutn first occurance

# # Time :  O(log(n)),  Space : O(1)

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

arr = [1,10,10,10,20,20,40]
x = 20
print(firstOcc_2(arr,0,len(arr)-1,x))