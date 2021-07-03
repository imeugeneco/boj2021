# 15649 N과 M(1)
n,m = map(int, input().split())
hist = [False]*n
perm = []

def backT1(l,n,m):
    if l==m:
        print(*perm)
        return
    for i in range(0,n):
        if hist[i]==False:
            perm.append(i+1)
            hist[i]=True
            backT1(l+1,n,m)
            perm.pop()
            hist[i]=False

backT1(0,n,m) # 29452KB, 232ms