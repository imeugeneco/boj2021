import sys
input = sys.stdin.readline

N, k = int(input()), int(input())
start, end = 1, k

while start <= end:
	mid = (start+end)//2
	