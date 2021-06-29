# # Using Left Shift Operator

def KthBit(n,k):
    if n&(1<<(k-1)) != 0:
        return True
    return False


# # Using Right Shift Operator

def KthBit_2(n,k):
    if n>>(k-1)&1 == 1:
        return True
    return False

n = 5
k = 3
print(KthBit(n,k))
print(KthBit_2(n,k))