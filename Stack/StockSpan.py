def getSpan(arr,n):
	temp = [1]
	res = [0]
	for i in range(1,n):
		while len(res) != 0 and arr[res[-1]] <= arr[i]:
			res.pop()
		if len(res) == 0:
			span = i+1
		else:
			span = i-res[-1]
		temp.append(span)
		res.append(i)
	return temp
		


arr = [10,4,5,90,120,80]
print(getSpan(arr,len(arr)))