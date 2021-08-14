import sys
input = sys.stdin.readline

stack = []
n = int(input())
for _ in range(n):
	inst = input().split()
	if inst[0]=="push":
		stack.append(inst[1])
	if inst[0]=="pop":
		if len(stack)!=0: print(stack.pop())
		else: print(-1)
	if inst[0]=="size":
		print(len(stack))
	if inst[0]=="empty":
		if len(stack)!=0: print(0)
		else: print(1)
	if inst[0]=="top":
		if len(stack)!=0: print(stack[-1])
		else: print(-1)
		
# 29200KB, 84ms