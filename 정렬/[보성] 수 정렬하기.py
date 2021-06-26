N=int(input())
list1=[]
temp=0

for i in range(0,N):
    list1.append(int(input()))

for j in range(0,N):
    for k in range(0,N):
        if list1[j]<list1[k]:
            temp=list1[j]      #스왑을 이용
            list1[j]=list1[k]
            list1[k]=temp
                 
for i in range(0,N):
    print(list1[i])
