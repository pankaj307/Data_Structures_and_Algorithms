def getPerm(s):
    s = list(s)
    for i in reversed(range(len(s)-1)):
        if s[i] < s[i+1]:
            # print('start',s[i])
            for j in range(i+1,len(s)):
                # print(s[j],j,len(s))
                if s[i] > s[j] or j == len(s)-1:
                    # print(s[j])
                    s[i], s[j] = s[j], s[i]
                    t1 = s[:i+1]
                    t2 = s[i+1:]
                    s = t1+t2[::-1]
                    # print(t1,t2)
                    return s
    else:
        return 'Already on last possible premutation.'


s = 'fjadbihgec'
# 'fjadcbeghi

# s = 'dchbaeglkonmji'
# s = 'dcba'

print(getPerm(s))