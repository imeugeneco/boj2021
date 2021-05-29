# 2798
from itertools import combinations

n,m = input().split()
n = int(n)
m = int(m)

cards = input().split()
cards = list(map(int, cards))

sums = set()
for i in combinations(cards, 3):
	temp = sum(i)
	if temp <= m: sums.add(temp)
	
print(max(sums)) # 37908 KB, 148 ms