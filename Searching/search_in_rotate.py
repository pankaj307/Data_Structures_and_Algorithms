# # Search element in sorted array which is rotared(clock-wise or 
# # anti-clock-wise) by some elements

def search_in_rotate(arr,n,x):
    low = 0
    high = n-1
    while low <= high:
        mid = low + (high-low)//2
        if arr[mid] == x:
            return mid
        if arr[low] < arr[mid]:
            if x >= arr[low] and x < arr[mid]:
                high = mid-1
            else:
                low = mid+1
        else:
            if x > arr[mid] and x <= arr[high]:
                low = mid+1
            else:
                high = mid-1
    return -1

arr = [10,20,40,60,5,8]
x = 8
print(search_in_rotate(arr,len(arr),x))