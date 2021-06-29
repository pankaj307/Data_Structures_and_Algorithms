# Time :- O (n^3)

def longPropPreSuf(string,n):
    # print('n-->',n)
    for length in range(n-1,0,-1):
        # print('length-->',length)
        flag = True
        for i in range(length):
            # print(i,n-length+i)
            if string[i] != string[n-length+i]:
                # print('False')
                flag = False

        if flag:
            # print('True')
            return length
    return 0    

def fillLPS(string,lps):
    for i in range(len(string)):
        lps.append(longPropPreSuf(string,i+1))

string = 'aaabaaaac'
lps = []
fillLPS(string,lps)
print(lps)


#---------------------------------------------


# Efficient, Time :- O (n)

def fillLPF_efficient(s,lps):
    n = len(s)
    length = 0
    lps[0] = 0
    i = 1
    while i < n:
        if s[i] == s[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length == 0:
                lps[i] = 0
                i += 1
            else:
                length = lps[length-1]

s = 'aaabaaaac'
lps = ['-']*len(s)
fillLPF_efficient(s,lps)
print(lps)