# # Time: O(n), Space: O(n)

def pairWithGivenSum(arr,s):
    s = set()
    for i in range(len(arr)):
        if (sm-arr[i]) in s:
            return True
        s.add(arr[i])
    return False


# arr = [3,2,8,15,-8]
# sm = 17
arr = [11,5,6]
sm = 10
print(pairWithGivenSum(arr,sm))