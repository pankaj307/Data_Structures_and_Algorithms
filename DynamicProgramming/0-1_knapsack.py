def knapsack(w, val, wt, n, i):
    if i == n:
        return 0

    if wt[i] > w:
        ans = knapsack(w, val, wt, n, i+1)
    else:
        ans1 = val[i] + knapsack(w-wt[i], val, wt, n, i+1)
        ans2 = knapsack(w, val, wt, n, i+1)
        ans = max(ans1, ans2)
    return ans

def showDP(arr):
    for i in range(len(arr)):
        print(arr[i])
    print()

def knapsackDPI(w, val, wt):
    n = len(val)
    dp = [[0 for i in range(w+1)] for j in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, w+1):
            if j < wt[i-1]:
                ans = dp[i-1][j]
            else:
                ans1 = val[i-1] + dp[i-1][j-wt[i-1]]
                ans2 = dp[i-1][j]
                ans = max(ans1, ans2)
            dp[i][j] = ans
            # print('ind ->', i, 'weight ->', j)
            # showDP(dp)
    # showDP(dp)
    return dp[n][w]

def knapsackDP(w, val, wt, n, dp):
    if n == 0 or w == 0:
        return 0
    if dp[n][w] != -1:
        return dp[n][w]
    if wt[n-1] > w:
        ans = knapsackDP(w, val, wt, n-1, dp)
    else:
        ans1 = val[n-1] + knapsackDP(w-wt[n-1], val, wt, n-1, dp)
        ans2 = knapsackDP(w, val, wt, n-1, dp)
        ans = max(ans1, ans2)
    dp[n][w] = ans
    return dp[n][w]

val = [200, 300, 100]
wt = [3, 4, 5]
w = 9
n = len(val)
print(knapsack(w, val, wt, n, 0))

print(knapsackDPI(w, val, wt))

dp = [[-1 for i in range(w + 1)] for j in range(n + 1)]
print(knapsackDP(w, val, wt, n, dp))