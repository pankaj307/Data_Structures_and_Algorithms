# # Intersection in two sorted array
# # Time : O(n+m)     Space : O(1)

def intersection(a, b, n, m):
    i, j = 0, 0
    l = []
    while i < n and j < m:
        if i > 0 and a[i-1] == a[i]:
            i+=1
            continue
        if a[i] < b[j]:
            i+=1
        elif a[i] > b[j]:
            j+=1
        else:
            l.append(a[i])
            i+=1
            j+=1
    return l

a = [1,2,2,3,4]
b = [2,2,4,6,7,8]
print(intersection(a,b,len(a),len(b)))