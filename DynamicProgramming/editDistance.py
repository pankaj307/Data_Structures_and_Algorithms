# def editDistance(s1, s2, m, n):
#     if m == 0:
#         return n
#     if n == 0:
#         return m
#     if s1[m-1] == s2[n-1]:
#         ans = editDistance(s1, s2, m-1, n-1)
#     else:
#         ans1 = editDistance(s1, s2, m, n-1)
#         ans2 = editDistance(s1, s2, m-1, n)
#         ans3 = editDistance(s1, s2, m-1, n-1)
#         ans = 1 + min(ans1, ans2, ans3)
#     return ans


# def editDistanceDPI(s1, s2, m, n):
#     dp = [[i+j for i in range(n + 1)] for j in range(m + 1)]
#     for i in range(1, m+1):
#         for j in range(1, n+1):
#             if s1[i-1] == s2[j-1]:
#                 dp[i][j] = dp[i-1][j-1]
#             else:
#                 dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
#     return dp[m][n]


# s1 = 'sunday'
# s2 = 'saturday'
# m = len(s1)
# n = len(s2)
# print(editDistance(s1, s2, m, n))

# print(editDistanceDPI(s1, s2, m, n))



def solve(s1, s2, i,  j, dp):
    if i == len(s1):
        return len(s2)-j
    if j == len(s2):
        return len(s1)-i


    if s1[i] == s2[j]:
        if dp[i+1][j+1] == -1:
            ans = solve(s1, s2, i+1, j+1, dp)
            dp[i+1][j+1] = ans
        else:
            ans = dp[i+1][j+1]
    else:
        if dp[i][j+1] == -1:
            ans1 = solve(s1, s2, i, j+1, dp)
            dp[i][j+1] = ans1
        else:
            ans1 = dp[i][j+1]
        if dp[i+1][j] == -1:
            ans2 = solve(s1, s2, i+1, j, dp)
            dp[i+1][j] = ans2
        else:
            ans2 = dp[i+1][j]
        if dp[i+1][j+1] == -1:
            ans3 = solve(s1, s2, i+1, j+1, dp)
            dp[i+1][j+1] = ans3
        else:
            ans3 = dp[i+1][j+1]
        ans = 1 + min(ans1, ans2, ans3)
    return ans

def solve2(s1, s2, i,  j):
    if i == 0:
        return j
    if j == 0:
        return i

    if s1[i-1] == s2[j-1]:
        return solve2(s1, s2, i-1, j-1)
    ans1 = solve2(s1, s2, i, j-1)
    ans2 = solve2(s1, s2, i-1, j)
    ans3 = solve2(s1, s2, i-1, j-1)
    return 1 + min(ans1, ans2, ans3)

def solveI(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[i+j for i in range(m+1)] for j in range(n+1)]
    # for i in dp:
    #     print(i)

    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                ans1 = dp[i][j-1]
                ans2 = dp[i-1][j]
                ans3 = dp[i-1][j-1]
                dp[i][j] = 1 + min(ans1, ans2, ans3)
    # for i in dp:
    #     print(i)
    return dp[n][m]

s1 = 'sa'
s2 = 'sun'
dp = [[-1 for i in range(len(s2)+1)] for j in range(len(s1)+1)]
print(solve(s1, s2, 0, 0, dp))
# for i in dp:
#     print(i)

print(solve2(s1, s2, len(s1), len(s2)))
print(solveI(s1, s2))