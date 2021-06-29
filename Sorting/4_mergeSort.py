def merge(a,b):
    i, j = 0, 0
    arr = []
    while i < len(a) and j < len(b):
        if b[j] <= a[i]:
            arr.append(b[j])
            j+=1
        else:
            arr.append(a[i])
            i+=1
    arr += (b[j:]+a[i:])
    return arr

# a = [10,15,20,40]
# b = [5,6,6,10,15]
# print(merge(a,b))

def mergeSort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    op1 = mergeSort(arr[:mid])
    op2 = mergeSort(arr[mid:])
    res = merge(op1,op2)
    return res

arr = [10,8,4,6,1,0]
print(mergeSort(arr))