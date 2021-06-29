def longestIncreasingSubsequenceDP(arr, n):
    lis = [1 for i in range(n)]
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                lis[i] = max(lis[i], lis[j] + 1)
    res = max(lis)
    return res


def ceilInd(tail, val):
    l, r = 0, len(tail)-1
    while r > l:
        m = (l+r)//2
        if tail[m] >= val:
            r = m
        else:
            l = m+1
    return r


def lisBinarySearch(arr, n):
    tail = [arr[0]]
    for i in range(1, n):
        if arr[i] > tail[-1]:
            tail.append(arr[i])
        else:
            ind = ceilInd(tail, arr[i])
            tail[ind] = arr[i]
    print(tail)
    return len(tail)


arr = [8, 100, 150, 10, 12, 14, 110]
n = len(arr)
print(longestIncreasingSubsequenceDP(arr, n))

print(lisBinarySearch(arr, n))
