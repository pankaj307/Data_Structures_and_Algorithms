# # Time: O(n)

def prevGreater(arr,n):
	stack = [arr[0]]
	res = [-1]
	for i in range(1,n):
		while len(stack) != 0 and stack[-1] <= arr[i]:
			stack.pop()
		if len(stack) == 0:
			res.append(-1)
		else:
			res.append(stack[-1])
		stack.append(arr[i])
	return res
		


arr = [20,30,10,5,15]
print(prevGreater(arr,len(arr)))