N=int(input())

list1=[]

for i in range(0,N+1): 
    sj=0 
    for j in str(i):
        sj+=int(j)
    if sj+i==N:
        list1.append(i)

if list1:
    print(min(list1))
else:
    print(0)
