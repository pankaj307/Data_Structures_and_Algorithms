# # Naive Approach
# # Time: O(n^2)

def largestArea(arr,n):
    res = float('-inf')
    for i in range(n):
        temp = arr[i]
        for j in range(i-1,-1,-1):
            if arr[j] >= arr[i]:
                temp += arr[i]
            else:
                break
        for j in range(i+1,n):
            if arr[j] >= arr[i]:
                temp += arr[i]
            else:
                break
        res = max(res,temp)
    return res

arr = [6,2,5,4,1,5,6]
n = len(arr)
print('Naive Approach ->',largestArea(arr,n))



# # Better Approach with Three Traversals of array
# # Time: O(n)

def prevSmaller(arr,n):
	stack = [arr[0]]
	res = [-1]
	for i in range(1,n):
		while len(stack) != 0 and arr[stack[-1]] >= arr[i]:
			stack.pop()
		if len(stack) == 0:
			res.append(-1)
		else:
			res.append(stack[-1])
		stack.append(i)
	return res

def nextSmaller(arr,n):
	stack = [arr[n-1]]
	res = [n]
	for i in range(n-2,-1,-1):
		while len(stack) != 0 and arr[stack[-1]] >= arr[i]:
			stack.pop()
		if len(stack) == 0:
			res.append(n)
		else:
			res.append(stack[-1])
		stack.append(i)
	return res[::-1]

def largestArea_2(arr,n,ps,ns):
    res = 0
    for i in range(n):
        cur = arr[i]
        cur += (i-ps[i]-1)*arr[i]
        cur += (ns[i]-i-1)*arr[i]
        res = max(res,cur)
    return res

arr = [6,2,5,4,1,5,6]
n = len(arr)
ps = prevSmaller(arr,n)
ns = nextSmaller(arr,n)
print('Better Approach ->',largestArea_2(arr,n,ps,ns))



# # Best Approach
# # Time: O(n)

def largestArea_3(arr,n):
    stack = []
    res = 0
    for i in range(n):
        while len(stack) != 0 and arr[stack[-1]] >= arr[i]:
            tp = stack.pop()
            if len(stack) == 0:
                cur = arr[tp]*i
            else:
                cur = arr[tp]*(i-stack[-1]-1)
            res = max(res,cur)
        stack.append(i)
    while len(stack) != 0:
        tp = stack.pop()
        if len(stack) == 0:
            cur = arr[tp]*n
        else:
            cur = arr[tp]*(n-stack[-1]-1)
        res = max(res,cur)
    return res

arr = [6,2,5,4,1,5,6]
n = len(arr)
print('Best Approach ->',largestArea_3(arr,n))
