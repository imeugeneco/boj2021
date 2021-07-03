# 15651 N과 M(4)
n,m = map(int, input().split())
perm = []

def backT4(l,n,m,prev):
    if l==m:
        print(*perm)
        return
    for i in range(0,n):
        if i+1>=prev:
            perm.append(i+1)
            backT4(l+1,n,m,i+1)
            perm.pop()

backT4(0,n,m,0) # 29452KB, 92ms