N=int(input())
list1=[]
rank=[1]*N

for i in range(0,N):
    height, weight=map(int, input().split())
    list1.append((height,weight))

for i in range(0,N):
    for j in range(0,N):
        if list1[i][0]<list1[j][0] and list1[i][1]<list1[j][1]:
            rank[i]+=1

for i in range(0,N):
    print(rank[i], end=' ')
