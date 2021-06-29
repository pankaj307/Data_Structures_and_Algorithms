def anagram(str1,str2):
    if len(str1) != len(str2):
        return False
    arr = [0]*256
    for i in range(len(str1)):
        arr[ord(str1[i])] += 1
    for i in range(len(str2)):
        arr[ord(str2[i])] -= 1
    for i in arr:
        if i != 0:
            return False
    return True

print(anagram('geeks','eskeg'))