import sys

N = int(sys.stdin.readline())
count_arr = [0] * (10000 + 1)

for _ in range(N):
    num = int(sys.stdin.readline())
    count_arr[num] += 1

for i in range(10000 + 1):
    while count_arr[i] > 0:
        print(i)
        count_arr[i] -= 1
