# 10989 수 정렬하기 3
import sys
x = int(sys.stdin.readline())
d = {key: 0 for key in range(1,10001)}

for _ in range(x):
    num = int(sys.stdin.readline())
    d[num] += 1

for k,v in d.items():
    if v!=0:
        for _ in range(v):
            print(k) # 29964KB, 10264ms