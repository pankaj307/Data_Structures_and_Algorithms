# # Time: O(n), Space: O(n)

def subArrayWithZeroSum(arr,n):
    s = {}
    prefixSum = 0
    for i in range(n):
        prefixSum += arr[i]
        if prefixSum in s:
            return True
        if prefixSum == 0:
            return True
        s[prefixSum] = i
    return False


# arr = [1,4,13,-3,-10,5]
arr = [3,-1,-2,5]
n = len(arr)
print(subArrayWithZeroSum(arr,n))


# -------------------------------------------------------------


def subArrayWithGivenSum(arr,n,sm):
    s = {}
    prefixSum = 0
    for i in range(n):
        prefixSum += arr[i]
        if prefixSum == sm:
            print('index',0,'to',i)
            return True
        if (prefixSum-sm) in s:
            print('index',s[prefixSum-sm]+1,'to',i)
            return True
        s[prefixSum] = i
    return False


arr = [1,2,3,4,5,6,7,8,9]
sm = 15
# arr = [1,2,4,7]
# sm = 3    
n = len(arr)
print(subArrayWithGivenSum(arr,n,sm))