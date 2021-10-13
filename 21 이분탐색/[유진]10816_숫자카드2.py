import sys
input = sys.stdin.readline

n1 = int(input())
lib = sorted(map(int,input().split()))

n2 = int(input())
cards = list(map(int,input().split()))

idx = 0
dic = {}

for card in sorted(cards):
	count = 0
	if card not in dic:
		while idx < n1:
			if card==lib[idx]:
				count += 1
				idx += 1
			elif card > lib[idx]:
				idx += 1
			else: break
		dic[card] = count

print(' '.join(str(dic[i]) for i in cards))

# 132424KB, 1492ms
		
	