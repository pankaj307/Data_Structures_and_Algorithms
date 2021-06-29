def firstNonRepeat(s):
    res = float('inf')
    arr = [-1]*256
    for i in range(len(s)):
        if arr[ord(s[i])] == -1:
            arr[ord(s[i])] = i
        else:
            arr[ord(s[i])] = -2
    for i in range(256):
        if arr[i] >= 0:
            res = min(res,arr[i]) 
    if res == float('inf'):
        return -1
    return res

s = 'geeksforgeeks'
print(firstNonRepeat(s))