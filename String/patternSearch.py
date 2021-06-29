def patSearch_1(s,p):             # O((n-m)*m)
    n = len(s)
    m = len(p)
    for i in range(n-m+1):
        c = 0
        for j in range(m):
            if s[i+j] != p[j]:
                break
            c+=1
        # print(j,m,c)
        if c == m:
            print(i)

s = 'ABABAB'
p = 'ABAB'
patSearch_1(s,p)


#--------------------------------------------------



# If input pattern has unique characters


def patSearch_2(s,p):
    n = len(s)
    m = len(p)
    i = 0
    while i < n-m+1:
        c = 0
        for j in range(m):
            if s[i+j] != p[j]:
                break
            c+=1
        if c == m:
            print(i)
        if j == 0:
            i+=1
        else:
            i+=j

s = 'ABCDABCE'
p = 'ABCE'
patSearch_2(s,p)