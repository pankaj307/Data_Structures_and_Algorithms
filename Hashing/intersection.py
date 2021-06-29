# # Naive solution Time: O(n*(n+m))

def intersection_length(a,b,n,m):
    res = 0
    for i in range(n):
        flag = False
        for j in range(i):
            if a[j] == a[i]:
                flag = True
                break
        if flag == True:
            continue
        for j in range(m):
            if a[i] == b[j]:
                res += 1
                break
    return res


a = [10,15,20,15,30,30,5]
n = len(a)
b = [30,5,30,80]
m = len(b)
print(intersection_length(a,b,n,m))



# # Time: O(m+n), Space: O(n)


def intersection_length_2(a,b,n,m):
    s = set()
    for i in range(n):
        s.add(a[i])
    res = 0
    for j in range(m):
        if (b[j] in s):
            res += 1
            s.remove(b[j])
    return res


a = [10,15,20,15,30,30,5]
n = len(a)
b = [30,5,30,80]
m = len(b)
print(intersection_length_2(a,b,n,m))



# # Pre-Defined functions

a = [10,15,20,15,30,30,5]
b = [30,5,30,80]

A = set(a)
B = set(b)

c = A & B
print(len(c),c)

d = A.intersection(B)
print(len(d),d)