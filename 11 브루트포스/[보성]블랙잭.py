N,M=map(int,input().split())

cards=list(map(int,input().split()))
list2=[]
for i in range(0,N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if cards[i]+cards[j]+cards[k]<=M:
                list2.append(cards[i]+cards[j]+cards[k])
                
print(max(list2))
