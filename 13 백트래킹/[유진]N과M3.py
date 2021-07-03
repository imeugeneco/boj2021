# 15651 N과 M(3)
n,m = map(int, input().split())
perm = []

def backT3(l,n,m):
    if l==m:
        print(*perm)
        return
    for i in range(0,n):
        perm.append(i+1)
        backT3(l+1,n,m)
        perm.pop()

backT3(0,n,m) # 29452KB, 2000ms