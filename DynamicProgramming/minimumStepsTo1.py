import sys

def minSteps(n):
    if n == 1:
        return 0
    a1 = sys.maxsize
    if n % 3 == 0:
        a1 = minSteps(n//3)
    a2 = sys.maxsize
    if n % 2 == 0:
        a2 = minSteps(n//2)
    a3 = minSteps(n-1)
    return 1 + min(a1, a2, a3)

def minStepsDP(n,dp):
    if n == 1:
        return 0

    a1 = sys.maxsize
    if n%3 == 0:
        if dp[n//3] == -1:
            a1 = minStepsDP(n//3,dp)
            dp[n//3] = a1
        else:
            a1 = dp[n//3]

    a2 = sys.maxsize
    if n%2 == 0:
        if dp[n//2] == -1:
            a2 = minStepsDP(n//2,dp)
            dp[n//2] = a2
        else:
            a2 = dp[n//2]

    if dp[n-1] == -1:
        a3 = minStepsDP(n-1,dp)
        dp[n-1] = a3
    else:
        a3 = dp[n-1]

    return 1 + min(a1,a2,a3)



n = 20
print(minSteps(n))

dp = [-1 for i in range(n+1)]
print(minStepsDP(n,dp))
print(dp)