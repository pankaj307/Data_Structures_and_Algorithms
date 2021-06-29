def maximumCuts(n, x, y, z):
    if n < 0:
        return -1
    if n == 0:
        return 0
    ans1 = maximumCuts(n-x, x, y, z)
    ans2 = maximumCuts(n-y, x, y, z)
    ans3 = maximumCuts(n-z, x, y, z)
    res = max(ans1, ans2, ans3)

    if res == -1:
        return res
    return res + 1


def maximumCutsDP(n, x, y, z):
    dp = [-1 for i in range(n+1)]
    dp[0] = 0
    for i in range(1, n+1):
        if i-x >= 0:
            dp[i] = max(dp[i], dp[i-x])
        if i-y >= 0:
            dp[i] = max(dp[i], dp[i-y])
        if i-z >= 0:
            dp[i] = max(dp[i], dp[i-z])
        if dp[i] != -1:
            dp[i] += 1
    return dp[n]


n = 5
x, y, z = 1, 2, 3
print(maximumCuts(n, x, y, z))

print(maximumCutsDP(n, x, y, z))
