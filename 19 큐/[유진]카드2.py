from collections import deque

def main():
	N = int(input())
	if N==1:
		return 1
	cards = deque(range(2,N+1))
	while len(cards)!=1:
		cards.append(cards.popleft())
		cards.popleft()
	return cards.pop()
	
print(main())
# 50780KB, 240ms