def areSame(a,b):
    for i in range(256):
        if a[i] != b[i]:
            return False
    return True

def isAnagram(s,pat):
    s_count = [0]*256
    pat_count = [0]*256
    for i in range(len(pat)):
        s_count[ord(s[i])] += 1
        pat_count[ord(pat[i])] += 1
    for i in range(len(pat),len(s)):
        if areSame(s_count,pat_count):
            return True
        s_count[ord(s[i])] += 1
        s_count[ord(s[i-len(pat)])] -= 1
    return False

s = 'geeksforgeeks'
pat = 'kese'
print(isAnagram(s,pat))