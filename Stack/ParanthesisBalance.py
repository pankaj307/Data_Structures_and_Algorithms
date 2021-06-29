from queue import LifoQueue
stack = LifoQueue()

def match(a,b):
    if a == '(' and b == ')':
        return True
    elif a == '[' and b == ']':
        return True
    elif a == '{' and b == '}':
        return True
    else:
        return False

def isBalanced(s):
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[' or s[i] == '{':
            stack.put(s[i])
        else:
            if stack.empty() == True:
                return False
            temp = stack.get()
            stack.put(temp)
            if match(temp,s[i]) == False:
                return False
            else:
                stack.get()
    return stack.empty() == True

s = '(([]))'
print(isBalanced(s))