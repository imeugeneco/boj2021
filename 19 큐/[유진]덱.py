import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
d = deque()

for _ in range(N):
	op = input().split()
	if op[0]=="push_front": d.appendleft(op[1])
	if op[0]=="push_back": d.append(op[1])
	if op[0]=="pop_front": print(d.popleft()) if len(d)!=0 else print(-1)
	if op[0]=="pop_back": print(d.pop()) if len(d)!=0 else print(-1)
	if op[0]=="size": print(len(d))
	if op[0]=="empty": print(1) if len(d)==0 else print(0)	
	if op[0]=="front": print(d[0]) if len(d)!=0 else print(-1)
	if op[0]=="back": print(d[-1]) if len(d)!=0 else print(-1)

#32084KB, 108ms
