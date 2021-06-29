# # Normal Fibonacci function

def fib(n):
    if n == 1 or n == 0:
        return n
    return fib(n-1)+fib(n-2)

print('1. Normal Recursive -->',fib(6))

def fib2(n):
    n1, n2 = 0, 1
    for _ in range(1,n):
        s = n1+n2
        n1 = n2
        n2 = s
    return s

print('2. Normal Iterative -->',fib2(6))

# # Fibonacci function using DP

def fibDP(n,dp):
    if n == 0 or n == 1:
        return n

    if dp[n-1] == -1:
        a1 = fibDP(n-1,dp)
        dp[n-1] = a1
    else:
        a1 = dp[n-1]

    if dp[n-2] == -1:
        a2 = fibDP(n-2,dp)
        dp[n-2] = a2
    else:
        a2 = dp[n-2]

    return a1+a2

n = 6
dp = [-1 for i in range(n+1)]
print('3. DP Recursive -->',fibDP(n,dp))
print(dp)


def fibDP2(n):
    dp = [-1 for i in range(n+1)]
    dp[0] = 0
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp)
    return dp[n]


print('4. DP Iterative -->',fibDP2(6))