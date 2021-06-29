# # For Sorted array only with O(n) time

def twoPointer(arr,n,x):
    i, j = 0, n-1
    while i < j:
        if arr[i]+arr[j] == x:
            return True
        elif arr[i]+arr[j] > x:
            j -= 1
        else:
            i += 1
    return False

arr = [2,4,8,9,11,12,20,30]
x = 23
print(twoPointer(arr,len(arr),x))



# # Triplet sum in O(n^2) Time

def triplet(arr,n,x):
    for i in range(n):
        if twoPointer(arr[i+1:n],len(arr[i+1:n]),x-arr[i]):
            return True
    return False

arr = [2,3,4,8,20,40]
x = 69
print(triplet(arr,len(arr),x))