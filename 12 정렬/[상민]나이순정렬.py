import sys

N = int(input())
members = []
for _ in range(N):
    members.append(sys.stdin.readline().rstrip().split())

members.sort(key=lambda x: int(x[0]))

for member in members:
    print(member[0], member[1])
