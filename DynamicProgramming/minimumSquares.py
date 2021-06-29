import math, sys
sys.setrecursionlimit(10000)

def minSquares(n):
    if n == 0:
        return 0
    ans = sys.maxsize
    root = int(math.sqrt(n))
    for i in range(1, root + 1):
        temp = 1 + minSquares(n - (i**2))
        ans = min(ans, temp)
    return ans

def minSquaresDP(n,dp):
    if n == 0:
        return 0

    a = sys.maxsize
    root = int(math.sqrt(n))
    for i in range(1,root+1):
        temp = n-(i**2)
        if dp[temp] == -1:
            val = minSquaresDP(n-(i**2),dp)
            dp[temp] = val
            cur = 1 + val
        else:
            cur = 1 + dp[temp]
        a = min(a,cur)

    return a


n = 41

# print(minSquares(n))

dp = [-1 for i in range(n+1)]
print(minSquaresDP(n,dp))