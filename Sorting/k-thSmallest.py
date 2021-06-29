# # Quick Select Algorithm

def partition(arr,l,h):
    pivot = arr[h]
    j = l-1
    for i in range(l,h):
        if arr[i] <= pivot:
            j+=1
            arr[j],arr[i] = arr[i],arr[j]
    arr[j+1],arr[h] = arr[h],arr[j+1]
    return j+1

def kthSmallest(arr,n,k):
    l, r = 0, n-1
    while l <= r:
        p = partition(arr,l,r)
        if p == k-1:
            return p
        elif p > k-1:
            r = p-1
        else:
            l = p+1
    return -1

arr = [10,4,5,8,11,6,26]
k = 5
print(kthSmallest(arr,len(arr),k))