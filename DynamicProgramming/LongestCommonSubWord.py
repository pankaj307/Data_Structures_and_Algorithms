def showDP(arr):
    t = list(v)
    tt = ['|' for i in range(len(v)+1)]
    print('   ',*t,'.')
    print('   ',*tt)
    for i in range(len(arr)):
        try:
            print(u[i],'-',*arr[i])
        except:
            print('.','-',*arr[i])
    print()

def lcw(u,v):
    dp = [['x' for i in range(len(v)+1)] for j in range(len(u)+1)]
    showDP(dp)
    for r in range(len(u)+1):
        dp[r][len(v)] = 0
    for c in range(len(v)+1):
        dp[len(u)][c] = 0
    showDP(dp)
    maxLCW = 0
    for c in range(len(v)-1,-1,-1):
        for r in range(len(u)-1,-1,-1):
            # print(r,c)
            if u[r] == v[c]:
                dp[r][c] = 1 + dp[r+1][c+1]
            else:
                dp[r][c] = 0
            if dp[r][c] > maxLCW:
                maxLCW = dp[r][c]
    showDP(dp)
    return maxLCW

u = 'bisect'
v = 'secret'
print(lcw(u,v))