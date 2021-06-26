# 18870 좌표압축
x = int(input())
coords = list(map(int, input().split()))
nums = sorted(set(coords))
nums = {nums[i]: i for i in range(len(nums))}
print(*[nums[i] for i in coords]) # 152716KB, 1812ms