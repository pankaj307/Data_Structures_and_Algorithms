def floorSqrt(n):
    low = 0
    high = n
    ans = -1
    while low <= high:
        mid = (low+high)//2
        sq = mid*mid
        if sq == n:
            return mid
        elif sq > n:
            high = mid-1
        else:
            low = mid+1
            ans = mid
    return ans

n = 10
print(floorSqrt(n))