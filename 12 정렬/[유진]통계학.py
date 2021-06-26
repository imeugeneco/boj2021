# 2108 통계학
import sys
x = int(sys.stdin.readline())
nums = list(map(int, [sys.stdin.readline() for _ in range(x)]))

print(round(sum(nums)/x)) # average
print(sorted(nums)[int(x/2)]) # median

freq = {}
for n in nums:
	if n in freq: freq[n]+=1
	else: freq[n]=1
mode_num = max(freq.values())
modes = sorted(list(filter(lambda x: x[1]==mode_num,freq.items())))
print(modes[0][0] if len(modes)==1 else modes[1][0]) # mode

print(max(nums)-min(nums)) # range

# 84444KB, 532ms