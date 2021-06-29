def countAndMerge(arr,l,m,r):
    n1 = m-l+1
    n2 = r-m
    left = [0]*n1
    right = [0]*n2
    for i in range(n1):
        left[i] = arr[i+l]
    for i in range(n2):
        right[i] = arr[m+i+1]
    res, i, j, k = 0, 0, 0, l
    while i < n1 and j < n2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i+=1
        else:
            arr[k] = right[j]
            j+=1
            res += n1-i
        k+=1
    while i < n1:
        arr[k] = left[i]
        i+=1
        k+=1
    while j < n2:
        arr[k] = right[j]
        j+=1
        k+=1
    return res

def countInversions(arr,l,r):
    res = 0
    if l < r:
        m = l + (r-l)//2
        res += countInversions(arr,l,m)
        res += countInversions(arr,m+1,r)
        res += countAndMerge(arr,l,m,r)
    return res

arr = [5,4,3,2,1]
print(countInversions(arr,0,len(arr)-1))