import sys
input = sys.stdin.readline

ans = []
n = int(input())
nums = list(map(int, input().split()))
while nums:
	i = nums.pop(0)
	try:
		ans.append(next(x for x in nums if x>i))
	except:
		ans.append(-1)
print(*ans)
