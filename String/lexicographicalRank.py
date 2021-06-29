def fact(n):
    if n == 1 or n == 0:
        return 1
    return n*fact(n-1)

# def lexRank(s):
#     rank = 1
#     for i in range(len(s)-1):
#         smaller = 0
#         for j in range(i,len(s)):
#             if ord(s[i]) > ord(s[j]):
#                 smaller+=1
#         rank += smaller*(fact(len(s)-i-1))
#     return rank

# # s = 'BAC'
# s = 'STRING'
# print(lexRank(s))        






# # Linear time
def lexRank(s):
    rank = 1
    n = len(s)
    mul = fact(n)
    arr = [0]*256
    for i in range(n):
        arr[ord(s[i])] += 1
    for i in range(1,256):
        arr[i] += arr[i-1]
    for i in range(n):
        mul = mul//(n-i)
        rank += arr[ord(s[i])-1]*mul
        for j in range(ord(s[i]),256):
            arr[j] -= 1
    return rank

s = 'STRING'
print(lexRank(s))