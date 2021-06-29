def mcm(p, i, j):
    if i == j:
        return 0
    minValue = float('inf')
    for k in range(i, j):
        ans1 = mcm(p, i, k)
        ans2 = mcm(p, k+1, j)
        mCost = p[i-1]*p[k]*p[j]
        curValue = ans1 + ans2 + mCost
        minValue = min(minValue, curValue)
    return minValue

def mcmDP(p, i, j, dp):
    if i == j:
        return 0
    minValue = float('inf')
    for k in range(i, j):
        if dp[i][k] == -1:
            ans1 = mcmDP(p, i, k, dp)
            dp[i][k] = ans1
        else:
            ans1 = dp[i][k]
        if dp[k+1][j] == -1:
            ans2 = mcmDP(p, k+1, j, dp)
            dp[k+1][j] = ans2
        else:
            ans2 = dp[k+1][j]
        mCost = p[i-1]*p[k]*p[j]
        curValue = ans1 + ans2 + mCost
        minValue = min(minValue, curValue)
    return minValue

p = [2,3,4,5,6]
n = len(p)-1
print(mcm(p, 1, n))

dp = [[-1 for i in range(n+1)] for j in range(n+1)]
print(mcmDP(p, 1, n, dp))