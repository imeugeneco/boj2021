N = int(input())
nums = list(map(int, input().split()))

sorted_nums = sorted(set(nums))
index_dict = {}
for i in range(len(sorted_nums)):
    if sorted_nums[i] not in index_dict:
        index_dict[sorted_nums[i]] = str(i)

print(' '.join([index_dict[num] for num in nums]))
