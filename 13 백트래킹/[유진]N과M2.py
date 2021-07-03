# 15650 N과 M(2)
n,m = map(int, input().split())
hist = [False]*n
perm = []

def backT2(l,cnt,n,m):
    if l==m:
        print(*perm)
        return
    for i in range(cnt,n):
        if hist[i]==False:
            hist[i]=True
            perm.append(i+1)
            backT2(l+1, i+1, n,m)
            hist[i]=False
            perm.pop()
backT2(0,0,n,m) # 29200KB, 68ms