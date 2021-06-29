def coinChange(sm, coins, n):
    if sm == 0:
        return 1
    if n == 0:
        return 0
    ans = coinChange(sm, coins, n-1)
    if coins[n-1] <= sm:
        ans += coinChange(sm-coins[n-1], coins, n)
    return ans


def coinChangeDPI(sm, coins, n):
    dp = [[0 for i in range(n+1)] for j in range(sm+1)]
    for i in range(len(dp[0])):
        dp[0][i] = 1
    for i in range(1, sm+1):
        for j in range(1, n+1):
            dp[i][j] = dp[i][j-1]
            if coins[j-1] <= i:
                dp[i][j] += dp[i-coins[j-1]][j]
    return dp[sm][n]


coins = [1, 2, 3]
n = len(coins)
sm = 4
print(coinChange(sm, coins, n))

print(coinChangeDPI(sm, coins, n))
