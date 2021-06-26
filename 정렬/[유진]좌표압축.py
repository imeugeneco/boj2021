# 18870 좌표압축
x = int(input())
coords = list(int(i) for i in input().split())
nums = sorted(set(coords))
for i in coords:
    print(sum(i>x for x in nums), end=' ') # 29964KB, 10624ms