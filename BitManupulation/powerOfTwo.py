def powerOfTwo(n):
    if n == 0:
        return False
    while n != 1:
        if n%2 != 0:
            return False
        n = n//2
    return True

def powerOfTwo_2(n):
    if n == 0:
        return False
    return (n&(n-1) == 0)

n = 16
print(powerOfTwo(n))
print(powerOfTwo_2(n))