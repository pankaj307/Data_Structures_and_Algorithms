# #Recursive
def lcs(s1, s2, i, j):
    if len(s1) == i or len(s2) == j:
        return 0
    if s1[i] == s2[j]:
        ans = 1 + lcs(s1, s2, i+1, j+1)
    else:
        ans1 = lcs(s1, s2, i+1, j)
        ans2 = lcs(s1, s2, i, j+1)
        ans = max(ans1, ans2)
    return ans

# #Recursive DP
def lcsDP(s1, s2, i, j, dp):
    if len(s1) == i or len(s2) == j:
        return 0
    if s1[i] == s2[j]:
        if dp[i+1][j+1] == -1:
            temp = lcsDP(s1, s2, i+1, j+1, dp)
            dp[i+1][j+1] = temp
            ans = 1 + temp
        else:
            ans = 1 + dp[i+1][j+1]
    else:
        if dp[i+1][j] == -1:
            ans1 = lcsDP(s1, s2, i+1, j, dp)
            dp[i+1][j] = ans1
        else:
            ans1 = dp[i+1][j]
        if dp[i][j+1] == -1:
            ans2 = lcsDP(s1, s2, i, j+1, dp)
            dp[i][j+1] = ans2
        else:
            ans2 = dp[i][j+1]
        ans = max(ans1, ans2)
    return ans

# #Iterative DP
def lcsDPI(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if s1[i] == s2[j]:
                dp[i][j] = 1 + dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])
    return dp[0][0]
    

s1 = 'abedgjc'
s2 = 'bmdgsc'
print(lcs(s1, s2, 0, 0))

n = len(s1)
m = len(s2)
dp = [[-1 for i in range(m+1)] for j in range(n+1)]
print(lcsDP(s1, s2, 0, 0, dp))

print(lcsDPI(s1, s2))