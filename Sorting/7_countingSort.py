def countSort(arr,n,k):
    countArr = [0]*k

    for i in range(n):
        c = arr.count(arr[i])
        countArr[arr[i]] = c

    for i in range(1,k):
        countArr[i] = countArr[i]+countArr[i-1]

    op = ['-']*n
    for i in range(n-1,-1,-1):
        op[countArr[arr[i]]-1] = arr[i]
        countArr[arr[i]] -= 1

    for i in range(n):
        arr[i] = op[i]

arr = [1,4,4,1,0,1]
k = 5
countSort(arr,len(arr),k)
print(arr)
