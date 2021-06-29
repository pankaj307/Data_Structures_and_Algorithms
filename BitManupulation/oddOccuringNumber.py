# # One only odd occuring
def oddOccur(arr):
    res = 0
    for i in arr:
        res = res^i
    return res

arr = [4,3,4,4,4,5,5,5,5,3,3]
print(oddOccur(arr))


# # Two odd occuring
def oddOccur_2(arr):
    xor = 0
    res1, res2 = 0, 0
    for i in range(len(arr)):
        xor ^= arr[i]
    s = xor & ~(xor-1)
    for i in range(len(arr)):
        if arr[i]&s != 0:
            res1 ^= arr[i]
        else:
            res2 ^= arr[i]
    return [res1,res2]

arr = [3,4,3,4,8,4,4,32,7,7]
print(oddOccur_2(arr))