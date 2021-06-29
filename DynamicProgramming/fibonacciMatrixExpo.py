
# # Time: O(log n)

def multiply(a, m):
    mod = 1000000007
    
    fValue = ((a[0][0]*m[0][0])%mod + (a[0][1]*m[1][0])%mod)%mod
    sValue = ((a[0][0]*m[0][1])%mod + (a[0][1]*m[1][1])%mod)%mod
    tValue = ((a[1][0]*m[0][0])%mod + (a[1][1]*m[1][0])%mod)%mod
    lValue = ((a[1][0]*m[0][1])%mod + (a[1][1]*m[1][1])%mod)%mod

    a[0][0] = fValue
    a[0][1] = sValue
    a[1][0] = tValue
    a[1][1] = lValue

def power(a, n):
    if n == 0 or n == 1:
        return
    
    power(a, n//2)
    multiply(a, a)

    if n%2 != 0:
        m = [[1,1],[1,0]]
        multiply(a, m)

def fib(n):
    n += 1
    a = [[1, 1], [1, 0]]
    if n == 0:
        return 0
    
    power(a, n-1)
    return a[0][0]

import math
 
def fibo(n):
    mod = 1000000007
    phi = (1 + math.sqrt(5)) / 2
    return (round(pow(phi, n) / math.sqrt(5)))%mod



n = 100
print(fib(n))
print(fibo(n))