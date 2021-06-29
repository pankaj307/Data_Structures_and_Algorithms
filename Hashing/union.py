# # Naive solution Time: O((m+n)*(m+n)), Space: O(m+n)

def union_length(a,b,n,m):
    c = a+b
    res = 0
    for i in range(m+n):
        flag = False
        for j in range(i):
            if c[i] == c[j]:
                flag = True
                break
        if flag == False:
            res += 1
    return res

a = [15,20,5,15]
n = len(a)
b = [15,15,15,20,10]
m = len(b)
print(union_length(a,b,n,m))



# # Time: O(m+n), Space: O(m+n)


def union_length_2(a,b,n,m):
    s = set()
    for i in a:
        s.add(i)
    for j in b:
        s.add(j)
    return len(s)


a = [15,20,5,15]
n = len(a)
b = [15,15,15,20,10]
m = len(b)
print(union_length_2(a,b,n,m))


# # Pre-Defined functions


a = set([15,20,5,15])
b = set([15,15,15,20,10])

c = a | b
print(len(c),c)

d = a.union(b)
print(len(d),d)