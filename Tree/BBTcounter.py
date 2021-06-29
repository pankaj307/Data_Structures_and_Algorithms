
# # Maximum number of balanced tree possible of height h

def solve(n):
    if n == 1 or n == 0:
        return 1
    x = solve(n-1)
    y = solve(n-2)

    ans = x*x + 2*x*y
    return ans

def solveI(n):
    dp = [-1 for i in range(n+1)]
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n+1):
        x = dp[i-1]
        y = dp[i-2]
        dp[i] = x*x + 2*x*y
    # print(dp)
    return dp[-1]

def solveII(h):
    m = 1000000007
    x = 1
    y = 1
    for i in range(2, h+1):
        a = ((x%m) * (x%m))%m
        b = ((x%m) * (y%m))%m
        c = ((2%m) * (b%m))%m
        t = (a%m + c%m)%m
        y = x
        x = t
    return x

n = 5
print(solve(n))
print(solveI(n))
print(solveII(n))