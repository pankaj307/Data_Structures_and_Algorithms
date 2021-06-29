# # Time: O(n), Space: O(n)

def longestSubArrayWithGivenSum(arr,n,sm):
    s = {}
    prefixSum = 0
    res = 0
    for i in range(n):
        prefixSum += arr[i]
        if prefixSum == sm:
            res = i+1
        elif prefixSum-sm in s:
            res = max(res,i-s[prefixSum-sm])
        if prefixSum not in s:
            s[prefixSum] = i
    return res


arr = [8,3,1,5,-6,6,2,2]
n = len(arr)
sm = 4
print(longestSubArrayWithGivenSum(arr,n,sm))



#-------------------------------------------------------


# # Time: O(n), Space: O(n)

def longestSubArrayWithEqualZeroAndOne(arr,n,sm):
    s = {}
    prefixSum = 0
    res = 0
    for i in range(n):
        prefixSum += arr[i]
        if prefixSum == sm:
            res = i+1
        elif prefixSum-sm in s:
            res = max(res,i-s[prefixSum-sm])
        if prefixSum not in s:
            s[prefixSum] = i
    return res


arr = [1,0,1,1,1,0,0]
n = len(arr)
for i in range(n):
    if arr[i] == 0:
        arr[i] = -1
sm = 0
print(longestSubArrayWithEqualZeroAndOne(arr,n,sm))