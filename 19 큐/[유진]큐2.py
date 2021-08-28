import sys
input = sys.stdin.readline

n = int(input())
idx = 0
q = []
for _ in range(n):
	op = input().split()
	if op[0]=="push": q.append(int(op[1]))
	if op[0]=="pop": 
		if len(q)>idx:
			print(q[idx])
			idx +=1
		else: print(-1)
	if op[0]=="size": print(len(q)-idx)
	if op[0]=="empty": 
		if len(q) == idx: 
			print(1)
			idx = 0
			q = []
		else: print(0)
	if op[0]=="front": print(q[idx]) if len(q)>idx else print(-1)
	if op[0]=="back": print(q[-1]) if len(q)>idx else print(-1)
			
# 91056KB, 2640ms