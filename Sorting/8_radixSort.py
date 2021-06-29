def countingSort(arr,n,exp):
    countArr = [0]*10

    for i in range(n):
        countArr[(arr[i]//exp)%10] += 1

    for i in range(1,10):
        countArr[i] = countArr[i] + countArr[i-1]

    op = ['-']*n
    for i in range(n-1,-1,-1):
        op[countArr[(arr[i]//exp)%10]-1] = arr[i]
        countArr[(arr[i]//exp)%10] -= 1

    for i in range(n):
        arr[i] = op[i]

def radixSort(arr,n):
    mx = max(arr)
    exp = 1
    while mx/exp > 0:
        countingSort(arr,n,exp)
        exp *= 10

arr = [319,212,6,8,100,50] 
radixSort(arr,len(arr))
print(arr)