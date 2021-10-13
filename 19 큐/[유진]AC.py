import sys, re
input = sys.stdin.readline
d = []

N = int(input())
for _ in range(N):
	op = re.split(r"(\W){0}", input().strip())[1:-1]
	op = [x for x in op if x!=None]
	l = int(input())
	d = list(map(int,re.findall(r'\d+',input())))
	if len(d) != l: print("error")
	try:
		for x in op:
			if x=="R": d = d[::-1]
			if x=="D": d.pop(0)
	except:
		print("error")
