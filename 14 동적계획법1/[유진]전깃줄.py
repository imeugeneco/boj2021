import sys
input = sys.stdin.readline
l = []
n = int(input())
for _ in range(n):
	l.append(tuple(map(int,input().split())))
	
A_none = 0
B_none = 0

for line in l:
	if sum(i[0]<line[0] and i[1]>line[1] for i in l) == 0:
		A_none += 1
	if sum(i[0]<line[0] and i[1]>line[1] for i in l) == 0:
		B_none += 1
		
print(min(A_none, B_none))