# # Union in two sorted arrays
# # Time : (n+m)   Space : O(1)

def union(a, b, n, m):
    i, j = 0, 0
    l = []
    while i < n and j < m:
        if i > 0 and a[i-1] == a[i]:
            i+=1
            continue
        if j > 0 and b[j-1] == b[j]:
            j+=1
            continue
        if a[i] < b[j]:
            l.append(a[i])
            i+=1
        elif a[i] > b[j]:
            l.append(b[j])
            j+=1
        else:
            l.append(a[i])
            i+=1
            j+=1
    while i < n:
        if i == 0 or a[i] != a[i-1]:
            l.append(a[i])
        i+=1
    while j < m:
        if j == 0 or b[j] != b[j-1]:
            l.append(b[j])
        j+=1
    return l

a = [3,8,8]
b = [2,8,8,10,15]
print(union(a,b,len(a),len(b)))