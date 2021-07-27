import sys
input = sys.stdin.readline
arr = []
dp = []
n = int(input())
for _ in range(n):
    arr.append(int(input()))
dp.append(arr[0])
dp.append(max(arr[0]+arr[1], arr[1]))
dp.append(max(arr[0]+arr[2], arr[1]+arr[2]))
for i in range(3,n):
    dp.append(max(dp[i-3]+arr[i-1]+arr[i], dp[i-2]+arr[i]))
print(dp.pop())
