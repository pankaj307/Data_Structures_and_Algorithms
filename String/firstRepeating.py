def firstRepeat_1(s):
    res = float('inf')
    arr = [-1]*256
    for i in range(len(s)):
        if arr[ord(s[i])] == -1:
            arr[ord(s[i])] = i
        else:
            res = min(res,arr[ord(s[i])])
    # print(arr)
    if res == float('inf'):
        return -1
    return res

s = 'gforeks'
print(firstRepeat_1(s))

#-------------------------------------------------


def firstRepeat_2(s):
    res = float('inf')
    arr = [-1]*256
    for i in range(len(s)-1,-1,-1):
        if arr[ord(s[i])] == -1:
            # print(i,'inn')
            arr[ord(s[i])] = i
        else:
            res = i
            # print(res)
    if res == float('inf'):
        return -1
    return res

s = 'geeksforgeeks'
print(firstRepeat_2(s))