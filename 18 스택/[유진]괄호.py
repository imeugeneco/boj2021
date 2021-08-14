import sys
input = sys.stdin.readline

n = int(input())
ps = []
for _ in range(n):
	ps.append(input())

for i in ps:
	while '()' in i:
		i = i.replace("()","").strip()
	if len(i)!=0: print("NO")
	if len(i)==0: print("YES")
	
# 29200KB, 72ms