# 2750 수 정렬하기
x = int(input())
nums = list(input() for _ in range(x))
nums = sorted(set(map(int, nums)))
for i in nums:
	print(i) # 29200KB, 112ms