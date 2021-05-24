#!/usr/bin/env python3
def hanoi_tower(n,fr,to,l):
	if n==1:
		print(fr,to)
		return
	hanoi_tower(n-1,fr,l,to)
	print(fr,to)
	hanoi_tower(n-1,l,to,fr)
	
n = int(input())
print(2**n-1)
hanoi_tower(n,1,3,2)	
