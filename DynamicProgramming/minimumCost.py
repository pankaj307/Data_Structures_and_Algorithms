import sys

def minCostPath(arr,i,j,n,m):
    if i == n-1 and j == m-1:
        return arr[i][j]
    
    if i >= n or j >= m:
        return sys.maxsize
    
    a1 = minCostPath(arr,i,j+1,n,m)
    a2 = minCostPath(arr,i+1,j,n,m)
    a3 = minCostPath(arr,i+1,j+1,n,m)
    return arr[i][j] + min(a1,a2,a3)

arr = [[1,5,11],[8,13,12],[2,3,7],[15,16,18]]
print(minCostPath(arr,0,0,4,3))


def minCostPathDP(arr,i,j,n,m,dp):
    if i == n-1 and j == m-1:
        return arr[i][j]
    
    if i >= n or j >= m:
        return sys.maxsize
    
    if dp[i][j+1] == sys.maxsize:
        a1 = minCostPathDP(arr,i,j+1,n,m,dp)
        dp[i][j+1] = a1
    else:
        a1 = dp[i][j+1]
    
    if dp[i+1][j] == sys.maxsize:
        a2 = minCostPathDP(arr,i+1,j,n,m,dp)
        dp[i+1][j] == a2
    else:
        a2 = dp[i+1][j]
    
    if dp[i+1][j+1] == sys.maxsize:
        a3 = minCostPathDP(arr,i+1,j+1,n,m,dp)
        dp[i+1][j+1] = a3
    else:
        a3 = dp[i+1][j+1]

    return arr[i][j] + min(a1,a2,a3)


arr = [[1,5,11],[8,13,12],[2,3,7],[15,16,18]]
n = 4
m = 3
dp = [[sys.maxsize for j in range(m+1)] for i in range(n+1)]
print(minCostPathDP(arr,0,0,n,m,dp))


def minCostPathDPI(arr,n,m):
    dp = [[sys.maxsize for j in range(m+1)] for i in range(n+1)]
    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):
            if i == n-1 and j == m-1:
                dp[i][j] = arr[i][j]
            else:
                dp[i][j] = arr[i][j] + min(dp[i][j+1],dp[i+1][j],dp[i+1][j+1])
    print(dp)
    return dp[0][0]


arr = [[1,5,11],[8,13,12],[2,3,7],[15,16,18]]
print(minCostPathDPI(arr,4,3))