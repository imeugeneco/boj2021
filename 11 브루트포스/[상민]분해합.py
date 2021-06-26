def decomposedSum(n):
    sum = n
    for num in str(n):
        sum += int(num)
    return sum

n = int(input())
flag = False
for i in range(n):
    sum = decomposedSum(i)
    if sum == n:
        print(i)
        flag = True
        break
if flag == False:
    print(0)

