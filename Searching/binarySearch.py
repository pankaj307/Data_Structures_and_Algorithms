# # Iterative code  Time : O(log(n)), Space : O(1)

def binarySearch(arr,low,high,x):
    while low <= high:
        mid = low + (high-low)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            high = mid-1
        else:
            low = mid+1
    return -1

arr = [10,20,30,40,50,60,70]
x = 25
print(binarySearch(arr,0,len(arr)-1,x))


#------------------------------------------

# # Recursive code   Time : O(log(n)),  Space : O(log(n))

def binarySearch_2(arr,low,high,x):
    if low > high:
        return -1
    mid = low + (high-low)//2
    if arr[mid] == x:
        return mid
    elif arr[mid] > x:
        return binarySearch_2(arr,low,mid-1,x)
    else:
        return binarySearch_2(arr,mid+1,high,x)

arr = [10,20,30,40,50,60,70]
x = 25
print(binarySearch_2(arr,0,len(arr)-1,x))