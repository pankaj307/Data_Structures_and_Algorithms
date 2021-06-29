# # Time: O(Total bits in n)
def countSet(n):
    res = 0
    while n>0:
        if n%2 != 0:
            res += 1
        n = n//2
    return res

# # Time: O(Total bits in n)
def countSet_2(n):
    res = 0
    while n>0:
        if n&1 == 1:
            res += 1
        n = n>>1
    return res

# # Time: O(Total set bits in n)
def countSet_3(n):
    res = 0
    while n>0:
        n = n&(n-1)
        res += 1
    return res

n = 7
print(countSet(n))
print(countSet_2(n))
print(countSet_2(n))