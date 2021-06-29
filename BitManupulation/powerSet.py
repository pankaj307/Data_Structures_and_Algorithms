# # Time: O(2^n * n)
def powerSet(s):
	n = len(s)
	setSize = pow(2,n)
	for i in range(setSize):
		for j in range(n):
			if i&(1<<j) != 0:
				print(s[j],end='')
		print()

s = 'abc'
powerSet(s)