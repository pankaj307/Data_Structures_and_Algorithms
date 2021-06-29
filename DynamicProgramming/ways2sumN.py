import sys

def solve(coins, val):
    if val == 0:
        return 1
    res = 0
    for i in coins:
        if i <= val:
            ans = solve(coins, val-i)
            res += ans
    return res

def solveDP(coins, val, dp):
    if val == 0:
        return 1
    res = 0
    for i in coins:
        if i <= val:
            if dp[val-i] == -1:
                ans = solveDP(coins, val-i, dp)
                dp[val-i] = ans
            else:
                ans = dp[val-i]
            res += ans
    return res

def solveDPI(coins, val):
    dp = [0 for i in range(val+1)]
    dp[0] = 1
    for i in range(1, val+1):
        for j in coins:
            if j <= i:
                dp[i] += dp[i-j]
    print(dp)
    return dp[val]
            
        

    

coins = [1, 5, 6]
val  = 7
# coins = [1,2,3]
# val = 3
print(solve(coins, val))
dp = [-1 for i in range(val+1)]
print(solveDP(coins, val, dp))
print(dp)
print(solveDPI(coins, val))