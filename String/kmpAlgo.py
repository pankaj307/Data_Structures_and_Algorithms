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

def KMP(string,pattern):
    n = len(string)
    m = len(pattern)
    lps = ['-']*n
    fillLPF_efficient(pattern,lps)
    i, j = 0, 0
    while i < n:
        if pattern[j] == string[i]:
            i += 1
            j += 1
        if j == m:
            print(i-j)
            j = lps[j-1]
        elif i < n and pattern[j] != string[i]:
                if j == 0:
                    i += 1
                else:
                    j = lps[j-1]

string = 'ababcababaad'
pattern = 'ababa'
KMP(string,pattern)