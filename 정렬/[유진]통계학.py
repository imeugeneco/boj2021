import sys
x = int(sys.stdin.readline())
nums = list(int(sys.stdin.readline()) for _ in range(x))

# average
print(round(sum(nums)/x))

# median
print(sorted(nums)[int(x/2)])

# mode
freq = {i:nums.count(i) for i in sorted(set(nums))}
mode = [f for f in freq if freq[f]==max(freq.values())]
if len(mode)==1: print(mode[0])
else: print(mode[1])

# range
print(max(nums)-min(nums))