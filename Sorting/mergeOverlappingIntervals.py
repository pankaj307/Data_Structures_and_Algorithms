# # Time: O(nlog(n))

def sortInterval(arr,n):
    arr.sort()
    res = 0
    for i in range(1,n):
        if arr[res][1] >= arr[i][0]:
            arr[res][1] = max(arr[res][1],arr[i][1])
            arr[res][0] = min(arr[res][0],arr[i][0])
        else:
            res += 1
            arr[res] = arr[i]
    print(arr[:res+1])

arr = [[5,10],[3,15],[18,30],[2,7]]
sortInterval(arr,len(arr))