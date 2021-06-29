# # Time: O(n)

def nextGreater(arr,n):
	stack = [arr[n-1]]
	res = [-1]
	for i in range(n-2,-1,-1): 
		while len(stack) != 0 and stack[-1] <= arr[i]:
			stack.pop()
		if len(stack) == 0:
			res.append(-1)
		else:
			res.append(stack[-1])
		stack.append(arr[i])
	return res[::-1]
		


arr = [1,3,2,4]
print(nextGreater(arr,len(arr)))