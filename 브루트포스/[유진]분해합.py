# 2231
n = int(input())
def min_creator(n):
	for i in range(1, n+1): # +1 accounting for 1 digit numbers
		m = i+sum((int(j) for j in str(i)))
		if m==n: 
			return(print(i))
	return(print(0))
min_creator(n)