import sys

def mnJumps(arr, n):
    if n == 1:
        return 0
    
    res = sys.maxsize
    for i in range(n-1):
        if i + arr[i] >= n-1:
            ans = mnJumps(arr, i+1)
            res = min(res, 1+ans)
    return res

def mnJumpsDP(arr, n, dp):
    if n == 1:
        return 0
    
    res = sys.maxsize
    for i in range(n-1):
        if i+arr[i] >= n-1:
            if dp[i+1] == -1:
                ans = mnJumpsDP(arr, i+1, dp)
                dp[i+1] = ans
            else:
                ans = dp[i+1]
            res = min(res, 1+ans)
    return res

def mnJumpsDPI(arr, n):
    dp = [sys.maxsize for i in range(n)]
    dp[0] = 0
    for i in range(1, n):
        for j in range(i):
            if j+arr[j] >= i:
                dp[i] = min(dp[i], dp[j]+1)
    print(dp)
    return dp[n-1]

def mnJumpsOP(arr, n):
    if n == 1:
        return 0
    if arr[0] == 0:
        return -1
    reach = arr[0]
    step = arr[0]
    jump = 1
    for i in range(1, n):
        if i == n-1:
            return jump
        reach = max(reach, i+arr[i])
        step -= 1
        if step == 0:
            jump += 1
            if i >= reach:
                return -1
            step = reach-i

    




arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
n = len(arr)
print(mnJumps(arr, n))

dp = [-1 for i in range(n)]
print(mnJumpsDP(arr, n, dp))
print(dp)
print(mnJumpsDPI(arr, n))

print(mnJumpsOP(arr, n))